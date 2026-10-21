# ARS deep-research · Phase 5 审查

审查对象：`08-ars-report.md` 第 1 轮修订稿。

第 1 轮审查只依据 deep-research 主说明中的要点，没有先读主编和伦理两个角色的完整定义文件。本文件是读完 `editor_in_chief_agent.md` 和 `ethics_review_agent.md` 之后按完整标准重做的版本，并纳入了报告编写角色本应在 Phase 4 完成的写作质量检查和时间表述检查。第 1 轮的意见汇总保留在文末。

---

## 0. 报告编写角色的定稿前自查（Phase 4 补做）

ARS 规定报告编写角色在定稿前要做三项自查。Phase 4 时漏做了，这里补上，结果交给 Phase 6 第 2 轮修订。

### 0.1 缩写检查（`scripts/check_acronyms.py`，ARS 自带脚本）
覆盖范围：正文 + 中文摘要（脚本的 `--lang` 只支持 `en` 和 `zh-TW`，这里用 `en` 输出报告）。主要发现：
- **UPF**：正文第一次出现时没有给出全称（摘要里有，但正文是独立范围）
- **领域缩写未定义**：RCT、GRADE、RR、HR、OR、CVD、BMI、DGA、FDA、USDA、CNKI
- **ARS**：在定义之前就已使用
- 期刊名、数据库名和通用缩写（BMJ、PLOS、BMC、PMC、PMID、APA、AI、WHO、GB）属于惯用写法，按脚本的 allowlist 规则豁免
- NOVA 是分类体系的名称，不是缩写，豁免

### 0.2 时间表述检查（Temporal Integrity Iron Rule）
逐句查了“目前”“现行”“最新”“新版”“首次”“此后”“同期”等表述：

| 位置 | 原文 | 问题 | 处理 |
| --- | --- | --- | --- |
| 发现 10 标题 | “中国现行政策以营养素为锚” | **事实错误**：GB 28050-2025 要到 2027-03-16 才实施，检索日（2026-10-21）还不是现行标准 | 改为“已发布、2027 年实施的” |
| 摘要 | “美国新版膳食指南” | 用了“新版”这种指示词，没有锚定日期 | 改为“2026 年 1 月发布的 DGA 2025–2030” |
| 摘要 | “中国的膳食指南和标签标准还没有使用 UPF 概念” | 把“检索未发现”写成了事实 | 改为“截至检索日未检到” |
| 1.1、对照表 | “第一次点名高度加工食品” | “第一次”是 HHS 情况说明自己的说法 | 改为“据 HHS 情况说明，这是第一次” |
| 1.1 | “反对意见也在增多” | 趋势判断没有依据 | 改为“2025–2026 年间也发表了有分量的反对意见” |
| 1.1 | “*Nature Food* 同期刊出正反两篇” | “同期”指代不明 | 改为“同一期刊出正反两篇” |
| 4.2 第 2 条 | “目前效果证据最充分的工具” | 没有锚定日期和范围 | 改为“在本研究纳入的证据中” |

### 0.3 写作质量与证据支持检查
写作诊断（`writing_quality_check.md`）没有发现需要改的空话、套话或强行三段式。下面四处主张在已纳入的来源中找不到依据，按规则标 `[MATERIAL GAP]` 或删除：
1. 4.2 第 2 条“拉美的 UPF 供能比远高于中国”：语料中没有拉美的 UPF 供能比数据
2. 4.2 第 2 条“零售结构和在家烹饪的比例也不同”：没有来源
3. 4.3“这类工具覆盖的多数产品，本身就是 UPF”：只有广东一项研究的钠含量对比，不能支持“多数”
4. 发现 2“植物肉只占 0.5%”：来源只是媒体转述的专家评论，报告参考文献中没有这条

---

## 1. 主编审查（editor_in_chief_agent）

### Overall Assessment
**Verdict**：Minor Revision
**Weighted Score**：3.35 / 5.0

### Dimension Scores
| Dimension | Weight | Score | Notes |
|-----------|--------|-------|-------|
| Originality & Contribution | 20% | 4/5 | 把国际 UPF 证据逐条对照中国政策，并按依据强度给出启示，这类整理少见 |
| Methodological Rigor | 25% | 3/5 | 方法写得清楚，局限也如实交代；但全部来源只读到摘要，而且检索流程的数字是事后估算（见 06 号文件） |
| Evidence Sufficiency | 25% | 3/5 | SQ1、SQ2 的证据充分；SQ3 偏薄。另有 4 处主张没有来源支持（见 0.3） |
| Argument Coherence | 15% | 4/5 | 研究问题 → 方法 → 发现 → 启示的链条清楚，也回应了预防原则 |
| Writing Quality | 15% | 3/5 | 结构清楚，表格得当；缩写定义不全，有一处时间表述错误，有几处 APA 引用格式不完整 |

计算：0.20 × 4 + 0.25 × 3 + 0.25 × 3 + 0.15 × 4 + 0.15 × 3 = 3.35，属于 Minor Revision 区间（3.0–3.9）。

### Strengths
1. **方法部分（2.5 节）如实说明了核实层级的限制**，没有把摘要级核对写成全文核对
2. **3.2 节同时呈现支持方和反方的试验证据**（Hall 对 Rego，Dicken 和批评通信），没有只挑有利结果
3. **4.2 节的启示按依据强度分级，并说明了“依据强度”的含义**，便于政策读者判断
4. **中外对照表单列了“文件类型”**，避免把指南、标准、税法直接拿来比

### Required Revisions

#### Critical
- 无

#### Major
- [ ] **M1 时间表述错误**（发现 10）：GB 28050-2025 不是现行标准。按 0.2 节的表格修改
- [ ] **M2 没有来源支持的主张**（4.2、4.3、发现 2）：按 0.3 节的四条，标 `[MATERIAL GAP]` 或删除
- [ ] **M3 正文引用了，但参考文献缺条目**：
  - 墨西哥警示标签研究（发现 6）
  - *BMJ* 社论（发现 1）
  - Ludwig 等和 Wang & Peng 的批评通信（发现 3）
  - PMID 42269970 的批判性综述（发现 3）
  - 国际食品科学技术联盟（IUFoST）的批评（发现 5）

  补齐这些条目，作者不全的标 [作者待核]

#### Minor
- [ ] **m1 缩写**：按 0.1 节，在正文第一次出现时给出全称
- [ ] **m2 Whelan 等（2024）的转述**：报告写“证据以动物和体外研究为主”，但摘要说的是“人体干预研究较少”。改为与摘要一致的说法

### Suggestions (Optional)
- 在 3.1 节表格下注明，政策部分 10 条中有 6 条是官方文件，不是研究证据

### Line-Level Feedback
| Section | Issue | Recommendation |
|---------|-------|---------------|
| 摘要 | “美国新版膳食指南”“还没有使用 UPF 概念” | 按 0.2 节锚定日期，改为“未检到” |
| 3.2 发现 2 | “植物肉只占 0.5%”没有参考文献 | 删除，改为“摘要没有报告该类别的构成” |
| 3.2 发现 4 | Whelan 的转述 | 见 m2 |
| 3.5 发现 10 | “现行” | 见 M1 |
| 4.2 第 2 条 | 拉美对比没有来源 | 见 M2 |

### Summary
报告的结构和论证是成立的，方法上的局限也写得诚实。主要问题集中在“写出来的话是否都有出处”：一处时间表述错误、四处没有依据的主张、五处引用缺参考文献条目。这些都是可以定点修改的问题，不需要重写。

修改后可以作为内部参考稿。但在补齐 [名待核] 并与全文核对之前，仍不适合对外发表。

---

## 2. 研究诚信与伦理审查（ethics_review_agent）

### AI-Assisted Research-Integrity Verdict: CONDITIONAL

Scope：这一结论只针对 AI 辅助研究的诚信问题，不是人类受试者方面的审批或许可。

### Dimension Assessment
| Dimension | Status | Notes |
|-----------|--------|-------|
| AI Disclosure | pass | 已声明 AI 参与了检索、核实、综合和起草，也写明了核实只到摘要层级、需要人工把关 |
| Attribution Integrity | warn | 正文有 5 组引用缺参考文献条目（见主编意见 M3），仍有 11 处 [名待核]。没有发现编造的参考文献，见下方说明 |
| Dual-Use Screening | pass | Risk Level：None。营养政策综述，没有可被滥用的操作性内容 |
| Fair Representation | pass | 争议问题呈现了正反两方；对拉美政策经验的引用没有贬损性表述 |
| Data Ethics | pass | 只使用公开发表的文献和政府文件，不涉及个人数据 |
| Conflict of Interest | warn | Braesco（Industry Research 页眉）和 Monteiro（NOVA 提出方）已在正文注明；Lancet 系列第 2、3 篇的作者团队中也有长期倡导 UPF 管控的学者，正文没有注明 |
| Human Subjects Ethics | see separate status | 不涉及人类受试者 |

### Human-Subjects Administrative Status
| Field | Value |
|-------|-------|
| submission_readiness | unresolved（不涉及人类受试者，没有提交审查的事项） |
| authorization_status | not_provided（不适用） |
| review_pathway | institutional determination required |
| authority_context | unavailable — missing or unresolved |
| profile_dependent_result_allowed | false |
| candidate rule trace | unavailable — no validated trace |
| applicable consent/information requirement IDs | unavailable — authority selection unresolved |
| actor and consumer scope per requirement | 不适用 |
| requirement and authority-anchor pointers | 不适用 |

### Issues Found

#### Critical (Blocks Delivery)
没有 Critical 级问题。

说明：Phase 2 起草文献目录时，曾经有几处作者名和名字缩写是凭印象补的，检索结果里并没有出现，比如 Monteiro 论文的两位合作者。这些在提交前已经全部删除，改为 [名待核]，没有进入任何已提交的版本。按“即使一条编造的参考文献也要阻断”的标准，当前文件中没有发现编造内容，但这一过程如实记在这里。

#### Conditional (Must Fix)
- **C1**：补齐主编意见 M3 列出的五组缺失参考文献
- **C2**：在 3.4 节引用 Lancet 系列时，注明作者团队的倡导立场，和对 Monteiro 的处理方式保持一致

#### Advisory (Recommended)
- 报告开头的“只供内部使用”状态说明，在 [名待核] 补齐前不要删除

### AI Disclosure Verification
- [x] Disclosure statement present：Yes
- [x] Scope accurate：Yes（检索、核实、综合、起草；核实只到摘要）
- [x] Limitations noted：Yes

### Reference Integrity Check
- **Total references cited**：27 条（第 2 轮修订补齐前）
- **Spot-checked**：17 条（63%），把报告中的转述与检索时拿到的摘要或官方索引页逐条对照
  - 一致：Lane、Hall、Rego、Dicken、Aramburu、Rauber、Braesco、Medin、Louie、Song、Taillie、Li 2024、Li & Shi、Pan、Wagner、Colombia、FDA/USDA RFI
- **Issues found**：
  - Whelan 等（2024）的转述比摘要更强（见主编意见 m2）
  - 墨西哥数据（44.8% 和 38.7%）在正文中没有引用来源
- **Retraction status**：本环境不能访问撤稿数据库，`bibliographic_integrity_signals` 没有生成，撤稿状态未核查

### Responsible Use Statement
不需要（dual-use risk 为 None）。

### Ethics Clearance Notes
- 报告把“证据是否足以支持政策行动”明确标为价值判断，留给读者决定，这种处理是恰当的

### Ethics Decision Log
| Item | Verdict | User decision | Reasoning |
|------|---------|---------------|-----------|
| C1 缺失参考文献 | CONDITIONAL | accept fix（用户已授权补做第 2、4、5 项） | — |
| C2 Lancet 系列作者立场 | CONDITIONAL | accept fix（同上） | — |

> **Human-subjects boundary:** This output does not authorize recruitment, consent, access to identifiable data, intervention, or data collection.

---

## 3. Devil's Advocate · Checkpoint 3

第 1 轮的意见（D1 预防原则、D2 可迁移性）已在第 1 轮修订中处理。复核结论：

- **D1 已解决**：4.3 节正面回应了预防原则，也承认了这一路径的代价
- **D2 部分解决**：可迁移性的说明里，用来对比的“拉美 UPF 供能比远高于中国”没有来源（见 0.3 第 1 条）。论点本身成立，但依据要改：要么补来源，要么改成“效果可能因饮食结构和零售环境不同而不同”，不做具体对比

**Verdict: PASS**，没有新的 Critical 或 Major 问题。

---

## 4. 第 2 轮修订清单

| 编号 | 来源 | 严重度 | 处理 |
| --- | --- | --- | --- |
| M1 | 主编 / 时间表述检查 | Major | “现行”改为“已发布、2027 年实施” |
| M2 | 主编 / 证据支持检查 | Major | 四处主张标 [MATERIAL GAP] 或删除 |
| M3 / C1 | 主编 / 伦理 | Major / Conditional | 补齐五组参考文献 |
| C2 | 伦理 | Conditional | 注明 Lancet 系列作者团队的立场 |
| m1 | 主编 / 缩写检查 | Minor | 正文第一次出现时给出全称 |
| m2 | 主编 / 伦理 | Minor | 改正 Whelan 的转述 |
| 0.2 其余各条 | 时间表述检查 | Minor | 按 0.2 节表格修改 |
| D2 | DA | Minor | 按 DA 复核意见修改 |

---

## 附：第 1 轮审查意见汇总（已在第 1 轮修订中处理）

| 编号 | 意见 | 处理结果 |
| --- | --- | --- |
| E1 | 启示的证据标签含义不清 | 已改为“依据强度” |
| E2 | DGA 的科学性争议 | 已补充 |
| E3 | 字数说明有误 | 已改正 |
| E4 | GB 28050 原文未核对 | 已补充 |
| Eth-1 | Braesco、Monteiro 的立场或利益说明 | 已补充 |
| Eth-2 | 报告状态说明 | 已加 |
| D1 | 预防原则 | 已新增 4.3 节 |
| D2 | 可迁移性 | 已补充（第 2 轮继续修改） |
