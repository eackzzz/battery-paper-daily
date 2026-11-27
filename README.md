# 钠电正极文献日报

每天自动抓取 **arXiv 预印本** 与 **Crossref 期刊** 上钠离子电池**正极材料**的新文献。

**重点推送聚阴离子路线**（NaFePO₄ / Na₃V₂(PO4)₃ / NFPP / NASICON），其次是层状氧化物、普鲁士蓝。硬碳负极、固态电解质等非正极方向已过滤。

期刊文献只保留电池方向主流顶刊（24 个刊，白名单见 `config.json`，可自行增删）；arXiv 是预印本，不做期刊过滤。

**最近更新**：2026-11-27 04:54 UTC　·　**今日新增**：3 篇　·　**累计收录**：38 篇

---

## 今日新增

- **[Symmetry-reduced superstructure enables high-voltage stable layered oxide cathodes for sodium-ion batteries](https://doi.org/10.1016/j.jechem.2026.11.029)**  
  <sub>2026-11-26 · Journal of Energy Chemistry · Zhiqiang Zhao、Mingbao Huang、Wenbo Liu 等</sub>  

- **[Covalent–Ionic Bonding Regulation Enables Chemo‐Mechanical Stabilization of High‐Voltage O3‐Type Sodium Layered Oxide Cathodes](https://doi.org/10.1002/adma.75884)**  
  <sub>2026-11-26 · Advanced Materials · Xingyue Yang、Jian Chen、Rui Li 等（期刊期次 2026-11-26）</sub>  
  > Ni–Fe–Mn‐based O3‐type layered oxides are attractive cathode materials for sodium‐ion batteries, but their high‐voltage operation suffers from the coupling between phase transitions and lattice oxygen instability. In this work, guided by ha…

- **[Programming Sodium-Storage Kinetics through Linear Quinone Oligomerization](https://doi.org/10.1021/acsenergylett.6c03180)**  
  <sub>2026-11-26 · ACS Energy Letters · Wenwen Deng、Tingting Jiang、Longfei Li 等（期刊期次 2026-11-26）</sub>  
  > Quinone-based organic cathodes enable reversible multielectron redox reactions but suffer from dissolution and sluggish sodium-storage kinetics. Here, two structurally homologous linear quinone oligomers, biphenyl–quinone dimer (2BQ) and te…

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
