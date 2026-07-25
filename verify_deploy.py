"""
Cloudflare Pages 部署验证脚本
用法: python3 verify_deploy.py <url>
"""
import sys
import requests
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python3 verify_deploy.py <url>")
    sys.exit(1)

url = sys.argv[1].rstrip('/')

print(f"🔍 验证 {url} ...")
print()

checks = []

# 1. 首页
try:
    r = requests.get(url, timeout=30)
    if r.status_code == 200:
        title = r.text.split('<title>')[1].split('</title>')[0] if '<title>' in r.text else 'N/A'
        size = len(r.text)
        print(f"✅ 首页: HTTP {r.status_code}")
        print(f"   标题: {title}")
        print(f"   大小: {size:,} 字符")
        checks.append(('首页', True))
    else:
        print(f"❌ 首页: HTTP {r.status_code}")
        checks.append(('首页', False))
except Exception as e:
    print(f"❌ 首页: {e}")
    checks.append(('首页', False))

print()

# 2. 资源
for path in ['article.html?id=01', 'article.html?id=02', 'article.html?id=03']:
    try:
        r = requests.get(f"{url}/{path}", timeout=30)
        if r.status_code == 200:
            print(f"✅ {path}: HTTP {r.status_code}")
            checks.append((path, True))
        else:
            print(f"❌ {path}: HTTP {r.status_code}")
            checks.append((path, False))
    except Exception as e:
        print(f"❌ {path}: {e}")
        checks.append((path, False))

print()

# 3. 音频
for audio in ['audio/01-rag-summary.mp3', 'audio/02-value-quant-summary.mp3', 'audio/03-memory-cycle-summary.mp3']:
    try:
        r = requests.head(f"{url}/{audio}", timeout=30)
        if r.status_code == 200:
            size = int(r.headers.get('Content-Length', 0))
            print(f"✅ {audio}: HTTP {r.status_code} ({size:,} bytes)")
            checks.append((audio, True))
        else:
            print(f"❌ {audio}: HTTP {r.status_code}")
            checks.append((audio, False))
    except Exception as e:
        print(f"❌ {audio}: {e}")
        checks.append((audio, False))

print()

# 4. 封面
for img in ['images/01-rag.jpg', 'images/02-value.jpg', 'images/03-memory-cycle.svg']:
    try:
        r = requests.head(f"{url}/{img}", timeout=30)
        if r.status_code == 200:
            print(f"✅ {img}: HTTP {r.status_code}")
            checks.append((img, True))
        else:
            print(f"❌ {img}: HTTP {r.status_code}")
            checks.append((img, False))
    except Exception as e:
        print(f"❌ {img}: {e}")
        checks.append((img, False))

print()
print("=" * 50)
passed = sum(1 for _, ok in checks if ok)
total = len(checks)
print(f"📊 结果: {passed}/{total} 项通过")
if passed == total:
    print("🎉 部署成功！所有资源都可访问。")
else:
    print(f"⚠️  {total - passed} 项失败，请检查。")
