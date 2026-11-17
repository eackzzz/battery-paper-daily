# 钠电文献日报

每天自动抓取 **arXiv 预印本** 与 **Crossref 期刊** 上钠离子电池相关的新文献。

**最近更新**：2026-11-17 04:56 UTC　·　**今日新增**：10 篇　·　**累计收录**：16 篇

---

## 今日新增

- **[Molecular Engineering of Customizable Resin-Derived Hard Carbon Framework for Efficient Sodium Storage](https://doi.org/10.1021/acsami.6c19377)**  
  <sub>2026-11-17 · ACS Applied Materials &amp; Interfaces · Xiaohui Huang、Yiduo Liu、Jingjing Hao 等（期刊期次 2026-11-17）</sub>  
  > Owing to their high carbon yield and molecular controllability, resins have emerged as promising precursors for hard carbon (HC) anodes in sodium-ion batteries (SIBs). However, achieving synergistic optimization of carbon microcrystals and…

- **[From Nonstep to Step: Voltage‑Response‑Driven Interfacial Evolution and Closed‑Pore Sodium Filling in Hard Carbon Anode](https://doi.org/10.1021/acsenergylett.6c02924)**  
  <sub>2026-11-17 · ACS Energy Letters · Yining Lao、Yuecong Chen、Pengwei Jing 等（期刊期次 2026-11-16）</sub>  
  > Hard carbon (HC) is regarded as the most commercially viable anode for sodium-ion batteries. However, during the initial discharge of the HC anode, the thick solid electrolyte interphase (SEI) derived from the decomposition of the ester-bas…

- **[Effect of Cycling Protocol on the Stress and Mechanical Degradation of Hard Carbon Electrodes](https://doi.org/10.1149/1945-7111/aec2ae)**  
  <sub>2026-11-16 · Journal of The Electrochemical Society · Amit Chanda、Abdulrahman Alfadhli、Vijay Anand Sethuraman 等（期刊期次 2026-11-16）</sub>  
  > Maximum stress experienced by an electrode during cycling is shown to cause mechanical degradation and capacity fade, but the effect of potential window and stress range (Δσ) on cycling behavior was not investigated. Here, stresses generate…

- **[NASICON type LAGP solid electrolytes: A comprehensive review](https://doi.org/10.1016/j.jpowsour.2026.241935)**  
  <sub>2026-11-16 · Journal of Power Sources · Jian Zhang、Shuangtao Pan</sub>  

- **[Waste-PET-Derived Nitrogen-Doped Hard Carbon for Sodium-Ion Batteries: A Comparative Study](https://doi.org/10.3390/batteries12110491)**  
  <sub>2026-11-16 · Batteries · Qiran Lu、Weinan Zhao、Saeed Habibpour 等（期刊期次 2026-11-16）</sub>  
  > Sodium-ion batteries (SIBs) are regarded as a promising alternative to lithium-ion batteries (LIBs). However, their advancement is constrained by the sluggish kinetics and modest capacity of conventional hard carbon (HC) anodes. Here, we re…

- **[Biomass-Derived Hard Carbon Anodes for Sodium-Ion Batteries: From Precursor Chemistry to Multiscale Structural Engineering](https://doi.org/10.3390/ma19224842)**  
  <sub>2026-11-16 · Materials · Junxuan Zhang、Mengyao Li、Tong Li 等（期刊期次 2026-11-15）</sub>  
  > Biomass-derived hard carbon (BHC) is a promising anode material for sodium-ion batteries owing to its renewable feedstocks, low cost, and favorable sodium-storage performance. However, variations in biomass composition and pyrolysis behavio…

- **[Understanding the Role of Solid Polymer Electrolyte Network Structure and Modulus in In Situ Anode Formation of “Anode-Free” Sodium Metal Batteries](https://doi.org/10.1021/acsami.6c17291)**  
  <sub>2026-11-16 · ACS Applied Materials &amp; Interfaces · William R. Fullerton、Mark C. Staub、Yuean Wu 等（期刊期次 2026-11-16）</sub>  
  > “Anode-free” solid-state battery concepts based on sodium metal have attracted greater research interest recently due to their potential economic advantages, namely lower material costs and simplified, less expensive processing. However, th…

- **[Highly conductive halide Na-ion conductor enabled by cost-effective aliovalent carbonate polyanion substitution for all-solid-state sodium batteries](https://doi.org/10.1038/s41467-026-79386-9)**  
  <sub>2026-11-16 · Nature Communications · Xiaolin Guo、Man Chen、James Burrow 等（期刊期次 2026-11-16）</sub>  

- **[Mechanistic Insights into Sodium Storage through Transport Kinetics, Bulk, and Interfacial Property Analyses of Hard and Soft Carbon Anodes](https://doi.org/10.1021/acsaem.6c02883)**  
  <sub>2026-11-16 · ACS Applied Energy Materials · Israr Ahmed、Hiroyuki Ueda、Jon Serrano Sevillano 等（期刊期次 2026-11-16）</sub>  
  > Understanding the sodium storage mechanism in disordered carbons remains critical for the development of high-capacity anodes for sodium–ion batteries. Here, we systematically investigate sodium storage in hard carbon, soft carbon, and a ha…

- **[A Hybrid State Space-Attention Architecture for Forecasting the Trajectories of Battery Degradation](https://arxiv.org/abs/2611.19116)**  
  <sub>2026-11-14 · arXiv preprint · Shrey Patel、Bhargav Srinivas Rao、Samet Ayhan 等</sub>  
  > Early-life battery degradation trajectory forecasting aims to predict a battery cell's full state-of-health (SOH) trajectory from its initial charge-discharge cycles, potentially reducing cell qualification and evaluation time from months t…

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
