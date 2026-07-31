# Tag Filter Bug — 手动作业指南

> **Date**: 2026-07-31
> **Status**: 本地已修好。Live 站点仍然是 OLD JS (有 bug)
> **原因**: GitHub PAT 撤销 (401 Bad credentials)，无法 git push

## Bug 是什么

`index.html` 的 tag filter JS 把 `data-prefix="essay"` 跟 grid ID `essays-grid` 错配:

```js
// 当前 LIVE (有 bug)
const grid = document.getElementById(prefix + '-grid');
// prefix="essay" → 找 "essay-grid" → 不存在 → grid = null
// if (!grid) return;  ← 静默退出，啥也不做
```

所以 **Essays section 的所有 tag pill 点击无效**。
Quant section 因为 `quant` ↔ `quant-grid` 对得上，**实际是工作的**。

## 验证 bug（不用 deploy）

```
1. 打开 https://hermes-notes.pages.dev/
2. 按 F12 → Console
3. 点 Essays section 的 "ai" tag
4. 没反应 (因为 grid = null)
5. 再点 Quant section 的 "ml" tag
6. 应该 work (因为 quant-grid 存在)
```

## 修复 (改 3 行)

打开 https://github.com/chasejwang/hermes-notes/blob/main/index.html
搜 `Tag filter logic` (大概 line 759)

把这一段:
```js
    function applyFilter(prefix, tag) {
      const grid = document.getElementById(prefix + '-grid');
      if (!grid) {
        console.warn('[tag-filter] No grid found for prefix:', prefix);
        return;
      }
```

替换成:
```js
    function applyFilter(prefix, tag) {
      // Map prefix to actual grid ID (essay prefix → essays-grid, quant → quant-grid)
      const gridId = (prefix === 'essay' ? 'essays' : prefix) + '-grid';
      const grid = document.getElementById(gridId);
      if (!grid) {
        console.warn('[tag-filter] No grid found for id:', gridId);
        return;
      }
```

Commit message:
```
Fix tag filter: essay prefix → essays-grid id mapping
```

## 等 Cloudflare Pages 自动部署

1-2 分钟后 https://hermes-notes.pages.dev/ 会更新。

## 测试 fix

1. 打开 https://hermes-notes.pages.dev/
2. F12 → Console (应该有 `[tag-filter] ready, pills: 24` 输出)
3. 点 Essays section 的 "ai"
4. 应该看到 4 篇 AI 文章 (autoresearch, copilot, LLM Wiki, NLP path)
5. 其他 7 篇隐藏

## 替代方案 (如果你不想手动)

- 给我新 GitHub PAT (https://github.com/settings/tokens, 勾 `repo`)
- 给我 Cloudflare API token (dash.cloudflare.com → API Tokens, Custom: Account → Pages → Edit)

我马上推。

## 经验教训

- `data-prefix` 命名要跟 grid ID 保持一致 (单/复数要统一)
- JS 写完马上加 `console.log` 调试输出
- 部署前先在本地 server 验证 (这本来能在第一分钟抓出 bug)
- 推送后 hard reload (Cmd+Shift+R) 强制刷新
