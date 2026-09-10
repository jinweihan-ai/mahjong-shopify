#!/usr/bin/env python3
"""Look at the live Klaviyo flows and tell which emails can be edited through the API.

Only templates made in the HTML/code editor (editor_type CODE) accept updates through the Templates API;
drag-and-drop templates (SYSTEM_DRAGGABLE) can only be changed in the Klaviyo editor.

    KLAVIYO_API_KEY=pk_... python tools/klaviyo_probe.py            # list flows, emails, template types
    KLAVIYO_API_KEY=pk_... python tools/klaviyo_probe.py --html ID  # dump one template's HTML to stdout

The key comes from the environment only (never from this repo). Scopes needed: flows:read, templates:read
(templates:write only if a template turns out to be editable and we decide to change it).
"""
from __future__ import annotations

import os
import sys

import requests

BASE = 'https://a.klaviyo.com/api'
HEADERS = {
    'Authorization': f'Klaviyo-API-Key {os.environ["KLAVIYO_API_KEY"]}',
    'revision': '2025-07-15',
    'accept': 'application/vnd.api+json',
}


def get(path: str, params: dict | None = None) -> dict:
    r = requests.get(f'{BASE}{path}', headers=HEADERS, params=params, timeout=30)
    if r.status_code >= 400:
        raise SystemExit(f'{r.status_code} {path}: {r.text[:300]}')
    return r.json()


def main() -> None:
    if '--html' in sys.argv:
        tid = sys.argv[sys.argv.index('--html') + 1]
        t = get(f'/templates/{tid}')['data']['attributes']
        sys.stdout.write(t.get('html') or t.get('text') or '')
        return

    flows = get('/flows', {'fields[flow]': 'name,status,trigger_type'})['data']
    for f in flows:
        a = f['attributes']
        print(f"\n{a['name']}  [{a['status']}]  flow {f['id']}")
        actions = get(f"/flows/{f['id']}/flow-actions", {'fields[flow-action]': 'action_type,status'})['data']
        for act in actions:
            if act['attributes'].get('action_type') != 'SEND_EMAIL':
                continue
            msgs = get(f"/flow-actions/{act['id']}/flow-messages", {'fields[flow-message]': 'name,content'})['data']
            for m in msgs:
                content = m['attributes'].get('content') or {}
                tpl = get(f"/flow-messages/{m['id']}/template", {'fields[template]': 'name,editor_type,html'})['data']
                ta = tpl['attributes']
                html = ta.get('html') or ''
                print(f"  email: {m['attributes'].get('name')}")
                print(f"    subject: {content.get('subject')}")
                print(f"    template {tpl['id']}  {ta.get('name')}  editor_type={ta.get('editor_type')}  html={len(html)} chars"
                      f"  has_play_link={'play.averillmahjong.com' in html}")


if __name__ == '__main__':
    main()
