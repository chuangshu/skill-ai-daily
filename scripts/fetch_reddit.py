#!/usr/bin/env python3
"""Reddit AI 热门帖子抓取 - 使用 RSSHub"""

import urllib.request
import json
from datetime import datetime

# 使用 RSSHub 提供的 Reddit RSS（不受限制）
RSS_URLS = [
    ("https://rsshub.app/reddit/top/artificial", "artificial"),
    ("https://rsshub.app/reddit/top/MachineLearning", "MachineLearning"),
    ("https://rsshub.app/reddit/top/OpenAI", "OpenAI"),
]

OUTPUT_FILE = "/root/clawd/reddit-ai/data/reddit_hot.json"

def fetch_reddit():
    posts = []
    
    for url, sub in RSS_URLS:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=15) as response:
                data = response.read().decode('utf-8')
                
                # 解析 RSSHub 格式
                import re
                items = re.findall(r'<item[^>]*>(.*?)</item>', data, re.DOTALL)
                
                for item in items[:10]:  # 每个 subreddit 取前10条
                    title_match = re.search(r'<title>([^<]+)</title>', item)
                    link_match = re.search(r'<link>([^<]+)</link>', item)
                    desc_match = re.search(r'<description>([^<]+)</description>', item)
                    
                    if title_match and link_match:
                        # 提取 upvotes
                        score = 0
                        score_match = re.search(r'(\d+)\s*votes?', item)
                        if score_match:
                            score = int(score_match.group(1))
                        
                        posts.append({
                            "subreddit": sub,
                            "title": title_match.group(1).strip(),
                            "url": link_match.group(1).strip(),
                            "score": score,
                            "comments": 0,
                            "created": datetime.now().isoformat()
                        })
        except Exception as e:
            print(f"Error fetching {sub}: {e}")
    
    # 按热度排序
    posts.sort(key=lambda x: x["score"], reverse=True)
    
    # 保存
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(posts[:20], f, ensure_ascii=False, indent=2)
    
    print(f"Saved {len(posts)} posts to {OUTPUT_FILE}")

if __name__ == "__main__":
    fetch_reddit()
