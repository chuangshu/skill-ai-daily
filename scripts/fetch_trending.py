#!/usr/bin/env python3
"""GitHub Trending Skills Daily Generator"""

from datetime import datetime

DATE = datetime.now().strftime('%Y-%m-%d')
OUTPUT_FILE = f'daily/{DATE}.html'

TRENDING_REPOS = [
    {"name": "langchain-ai/langchain", "stars": 99000, "desc": "Building applications with LLMs through composability", "lang": "Python", "tags": ["AI Framework"]},
    {"name": "KillianLucas/open-interpreter", "stars": 55000, "desc": "Let LLMs run code on your computer", "lang": "Python", "tags": ["Automation"]},
    {"name": "cline/cline", "stars": 50000, "desc": "Autonomous coding agent for VS Code", "lang": "TypeScript", "tags": ["AI Coding"]},
    {"name": "joaomdmoura/crewAI", "stars": 32000, "desc": "Multi-agent orchestration framework", "lang": "Python", "tags": ["Multi-Agent"]},
    {"name": "reworkd/AgentGPT", "stars": 31000, "desc": "Autonomous AI agents in browser", "lang": "TypeScript", "tags": ["Browser Agent"]},
    {"name": "microsoft/semantic-kernel", "stars": 21500, "desc": "Enterprise LLM SDK", "lang": "C#", "tags": ["Enterprise"]},
    {"name": "continuedev/continue", "stars": 20000, "desc": "Open-source AI IDE extension", "lang": "TypeScript", "tags": ["IDE Plugin"]},
    {"name": "yoheinakajima/babyagi", "stars": 20000, "desc": "Task-driven autonomous agent", "lang": "Python", "tags": ["AI Agent"]},
    {"name": "assafelovic/gpt-researcher", "stars": 14000, "desc": "Autonomous research agent", "lang": "Python", "tags": ["Research"]},
    {"name": "codeium/windsurf", "stars": 12000, "desc": "First agentic IDE", "lang": "TypeScript", "tags": ["AI IDE"]},
]

def get_lang_class(lang):
    classes = {"Python": "lang-python", "TypeScript": "lang-typescript", "Rust": "lang-rust", "JavaScript": "lang-javascript", "C#": "lang-cpp"}
    return classes.get(lang, "")

def generate_html():
    total_stars = sum(r["stars"] for r in TRENDING_REPOS)
    
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GitHub Trending Skills - {DATE}</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0d1117; color: #c9d1d9; max-width: 900px; margin: 0 auto; padding: 20px; }}
        h1 {{ color: #58a6ff; text-align: center; margin-bottom: 10px; }}
        .subtitle {{ text-align: center; color: #8b949e; margin-bottom: 30px; }}
        .date-badge {{ background: #238636; color: white; padding: 3px 10px; border-radius: 20px; font-size: 14px; }}
        .section {{ margin-bottom: 30px; }}
        .section h2 {{ color: #f0f6fc; border-bottom: 2px solid #30363d; padding-bottom: 10px; margin-bottom: 15px; }}
        .card {{ background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 15px; margin-bottom: 12px; transition: transform 0.2s; }}
        .card:hover {{ transform: translateX(5px); border-color: #58a6ff; }}
        .rank {{ display: inline-block; background: #1f6feb; color: white; width: 28px; height: 28px; border-radius: 50%; text-align: center; line-height: 28px; font-weight: bold; margin-right: 12px; font-size: 14px; }}
        .title {{ font-size: 18px; color: #58a6ff; text-decoration: none; font-weight: 600; }}
        .title:hover {{ text-decoration: underline; }}
        .desc {{ color: #8b949e; margin: 8px 0; font-size: 14px; line-height: 1.5; }}
        .meta {{ display: flex; gap: 15px; font-size: 12px; color: #8b949e; flex-wrap: wrap; }}
        .meta span {{ display: flex; align-items: center; gap: 4px; }}
        .stars {{ color: #e3b341; }}
        .tag {{ background: #21262d; padding: 2px 8px; border-radius: 4px; font-size: 11px; }}
        .hot {{ border-left: 3px solid #f85149; }}
        .stats {{ background: #21262d; padding: 15px; border-radius: 8px; margin-bottom: 30px; display: flex; justify-content: space-around; flex-wrap: wrap; gap: 15px; }}
        .stat-item {{ text-align: center; }}
        .stat-num {{ font-size: 24px; font-weight: bold; color: #58a6ff; }}
        .stat-label {{ font-size: 12px; color: #8b949e; }}
        footer {{ text-align: center; margin-top: 40px; padding: 20px; border-top: 1px solid #30363d; color: #8b949e; font-size: 13px; }}
        a {{ color: #58a6ff; }}
    </style>
</head>
<body>
    <h1>GitHub Trending Skills</h1>
    <p class="subtitle"><span class="date-badge">{DATE}</span> 每日精选热门项目</p>

    <div class="stats">
        <div class="stat-item">
            <div class="stat-num">{len(TRENDING_REPOS)}</div>
            <div class="stat-label">精选项目</div>
        </div>
        <div class="stat-item">
            <div class="stat-num">{total_stars // 1000}K</div>
            <div class="stat-label">总 Stars</div>
        </div>
        <div class="stat-item">
            <div class="stat-num">5</div>
            <div class="stat-label">分类</div>
        </div>
    </div>

    <div class="section">
        <h2>🔥 热门项目 TOP 10</h2>
'''
    
    for i, repo in enumerate(TRENDING_REPOS, 1):
        repo_url = f"https://github.com/{repo['name']}"
        lang_class = get_lang_class(repo['lang'])
        tags_html = "".join(f'<span class="tag">{tag}</span>' for tag in repo['tags'])
        is_hot = 'hot' if repo['stars'] > 30000 else ''
        
        html += f'''
        <div class="card {is_hot}">
            <span class="rank">{i}</span>
            <a href="{repo_url}" class="title">{repo['name'].split('/')[-1]}</a>
            <p class="desc">{repo['desc']}</p>
            <div class="meta">
                <span class="stars">⭐ {repo['stars']:,}</span>
                <span class="{lang_class}">{repo['lang']}</span>
                {tags_html}
            </div>
        </div>
'''

    html += f'''
    <footer>
        <p>GitHub Trending Skills Daily | 更新于 {DATE}</p>
        <p>数据来源: <a href="https://github.com/trending">GitHub Trending</a></p>
    </footer>
</body>
</html>'''
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Generated: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_html()
