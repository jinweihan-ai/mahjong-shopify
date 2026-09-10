#!/usr/bin/env python3
"""Add the "learn to play" line to the live Klaviyo emails that are CODE templates (see klaviyo_probe.py).

    KLAVIYO_API_KEY=pk_... python tools/klaviyo_add_link.py            # dry run: shows what would be inserted where
    KLAVIYO_API_KEY=pk_... python tools/klaviyo_add_link.py --apply    # backs up, patches, reads back

The new paragraph copies the inline styles of the paragraph it follows, so it looks like the rest of the email.
Backups go to ~/companion/klaviyo-backups/<template>-<timestamp>.html on the machine that runs this.
"""
from __future__ import annotations

import datetime as dt
import os
import re
import sys
from pathlib import Path

import requests

BASE = 'https://a.klaviyo.com/api'
HEADERS = {
    'Authorization': f'Klaviyo-API-Key {os.environ["KLAVIYO_API_KEY"]}',
    'revision': '2025-07-15',
    'accept': 'application/vnd.api+json',
    'content-type': 'application/vnd.api+json',
}
LINK = 'https://play.averillmahjong.com/?src=email'
BACKUPS = Path.home() / 'companion' / 'klaviyo-backups'

# template id -> where and what. `after` is text that exists once in the email; the new paragraph goes
# after the block that contains it ('p' = the enclosing paragraph, 'row' = the enclosing table row).
RULES = {
    'RAsZyQ': {  # Welcome 1: after the coupon-code box
        'after': 'One use per customer.',
        'block': 'row',
        'style_from': 'Here is your welcome code again',
        'text': 'New to American mahjong? <a href="{link}" style="{a}">Learn to play in ten minutes</a>, free and with no account, so the set is ready to play the evening it arrives.',
    },
    'UVqZxC': {  # Abandoned checkout 1: after the "everything is still there" paragraph
        'after': 'picks up exactly where you left off.',
        'block': 'p',
        'style_from': 'picks up exactly where you left off.',
        'text': 'Worried about learning? <a href="{link}" style="{a}">Free ten-minute lessons</a> are included, with three patient players who explain every move.',
    },
}


def get_html(tid: str) -> str:
    r = requests.get(f'{BASE}/templates/{tid}', headers=HEADERS, params={'fields[template]': 'html'}, timeout=30)
    r.raise_for_status()
    return r.json()['data']['attributes']['html']


def put_html(tid: str, html: str) -> None:
    body = {'data': {'type': 'template', 'id': tid, 'attributes': {'html': html}}}
    r = requests.patch(f'{BASE}/templates/{tid}', headers=HEADERS, json=body, timeout=60)
    if r.status_code >= 400:
        raise SystemExit(f'PATCH {tid}: {r.status_code} {r.text[:400]}')


def style_before(html: str, pos: int, tag: str) -> str:
    """Inline style of the nearest <tag ...> opened before pos."""
    m = None
    for m in re.finditer(rf'<{tag}\b[^>]*?style="([^"]*)"', html[:pos]):
        pass
    return m.group(1) if m else ''


def build(html: str, rule: dict) -> tuple[str, str]:
    at = html.find(rule['after'])
    if at < 0 or html.count(rule['after']) != 1:
        raise SystemExit(f"anchor not found exactly once: {rule['after']!r}")
    p_style = style_before(html, html.find(rule['style_from']), 'p')
    td_style = style_before(html, html.find(rule['style_from']), 'td')
    color = re.search(r'color:\s*([^;]+)', p_style)
    a_style = f'color:{color.group(1).strip() if color else "#232323"};text-decoration:underline;'
    para = f'<p style="{p_style}">' + rule['text'].format(link=LINK, a=a_style) + '</p>'
    if rule['block'] == 'p':
        end = html.index('</p>', at) + len('</p>')
        snippet = '\n' + para
    else:
        end = html.index('</tr>', at) + len('</tr>')  # inner row of the code box
        end = html.index('</tr>', end) + len('</tr>')  # the outer row
        # same background as the text block, but sitting close under the code box rather than a full block apart
        td_style = re.sub(r'padding:[^;]+;', 'padding:4px 34px 30px;', td_style)
        snippet = f'\n<tr><td style="{td_style}">{para.replace("margin:0 0 15px", "margin:0", 1)}</td></tr>'
    return html[:end] + snippet + html[end:], snippet


def main() -> None:
    apply = '--apply' in sys.argv
    stamp = dt.datetime.now().strftime('%Y%m%d-%H%M%S')
    for tid, rule in RULES.items():
        html = get_html(tid)
        if LINK.split('?')[0] in html:
            print(f'{tid}: already has the link, skipped')
            continue
        new_html, snippet = build(html, rule)
        print(f'\n{tid}: would insert after {rule["after"]!r} ({rule["block"]}):\n  {snippet.strip()[:400]}')
        if not apply:
            continue
        BACKUPS.mkdir(parents=True, exist_ok=True)
        (BACKUPS / f'{tid}-{stamp}.html').write_text(html, encoding='utf-8')
        put_html(tid, new_html)
        back = get_html(tid)
        ok = LINK in back and back.count('<p') == html.count('<p') + 1
        (BACKUPS / f'{tid}-{stamp}-new.html').write_text(back, encoding='utf-8')
        print(f'{tid}: {"updated and read back ok" if ok else "MISMATCH after update"}')
        if not ok:
            sys.exit(1)


if __name__ == '__main__':
    main()
