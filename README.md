# 钠电文献日报

每天自动抓取 **arXiv 预印本** 与 **Crossref 期刊** 上钠离子电池相关的新文献。

**最近更新**：2026-11-18 04:00 UTC　·　**今日新增**：4 篇　·　**累计收录**：20 篇

---

## 今日新增

- **[Unravelling Descriptor–Performance Relationships in Machine Learning of Sodium-Ion Cathode Capacity](https://doi.org/10.1016/j.electacta.2026.150474)**  
  <sub>2026-11-18 · Electrochimica Acta · Muhammad Saeidi、Reza Ebrahimi-Kahrizsangi、Masoud Kasiri-Asgarani 等</sub>  

- **[Na3.95Fe1.475Mn1.475V0.05(PO4)2(P2O7): A high-rate mixed-polyanion cathode with enhanced sodium-ion diffusion kinetics](https://doi.org/10.1016/j.jpowsour.2026.241981)**  
  <sub>2026-11-17 · Journal of Power Sources · Yan Lu、Zheng Li、Yanzhe Zhang 等</sub>  

- **[Decoding the effect of bamboo precursor size on the microstructure and electrochemical behavior of hard carbon anodes for sodium-ion batteries](https://doi.org/10.1016/j.est.2026.125529)**  
  <sub>2026-11-17 · Journal of Energy Storage · Yujun Li、Quanyan Man、Lin Zhao 等</sub>  

- **[Kinetic and Thermodynamic Limits of Sodium Pore Filling in Hard Carbon](https://arxiv.org/abs/2611.20749)**  
  <sub>2026-11-16 · arXiv preprint · Ihor Radchenko、Andrés Felipe Usuga、Yuxin Tang 等</sub>  
  > The low-voltage plateau-like capacity of hard carbon anodes is widely regarded as a key signature of sodium storage in closed pores, often defining the performance of Na-ion batteries. Here, we combine first-principles calculations with a g…

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
