"""Safe Shopify article read/write for Averill.

Wraps shopify-admin-theme-ops/scripts/shopify_admin.py and hard-blocks the three
traps documented in references/shopify-api-playbook.md:

  1. Article bodies NEVER pass through stdout (Windows GBK console corrupts
     em dashes into U+FFFD -> permanent data loss). All bodies move via UTF-8
     files, and every read/write is mojibake-checked.
  2. `update` refuses to run without an explicit --draft or --published, because
     ArticleUpdateInput.isPublished defaults to true and silently publishes drafts.
  3. `verify` reports the Admin API (source of truth) plus the atom feed, never
     trusting a curl of the HTML page (full-page cache lags).
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

ADMIN = Path(__file__).resolve().parent / "shopify_admin.py"
BLOG_GID = "gid://shopify/Blog/117575811369"
STORE = "https://www.averillmahjong.com"
AUTHOR = "Averill Mahjong"
REPL = "\ufffd"

BLOCKED_TITLE = ["for women", "ultimate guide", "best ever",
                 "what to know before you choose"]
AI_TELLS = ["elevate your experience", "perfect for every occasion",
            "in today's fast-paced", "delve into", "it's important to note",
            "when it comes to", "a testament to", "navigate the landscape"]


# --------------------------------------------------------------------------- io

def gql(query, variables=None):
    """Run a GraphQL call. Response comes back via a temp file, never stdout
    parsing of a body, and the child process is forced to UTF-8."""
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    cmd = [sys.executable, str(ADMIN), "graphql", "--query", query]
    tmp_vars = None
    if variables is not None:
        fd, tmp_vars = tempfile.mkstemp(suffix=".json")
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(variables, fh, ensure_ascii=False)
        cmd += ["--variables-file", tmp_vars]
    try:
        proc = subprocess.run(cmd, capture_output=True, env=env)
    finally:
        if tmp_vars:
            os.unlink(tmp_vars)
    out = proc.stdout.decode("utf-8", "replace")
    if proc.returncode != 0 or not out.strip():
        sys.exit(f"shopify_admin.py failed (rc={proc.returncode})\n"
                 f"{proc.stderr.decode('utf-8', 'replace')[:1500]}")
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        sys.exit(f"Non-JSON response (console encoding crash?):\n{out[:1500]}")
    if "errors" in data:
        sys.exit(f"GraphQL errors: {json.dumps(data['errors'], ensure_ascii=False)}")
    return data["data"]


def check_mojibake(body, label, fatal=True):
    n = body.count(REPL)
    if not n:
        return 0
    runs = [(m.start(), len(m.group(0))) for m in re.finditer(REPL + "+", body)]
    msg = [f"MOJIBAKE: {label} contains {n} U+FFFD in {len(runs)} runs."]
    for pos, ln in runs[:8]:
        msg.append(f"  [{ln}x] ...{body[max(0,pos-50):pos]}<<HERE>>{body[pos+ln:pos+ln+50]}...")
    msg.append("  2x between spaces = em dash; 1x followed by 'C' = en dash;")
    msg.append("  2x touching a word = curly quote/apostrophe. Disambiguate by context.")
    msg.append("  See references/shopify-api-playbook.md trap 1.")
    text = "\n".join(msg)
    if fatal:
        sys.exit(text + "\n\nREFUSING TO WRITE. Fix the source first.")
    print(text)
    return n


# ------------------------------------------------------------------------- toc

def slugify(inner):
    import html as _h
    t = _h.unescape(re.sub(r"<[^>]+>", "", inner))
    t = t.replace("'", "").replace("\u2019", "").replace("\u2018", "")
    t = re.sub(r"[^a-zA-Z0-9\s-]", " ", t)
    return re.sub(r"-+", "-", re.sub(r"\s+", "-", t.strip().lower())).strip("-")


def add_toc(body):
    """Insert the site-standard <nav id="article-toc"> and give every h2/h3 an id.
    Matches the pattern already used on the published articles."""
    if "article-toc" in body:
        body = re.sub(r'<nav id="article-toc".*?</nav>\s*', "", body, flags=re.S)
    collected = {2: [], 3: []}

    def make(level):
        def rep(m):
            attrs, inner = m.group(1), m.group(2)
            if "id=" in attrs:
                s = re.search(r'id="([^"]+)"', attrs).group(1)
            else:
                s = slugify(inner)
                attrs = f' id="{s}"' + attrs
            collected[level].append((s, inner))
            return f"<h{level}{attrs}>{inner}</h{level}>"
        return rep

    for lvl in (2, 3):
        body = re.sub(rf"<h{lvl}([^>]*)>(.*?)</h{lvl}>", make(lvl), body, flags=re.S)

    h2 = collected[2]
    if not h2:
        return body, []
    nav = ['<nav id="article-toc" aria-label="On this page">',
           "<strong>On this page</strong>", "<ul>"]
    nav += [f'<li><a href="#{s}">{re.sub(r"<[^>]+>", "", i)}</a></li>' for s, i in h2]
    nav += ["</ul>", "</nav>", ""]
    first = re.search(r"<h2[^>]*id=", body)
    body = body[:first.start()] + "\n".join(nav) + "\n" + body[first.start():]
    return body, h2


def validate_toc(body, label="body"):
    hrefs = re.findall(r'<a href="#([^"]+)">', body)
    ids = re.findall(r'<h[23][^>]*id="([^"]+)"', body)
    bad = sorted(set(hrefs) - set(ids))
    dup = len(ids) - len(set(ids))
    if bad or dup:
        sys.exit(f"TOC BROKEN in {label}: unmatched={bad} duplicate_ids={dup}")
    return len(hrefs), len(ids)


# ------------------------------------------------------------------- gate

def quality_gate(title, body, meta_title, meta_desc, strict=True):
    issues, warns = [], []
    low = title.lower()
    for p in BLOCKED_TITLE:
        if p in low:
            issues.append(f"title contains blocked phrase: {p!r}")
    tl = body.lower()
    for p in AI_TELLS:
        if p in tl:
            warns.append(f"possible AI tell in body: {p!r}")
    if meta_title and len(meta_title) > 60:
        warns.append(f"meta title {len(meta_title)} chars (>60, will truncate)")
    if meta_desc and not (120 <= len(meta_desc) <= 160):
        warns.append(f"meta description {len(meta_desc)} chars (target 120-160)")
    if "/products/monets-garden" not in body:
        issues.append("no link to the Monet's Garden product page")
    if len(re.findall(r'href="(?:https://www\.averillmahjong\.com)?/blogs/news/', body)) == 0:
        warns.append("no internal link to another Journal article")
    for ph in ["Brief only", "expand this outline", "TODO", "PLACEHOLDER", "link naturally to"]:
        if ph.lower() in tl:
            issues.append(f"outline/SEO placeholder left in body: {ph!r}")
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    if words < 900:
        warns.append(f"body is {words} words (published articles run 1,100-1,500)")
    if not re.search(r"<h2[^>]*>\s*FAQ\s*</h2>", body, re.I):
        warns.append("no FAQ section (h2 'FAQ') - FAQ drives the FAQPage schema plan")
    return issues, warns, words


# --------------------------------------------------------------------- actions

Q_ARTICLE = """query($id: ID!) { article(id: $id) {
  id title handle isPublished publishedAt updatedAt summary tags
  author { name } image { url altText }
  metafields(first: 10) { edges { node { namespace key value } } }
  body } }"""


def fetch(gid):
    return gql(Q_ARTICLE, {"id": gid})["article"]


def cmd_get(a):
    art = fetch(a.id)
    check_mojibake(art["body"], f"stored body of {art['handle']}", fatal=False)
    Path(a.out).write_text(art["body"], encoding="utf-8")
    meta = {m["node"]["key"]: m["node"]["value"] for m in art["metafields"]["edges"]}
    print(f"handle       : {art['handle']}")
    print(f"isPublished  : {art['isPublished']}  publishedAt: {art['publishedAt']}")
    print(f"updatedAt    : {art['updatedAt']}")
    print(f"image        : {(art.get('image') or {}).get('url')}")
    print(f"title_tag    : {meta.get('title_tag')}")
    print(f"desc_tag     : {meta.get('description_tag')}")
    print(f"body written -> {a.out} ({len(art['body'])} chars)")


def build_metafields(meta_title, meta_desc):
    mf = []
    if meta_title:
        mf.append({"namespace": "global", "key": "title_tag",
                   "type": "single_line_text_field", "value": meta_title})
    if meta_desc:
        mf.append({"namespace": "global", "key": "description_tag",
                   "type": "single_line_text_field", "value": meta_desc})
    return mf


def cmd_create(a):
    body = Path(a.body_file).read_text(encoding="utf-8")
    check_mojibake(body, a.body_file)                       # fatal
    if not a.no_toc:
        body, h2 = add_toc(body)
    validate_toc(body, a.body_file)
    issues, warns, words = quality_gate(a.title, body, a.meta_title, a.meta_desc)
    for w in warns:
        print(f"  WARN  {w}")
    if issues:
        print("\nQUALITY GATE FAILED:")
        for i in issues:
            print(f"  BLOCK {i}")
        if not a.force:
            sys.exit("\nRefusing to create. Fix the body, or pass --force to override.")
    art = {"blogId": BLOG_GID, "title": a.title, "handle": a.handle,
           "body": body, "author": {"name": AUTHOR},
           "isPublished": False}                            # hard rule: drafts only
    if a.summary:
        art["summary"] = a.summary
    if a.tags:
        art["tags"] = [t.strip() for t in a.tags.split(",") if t.strip()]
    mf = build_metafields(a.meta_title, a.meta_desc)
    if mf:
        art["metafields"] = mf
    m = """mutation($article: ArticleCreateInput!) { articleCreate(article: $article) {
      article { id title handle isPublished publishedAt } userErrors { field message } } }"""
    r = gql(m, {"article": art})["articleCreate"]
    if r["userErrors"]:
        sys.exit(f"userErrors: {r['userErrors']}")
    print(f"\ncreated  : {r['article']['id']}")
    print(f"handle   : {r['article']['handle']}")
    print(f"published: {r['article']['isPublished']}  (must be False)")
    print(f"words    : {words}")
    assert r["article"]["isPublished"] is False, "DRAFT INVARIANT VIOLATED"


def cmd_update(a):
    if a.draft == a.published:
        sys.exit("Pass exactly one of --draft / --published. ArticleUpdateInput."
                 "isPublished defaults to TRUE, so omitting it silently publishes "
                 "drafts (playbook trap 2).")
    before = fetch(a.id)
    body = Path(a.body_file).read_text(encoding="utf-8") if a.body_file else before["body"]
    check_mojibake(body, a.body_file or "existing body")     # fatal
    if a.add_toc:
        body, _ = add_toc(body)
    if "article-toc" in body:
        validate_toc(body, a.id)
    art = {"body": body, "isPublished": bool(a.published)}
    if a.published:
        pd = a.publish_date or before["publishedAt"]
        if not pd:
            sys.exit("--published needs --publish-date (or the article must already have one); "
                     "omitting it resets datePublished and pollutes Article schema.")
        art["publishDate"] = pd
    mf = build_metafields(a.meta_title, a.meta_desc)
    if mf:
        art["metafields"] = mf
    m = """mutation($id: ID!, $article: ArticleUpdateInput!) {
      articleUpdate(id: $id, article: $article) {
        article { handle isPublished publishedAt updatedAt } userErrors { field message } } }"""
    r = gql(m, {"id": a.id, "article": art})["articleUpdate"]
    if r["userErrors"]:
        sys.exit(f"userErrors: {r['userErrors']}")
    got = r["article"]
    print(f"updated      : {got['handle']}")
    print(f"isPublished  : {got['isPublished']} (intended {bool(a.published)})")
    print(f"publishedAt  : {got['publishedAt']} (was {before['publishedAt']})")
    if got["isPublished"] != bool(a.published):
        sys.exit("PUBLISH STATE MISMATCH - revert immediately.")
    if a.published and before["publishedAt"] and got["publishedAt"] != before["publishedAt"]:
        print("  WARN publishedAt changed - this alters Article schema datePublished.")


def atom_bodies():
    req = urllib.request.Request(f"{STORE}/blogs/news.atom",
                                 headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")


def cmd_verify(a):
    art = fetch(a.id)
    body = art["body"]
    print("--- Admin API (source of truth) ---")
    print(f"handle      : {art['handle']}")
    print(f"isPublished : {art['isPublished']}  publishedAt: {art['publishedAt']}")
    print(f"updatedAt   : {art['updatedAt']}")
    print(f"image       : {(art.get('image') or {}).get('url') or 'NONE  <-- breaks Article schema'}")
    n = check_mojibake(body, "stored body", fatal=False)
    print(f"mojibake    : {n}")
    try:
        t, i = validate_toc(body, "stored body")
        print(f"toc         : {t} links / {i} ids  OK")
    except SystemExit as e:
        print(f"toc         : {e}")
    if art["isPublished"]:
        print("\n--- atom feed (bypasses full-page cache) ---")
        try:
            feed = atom_bodies()
            print(f"feed mojibake: {feed.count(REPL)}")
            print(f"feed em dash : {feed.count(chr(0x2014))}")
        except Exception as e:
            print(f"feed fetch failed: {e}")
        print("\nNote: do NOT trust a curl of the HTML page; full-page cache can lag "
              ">10 min even with cache-busting params (playbook trap 3).")
    else:
        url = f"{STORE}/blogs/news/{art['handle']}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        try:
            urllib.request.urlopen(req, timeout=20)
            code = 200
        except urllib.error.HTTPError as e:
            code = e.code
        except Exception:
            code = "?"
        print(f"\ndraft not public: {url} -> {code} (expect 404)")


def cmd_scan(a):
    q = """{ blog(id: "%s") { articles(first: 50) { edges { node {
        handle isPublished body } } } } }""" % BLOG_GID
    total = 0
    for e in gql(q)["blog"]["articles"]["edges"]:
        n = e["node"]
        c = (n["body"] or "").count(REPL)
        total += c
        flag = "  <-- MOJIBAKE" if c else ""
        print(f"{str(n['isPublished']):6} {n['handle'][:50]:50} {c:>4}{flag}")
    print(f"\nTOTAL U+FFFD across blog: {total}")
    if total:
        sys.exit(1)


def cmd_toc(a):
    body = Path(a.body_file).read_text(encoding="utf-8")
    check_mojibake(body, a.body_file)
    body, h2 = add_toc(body)
    t, i = validate_toc(body, a.body_file)
    Path(a.out or a.body_file).write_text(body, encoding="utf-8")
    print(f"toc: {t} links / {i} ids -> {a.out or a.body_file}")
    for s, _ in h2:
        print("   ", s)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("get", help="read an article; body goes to a UTF-8 file")
    g.add_argument("--id", required=True); g.add_argument("--out", required=True)
    g.set_defaults(fn=cmd_get)

    c = sub.add_parser("create", help="create an UNPUBLISHED draft")
    for f in ("title", "handle", "body-file"):
        c.add_argument(f"--{f}", required=True)
    for f in ("meta-title", "meta-desc", "summary", "tags"):
        c.add_argument(f"--{f}", default="")
    c.add_argument("--no-toc", action="store_true")
    c.add_argument("--force", action="store_true", help="override quality gate blocks")
    c.set_defaults(fn=cmd_create)

    u = sub.add_parser("update", help="update an article (publish state is mandatory)")
    u.add_argument("--id", required=True)
    u.add_argument("--body-file")
    u.add_argument("--draft", action="store_true")
    u.add_argument("--published", action="store_true")
    u.add_argument("--publish-date")
    u.add_argument("--add-toc", action="store_true")
    u.add_argument("--meta-title", default=""); u.add_argument("--meta-desc", default="")
    u.set_defaults(fn=cmd_update)

    v = sub.add_parser("verify", help="verify via Admin API + atom feed")
    v.add_argument("--id", required=True); v.set_defaults(fn=cmd_verify)

    s = sub.add_parser("scan-mojibake", help="scan every article for U+FFFD")
    s.set_defaults(fn=cmd_scan)

    t = sub.add_parser("toc", help="add/refresh the TOC in a local body file")
    t.add_argument("--body-file", required=True); t.add_argument("--out")
    t.set_defaults(fn=cmd_toc)

    a = p.parse_args()
    a.body_file = getattr(a, "body_file", None)
    a.fn(a)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
