#!/usr/bin/env python3
"""Add "learn to play" links to a Shopify journal article through the Admin GraphQL API.

    SHOPIFY_SHOP=1129i1-nf.myshopify.com SHOPIFY_CLIENT_ID=... SHOPIFY_CLIENT_SECRET=... \\
      python tools/article_add_link.py show 618480894249          # outline of the body: block tags and first words
      python tools/article_add_link.py apply 618480894249 --dry   # print the two insertions in context
      python tools/article_add_link.py apply 618480894249         # back up, update, read back

Credentials come from the environment only. The update keeps the article published with its original
publish date (an update that omits those can unpublish a post). Backups: ~/companion/shopify-backups/.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

import requests

API = '2025-07'
LINK = 'https://play.averillmahjong.com/?src=blog'
BACKUPS = Path.home() / 'companion' / 'shopify-backups'

# per article: (anchor that exists once, 'after' the block that contains it, html to insert)
RULES = {
    '618480894249': [
        {
            'after': 'first </p>',
            'html': '<p><em>Prefer to learn by doing?</em> Our free practice table deals you a hand and walks you through it with three '
                    'patient players who explain every move: <a href="{link}" target="_blank" rel="noopener">play.averillmahjong.com</a>.</p>',
        },
        {
            'before': 'last <h2',
            'html': '<p>Want to see these rules in motion before the box arrives? <a href="{link}" target="_blank" rel="noopener">'
                    'Play a practice hand</a> and the coach will call out every step. Free, and no account needed.</p>',
        },
    ],
}


class Shop:
    def __init__(self) -> None:
        self.shop = os.environ['SHOPIFY_SHOP']
        r = requests.post(
            f'https://{self.shop}/admin/oauth/access_token',
            data={'grant_type': 'client_credentials', 'client_id': os.environ['SHOPIFY_CLIENT_ID'], 'client_secret': os.environ['SHOPIFY_CLIENT_SECRET']},
            timeout=30,
        )
        r.raise_for_status()
        self.h = {'X-Shopify-Access-Token': r.json()['access_token'], 'Content-Type': 'application/json'}

    def gql(self, query: str, variables: dict) -> dict:
        r = requests.post(f'https://{self.shop}/admin/api/{API}/graphql.json', headers=self.h, json={'query': query, 'variables': variables}, timeout=60)
        r.raise_for_status()
        body = r.json()
        if body.get('errors'):
            raise SystemExit(json.dumps(body['errors'], indent=2, ensure_ascii=False))
        return body['data']

    def article(self, aid: str) -> dict:
        d = self.gql('query($id: ID!) { article(id: $id) { id title handle body isPublished publishedAt } }', {'id': f'gid://shopify/Article/{aid}'})
        return d['article']

    def update_body(self, art: dict, body: str) -> dict:
        d = self.gql(
            '''mutation($id: ID!, $article: ArticleUpdateInput!) {
                 articleUpdate(id: $id, article: $article) { article { id body isPublished publishedAt } userErrors { field message } } }''',
            {'id': art['id'], 'article': {'body': body, 'isPublished': True, 'publishDate': art['publishedAt']}},
        )
        errs = d['articleUpdate']['userErrors']
        if errs:
            raise SystemExit(json.dumps(errs, indent=2, ensure_ascii=False))
        return d['articleUpdate']['article']


def outline(body: str) -> str:
    out = []
    for m in re.finditer(r'<(p|h1|h2|h3|ul|ol|table|nav|div)\b[^>]*>(.*?)</\1>', body, re.S):
        text = re.sub(r'<[^>]+>', ' ', m.group(2))
        text = re.sub(r'\s+', ' ', text).strip()
        out.append(f'{m.group(1):5} @{m.start():6} | {text[:90]}')
    return '\n'.join(out)


def build(body: str, rules: list[dict]) -> str:
    for rule in rules:
        html = '\n\n' + rule['html'].format(link=LINK) + '\n\n'
        if rule.get('after') == 'first </p>':
            i = body.index('</p>') + len('</p>')
            body = body[:i] + html + body[i:]
        elif rule.get('before') == 'last <h2':
            # inside the closing "Ready to put the rules to work" section: after its first paragraph
            i = body.index('</p>', body.rfind('<h2')) + len('</p>')
            body = body[:i] + html + body[i:]
        else:
            raise SystemExit(f'unknown rule {rule}')
    return body


def main() -> None:
    cmd, aid = sys.argv[1], sys.argv[2]
    shop = Shop()
    art = shop.article(aid)
    print(f"{art['title']}  published={art['isPublished']} at {art['publishedAt']}  body={len(art['body'])} chars")
    if cmd == 'show':
        print(outline(art['body']))
        return
    if LINK.split('?')[0] in art['body']:
        raise SystemExit('article already links to the app')
    new = build(art['body'], RULES[aid])
    if '--dry' in sys.argv:
        for m in re.finditer(re.escape(LINK.split('?')[0]), new):
            print('...', re.sub(r'\s+', ' ', new[max(0, m.start() - 260): m.start() + 160]), '...\n')
        return
    BACKUPS.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now().strftime('%Y%m%d-%H%M%S')
    (BACKUPS / f'article-{aid}-{stamp}.html').write_text(art['body'], encoding='utf-8')
    res = shop.update_body(art, new)
    ok = res['body'].count(LINK) == 2 and res['isPublished'] and res['publishedAt'] == art['publishedAt']
    print('updated, read back:', 'ok' if ok else 'MISMATCH', res['isPublished'], res['publishedAt'])
    if not ok:
        sys.exit(1)


if __name__ == '__main__':
    main()
