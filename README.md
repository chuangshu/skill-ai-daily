# Reddit AI 情报日报

自动抓取 Reddit AI 热门讨论，生成每日情报日报。

## 功能

- 🤖 监控 Reddit AI 热门社区（r/artificial, r/MachineLearning, r/OpenAI）
- 📊 筛选高热度、高价值帖子
- 📰 生成每日情报日报
- 🌐 GitHub Pages 自动发布

## 定时任务

```bash
# 每天 9:00, 13:00, 21:00 自动更新
0 9,13,21 * * * cd /root/clawd/reddit-ai && ./scripts/fetch_all.sh >> logs/fetch.log 2>&1
```

## 仓库地址

https://github.com/chuangshu/reddit-ai-daily

## 发布地址

https://chuangshu.github.io/reddit-ai-daily/
