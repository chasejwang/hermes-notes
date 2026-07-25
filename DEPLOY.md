# 🚀 Hermes Notes · 部署指南

> **Apple 简约 + Indie Granola 风格** · 公众号文章 + 音频 · Cloudflare Pages

---

## 📋 **部署前清单**

- [x] 静态网站（2.8 MB）· 5 个 HTML + 3 个 MD + 3 个 MP3
- [x] Apple 简约设计
- [x] Indie Granola 风格应用
- [x] 3 篇公众号文章 + 音频
- [x] README + 部署说明

---

## 🚀 **部署到 Cloudflare Pages · 3 步**

### **步骤 1**：推送到 GitHub

#### **方法 A：用 GitHub Desktop（最简单）**

1. 下载 [GitHub Desktop](https://desktop.github.com)
2. File → New Repository → 选 `/Users/javis/Documents/Code/articles-site`
3. Commit to main
4. Publish to GitHub → 选 public

#### **方法 B：用 git 命令（需要先配置 SSH / Token）**

```bash
cd /Users/javis/Documents/Code/articles-site

# 1. 配置 git（首次）
git config --global user.name "Javis"
git config --global user.email "your-email@example.com"

# 2. 提交
git add .
git commit -m "Initial: Hermes Notes article site"

# 3. 创建 GitHub 仓库
# 访问 https://github.com/new
# Repository name: hermes-notes
# Public
# 不要勾选 README / .gitignore（已有）

# 4. 推送
git remote add origin https://github.com/你的用户名/hermes-notes.git
git branch -M main
git push -u origin main
```

---

### **步骤 2**：连接 Cloudflare Pages

1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com)
2. **Workers & Pages** → **Pages** → **Create a project**
3. **Connect to Git** → 选 GitHub → 授权
4. 选 `hermes-notes` 仓库
5. **Build settings**：

| 设置 | 值 |
|---|---|
| Framework preset | **None** |
| Build command | **（空）** |
| Build output directory | **/** |
| Root directory | **（空）** |

6. **Save and Deploy**
7. 等待 1-2 分钟 → 拿到 `xxx.pages.dev`

---

### **步骤 3**：（可选）自定义域名

1. Cloudflare Pages → 你的项目 → **Custom domains**
2. 输入你的域名（如 `notes.javis.com`）
3. 添加 CNAME 记录到你的 DNS
4. Cloudflare 自动签发 SSL 证书

---

## 🎨 **网站功能**

| 功能 | 状态 |
|---|---|
| ✅ Apple 简约 + Indie Granola 风格 | **完成** |
| ✅ 3 篇文章展示 | ✅ |
| ✅ 文章详情页（含 Markdown 渲染）| ✅ |
| ✅ 3 个 MiniMax TTS 音频 | ✅ |
| ✅ 内嵌 HTML5 音频播放器 | ✅ |
| ✅ 响应式（3 列 → 1 列）| ✅ |
| ✅ 0 emoji · 0 渐变 · taste-skill anti-slop | ✅ |

---

## 📂 **项目结构**

```
articles-site/
├── index.html               # 首页（文章列表 + Hero + About）
├── article.html             # 文章详情（音频内嵌）
├── README.md                # 本文档
├── articles/                # 3 篇 Markdown 源
│   ├── 01-rag-vs-autorag.md
│   ├── 02-value-quant.md
│   └── 03-memory-cycle.md
├── audio/                   # 3 个 MiniMax TTS 音频
│   ├── 01-rag-summary.mp3
│   ├── 02-value-quant-summary.mp3
│   └── 03-memory-cycle-summary.mp3
└── images/                  # 封面图
    ├── 01-rag.jpg
    ├── 02-value.jpg
    └── 03-memory-cycle.svg
```

---

## 🔗 **本地预览**

```bash
# 打开 index.html（任意方式）
open /Users/javis/Documents/Code/articles-site/index.html
```

或用 Python 起一个简单 HTTP server：

```bash
cd /Users/javis/Documents/Code/articles-site
python3 -m http.server 8080
# 访问 http://localhost:8080
```

---

## 🎨 **设计来源**

| 元素 | 风格 |
|---|---|
| 底色 | Indie Granola · 暖米 #faf8f2 + 径向暖渐变 |
| 强调色 | 陶土 #b45837 |
| 显示字体 | PP Editorial New 衬线（fallback: Lyon Text / Georgia） |
| 正文字体 | Söhne / Inter / SF Pro |
| 毛玻璃 | backdrop-filter blur(16px) saturate(150%) |
| 软阴影 | rgba(180, 88, 55, 0.08) |
| 字重 | 400-500（轻量感 · 避免粗体） |

---

## 🎤 **音频制作**

3 个音频用 **MiniMax TTS** 制作：
- 模型：`speech-2.8-hd`
- 音色：`male-qn-jingying`（精英青年男声）
- 情绪：`calm`（沉稳）
- 成本：约 **¥0.20** 全部

---

## 📚 **相关资料**

- [Cloudflare Pages 文档](https://developers.cloudflare.com/pages/)
- [Indie Granola DESIGN.md](https://github.com/rohitg00/awesome-claude-design/blob/main/design-md/indie/granola.md)
- [taste-skill GitHub](https://github.com/Leonxlnx/taste-skill)
- [MiniMax TTS 文档](https://api.minimaxi.com)

---

## 📌 **更新文章流程**

```bash
# 1. 写新文章
echo "# 新文章..." > articles/04-new.md

# 2. 生成音频
python3 ~/.hermes/skills/creative/minimax-speech/scripts/gen_speech.py \
  --text "..." \
  --voice male-qn-jingying \
  --model speech-2.8-hd \
  --output audio/04-new-summary.mp3

# 3. 在 article.html 的 articles 对象中加 04 条目

# 4. 在 index.html 加 04 卡片

# 5. 提交 + 推送
git add .
git commit -m "Add 04 article"
git push
```

Cloudflare Pages 会**自动检测 push → 自动重新部署**。

---

*部署指南 · 2026-07-24 · Hermes Agent*
