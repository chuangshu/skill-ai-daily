# 📰 Reddit AI 情报日报 - 更新指南

由于 Reddit 限制服务器访问，请手动更新：

## 方法 1：手动添加链接

1. 打开 Reddit AI 热门：
   - https://www.reddit.com/r/artificial/hot
   - https://www.reddit.com/r/MachineLearning/hot
   - https://www.reddit.com/r/OpenAI/hot

2. 复制热门帖子链接和标题

3. 编辑 `daily/YYYY-MM-DD.html`

4. 提交并推送：
```bash
git add daily/
git commit -m "📰 Update $(date +%Y-%m-%d)"
git push
```

## 方法 2：使用 GitHub Actions（推荐）

GitHub Actions 会在每天 17:00 (北京时间) 自动运行，但由于 Reddit 限制，可能需要手动更新。

## 提示

- 筛选标准： upvotes > 500，评论 > 50
- 分类：技术突破、产品更新、行业动态、投资机会
- 建议每天添加 3-5 条热门内容
