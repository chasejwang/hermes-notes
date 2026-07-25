# Hermes Notes · 公众号文章站

Apple 简约风格 · 公众号文章 + 音频 · 部署到 Cloudflare Pages

## 📂 目录结构

```
.
├── index.html              # 首页（文章列表）
├── article.html            # 文章详情页（含音频）
├── articles/               # 3 篇文章（Markdown）
├── audio/                  # 3 个音频（MiniMax TTS）
└── images/                 # 封面图
```

## 🎨 设计

- **风格**：Apple 简约（白底 · SF Pro · 大留白 · 干净）
- **强调色**：Apple Blue #0066cc
- **遵循规则**：taste-skill anti-slop（无渐变 · 无 emoji · 无衬线大标）

## 🚀 部署到 Cloudflare Pages

### 方法 1：Git 集成（推荐）

1. 推送到 GitHub
2. https://dash.cloudflare.com → Pages
3. Connect to Git → 选择仓库
4. Build settings:
   - Framework preset: None
   - Build command: （空）
   - Build output directory: /
5. Save and Deploy
6. 拿到 `xxx.pages.dev`

### 方法 2：直接上传

1. https://dash.cloudflare.com → Pages
2. Create → Direct Upload
3. 项目名称
4. 上传整个文件夹
5. Deploy

## 🔗 链接

- 完整部署研究：`~/Documents/Obsidian Vault/Finance/_部署研究/`
- 项目主页：`https://github.com/javis/articles-site`
