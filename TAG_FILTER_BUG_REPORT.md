# Tag Filter — Bug + Fix 记录

> **日期**: 2026-07-31
> **状态**: Bug 已找到 + 修复在本地，**未部署**

## Bug

`index.html` 的 tag filter JS 有命名不匹配 bug：

| 前缀 (data-prefix) | 实际 grid ID | 状态 |
|---|---|---|
| `essay` | `essays-grid` | ❌ 不匹配 (差一个 's') |
| `quant` | `quant-grid` | ✅ 匹配 |

JS 代码：
```js
const grid = document.getElementById(prefix + '-grid');
// prefix="essay" → 找 "essay-grid" → 不存在 → grid = null
// prefix="quant" → 找 "quant-grid" → 存在 → 工作
```

**结果**: Essays section 的 tag pill 点击完全无效 (用户点任何 essay tag，都被 `if (!grid) return;` 拦截)。Quant section 实际**是工作的**。

## Fix

把 `applyFilter` 改成：

```js
function applyFilter(prefix, tag) {
  // Map prefix to actual grid ID (essay prefix → essays-grid, quant → quant-grid)
  const gridId = (prefix === 'essay' ? 'essays' : prefix) + '-grid';
  const grid = document.getElementById(gridId);
  if (!grid) {
    console.warn('[tag-filter] No grid found for id:', gridId);
    return;
  }
  // ... rest unchanged
}
```

同时把整个 JS 重写成 **event delegation** 模式（一个 document 级 listener，检查 click 目标是不是 tag-pill），并加了 `console.log` 调试输出。

## 部署状态

- **本地**: `index.html` 已经修好 (30,506 bytes)
- **GitHub**: 推不上去，PAT `ghp_5A5Iqy5f4ttKkUWPmRbs2PxqBYub1FOclc` 已被撤销 (401 Bad credentials)
- **CF Pages**: live 站点是 OLD JS，没有 fix

## 验证 fix 真的修好

```bash
# 启动本地 server
cd ~/Documents/Code/articles-site
python3 -m http.server 8080

# 在浏览器打开
open "http://127.0.0.1:8080/"

# 试 Essays section 的 tag pill
# 应该看到 console.log:
#   [tag-filter] ready, pills: 24
#   [tag-filter] prefix=essay tag=ai visible=4/11
```

## 部署需要

任一：

1. **新的 GitHub PAT** (github.com/settings/tokens, 勾 `repo` 权限)
2. **Cloudflare API token** (dash.cloudflare.com → API Tokens → Create Custom Token → Account → Cloudflare Pages → Edit)
3. **手动 push** (用户在浏览器登录 GitHub Web，merge 一个 PR，或者直接 GitHub Web 编辑 index.html)

## 经验教训 (memory entry)

- **CSS / HTML 命名不匹配是 JS 死代码的最常见原因**
- **调试时加 `console.log` 显式打印** — 这本来能在第一分钟就发现
- **data-prefix 命名要和 grid ID 保持一致** — 这次错在 prefix 用单数 (essay)，ID 用复数 (essays-grid)
- **live site 跟本地代码可能差几个小时** — 推送后等 CF Pages build 完，浏览器可能要 hard reload (Cmd+Shift+R)
