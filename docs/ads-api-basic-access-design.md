# Averill Mahjong — Google Ads API Tool Design Document

*Prepared for the Google Ads API Basic Access application · September 5, 2026*

## 1. Company and account

| Item | Value |
| --- | --- |
| Company | Averill Mahjong (brand of an independent direct-to-consumer e-commerce store) |
| Website | https://averillmahjong.com (Shopify storefront, live) |
| Business | We design and sell American mahjong sets online. We advertise our own products only. |
| Google Ads manager account (MCC) | 593-654-7386 |
| Advertiser account managed | 407-451-4233 (our own single account) |
| Google Cloud project number | 638468010830 (project ID: mahjong-seo) |
| API contact | jinwei.han93@gmail.com (founder, monitored daily) |

We do not manage accounts for clients or third parties. The tool serves one advertiser: ourselves.

## 2. What the tool is

An internal, automated **daily reporting assistant**. Once a day it reads performance data from our Google Ads account through the Google Ads API, combines it with our store orders and Search Console data, and posts a short summary to our team chat (Feishu / Lark). A second internal use is **keyword research for our own SEO content planning**: we want to read Keyword Planner idea and volume data to decide which help articles to write for our blog.

The tool is **read-only by design**. It never creates, edits, pauses, or removes campaigns, ad groups, ads, keywords, budgets, or bids. Account changes are made by humans in the Google Ads web interface. The tool's own policy forbids calling any mutate method.

## 3. Users

Internal users only: the founder and two employees who read the daily report in our team chat. Nobody outside the company has access to the tool, the developer token, or the reports. There is no customer-facing interface.

## 4. Architecture and data flow

1. **Scheduler** — a hosted routine runs once per day at 09:00 Beijing time. On-demand reruns can be requested by a team member in the chat group.
2. **Authentication** — OAuth 2.0 with a refresh token belonging to the account owner. The refresh token is stored on our own server (Ubuntu VM, file permissions 0600). The routine requests a short-lived access token from that server; it never holds the refresh token.
3. **Google Ads API calls** — REST `googleAds:searchStream` with GAQL, using the manager account as `login-customer-id`. Reports pulled daily:
   - Campaign metrics by day for the last 14 days (cost, clicks, impressions, CPC, CTR, conversions, conversion value)
   - Conversion actions breakdown
   - Search impression share and lost impression share for the search campaign
   - `change_event` for the last 2 days (to audit who changed what in the account)
   - Occasionally `user_location_view`, `geo_target_constant`, and `click_view` to reconcile Google Ads conversions with store orders by state
   - With Basic access: `KeywordPlanIdeaService` (generate keyword ideas and historical metrics) for our SEO content calendar, roughly once a week
4. **Other data sources** — Shopify Admin API (our orders), Google Search Console API, Google Analytics 4 Data API, Merchant API. All read-only.
5. **Output** — one card message plus one chart image per day in our internal chat. No data leaves the company.

Estimated volume: fewer than 30 API operations per day, well under the Explorer and Basic access quotas.

## 5. Security and compliance

- Credentials live only on our server and in the scheduler's private configuration; they are not committed to source control.
- The tool is single-tenant: one company, one advertiser account, one manager account.
- No data is resold, shared, or exposed to any third party. Reports are visible only to our employees.
- The tool complies with the Google Ads API Terms and Conditions and the Required Minimum Functionality rules do not apply because the tool has no campaign management functionality.

## 6. Why Basic access

Explorer access covers our daily reporting today. We are applying for Basic access to use Keyword Planner data (keyword ideas and search volumes) for planning our own educational blog content, and for headroom as the report grows. We do not build tools for external users and have no plans to.

## 7. Contact

Jinwei Han, founder — jinwei.han93@gmail.com — Averill Mahjong, https://averillmahjong.com
