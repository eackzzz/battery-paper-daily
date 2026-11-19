# 钠电文献日报

每天自动抓取 **arXiv 预印本** 与 **Crossref 期刊** 上钠离子电池相关的新文献。

**最近更新**：2026-11-19 03:57 UTC　·　**今日新增**：1 篇　·　**累计收录**：21 篇

---

## 今日新增

- **[Biomass-derived hard carbon anodes for sodium-ion batteries: A critical review of structure engineering, sodium storage mechanisms, and practical performance](https://doi.org/10.1016/j.biortech.2026.136275)**  
  <sub>2026-11-19 · Bioresource Technology · Yifan Chen、Zhaojun Wu、Bingzhou Bai 等</sub>  

---

<details>
<summary>使用说明（点开）</summary>

**改关键词**：编辑 `config.json` 里的 `arxiv_queries` 和 `crossref_queries`，提交后第二天生效。

**马上跑一次**：仓库页 → Actions → 左侧「钠电文献日报」→ 右侧 Run workflow。

**改时间**：`.github/workflows/daily.yml` 里的 `cron: "0 23 * * *"` 是 UTC，23:00 UTC = 北京时间次日 07:00。想改北京时间 08:00 就写 `0 0 * * *`。

**往期存档**：`digest/` 目录，一天一个 md 文件。

**去重**：`data/papers.json` 记录所有见过的文献，同一篇不会重复出现。想重新来过就清空这个文件。

**为什么某天没有新文献**：arXiv 周末不更新，Crossref 期刊也有淡季。连续三天为空才需要检查配置。

</details>
