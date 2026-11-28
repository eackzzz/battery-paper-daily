# 钠电正极文献日报

每天自动抓取 **arXiv 预印本** 与 **Crossref 期刊** 上钠离子电池**正极材料**的新文献。

**重点推送聚阴离子路线**（NaFePO₄ / Na₃V₂(PO4)₃ / NFPP / NASICON），其次是层状氧化物、普鲁士蓝。硬碳负极、固态电解质等非正极方向已过滤。

期刊文献只保留电池方向主流顶刊（24 个刊，白名单见 `config.json`，可自行增删）；arXiv 是预印本，不做期刊过滤。

**最近更新**：2026-11-28 04:38 UTC　·　**今日新增**：2 篇　·　**累计收录**：40 篇

---

## 今日新增

- **[An Amorphous Phosphate-Based Chloride Electrolyte for Low-Stacking-Pressure All-Solid-State Sodium Batteries](https://doi.org/10.1021/acsenergylett.6c03064)**  
  <sub>2026-11-27 · ACS Energy Letters · Zi-Wei Wang、Jin-Da Luo、Zhang-Chi Yang 等（期刊期次 2026-11-27）</sub>  
  > Conventional inorganic solid electrolytes (SEs) rarely combine sufficient deformability for stable interfacial contact in composite cathodes with high ionic conductivity and low cost, hindering the development of stable all-solid-state sodi…

- **[Harnessing Bio‑Digestion for Surface Porous Hard Carbon With Rich Internal Closed Pores Toward Exceptional Sodium Storage](https://doi.org/10.1002/adfm.79919)**  
  <sub>2026-11-27 · Advanced Functional Materials · Tengtao Hu、Yujuan Zhang、Chenlu Xu 等（期刊期次 2026-11-27）</sub>  
  > Sodium‐ion batteries (SIBs) are attractive for grid‐scale energy storage, yet their anode development is hindered by irreversible Na + trapping and insufficient rate capability, primarily due to microstructural defects and poor surface chem…

---

<details>
<summary>使用说明（点开）</summary>

**改关键词**：编辑 `config.json` 里的 `arxiv_queries` 和 `crossref_queries`，提交后第二天生效。

**改期刊白名单**：`config.json` 里的 `crossref_journal_whitelist`，一行一个刊名（IF 每年会浮动，自行增删）。

**马上跑一次**：仓库页 → Actions → 左侧「钠电正极文献日报」→ 右侧 Run workflow。

**改时间**：`.github/workflows/daily.yml` 里的 `cron: "0 23 * * *"` 是 UTC，23:00 UTC = 北京时间次日 07:00。想改北京时间 08:00 就写 `0 0 * * *`。

**往期存档**：`digest/` 目录，一天一个 md 文件。

**去重**：`data/papers.json` 记录所有见过的文献，同一篇不会重复出现。换方向后想重新来过，就把这个文件内容改成 `{"papers": {}}`。

**为什么某天没有新文献**：顶刊 + 正极两个条件叠加后，一天一两条是正常频率。arXiv 周末不更新，Crossref 也有淡季。连续三天为空才需要检查配置。

</details>
