"""Averill blog SEO audit.

Runs the checks that produced the 2026-08-07 audit (13 findings). Every check
states how it got its evidence so results are reproducible.

Schema caveat: this script reads STATIC HTML, which cannot see JS-injected
JSON-LD. It reports what it finds and tells you to confirm in a rendered
browser. Never report "no schema" from static HTML alone.
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
REPL = "\ufffd"

STOP = set("a an the and or of for to in on at with your you how what why is are "
           "that this it its from by as be can do does".split())


def gql(query, variables=None):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    cmd = [sys.executable, str(ADMIN), "graphql", "--query", query]
    tmp = None
    if variables is not None:
        fd, tmp = tempfile.mkstemp(suffix=".json")
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(variables, fh, ensure_ascii=False)
        cmd += ["--variables-file", tmp]
    try:
        proc = subprocess.run(cmd, capture_output=True, env=env)
    finally:
        if tmp:
            os.unlink(tmp)
    out = proc.stdout.decode("utf-8", "replace")
    if proc.returncode != 0 or not out.strip():
        sys.exit(f"admin call failed rc={proc.returncode}\n"
                 f"{proc.stderr.decode('utf-8','replace')[:1200]}")
    data = json.loads(out)
    if "errors" in data:
        sys.exit(f"GraphQL errors: {data['errors']}")
    return data["data"]


Q = """{ blog(id: "%s") { articles(first: 50) { edges { node {
  id title handle isPublished publishedAt summary tags
  author { name } image { url altText }
  metafields(first: 10) { edges { node { key value } } }
  body } } } } }""" % BLOG_GID


def load():
    arts = []
    for e in gql(Q)["blog"]["articles"]["edges"]:
        n = e["node"]
        n["meta"] = {m["node"]["key"]: m["node"]["value"] for m in n["metafields"]["edges"]}
        b = n["body"] or ""
        n["_text"] = re.sub(r"<[^>]+>", " ", b)
        n["_words"] = len(n["_text"].split())
        n["_toc"] = len(re.findall(r'<a href="#', b))
        n["_ids"] = len(re.findall(r"<h[23][^>]*id=", b))
        n["_h2"] = [re.sub(r"<[^>]+>", "", x).strip()
                    for x in re.findall(r"<h2[^>]*>(.*?)</h2>", b, re.S)]
        n["_mojibake"] = b.count(REPL)
        n["_prodlink"] = b.count("/products/monets-garden")
        n["_inbound_targets"] = set(re.findall(r'href="(?:https://www\.averillmahjong\.com)?'
                                              r'/blogs/news/([a-z0-9-]+)"', b))
        arts.append(n)
    return arts


def terms(s):
    return {w for w in re.findall(r"[a-z]+", s.lower()) if w not in STOP and len(w) > 2}


def inventory(arts):
    print(f"{'PUB':6} {'HANDLE':46} {'WORDS':>6} {'TOC':>4} {'IDS':>4} {'IMG':>4} "
          f"{'FFFD':>5} {'PROD':>5}  PUBLISHED_AT")
    for a in sorted(arts, key=lambda x: (not x["isPublished"], x["publishedAt"] or "")):
        img = "yes" if (a.get("image") or {}).get("url") else "NO"
        print(f"{str(a['isPublished']):6} {a['handle'][:46]:46} {a['_words']:>6} "
              f"{a['_toc']:>4} {a['_ids']:>4} {img:>4} {a['_mojibake']:>5} "
              f"{a['_prodlink']:>5}  {a['publishedAt']}")
    print(f"\n{len(arts)} articles "
          f"({sum(1 for a in arts if a['isPublished'])} published, "
          f"{sum(1 for a in arts if not a['isPublished'])} draft)")


def findings(arts):
    out = []

    # A1/A2 cannibalisation between existing articles
    for i, x in enumerate(arts):
        for y in arts[i + 1:]:
            tx, ty = terms(x["title"]), terms(y["title"])
            if not tx or not ty:
                continue
            ov = len(tx & ty) / min(len(tx), len(ty))
            if ov >= 0.6:
                out.append(("HIGH", "cannibalisation",
                            f"{x['handle']} vs {y['handle']} - title term overlap "
                            f"{ov:.0%} ({sorted(tx & ty)}). Two pages chasing one term "
                            f"split link equity; merge + 301 or differentiate."))

    # A3 FAQPage: RETIRED as a finding on 2026-08-10.
    # Google removed FAQ rich results from Search entirely on 2026-05-07 (restricted
    # to gov/health sites in Aug 2023, then dropped for everyone), pulled the docs
    # page on 2026-06-15, and is removing Search Console support through Aug 2026.
    # FAQPage markup therefore buys zero Google search appearance. Do not re-add this
    # check. Written FAQ sections remain worth having for readers and for machine
    # parsing; they are simply not a rich-result surface any more.
    # BreadcrumbList is a SEPARATE feature and is still live -- see A3b below.

    # A4 missing featured image -> Article schema invalid
    for a in arts:
        if not (a.get("image") or {}).get("url"):
            sev = "HIGH" if a["isPublished"] else "MED"
            out.append((sev, "missing-image",
                        f"{a['handle']} has no featured image. Article schema then lacks "
                        f"`image`, which Google requires for Article rich results; og:image "
                        f"falls back to the site logo."))
        elif not (a.get("image") or {}).get("altText"):
            out.append(("LOW", "missing-alt",
                        f"{a['handle']} featured image has no alt text."))

    # A5 meta title/desc hygiene
    for a in arts:
        mt, md = a["meta"].get("title_tag"), a["meta"].get("description_tag")
        if not mt:
            out.append(("MED", "meta-title", f"{a['handle']} has no title_tag metafield; "
                                             "Shopify will append its own brand suffix."))
        else:
            if len(mt) > 60:
                out.append(("LOW", "meta-title", f"{a['handle']} title_tag {len(mt)} chars (>60, truncates)."))
            if "| Averill" not in mt:
                out.append(("LOW", "meta-title", f"{a['handle']} title_tag lacks the '| Averill' "
                                                 "suffix used site-wide; Shopify adds a mismatched ndash."))
        if not md:
            out.append(("MED", "meta-desc", f"{a['handle']} has no description_tag metafield."))
        elif not (120 <= len(md) <= 160):
            out.append(("LOW", "meta-desc", f"{a['handle']} description_tag {len(md)} chars (target 120-160)."))

    # A6/A7 tags + author consistency
    for a in arts:
        if not a["tags"]:
            out.append(("LOW", "tags", f"{a['handle']} has no tags."))
    authors = {(a.get("author") or {}).get("name") for a in arts}
    if len(authors) > 1:
        out.append(("LOW", "author", f"Inconsistent author names {authors}; propagates into "
                                     "Article.author.name in schema."))

    # A8 thin content
    pub = [a for a in arts if a["isPublished"]]
    if pub:
        med = sorted(a["_words"] for a in pub)[len(pub) // 2]
        for a in pub:
            if a["_words"] < med * 0.6:
                out.append(("MED", "thin-content",
                            f"{a['handle']} is {a['_words']} words vs median {med}."))

    # A9 internal link depth
    inbound = {a["handle"]: 0 for a in arts}
    for a in arts:
        for t in a["_inbound_targets"]:
            if t in inbound and t != a["handle"]:
                inbound[t] += 1
    for a in arts:
        if a["isPublished"] and inbound[a["handle"]] < 2:
            out.append(("MED", "internal-links",
                        f"{a['handle']} has {inbound[a['handle']]} inbound internal link(s); "
                        f"target >=2."))
    for a in arts:
        if a["_prodlink"] == 0:
            out.append(("HIGH", "no-product-link",
                        f"{a['handle']} does not link to the product page."))

    # A13 anchor navigation consistency
    for a in arts:
        if len(a["_h2"]) >= 4 and a["_toc"] == 0:
            out.append(("MED", "no-toc",
                        f"{a['handle']} has {len(a['_h2'])} H2 sections but no "
                        f"'On this page' anchor nav. Fix with "
                        f"`shopify_article.py update --add-toc`."))
        hrefs = set(re.findall(r'<a href="#([^"]+)">', a["body"] or ""))
        ids = set(re.findall(r'<h[23][^>]*id="([^"]+)"', a["body"] or ""))
        if hrefs - ids:
            out.append(("HIGH", "broken-anchors",
                        f"{a['handle']} anchors resolve to nothing: {sorted(hrefs - ids)}"))

    # mojibake
    for a in arts:
        if a["_mojibake"]:
            out.append(("HIGH", "mojibake",
                        f"{a['handle']} contains {a['_mojibake']} U+FFFD. See playbook trap 1."))

    # draft cross-links to unpublished handles
    live = {a["handle"] for a in arts if a["isPublished"]}
    known = {a["handle"] for a in arts}
    for a in arts:
        for t in a["_inbound_targets"]:
            if t in known and t not in live:
                out.append(("MED", "link-to-draft",
                            f"{a['handle']} links to /blogs/news/{t}, which is an unpublished "
                            f"draft (404 until published). Publish together or remove."))
    return out


def technical():
    print("\n=== technical (live) ===")
    def get(u):
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        r = urllib.request.urlopen(req, timeout=30)
        return r.geturl(), r.read().decode("utf-8", "replace")
    try:
        final, robots = get("https://averillmahjong.com/robots.txt")
        print(f"non-www redirect -> {final}")
        print(f"sitemap declared : {'Sitemap:' in robots}")
        _, sm = get(f"{STORE}/sitemap_blogs_1.xml")
        locs = re.findall(r"<loc>([^<]+)</loc>", sm)
        print(f"blog sitemap URLs: {len(locs)}")
        for l in locs:
            print(f"   {l}")
    except Exception as e:
        print(f"technical checks failed: {e}")
    print("\nSchema: static HTML cannot see JS-injected JSON-LD. Confirm BreadcrumbList "
          "in a rendered browser via\n"
          "  document.querySelectorAll('script[type=\"application/ld+json\"]')\n"
          "  (FAQPage is NOT worth checking: Google retired FAQ rich results 2026-05-07.)")


def cannibalize(arts, kw):
    k = terms(kw)
    # Corpus-frequency weighting. "mahjong" is in every title, so an unweighted
    # overlap score flags everything (false positive on e.g. "mahjong table mat").
    # Terms appearing in >60% of titles carry no discriminating power.
    n = max(len(arts), 1)
    df = {t: sum(1 for a in arts if t in terms(a["title"])) for t in k}
    weights = {t: 0.0 if df[t] / n > 0.6 else 1.0 for t in k}
    generic = sorted(t for t in k if weights[t] == 0.0)
    total_w = sum(weights.values())
    if total_w == 0:
        print(f"All terms in {kw!r} are generic across this blog ({generic}); "
              f"cannot judge overlap by title alone. Compare H2s and intent manually.\n")
        total_w = 1e-9
    print(f"Cannibalisation check for {kw!r}")
    print(f"  discriminating terms: {sorted(t for t in k if weights[t])}")
    if generic:
        print(f"  ignored as generic (in >60% of titles): {generic}")
    print()

    def wov(other):
        return sum(weights[t] for t in k & other) / total_w

    rows = []
    for a in arts:
        body = a["body"] or ""
        title_ov = max(wov(terms(a["title"])), wov(terms(a["meta"].get("title_tag", ""))))
        body_hits = len(re.findall(re.escape(kw.lower()), (a["_text"] or "").lower()))
        # Sub-heading / FAQ-question overlap. The real cannibalisation risk often
        # sits in an existing article's FAQ rather than its title: the beginner
        # guide answers "how many tiles does American mahjong use?" in its FAQ while
        # its title shares almost nothing with that query. FAQ questions appear as
        # <h3> in some articles and <strong> in others, so scan both.
        units = re.findall(r"<h[234][^>]*>(.*?)</h[234]>", body, re.S)
        units += re.findall(r"<strong>(.*?)</strong>", body, re.S)
        best_unit, unit_ov = None, 0.0
        for u in units:
            txt = re.sub(r"<[^>]+>", "", u).strip()
            o = wov(terms(txt))
            if o > unit_ov:
                unit_ov, best_unit = o, txt
        # how many discriminating terms show up anywhere in the body
        present = sum(1 for t in k if weights[t] and re.search(rf"\b{re.escape(t)}", (a['_text'] or '').lower()))
        disc = sum(1 for t in k if weights[t]) or 1
        rows.append((max(title_ov, unit_ov), title_ov, unit_ov, best_unit,
                     body_hits, present / disc, a))
    rows.sort(key=lambda r: -r[0])
    risk = False
    for score, tov, uov, unit, hits, dens, a in rows:
        # Term density alone is a weak signal: in a 1,400-word article every
        # discriminating term usually appears somewhere. It is shown as context
        # but never promotes a row on its own, or every article flags MED.
        if score < 0.34 and hits == 0:
            continue
        lvl = ("HIGH" if score >= 0.6 or hits >= 3
               else "MED" if score >= 0.34
               else "LOW")
        if lvl in ("HIGH", "MED"):
            risk = True
        print(f"  [{lvl:4}] {a['handle'][:46]:46}")
        print(f"           title/meta {tov:.0%} | heading/FAQ {uov:.0%} | "
              f"exact phrase x{hits} | discriminating terms in body {dens:.0%}")
        if unit and uov >= 0.34:
            print(f"           closest existing heading/question: {unit[:78]}")
    if not risk:
        print("  no meaningful overlap - safe to target.")
    else:
        print("\n  Overlap found. Either pick a different angle, or fold the keyword into "
              "the existing article (often better: add an FAQ entry there rather than "
              "writing a competing page).")
    return risk


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--inventory", action="store_true")
    p.add_argument("--full", action="store_true")
    p.add_argument("--cannibalize", metavar="KEYWORD")
    a = p.parse_args()
    if not (a.inventory or a.full or a.cannibalize):
        a.inventory = True
    arts = load()
    if a.inventory or a.full:
        inventory(arts)
    if a.cannibalize:
        print()
        sys.exit(1 if cannibalize(arts, a.cannibalize) else 0)
    if a.full:
        fs = findings(arts)
        order = {"HIGH": 0, "MED": 1, "LOW": 2}
        fs.sort(key=lambda f: order[f[0]])
        print(f"\n=== {len(fs)} findings ===")
        for sev, cat, msg in fs:
            print(f"[{sev:4}] {cat:18} {msg}")
        technical()


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
