# 飞书群 @bot 重跑供应链日报 —— 事件驱动链路

## 链路总览

```
飞书群 @Daily Report Bot "重跑供应链"
  → 飞书事件订阅回调 → Vercel 函数（本文件代码，部署在张勇的 Vercel 项目）
  → GitHub API 在 jinweihan-ai/mahjong-shopify 开一个 issue（标题「供应链重跑」）
  → Claude webhook 触发器（issues:opened → 云任务 trig_01GNza5w5wLagyf6m8JZUC6n）
  → 云端跑供应链日报（标题带「（按需重跑）」）→ Bot 发回群里
```

预计延迟 1-3 分钟。护栏：只认指定群 chat_id、只认 @bot 且含"供应链"+"重跑/再跑/rerun"的消息、webhook 过滤器只认 issues 的 opened 动作（关闭 issue 不会重复触发）。

## Vercel 函数（api/feishu-event.js）

```js
export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).end();
  const body = req.body || {};

  // 飞书 URL 验证握手
  if (body.type === 'url_verification') {
    if (process.env.FEISHU_VERIFICATION_TOKEN && body.token !== process.env.FEISHU_VERIFICATION_TOKEN)
      return res.status(403).end();
    return res.status(200).json({ challenge: body.challenge });
  }

  const header = body.header || {};
  if (process.env.FEISHU_VERIFICATION_TOKEN && header.token !== process.env.FEISHU_VERIFICATION_TOKEN)
    return res.status(403).end();

  try {
    if (header.event_type === 'im.message.receive_v1') {
      const msg = (body.event || {}).message || {};
      // 只认日报群
      if (msg.chat_id === 'oc_f92e446e402e2b73b3968e15e3c377c9') {
        const mentions = msg.mentions || [];
        const atBot = mentions.length > 0; // 群内 @ 了应用机器人才会带 mentions
        let text = '';
        try { text = (JSON.parse(msg.content || '{}').text || ''); } catch {}
        if (atBot && text.includes('供应链') && /重跑|再跑|rerun/i.test(text)) {
          await fetch('https://api.github.com/repos/jinweihan-ai/mahjong-shopify/issues', {
            method: 'POST',
            headers: {
              Authorization: `Bearer ${process.env.GH_TOKEN}`,
              'Content-Type': 'application/json',
              'User-Agent': 'feishu-rerun',
              Accept: 'application/vnd.github+json',
            },
            body: JSON.stringify({
              title: '供应链重跑',
              body: `由飞书群 @bot 触发（消息时间 ${new Date().toISOString()}）。云任务完成后本 issue 可随手关闭。`,
              labels: ['auto-rerun'],
            }),
          });
        }
      }
    }
  } catch (e) {
    console.error('feishu-event error', e);
  }
  return res.status(200).json({});
}
```

## 部署配置（张勇）

1. 把上面文件放进 Vercel 项目 `api/feishu-event.js`，部署后得到公网地址 `https://<项目域名>/api/feishu-event`
2. 环境变量两枚：
   - `GH_TOKEN`：GitHub fine-grained PAT，仓库限定 jinweihan-ai/mahjong-shopify，权限只勾 **Issues: Read and write**（店主创建后交给张勇配置）
   - `FEISHU_VERIFICATION_TOKEN`：飞书应用「事件订阅」页面的 Verification Token（可先留空跳过校验，联调通过后补上）

## 飞书控制台配置（店主）

1. 开发者后台 → Daily Report Bot → **权限管理**：开通「接收群聊中@机器人消息事件」（im:message.group_at_msg:readonly，只读、最小权限）
2. **事件订阅**：请求地址填 Vercel 函数地址（保存时飞书会发 challenge 握手，函数已处理）；**不要启用 Encrypt Key**（留空，函数按明文解析）
3. 添加事件：**接收消息 im.message.receive_v1**
4. 创建版本并发布

## Claude 侧（已配置完成，无需操作）

- 云任务「供应链重跑（群@事件入口）」trig_01GNza5w5wLagyf6m8JZUC6n：与每日供应链专报同一 SKILL/流程，固定发日报体例，标题带「（按需重跑）」；cron 为年度占位（每年 1/1），实际靠事件唤起
- webhook 触发器 7c0ed7b0：github issues(opened) on jinweihan-ai/mahjong-shopify → 唤起上述云任务
- **前置条件**：Claude GitHub App 需安装在 jinweihan-ai/mahjong-shopify 仓库（github.com/apps/claude → Install → 选择该仓库），否则 GitHub 事件到不了 Claude 平台

## 已验证/待验证

- ✅ webhook 触发器创建、issues(opened) 过滤器
- ✅ repository_dispatch 事件平台不转发（已弃用该路径）
- ⬜ GitHub App 安装后，开 issue → 云任务唤起（安装完成后开一个「供应链重跑」issue 即可验收）
- ⬜ Vercel 部署后，群内 @bot 全链路
