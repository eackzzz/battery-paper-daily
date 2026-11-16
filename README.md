# 钠电文献日报

每天自动抓取 **arXiv 预印本** 与 **Crossref 期刊** 上钠离子电池相关的新文献。

**最近更新**：2026-11-16 13:39 UTC　·　**今日新增**：6 篇　·　**累计收录**：6 篇

---

## 今日新增

- **[Cell teardown and post mortem degradation analysis of commercial 18650 sodium-ion batteries](https://doi.org/10.1016/j.jpowsour.2026.241952)**  
  <sub>2026-11-16 · Journal of Power Sources · Nick Fehlings、Lukas Ihlbrock、Philipp Voß 等</sub>  

- **[Nitrogen doping of porous carbon material through defluorination in ammonia for electrochemical applications in sodium-ion batteries and capacitors](https://doi.org/10.1016/j.jpowsour.2026.241959)**  
  <sub>2026-11-16 · Journal of Power Sources · Y.V. Fedoseeva、A.D. Panfilova、A.A. Zaguzina 等</sub>  

- **[Coking–Crosslinking Competition Shapes Alveolar Hard Carbon Formation From Heterogeneous Precursors for Wide‐Temperature Sodium Storage](https://doi.org/10.1002/ange.9097834)**  
  <sub>2026-11-16 · Angewandte Chemie · Yuhan Liu、Hao Yang、Qianxun Li 等（期刊期次 2026-11-16）</sub>  
  > Competing with lithium‐ion technology on cost and resource abundance requires sodium‐ion batteries to use hard‐carbon anodes produced from abundant, inexpensive feedstocks without sacrificing structural control. Yet the natural and residual…

- **[Advancement in graphene-based anode materials for high-performance sodium-ion batteries](https://doi.org/10.1039/d6ra09929g)**  
  <sub>2026-11-16 · RSC Advances · Ababay Ketema Worku、Bhekie B. Mamba、Nithyadharseni Palaniyandy 等</sub>  
  > This work highlights current developments in pure, porous, and heteroatom-doped graphene as anode materials for SIBs. Additionally, it addresses graphene nanocomposite anodes, particularly conversion, intercalation, and alloy-based material…

- **[Highly Stable and Practical Sodium-Ion Batteries: Key Materials, Electrode Engineering, Manufacturing, and Prospects](https://doi.org/10.53941/sen.2026.100015)**  
  <sub>2026-11-16 · Sustainable Engineering Novit · Lu Yue、Yujie Zhang、Jiajun Wan 等（期刊期次 2026-11-16）</sub>  
  > Sodium-ion batteries (SIBs) are promising for large-scale energy storage owing to abundant sodium resources, low cost, and good manufacturing compatibility. However, their practical application remains limited by the structural stability of…

- **[Fine-tuned atomistic foundation model for accurate sodium-carbon chemistry in Na-ion batteries](https://arxiv.org/abs/2611.18490)**  
  <sub>2026-11-13 · arXiv preprint · Andres Felipe Usuga、Ihor Radchenko、Yuxin Tang 等</sub>  
  > Atomistic foundation models have emerged as a promising route to DFT-level accuracy for materials simulation with complex chemical environments. However, their reliability across competing bonding regimes and, more importantly, how complex…

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
