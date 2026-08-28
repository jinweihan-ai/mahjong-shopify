#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
import os
import sys
from pathlib import Path

import requests


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_CONFIG_PATHS = [
    SCRIPT_DIR.parent / "config" / "thecrystaldreams.json",
    SCRIPT_DIR.parent / "config" / "default.json",
    Path.home() / ".shopify" / "thecrystaldreams.json",
    Path.home() / ".shopify" / "default.json",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Shopify Admin API helper")
    subparsers = parser.add_subparsers(dest="command", required=True)

    def add_auth_args(p: argparse.ArgumentParser) -> None:
        p.add_argument("--shop", help="your-store.myshopify.com")
        p.add_argument("--client-id")
        p.add_argument("--client-secret")
        p.add_argument("--api-version")
        p.add_argument("--config", help="Path to a Shopify JSON config file")

    token_parser = subparsers.add_parser("token")
    add_auth_args(token_parser)

    themes_parser = subparsers.add_parser("list-themes")
    add_auth_args(themes_parser)

    graphql_parser = subparsers.add_parser("graphql")
    add_auth_args(graphql_parser)
    graphql_group = graphql_parser.add_mutually_exclusive_group(required=True)
    graphql_group.add_argument("--query")
    graphql_group.add_argument("--query-file")
    graphql_parser.add_argument("--variables", default="{}")
    graphql_parser.add_argument("--variables-file")

    asset_get_parser = subparsers.add_parser("get-asset")
    add_auth_args(asset_get_parser)
    asset_get_parser.add_argument("--theme-id", required=True, type=int)
    asset_get_parser.add_argument("--key", required=True)

    asset_put_parser = subparsers.add_parser("put-asset")
    add_auth_args(asset_put_parser)
    asset_put_parser.add_argument("--theme-id", required=True, type=int)
    asset_put_parser.add_argument("--key", required=True)
    value_group = asset_put_parser.add_mutually_exclusive_group(required=True)
    value_group.add_argument("--value")
    value_group.add_argument("--value-file")

    rest_get_parser = subparsers.add_parser("rest-get")
    add_auth_args(rest_get_parser)
    rest_get_parser.add_argument("--path", required=True, help="e.g. products.json")

    return parser.parse_args()


def get_token(shop: str, client_id: str, client_secret: str) -> dict:
    response = requests.post(
        f"https://{shop}/admin/oauth/access_token",
        data={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        },
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def headers(token: str) -> dict[str, str]:
    return {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json",
    }


def read_text(value: str | None, value_file: str | None) -> str:
    if value is not None:
        return value
    return Path(value_file).read_text(encoding="utf-8")


def read_json_text(raw: str | None, raw_file: str | None) -> dict:
    if raw_file:
        return json.loads(Path(raw_file).read_text(encoding="utf-8"))
    return json.loads(raw or "{}")


def dump(payload) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def load_config(path: Path | None) -> dict:
    if path is not None:
        return json.loads(path.read_text(encoding="utf-8"))

    for candidate in DEFAULT_CONFIG_PATHS:
        if candidate.exists():
            return json.loads(candidate.read_text(encoding="utf-8"))

    return {}


def resolve_auth(args: argparse.Namespace) -> tuple[str, str, str, str]:
    config_path = Path(args.config).expanduser() if getattr(args, "config", None) else None
    config = load_config(config_path)

    shop = args.shop or os.getenv("SHOPIFY_SHOP") or config.get("shop")
    client_id = args.client_id or os.getenv("SHOPIFY_CLIENT_ID") or config.get("client_id")
    client_secret = (
        args.client_secret
        or os.getenv("SHOPIFY_CLIENT_SECRET")
        or config.get("client_secret")
    )
    api_version = (
        args.api_version
        or os.getenv("SHOPIFY_API_VERSION")
        or config.get("api_version")
        or "2026-01"
    )

    missing = []
    if not shop:
        missing.append("shop")
    if not client_id:
        missing.append("client_id")
    if not client_secret:
        missing.append("client_secret")

    if missing:
        locations = ", ".join(str(path) for path in DEFAULT_CONFIG_PATHS)
        raise SystemExit(
            "Missing Shopify auth values: "
            + ", ".join(missing)
            + ". Provide CLI args, env vars, or a config file. Default config paths: "
            + locations
        )

    return shop, client_id, client_secret, api_version


def main() -> int:
    args = parse_args()
    shop, client_id, client_secret, api_version = resolve_auth(args)
    token_payload = get_token(shop, client_id, client_secret)
    token = token_payload["access_token"]

    if args.command == "token":
        dump(token_payload)
        return 0

    if args.command == "list-themes":
        response = requests.get(
            f"https://{shop}/admin/api/{api_version}/themes.json",
            headers=headers(token),
            timeout=30,
        )
        response.raise_for_status()
        dump(response.json())
        return 0

    if args.command == "graphql":
        query = read_text(args.query, args.query_file)
        variables = read_json_text(args.variables, args.variables_file)
        response = requests.post(
            f"https://{shop}/admin/api/{api_version}/graphql.json",
            headers=headers(token),
            json={"query": query, "variables": variables},
            timeout=30,
        )
        response.raise_for_status()
        dump(response.json())
        return 0

    if args.command == "get-asset":
        response = requests.get(
            f"https://{shop}/admin/api/{api_version}/themes/{args.theme_id}/assets.json",
            headers=headers(token),
            params={"asset[key]": args.key},
            timeout=30,
        )
        response.raise_for_status()
        asset = response.json()["asset"]
        if "value" in asset:
            sys.stdout.write(asset["value"])
        else:
            dump(asset)
        return 0

    if args.command == "put-asset":
        value = read_text(args.value, args.value_file)
        response = requests.put(
            f"https://{shop}/admin/api/{api_version}/themes/{args.theme_id}/assets.json",
            headers=headers(token),
            json={"asset": {"key": args.key, "value": value}},
            timeout=30,
        )
        response.raise_for_status()
        dump(response.json())
        return 0

    if args.command == "rest-get":
        response = requests.get(
            f"https://{shop}/admin/api/{api_version}/{args.path.lstrip('/')}",
            headers=headers(token),
            timeout=30,
        )
        response.raise_for_status()
        dump(response.json())
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
