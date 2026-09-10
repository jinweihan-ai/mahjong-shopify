#!/usr/bin/env python3
"""Put the "learn to play" links into the live theme: a line under the Add-to-cart benefits on the
Charleston product page and a sentence in the FAQ page's "suitable for beginners" answer.

Credentials come from the environment only (never from this repo):
  SHOPIFY_SHOP=1129i1-nf.myshopify.com
  SHOPIFY_ACCESS_TOKEN=...            or   SHOPIFY_CLIENT_ID=... SHOPIFY_CLIENT_SECRET=...

  python tools/theme_learn_links.py inspect            # live theme, block schema, current blocks, FAQ answer
  python tools/theme_learn_links.py apply --dry-run    # print the exact files that would be written
  python tools/theme_learn_links.py apply              # back up to theme/backups/<ts>/, write, read back

The theme is edited with GraphQL themeFilesUpsert (Admin API 2025-07).
"""
from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

import requests

API = '2025-07'
ROOT = Path(__file__).resolve().parent.parent
PRODUCT_TEMPLATE = 'templates/product.charleston-garden-no-8.json'
PRODUCT_SECTION = 'sections/main-product.liquid'
APP = 'https://play.averillmahjong.com/'
PRODUCT_TEXT = 'New to the game? Learn to play in 10 minutes'
FAQ_SENTENCE = (
    ' If you have never played, our free online lessons at '
    f'<a href="{APP}?src=faq">play.averillmahjong.com</a> teach the game in about ten minutes, '
    'then let you practise against three patient opponents.'
)

FILES_QUERY = """
query($id: ID!, $names: [String!]) {
  theme(id: $id) {
    files(filenames: $names, first: 50) {
      nodes { filename body { ... on OnlineStoreThemeFileBodyText { content } } }
    }
  }
}
"""
LIST_QUERY = """
query($id: ID!, $after: String) {
  theme(id: $id) {
    files(first: 250, after: $after) { pageInfo { hasNextPage endCursor } nodes { filename } }
  }
}
"""
UPSERT = """
mutation($id: ID!, $files: [OnlineStoreThemeFilesUpsertFileInput!]!) {
  themeFilesUpsert(themeId: $id, files: $files) {
    upsertedThemeFiles { filename }
    userErrors { field message }
  }
}
"""


class Shop:
    def __init__(self) -> None:
        self.shop = os.environ['SHOPIFY_SHOP']
        token = os.environ.get('SHOPIFY_ACCESS_TOKEN')
        if not token:
            r = requests.post(
                f'https://{self.shop}/admin/oauth/access_token',
                data={
                    'grant_type': 'client_credentials',
                    'client_id': os.environ['SHOPIFY_CLIENT_ID'],
                    'client_secret': os.environ['SHOPIFY_CLIENT_SECRET'],
                },
                timeout=30,
            )
            r.raise_for_status()
            token = r.json()['access_token']
        self.h = {'X-Shopify-Access-Token': token, 'Content-Type': 'application/json'}

    def gql(self, query: str, variables: dict | None = None) -> dict:
        r = requests.post(
            f'https://{self.shop}/admin/api/{API}/graphql.json',
            headers=self.h,
            json={'query': query, 'variables': variables or {}},
            timeout=60,
        )
        r.raise_for_status()
        body = r.json()
        if body.get('errors'):
            raise SystemExit(json.dumps(body['errors'], indent=2, ensure_ascii=False))
        return body['data']

    def live_theme(self) -> dict:
        d = self.gql('{ themes(first: 5, roles: [MAIN]) { nodes { id name role } } }')
        return d['themes']['nodes'][0]

    def files(self, theme_id: str, names: list[str]) -> dict[str, str]:
        d = self.gql(FILES_QUERY, {'id': theme_id, 'names': names})
        return {n['filename']: n['body'].get('content', '') for n in d['theme']['files']['nodes']}

    def list_files(self, theme_id: str, prefix: str) -> list[str]:
        out: list[str] = []
        cursor = None
        while True:
            d = self.gql(LIST_QUERY, {'id': theme_id, 'after': cursor})
            f = d['theme']['files']
            out += [n['filename'] for n in f['nodes'] if n['filename'].startswith(prefix)]
            if not f['pageInfo']['hasNextPage']:
                return out
            cursor = f['pageInfo']['endCursor']

    def upsert(self, theme_id: str, files: dict[str, str]) -> None:
        payload = [{'filename': k, 'body': {'type': 'TEXT', 'value': v}} for k, v in files.items()]
        d = self.gql(UPSERT, {'id': theme_id, 'files': payload})
        errs = d['themeFilesUpsert']['userErrors']
        if errs:
            raise SystemExit(json.dumps(errs, indent=2, ensure_ascii=False))


def schema_of(liquid: str) -> dict:
    m = re.search(r'{%-?\s*schema\s*-?%}(.*?){%-?\s*endschema\s*-?%}', liquid, re.S)
    return json.loads(m.group(1)) if m else {}


def faq_template(shop: Shop, theme_id: str) -> tuple[str, str]:
    for name in shop.list_files(theme_id, 'templates/page.'):
        body = shop.files(theme_id, [name]).get(name, '')
        if 'codex-faq' in body:
            return name, body
    raise SystemExit('no page template with a codex-faq section')


def build_product(template: str, block_schema: dict) -> str:
    """Adds one benefit line after the delivery line, cloning its icon settings."""
    data = json.loads(template)
    blocks = data['sections']['main']['blocks']
    order = data['sections']['main']['block_order']
    if 'learn_to_play' in blocks:
        raise SystemExit('product template already has the learn_to_play block')
    src_id = 'custom_information_delivery_14' if 'custom_information_delivery_14' in blocks else next(
        k for k, b in blocks.items() if b['type'] == 'custom_information' and b['settings'].get('show_as_benefit')
    )
    block = copy.deepcopy(blocks[src_id])
    settings = block_schema.get('settings', [])
    text_ids = [s['id'] for s in settings if s.get('type') in ('richtext', 'inline_richtext', 'html', 'text', 'textarea')]
    url_ids = [s['id'] for s in settings if s.get('type') == 'url']
    if not text_ids:
        raise SystemExit(f'custom_information has no text setting; ids: {[s.get("id") for s in settings]}')
    rich = any(s.get('type') in ('richtext', 'inline_richtext', 'html') for s in settings if s['id'] == text_ids[0])
    link = f'{APP}?src=product'
    for sid in text_ids:
        block['settings'][sid] = ''
    block['settings'][text_ids[0]] = f'<p><a href="{link}">{PRODUCT_TEXT}</a></p>' if rich else PRODUCT_TEXT
    for sid in url_ids:
        block['settings'][sid] = link
    blocks['learn_to_play'] = block
    order.insert(order.index(src_id) + 1, 'learn_to_play')
    return json.dumps(data, indent=2, ensure_ascii=False) + '\n'


def build_faq(template: str) -> str:
    data = json.loads(template)
    for sec in data['sections'].values():
        for blk in (sec.get('blocks') or {}).values():
            q = str(blk.get('settings', {}).get('question', ''))
            if 'suitable for beginners' in q.lower():
                ans = blk['settings']['answer'].rstrip()
                if 'play.averillmahjong.com' in ans:
                    raise SystemExit('FAQ answer already has the link')
                if ans.endswith('</p>'):
                    blk['settings']['answer'] = ans[: -len('</p>')] + FAQ_SENTENCE + '</p>'
                else:
                    blk['settings']['answer'] = ans + FAQ_SENTENCE
                return json.dumps(data, indent=2, ensure_ascii=False) + '\n'
    raise SystemExit('no "suitable for beginners" question in the FAQ template')


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('inspect')
    a = sub.add_parser('apply')
    a.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    shop = Shop()
    theme = shop.live_theme()
    print('live theme:', theme['name'], theme['id'])
    got = shop.files(theme['id'], [PRODUCT_TEMPLATE, PRODUCT_SECTION])
    schema = schema_of(got[PRODUCT_SECTION])
    block_schema = next((b for b in schema.get('blocks', []) if b.get('type') == 'custom_information'), {})
    faq_name, faq_body = faq_template(shop, theme['id'])

    if args.cmd == 'inspect':
        print('main-product block types:', [b.get('type') for b in schema.get('blocks', [])])
        print('custom_information settings:', [(s.get('id'), s.get('type')) for s in block_schema.get('settings', [])])
        main_section = json.loads(got[PRODUCT_TEMPLATE])['sections']['main']
        for k in main_section['block_order']:
            b = main_section['blocks'][k]
            if b['type'] == 'custom_information':
                print(k, json.dumps(b['settings'], ensure_ascii=False)[:300])
        print('FAQ template:', faq_name)
        for sec in json.loads(faq_body)['sections'].values():
            for blk in (sec.get('blocks') or {}).values():
                if 'beginners' in str(blk.get('settings', {}).get('question', '')).lower():
                    print(json.dumps(blk['settings'], ensure_ascii=False))
        return

    new_product = build_product(got[PRODUCT_TEMPLATE], block_schema)
    new_faq = build_faq(faq_body)
    if args.dry_run:
        print(new_product)
        print(new_faq)
        return
    stamp = dt.datetime.now().strftime('%Y%m%d-%H%M%S')
    bdir = ROOT / 'theme' / 'backups' / stamp
    for name, body in ((PRODUCT_TEMPLATE, got[PRODUCT_TEMPLATE]), (faq_name, faq_body)):
        p = bdir / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body, encoding='utf-8')
    print('backup:', bdir)
    shop.upsert(theme['id'], {PRODUCT_TEMPLATE: new_product, faq_name: new_faq})
    back = shop.files(theme['id'], [PRODUCT_TEMPLATE, faq_name])
    ok = 'learn_to_play' in back[PRODUCT_TEMPLATE] and 'play.averillmahjong.com' in back[faq_name]
    print('read back:', 'ok' if ok else 'MISMATCH')
    if not ok:
        sys.exit(1)


if __name__ == '__main__':
    main()
