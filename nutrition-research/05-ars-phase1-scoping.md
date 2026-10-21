# ARS deep-research · Phase 1 范围界定（待确认）

模式：`full`。流程：Phase 1 范围界定 → 用户确认 → Phase 2 文献检索与来源核实 → Phase 3 综合 → Phase 4 成稿 → Phase 5 审查 → Phase 6 修订。

本文件是 Phase 1 的产出，需要你确认后才进入 Phase 2。01–04 号文件作为第一轮检索底稿，其中标 [二手] 的条目会在 Phase 2 逐条核对原文。按 ARS 的规则，无法确认存在的来源一律剔除，不能以“待查”状态留在报告里。

---

## Research Question Brief

### Topic Area
公共营养与健康饮食的前沿进展：比较国内与国际。

### Primary Research Question
2022 年 1 月至 2026 年 10 月，中国与国际权威机构对一般人群提出的膳食建议出现了哪些新方向，每个方向分别有哪一级别的证据支持？

### FINER Assessment
| Criterion | Score | Justification |
|-----------|-------|---------------|
| Feasible | 4/5 | 指南、政策文件和系统综述大多可以公开获取；部分中文政策原文和 CNKI 全文可能拿不到 |
| Interesting | 4/5 | 美国 DGA 转向、UPF 证据之争、GLP-1 普及，正在改变“健康饮食”的公共定义 |
| Novel | 3/5 | 单项议题已有很多综述，把中外指南放在一起按证据等级对照的整理较少 |
| Ethical | 5/5 | 只做二手文献与政策文本分析，不涉及人类受试者 |
| Relevant | 4/5 | 可直接用于科普、教学和政策建议，也能指出国内指南修订时可能要回应的议题 |
| **Average** | **4.0/5** | |

### Scope Boundaries
**In Scope:** 面向一般健康人群的膳食指南；国家和国际层面的公共营养政策，包括标签、税收、减盐、体重管理；有系统综述或 RCT 证据的前沿膳食议题

**Out of Scope:** 临床营养治疗（住院、肠内肠外营养）；单一疾病的医学营养治疗细则；食品安全与毒理；企业产品宣传

**Domain:** 公共营养学 / 营养流行病学 / 食品政策

**Timeframe:** 2022-01 至 2026-10。更早的基础证据只作背景

**Geography:** 中国大陆；国际以 WHO、美国 USDA/HHS、EAT-Lancet 为主，必要时补充英国、拉美的政策评估

**Population:** 2 岁及以上一般人群；涉及老年、儿童青少年时单独标注

**Key Assumptions:** 指南文本可以代表官方立场；证据等级可以按 ARS 证据层级（Level I–VII）统一评定

### Sub-questions
1. 国际权威机构（WHO、美国 DGA 2025–2030、EAT-Lancet 2.0）在这段时间提出了哪些新的人群膳食建议，各自依据什么证据？
2. 中国（《中国居民膳食指南（2022）》、体重管理年、GB 28050-2025、减盐行动）在同一时期提出了哪些新建议，各自依据什么证据？
3. 超加工食品、GLP-1 用药期间的营养、限时进食、精准营养、东方健康膳食模式这五个前沿议题，证据等级如何，国内外的采纳程度差在哪里？

### Sub-Question Bindings
1. inherits: timeframe=2022-01–2026-10; population=一般人群; deviations: geography 只取国际
2. inherits: timeframe=2022-01–2026-10; population=一般人群; deviations: geography 只取中国大陆
3. inherits: timeframe=2022-01–2026-10; geography=中外对照; deviations: GLP-1 议题的人群为使用该类药物的成人肥胖者（经用户批准前为待定偏离）

### Candidate Questions Considered
| # | Candidate | FINER Avg | Why not selected |
|---|-----------|-----------|-----------------|
| 1 | 中外膳食建议新方向及其证据等级（上文） | 4.0 | Selected |
| 2 | 超加工食品的健康证据对中国营养政策有什么启示？ | 3.8 | 只覆盖一个议题，比你“调研前沿知识”的目标窄 |
| 3 | GLP-1 药物普及后，人群营养建议应如何调整？ | 3.6 | 证据多为专家共识，可检索的 RCT 少，可行性较低 |

---

## Methodology Blueprint

### Research Paradigm
**Selected**: 实用主义（pragmatist）
**Justification**: 目标是给出可以直接使用的证据地图，不检验某一理论

### Method
**Type**: 定性为主，辅以描述性统计
**Specific Method**: 整合性文献回顾（integrative review）加政策文本比较分析
**Justification**: 研究问题同时涉及指南文本和研究证据。整合性回顾允许合并不同研究设计并记录检索过程；政策文本比较用来回答“新方向是什么”

### Data Strategy
**Data Type**: 二手资料
**Sources**:
- 指南和政策原文：WHO IRIS、realfood.gov / DietaryGuidelines.gov、国家卫健委、中国营养学会、国家标准全文公开系统
- 研究证据：PubMed、Semantic Scholar、OpenAlex、Crossref（用于核实 DOI），以及 CNKI / 万方中文期刊
**Sampling**: 目的性抽样。指南和政策全部纳入；研究证据优先取系统综述、meta 分析和大型 RCT，再取大型队列研究
**Time Frame**: 2022-01-01 至 2026-10-21

### Analytical Framework
**Technique**: 主题综合，加证据等级评定（Level I–VII）
**Steps**:
1. 为指南和政策条目建表，每条记录机构、日期、建议内容、引用的证据
2. 对每个前沿议题，检索并分级最新的系统综述和 RCT
3. 做中外对照矩阵：同一议题在国内外的立场是否一致、证据等级、存在的差距
4. 标出证据冲突和行业争议，例如 UPF 分类之争、DGA 的饱和脂肪表述
**Tools**: Markdown 证据表；按 APA 7 格式引用

### Validity Criteria
| Criterion | Strategy to Ensure |
|-----------|-------------------|
| 来源真实性 | 每条文献都核对 DOI、PMID 或官方链接，核不到的剔除 |
| 引用忠实度 | 结论必须和原文表述一致，不能根据摘要或媒体转述下结论 |
| 平衡性 | 每个议题都检索反方证据和批评意见，例如行业观点、方法学批评 |
| 可重复性 | 记录检索式、数据库、检索日期和纳入排除标准 |

### Limitations (By Design)
- 不是系统综述，可能遗漏文献。缓解办法是公开检索式，并说明覆盖范围
- 中文全文获取受限。缓解办法是优先使用官方发布的原文和开放获取期刊
- 2026 年的新文献可能还没被数据库完整收录。缓解办法是在报告中标注检索截止日期

### Ethical Considerations
- 不涉及人类受试者，不需要伦理审查
- 报告会附 AI 辅助声明
- 涉及行业资助研究时标注利益冲突

---

## Devil's Advocate · Checkpoint 1

**Verdict: PASS（附条件）**。没有 Critical 级问题，但有两个 Major 级问题需要你在确认时一并回应：

1. **[Major] “新方向”的判定标准还不明确。** 如果不事先定义，很容易只挑有新闻热度的议题，造成选择偏倚。建议在 Phase 2 开始前定好标准：与本机构上一版相比，建议内容发生了实质变化，或者首次提出。
2. **[Major] 中外两侧的文件类型不对等。** 国际一侧主要是指南，国内一侧不少是行动方案和标准，“建议”的含义不同。建议在对照矩阵里单列“文件类型”一栏，避免拿不同类型的文件直接比。
3. **[Minor] 子问题 3 的五个议题是根据第一轮检索结果定的，带有先入为主。** 建议在 Phase 2 再做一次开放检索，确认有没有遗漏重要议题，比如膳食纤维与肠道菌群、植物基饮食、包装正面警示标签。
4. **[Minor] 证据等级是“医学式”的层级，不太适合政策类问题。** 政策效果类证据（比如含糖饮料税）常常来自自然实验或间断时间序列，应该按这类研究在本领域的标准来评级，不能一律算作低等级。
