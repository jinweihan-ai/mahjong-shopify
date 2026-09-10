#!/usr/bin/env python3
"""Plan A for editing a live flow email: create a new CODE template with the changed HTML, then try to point
the flow message at it. The relink is not in Klaviyo's published OpenAPI (stable or beta), so this is a
single careful attempt: if the relink is refused, the new template is deleted again and nothing changes.

    KLAVIYO_API_KEY=pk_... python tools/klaviyo_relink.py RAsZyQ VNjPcr     # template id, flow message id
"""
from __future__ import annotations

import os
import sys

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from klaviyo_add_link import BASE, HEADERS, LINK, RULES, build, get_html  # noqa: E402


def create_template(name: str, html: str) -> str:
    body = {'data': {'type': 'template', 'attributes': {'name': name, 'editor_type': 'CODE', 'html': html}}}
    r = requests.post(f'{BASE}/templates', headers=HEADERS, json=body, timeout=60)
    if r.status_code >= 400:
        raise SystemExit(f'create template: {r.status_code} {r.text[:300]}')
    return r.json()['data']['id']


def delete_template(tid: str) -> None:
    r = requests.delete(f'{BASE}/templates/{tid}', headers=HEADERS, timeout=30)
    print('cleanup delete template', tid, r.status_code)


def current_template(msg_id: str) -> tuple[str, bool]:
    r = requests.get(f'{BASE}/flow-messages/{msg_id}/template', headers=HEADERS, params={'fields[template]': 'name,html'}, timeout=30)
    r.raise_for_status()
    d = r.json()['data']
    return d['id'], LINK in (d['attributes'].get('html') or '')


def main() -> None:
    old_tid, msg_id = sys.argv[1], sys.argv[2]
    rule = RULES[old_tid]
    html = get_html(old_tid)
    if LINK.split('?')[0] in html:
        raise SystemExit('already has the link')
    new_html, _ = build(html, rule)
    name_r = requests.get(f'{BASE}/templates/{old_tid}', headers=HEADERS, params={'fields[template]': 'name'}, timeout=30)
    name = name_r.json()['data']['attributes']['name'] + ' (learn link)'
    new_tid = create_template(name, new_html)
    print('created template', new_tid, name)

    attempts = [
        ('PATCH flow-message relationships', f'{BASE}/flow-messages/{msg_id}',
         {'data': {'type': 'flow-message', 'id': msg_id, 'relationships': {'template': {'data': {'type': 'template', 'id': new_tid}}}}}),
        ('PATCH relationships/template', f'{BASE}/flow-messages/{msg_id}/relationships/template',
         {'data': {'type': 'template', 'id': new_tid}}),
    ]
    for label, url, body in attempts:
        r = requests.patch(url, headers=HEADERS, json=body, timeout=60)
        print(f'{label}: {r.status_code} {r.text[:200]}')
        if r.status_code < 300:
            tid, has = current_template(msg_id)
            print('message now uses template', tid, 'has link:', has)
            if tid == new_tid and has:
                print('RELINK OK')
                return
    delete_template(new_tid)
    print('RELINK NOT POSSIBLE: nothing changed')
    sys.exit(2)


if __name__ == '__main__':
    main()
