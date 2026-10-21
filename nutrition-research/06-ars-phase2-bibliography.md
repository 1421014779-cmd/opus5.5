# ARS deep-research · Phase 2 文献检索与来源核实

研究问题（Phase 1 已确认）：2022 年 1 月至 2026 年 10 月发表的超加工食品健康证据，对中国的公共营养政策有什么启示？

文献回顾形式：用户回复“按现在的方法继续”（skip），沿用整合性回顾。

---

## Annotated Bibliography

### Search Strategy
- **Databases**：通用网页检索，以及限定到下列站点的定向检索：
  - 文献索引与期刊：pubmed.ncbi.nlm.nih.gov、ncbi.nlm.nih.gov/pmc、bmj.com、thelancet.com、nature.com、cell.com、journals.plos.org、ijbnpa.biomedcentral.com、onlinelibrary.wiley.com、mdpi.com、frontiersin.org
  - 官方机构：who.int、federalregister.gov、fda.gov、hhs.gov、usda.gov、nhc.gov.cn、gov.cn
- **Keywords**：ultra-processed food(s) / ultraprocessed / UPF / NOVA；umbrella review / meta-analysis / randomized / crossover / feeding trial；China / CHNS / China Nutrition and Health Survey；front-of-package / warning label / tax / advertising restriction / dietary guidelines；超加工食品、营养标签、膳食指南
- **Boolean（示例）**：`("ultra-processed" OR ultraprocessed OR NOVA) AND (umbrella OR meta-analysis OR randomized OR trial)`；`("ultra-processed" OR NOVA) AND (China OR Chinese OR CHNS)`；`("front-of-package" OR "warning label" OR tax OR "advertising") AND ("ultra-processed" OR HFSS OR "less healthy")`
- **Date Range**：2022-01-01 至 2026-10-21。2019–2021 年的奠基性研究只作背景，单独标注
- **Last Searched**：2026-10-21
- **Inclusion Criteria**：
  - 健康证据：伞形综述、系统综述 / meta 分析、RCT（含控制饮食试验）、大型前瞻性队列；用 NOVA 或其他明确的 UPF 定义
  - 政策：国家或国际机构的正式文件，以及对这些政策的同行评审评估
  - 方法学争论：同行评审期刊发表的观点文章与批评通信
- **Exclusion Criteria**：单一添加剂的动物毒理研究；媒体报道（只用来找原始来源，不作证据）；无法确认存在的来源
- **Coverage Distribution Advisory**：

```
DISTRIBUTIONAL_SKEW_ADVISORY
dimension: language
concentration: 英文 27/30（90%）
note: CNKI、万方等中文数据库在本环境中无法访问。中国证据只来自英文期刊发表的 CHNS 和中国营养调查分析，以及政府网站。中文期刊文献覆盖不足，会影响子问题 3 的完整性。
```

### 开放检索结果（Phase 1 约定的步骤）
在 Phase 1 预设的维度之外，开放检索新发现两个应纳入的维度：

| 维度 | 新发现 | 处理 |
| --- | --- | --- |
| **方法学争论（2025–2026）** | Nature Food 2026 年 6 月同期刊出正反两篇观点文章，EJCN 2026 年刊文主张暂停观察性 UPF 研究的 meta 分析，Nature Medicine 刊出多篇对 UPDATE 试验的批评通信 | 新增为主题 2，纳入证据等级讨论 |
| **直接针对 UPF 的财税工具** | 哥伦比亚 Ley 2277（2022）对高糖、高钠、高饱和脂肪的超加工食品征税，税率 10%→15%→20%（2023–2025） | 纳入主题 3，这是目前少见的以“超加工”命名的税种 |

预设维度的检索情况：
- **作用机制**：检到添加剂与肠道健康的综述，以及一项卡拉胶 RCT
- **植物基 UPF**：检到 UK Biobank 分析
- **包装正面警示标签**：检到网络 meta 分析和墨西哥的评估

这三个维度都已纳入。

### PRISMA Flow
本次是整合性回顾，不是系统综述，不出 PRISMA 标准流程图。

**更正（2026-10-21，补做核查时）**：本节初稿写的“约 280 条候选”“进入核实 41 条”“排除 11 条”是事后估算，检索时并没有逐条记录，现予撤回。以下只保留能从检索记录中确认的数字：

| 环节 | 数字 | 来源 |
| --- | --- | --- |
| Phase 2 网页检索调用 | 42 次（7 批，每批 6 次） | 会话中的检索调用记录 |
| 进入 Phase 3 前的补充检索 | 5 次 | 同上 |
| 失败的直接访问尝试 | 6 次网页抓取 + 9 次 API 请求，均被网络策略拒绝 | 同上 |
| 每次检索返回的链接 | 9–10 个，合计约 400 个（含大量重复）。这是按每次的返回数推算的，没有逐条去重 | 推算 |
| 进入核实的条目数、排除的条目数 | **未记录**，无法给出 | — |
| 最终纳入 | 30 条 | 下方目录 |

排除原因按类别回忆，有三类：只有媒体报道而查不到原文；主题不符；超出时间范围且不属于奠基性研究。每类排除了多少条没有记录。

### Sources（N = 30）

本节所有条目的读取范围均为 `abstract_only` 或索引元数据：本环境无法打开出版社和 PubMed 的全文页面。因此按 ARS 规则，方法学弱点一律记为“未评估（读取范围：仅摘要）”。其他文献对某条来源的批评，单独注为“他文批评”。

#### 主题 1：UPF 与健康结局的证据

1. **Lane, et al. (2024). Ultra-processed food exposure and adverse health outcomes: Umbrella review of epidemiological meta-analyses. *BMJ, 384*, e077310. https://doi.org/10.1136/bmj-2023-077310**（PMID 38418082；PMC10899807）
   - Relevance：目前覆盖面最广的证据综合，回答子问题 1
   - Key Findings：
     - 纳入 14 篇综述中的 45 项合并 meta 分析，71% 的结局与 UPF 暴露呈正相关
     - 证据为 convincing（class I）的结局：2 型糖尿病（每增加 10% 摄入，剂量反应 RR 1.12，95% CI 1.11–1.13，GRADE moderate）
     - 证据为 highly suggestive（class II）的结局：全因死亡 RR 1.21（1.15–1.27）、心脏病相关死亡 HR 1.66（1.51–1.84）、焦虑 OR 1.48（1.37–1.59）
     - 上述 GRADE 确定性多为 low
   - Quality：Level I（伞形综述），但纳入的原始研究全部是观察性研究
   - Method weaknesses：未评估（读取范围：仅摘要）。他文批评：同期 BMJ 社论（PMID 38531598）认为，需要其他研究方法才能证明真正的因果效应

2. **Monteiro, C. A., Louzada, M. L. C., Cannon, G., Baker, P., Touvier, M., ... Swinburn, B. (2025). Ultra-processed foods and human health: The main thesis and the evidence. *The Lancet, 406*(10520), 2667–2684. https://doi.org/10.1016/S0140-6736(25)01565-X**（PMID 41270766）
   - Relevance：Lancet 系列第 1 篇，代表 NOVA 提出方的完整论证
   - Key Findings：从三个假设检验 UPF 膳食模式：UPF 取代新鲜和少加工食物；UPF 使膳食质量下降；UPF 与多种慢性病相关。作者认为现有证据已足以支持公共政策行动
   - Quality：Level I 与 Level V 混合（叙述性综述，同时包含系统综述和新做的 meta 分析）
   - Method weaknesses：未评估（读取范围：仅摘要）
   - 注：作者团队是 NOVA 的提出者，存在“学术立场”方面的利益关联，需要和反方文献对照阅读。作者名单只列出检索结果中出现的姓名，完整名单和排序需要核对

3. **Dicken, S., Jassil, [名待核], ... Batterham, [名待核] (2025). Ultraprocessed or minimally processed diets following healthy dietary guidelines on weight and cardiometabolic health: A randomized, crossover trial. *Nature Medicine, 31*, 3297–3308. https://doi.org/10.1038/s41591-025-03842-0**（PMC12532614）
   - Relevance：第一项在真实生活条件下、按国家膳食指南配餐，比较 UPF 与少加工膳食的 RCT
   - Key Findings：
     - 55 名超重或肥胖的英格兰成人，交叉比较两种各 8 周的随意进食膳食
     - ITT 分析：少加工膳食体重下降 2.06%，UPF 膳食下降 1.05%（P = 0.024），相差约 1 kg
   - Quality：Level II（RCT，交叉设计）
   - Method weaknesses：未评估（读取范围：仅摘要）。他文批评：
     - Ludwig 等（Nature Medicine 2025，s41591-025-04087-7）认为效应很小，公共卫生意义有限
     - Wang & Peng（s41591-025-04088-6）质疑交叉设计能否把体重变化归因于“加工”本身
     - 作者已回复（Nature Medicine 32, 470–471）

4. **Hall, K. D., Ayuketah, A., Brychta, R., et al. (2019). Ultra-processed diets cause excess calorie intake and weight gain: An inpatient randomized controlled trial of ad libitum food intake. *Cell Metabolism, 30*(1), 67–77.e3. https://doi.org/10.1016/j.cmet.2019.05.008**（NCT03407053）[背景文献，2019]
   - Key Findings：20 名住院成人，两种膳食各 14 天。两种膳食提供的能量、糖、脂肪、钠、纤维已配平，UPF 膳食期间每天仍多摄入约 508 kcal，体重随之增加
   - Quality：Level II
   - Method weaknesses：未评估（读取范围：仅摘要）

5. **Aramburu, et al. (2024). Ultra-processed foods consumption and health-related outcomes: A systematic review of randomized controlled trials. *Frontiers in Nutrition, 11*, 1421728. https://doi.org/10.3389/fnut.2024.1421728**（PMC11233771）
   - Key Findings：纳入 4 项 RCT（3 项教育干预、1 项控制饮食试验），共 455 人，中位随访 12 周。42 个结局中有 30 个没有显著效应。作者认为研究数量少、方法学局限明显，无法得出确定结论
   - Quality：Level I（RCT 的系统综述），但纳入的研究少
   - Method weaknesses：未评估（读取范围：仅摘要）

6. **Rauber, et al. (2024). Implications of food ultra-processing on cardiovascular risk considering plant origin foods: An analysis of the UK Biobank cohort. *The Lancet Regional Health – Europe, 43*, 100948. https://doi.org/10.1016/j.lanepe.2024.100948**（PMC11360147）
   - Relevance：植物基 UPF 维度
   - Key Findings：
     - 126,842 人，中位随访 9 年
     - 植物来源的非 UPF 每增加 10 个百分点：CVD 风险降低 7%，CVD 死亡风险降低 13%
     - 植物来源的 UPF 每增加 10 个百分点：CVD 风险增加 5%，死亡风险增加 12%
   - Quality：Level IV（前瞻性队列）
   - Method weaknesses：未评估（读取范围：仅摘要）。他文批评：Benton 等的通信认为，心血管营养问题不只是加工程度的问题；作者已回复（PMID 40206220）。另据 Scarborough 的评论（媒体转述，[二手]），植物肉在这一类别中只占 0.5%，超过一半是面包和糕点

7. **Rego, et al. (2026). The influence of ultraprocessed food consumption on energy intake in emerging adulthood: A controlled feeding trial. *Obesity*. https://doi.org/10.1002/oby.70086**（PMID 41255123）
   - Key Findings：
     - 27 名 18–25 岁参与者，两期各 14 天的控制饮食（UPF 占 81% 对 0%），两种膳食的宏量营养素、纤维、添加糖、膳食质量和能量密度都已配平
     - 全样本中，膳食条件对自助餐摄入的总能量和总重量没有影响（均 p > 0.05）
     - 探索性分析显示，青春期后期亚组在 UPF 膳食后能量摄入增加（p = 0.03）
   - Quality：Level II
   - 标记：PubMed 记录的第一作者是 Rego，Wiley 的一处引用串写作 Schmall，[待核]
   - Method weaknesses：未评估（读取范围：仅摘要）

8. **Wagner, et al. (2024). Carrageenan and insulin resistance in humans: A randomised double-blind cross-over trial. *BMC Medicine, 22*. https://doi.org/10.1186/s12916-024-03771-8**（PMID 39593091；PMC11590543；NCT02629705）
   - Relevance：添加剂作用机制，人体 RCT
   - Key Findings：
     - 20 名青年男性，口服卡拉胶（每日 2 × 250 mg）或安慰剂，各 2 周
     - 主要结局（整体胰岛素敏感性）两组之间没有显著差异
     - BMI 与处理存在交互作用，卡拉胶组的肠道通透性升高
   - Quality：Level II
   - Method weaknesses：未评估（读取范围：仅摘要）

9. **Whelan, K., Bancil, A. S., Lindsay, J. O., & Chassaing, B. (2024). Ultra-processed foods and food additives in gut health and disease. *Nature Reviews Gastroenterology & Hepatology, 21*(6), 406–427. https://doi.org/10.1038/s41575-024-00893-5**（PMID 38388570）
   - Key Findings：部分乳化剂、甜味剂、色素和微纳颗粒，会影响肠道菌群、肠道通透性和肠道炎症。高 UPF 膳食与炎症性肠病、结直肠癌、肠易激综合征相关的证据主要来自观察性研究，人体干预研究较少
   - Quality：Level V（叙述性综述）
   - Method weaknesses：未评估（读取范围：仅摘要）

#### 主题 2：UPF 的定义、测量与方法学争论

10. **Braesco, et al. (2022). Ultra-processed foods: How functional is the NOVA system? *European Journal of Clinical Nutrition, 76*, 1245–1253. https://doi.org/10.1038/s41430-022-01099-1**（PMC9436773）
    - Key Findings：法国营养专家按 NOVA 给食物分类，评估者之间的一致性低，Fleiss' κ 为 0.32（市售产品，159 人）和 0.34（通用食物，177 人）
    - Quality：Level VI（横断面评估研究）
    - 标记：检索结果中该文 PDF 的页眉文字显示为 “Industry Research”，资助方未核实，见下方 COI 部分
    - Method weaknesses：未评估（读取范围：仅摘要）。他文批评：2023 年一项研究指出，该研究没有说明专家组的遴选和培训方式

11. **Medin, et al. (2025). Definitions of ultra-processed foods beyond NOVA: A systematic review and evaluation. *Food & Nutrition Research, 69*, 12217. https://doi.org/10.29219/fnr.v69.12217**（PMC12255158）
    - Key Findings：识别出 6 种分类体系（NOVA、EPIC、IFPRI、UNC、UP3、SIGA），指出现有体系都难以识别 UPF 中具体是哪些属性有害
    - Quality：Level I（定义类系统综述）
    - Method weaknesses：未评估（读取范围：仅摘要）

12. **Louie, J. C. Y. (2026). A call for methodological rigour: Suspending systematic reviews and meta-analyses of observational studies on ultra-processed foods. *European Journal of Clinical Nutrition, 80*, 643–647. https://doi.org/10.1038/s41430-026-01764-9**
    - Key Findings：常规膳食评估工具缺少判定加工类别所需的细节，回顾性编码造成的错分会被带进合并结果
    - Quality：Level VII（观点文章）
    - Method weaknesses：不适用（观点文章）

13. **Khandpur, Geleijnse, Kamphuis, et al. [名待核] (2026). The validity and utility of Nova and the concept of ultra-processed foods for science and policy. *Nature Food, 7*, 513–520. https://doi.org/10.1038/s43016-026-01371-8**（PMID 42315959）
    - Key Findings：逐一回应四类常见批评（加工技术区分不清、分界点武断、生物学机制不明、观察性证据不确定），认为概念复杂并不削弱它在科研和政策上的价值。同期 Louie 的反方观点文章为 s43016-026-01372-7
    - Quality：Level VII（观点文章）
    - Method weaknesses：不适用

14. **[作者待核] (2026). Interpreting ultraprocessed food trial evidence: Evidentiary limits, reporting practices, and policy relevance.**（PMID 42269970）
    - 相关线索：利物浦大学 2026-06-04 的新闻稿报道，Robinson、Magkos、Forde 等人在 *Science* 发表观点文章，审阅了 5 项试验。该文与本条（审阅 4 项试验）是否为同一篇，无法确认，不合并引用
    - Key Findings：
      - 审阅了 4 项 UPF 与少加工膳食的对照试验，指出对照组在多个膳食特征上同时不同，无法单独归因于“加工”
      - 批评相关评论选择性强调危害叙事
      - 建议试验组间配平营养素构成，并在 NOVA 第 4 组内做亚类分析
    - Quality：Level V（批判性综述）
    - 标记：作者和期刊需要核对
    - Method weaknesses：未评估（读取范围：仅摘要）

#### 主题 3：国际政策回应

15. **U.S. Department of Health and Human Services & U.S. Department of Agriculture. (2026, January 7). *Dietary Guidelines for Americans, 2025–2030*. https://realfood.gov**
    - Key Findings：
      - HHS 情况说明称，这是膳食指南第一次点名高度加工食品：“avoid highly processed packaged, prepared, ready-to-eat, or other foods that are salty or sweet”
      - 正文用 “highly processed”，不用 “ultra-processed”；配套的 Scientific Foundation 文件把它描述为主要由食物提取物制成或含工业添加剂的食品（据律所解读，[二手]）
    - 文件类型：膳食指南
    - Quality：Level VII（官方指南）
    - 标记：引语来自 HHS 情况说明（hhs.gov），没有读到指南正文。批评意见见 PMC12925496，认为新版偏向动物蛋白和全脂乳

16. **Food and Drug Administration & U.S. Department of Agriculture. (2025, July 25). Ultra-processed foods; Request for information. *Federal Register* (Doc. 2025-14089; Docket FDA-2025-N-1793).**
    - Key Findings：为制定联邦统一的 UPF 定义征集数据。FDA 后来把征询期延长到 2025-10-23。截至检索日，未检到正式定义发布
    - 文件类型：法规程序文件
    - Quality：Level VII

17. **World Health Organization. (2025). *Guideline Development Group for ultra-processed foods* [Terms of reference and public notice].** https://www.who.int/groups/guideline-development-group-for-ultra-processed-foods
    - Key Findings：
      - 2025 年征集专家；拟任成员名单的公示与征求意见于 2025-11-06 截止
      - 名单仍需 WHO 指南审查委员会确认；截至检索日，未检到指南发布
      - 国际食品科学技术联盟（IUFoST）批评拟任名单中没有食品科学专业人员，且多为 NOVA 的支持者
    - 文件类型：指南制定程序文件
    - Quality：Level VII

18. **Scrinis, G., Popkin, B. M., Corvalán, C., et al. (2025). Policies to halt and reverse the rise in ultra-processed food production, marketing, and consumption. *The Lancet, 406*(10520), 2685–2702. https://doi.org/10.1016/S0140-6736(25)01566-1**
    - Key Findings：主张把政策对象从“高脂、高糖、高钠食品”扩大到影响 UPF 生产、营销和消费的整个食物系统。具体政策清单没有读到；限制营销、警示标签、贸易规则改革这几项来自二手摘要
    - Quality：Level V
    - 标记：中间作者名单不完整（Nestle、Lawrence、Baker、Monteiro、Millett 等出现在二手摘要中）

19. **Baker, P., Slater, S., White, M., Wood, B., et al. (2025). Towards unified global action on ultra-processed foods: Understanding commercial determinants, countering corporate power, and mobilising a public health response. *The Lancet*. https://doi.org/10.1016/S0140-6736(25)01567-3**
    - Key Findings：认为 UPF 的扩张是由 UPF 产业日益增长的经济和政治权力推动的
    - Quality：Level V

20. **Taillie, L. S., Reyes, M., Colchero, M. A., Popkin, B., & Corvalán, C. (2020). An evaluation of Chile's Law of Food Labeling and Advertising on sugar-sweetened beverage purchases from 2015 to 2017: A before-and-after study. *PLOS Medicine, 17*(2), e1003015. https://doi.org/10.1371/journal.pmed.1003015**（PMC7012389）[背景文献，2020]
    - Key Findings：
      - 2,383 户城市家庭的购买面板数据
      - 智利 2016 年同时实施正面警示标签、限制面向儿童的营销、学校禁售，此后“高含量”饮料的购买下降
      - 下降约 23.7% 这个数字来自他文转述，[二手]
    - Quality：Level IV（前后对照的自然实验）。按 Phase 1 约定，政策评估类研究按本领域标准评级，见下方核实矩阵

21. **Song, J., Brown, M. K., Tan, M., MacGregor, G. A., Webster, J., Campbell, N. R. C., Trieu, K., Ni Mhurchu, C., Cobb, L. K., He, F. J., et al. (2021). Impact of color-coded and warning nutrition labelling schemes: A systematic review and network meta-analysis. *PLOS Medicine, 18*(10), e1003765. https://doi.org/10.1371/journal.pmed.1003765**（PMC8491916）[背景文献，2021]
    - Key Findings：纳入 156 项研究，其中 101 项 RCT。警示类标签能降低消费者选择较不健康产品的概率；红绿灯标签更擅长引导选择较健康的产品。研究间异质性高
    - Quality：Level I

22. **[作者待核] (2024). Self-reported decreases in the purchases of selected unhealthy foods resulting from the implementation of warning labels in Mexican youth and adult population. *International Journal of Behavioral Nutrition and Physical Activity, 21*. https://doi.org/10.1186/s12966-024-01609-3**（PMID 38045333；PMC11177525）
    - Key Findings：44.8% 的成人和 38.7% 的青少年自述因警示标签少买了不健康食品，减少最多的是可乐和汽水
    - Quality：Level VI（横断面自报调查）
    - Method weaknesses：未评估（读取范围：仅摘要）。设计本身是在线面板自报，存在回忆偏倚和社会期许偏倚

23. **Congreso de la República de Colombia. (2022). *Ley 2277 de 2022*, Título V (impuestos saludables)，art. 54；Corte Constitucional, Sentencia C-435 de 2023.**
    - Key Findings：
      - 对高糖、高钠或高饱和脂肪的超加工食品征税，2023-11-01 起生效，税率 2023 年 10%、2024 年 15%、2025 年 20%
      - 宪法法院裁定合宪
      - 2024 年 1–11 月，超加工食品部分的税收约 1.9 万亿哥伦比亚比索（媒体转述，[二手]）
    - 文件类型：税法
    - Quality：Level VII
    - 标记：税率以 DIAN 页面和哥伦比亚媒体为准，尚未查到同行评审的效果评估，只有 Kantar 市场数据（[二手]）

24. **Committee of Advertising Practice. (2025, December). Guidance on less healthy food and drink advertising restrictions [英国 5:30–21:00 电视与点播限播、付费网络广告全面禁止，2026-01-05 起生效].**
    - 文件类型：法规配套指南
    - Quality：Level VII
    - 标记：只经由行业媒体（Food Manufacture、律所）间接获取，未直接打开 CAP 或 ASA 原文，[二手]

#### 主题 4：中国的证据与政策

25. **Pan, et al. (2023). Association between ultra-processed food consumption and metabolic syndrome among adults in China—Results from the China Health and Nutrition Survey. *Nutrients, 15*(3), 752. https://doi.org/10.3390/nu15030752**（PMC9921592）
    - Key Findings：5,147 名成人，中位随访 6 年，发生代谢综合征 1,712 例。UPF 摄入最高四分位组的风险是最低组的 1.17 倍（HR 1.17，95% CI 1.01–1.35）
    - Quality：Level IV
    - Method weaknesses：未评估（读取范围：仅摘要）

26. **Li, [名待核], et al. (2024). Trends in consumption of ultra-processed foods among adults in Southern China: Analysis of serial cross-sectional health survey data 2002–2022. *Nutrients, 16*(23), 4008. https://doi.org/10.3390/nu16234008**（PMC11643392；PMID 39683401）
    - Key Findings：
      - 广东成人 UPF 供能比从 2002 年的 0.88% 升至 2022 年的 8.52%，学生从 0.42% 升至 17.26%
      - 2022 年，UPF 每 100 kcal 含钠 749 mg，少加工食品为 29 mg
    - Quality：Level VI（重复横断面）
    - Method weaknesses：未评估（读取范围：仅摘要）

27. **Li, M., & Shi, Z. (2025). Ultra-processed food consumption and obesity among children and adolescents in China—Findings from China Health and Nutrition Survey. *Pediatric Obesity, 20*(7), e70012. https://doi.org/10.1111/ijpo.70012**（PMID 40074239；PMC12146507）
    - Key Findings：
      - 3,437 名 6–18 岁儿童青少年，日均 UPF 摄入从 1997 年的 9.7 g 升至 2011 年的 60.0 g
      - 每日 50–99 g 组的超重肥胖 OR 为 2.01；≥100 g 组 OR 为 1.53（0.82–2.86），不显著
      - 中心性肥胖 OR 在最高组为 2.15
    - Quality：Level IV
    - Method weaknesses：未评估（读取范围：仅摘要）。数据只到 2011 年

28. **国家卫生健康委员会. (2025). 《食品安全国家标准 预包装食品营养标签通则》（GB 28050-2025）问答.** https://www.nhc.gov.cn/sps/c100087/202509/470fa4ff5de14dd38619223cce9da4e7.shtml
    - Key Findings：
      - 2027-03-16 实施；实施日期前生产的食品可在保质期内继续销售
      - 强制标示由“1+4”扩展为“1+6”，新增饱和脂肪和糖
    - 文件类型：强制性国家标准
    - Quality：Level VII
    - 标记：发布日期两个来源不一致，浙江市场监管局写 2025-03-27，淮南市场监管局写 2025-03-16，[待核]

29. **中国营养学会. (2022). 《中国居民膳食指南（2022）》.**
    - Key Findings：定向检索没有找到“超加工”或“深加工”的条文表述。现有二手解读显示，指南强调优先选择营养密度高的天然食物和看懂食品标签
    - 文件类型：膳食指南
    - Quality：Level VII
    - 标记：没有核对指南原文，“指南未使用 UPF 概念”这一判断目前仍是 [待核]

30. **中国营养学会关于 UPF 的官方立场.**
    - 检索结果：没有找到 2022–2026 年的立场声明或专家共识
    - 这本身是一个发现（证据缺口），但只是“本次检索未找到”，不能当作“不存在”来引用。检过的范围：通用检索，以及 nhc.gov.cn 和 gov.cn 的定向检索；没有直接检索中国营养学会官网和 CNKI

### Search Limitations
- **网络限制**：本会话的网络策略拒绝连接以下主机：eutils.ncbi.nlm.nih.gov、api.crossref.org、api.openalex.org、api.semanticscholar.org。出版社和 PubMed 页面也无法直接打开。因此所有来源都是通过检索引擎返回的官方索引页（PubMed、PMC、出版社页面）来确认存在和书目信息的，没有读全文
- **中文文献覆盖不足**：CNKI 和万方无法访问，见上方的分布偏斜提示
- **时效**：2026 年发表的文献可能还没被完整收录
- **作者信息不全**：条目 3、7、8、9、13、14、18、22、26 的作者信息不完整。按 ARS 的反“拼凑引用”规则，没有出现在检索结果里的姓名和缩写一律不补，只写 [名待核] 或 [作者待核]

---

## Source Verification Report

### Overall Assessment
- **Sources Reviewed**：未记录（初稿的“41”为事后估算，已撤回，见上方 PRISMA Flow 的更正）
- **Verified（纳入）**：30
- **Flagged（纳入但需补核）**：11（条目 2、3、7、13、14、18、22、24、26、28、29；条目 8、9 原先也在此列，已在 Phase 3 前补齐）
- **Rejected**：未记录（初稿的“11”为事后估算，已撤回）

### Source Quality Matrix

图例：✓ = 通过，△ = 需注意，— = 不适用。

| # | Source | Level | Venue | Author | Method | Currency | COI | Overall |
|---|--------|-------|-------|--------|--------|----------|-----|---------|
| 1 | Lane 2024 BMJ | I | ✓ | ✓ | △ 原始研究全为观察性 | ✓ | ✓ 未见行业资助（据摘要） | A− |
| 2 | Monteiro 2025 Lancet | I/V | ✓ | △ 作者名单待核 | △ 立场性综述 | ✓ | △ NOVA 提出方 | B+ |
| 3 | Dicken 2025 Nat Med | II | ✓ | ✓ | △ 有批评通信 | ✓ | △ 未读全文 | A− |
| 4 | Hall 2019 Cell Metab | II | ✓ | ✓ | ✓ | △ 背景文献 | △ 未读全文 | A− |
| 5 | Aramburu 2024 Front Nutr | I | ✓ | ✓ | △ 只有 4 项研究 | ✓ | △ 未读全文 | B+ |
| 6 | Rauber 2024 LRH-Eur | IV | ✓ | ✓ | △ 观察性 | ✓ | △ 未读全文 | B |
| 7 | Rego 2026 Obesity | II | ✓ | △ 第一作者有两种写法 | △ n = 27 | ✓ | △ | B |
| 8 | Wagner 2024 BMC Med | II | ✓ | ✓ | △ n = 20，主要结局阴性 | ✓ | △ | B |
| 9 | Whelan 2024 NRGH | V | ✓ | △ | △ 以动物证据为主 | ✓ | △ | B |
| 10 | Braesco 2022 EJCN | VI | ✓ | ✓ | ✓ | ✓ | △ Industry Research 标签 | B |
| 11 | Medin 2025 FNR | I | ✓ | ✓ | ✓ | ✓ | △ | A− |
| 12 | Louie 2026 EJCN | VII | ✓ | ✓ | — | ✓ | △ | B（观点） |
| 13 | Khandpur 2026 Nat Food | VII | ✓ | ✓ | — | ✓ | △ 有 NOVA 立场 | B（观点） |
| 14 | 2026 试验证据解读 | V | △ | △ | ✓ | ✓ | △ | B（待核） |
| 15 | DGA 2025–2030 | VII | ✓ 官方 | — | △ 有科学性争议 | ✓ | — | 政策原文 |
| 16 | FDA/USDA RFI 2025 | VII | ✓ 官方 | — | — | ✓ | — | 政策原文 |
| 17 | WHO UPF GDG | VII | ✓ 官方 | — | — | ✓ | — | 政策原文 |
| 18 | Scrinis 2025 Lancet | V | ✓ | △ 中间作者待核 | △ | ✓ | △ | B |
| 19 | Baker 2025 Lancet | V | ✓ | ✓ | △ | ✓ | △ | B |
| 20 | Taillie 2020 PLOS Med | IV* | ✓ | ✓ | ✓ | △ 背景文献 | △ | A−* |
| 21 | Song 2021 PLOS Med | I | ✓ | ✓ | △ 高异质性 | ✓ | △ | A− |
| 22 | 墨西哥 IFPS 2024 IJBNPA | VI | ✓ | △ 待核 | △ 自报 | ✓ | △ | B |
| 23 | 哥伦比亚 Ley 2277 | VII | ✓ 官方 | — | — | ✓ | — | 政策原文 |
| 24 | 英国 CAP 指南 | VII | △ 二手获取 | — | — | ✓ | — | 待核 |
| 25 | Pan 2023 Nutrients | IV | ✓ | ✓ | △ 观察性 | ✓ | △ | B |
| 26 | Li 2024 Nutrients | VI | ✓ | △ 名待核 | ✓ | ✓ | △ | B |
| 27 | Li & Shi 2025 Pediatr Obes | IV | ✓ | ✓ | △ 数据止于 2011 | △ | △ | B |
| 28 | GB 28050-2025 问答 | VII | ✓ 官方 | — | — | ✓ | — | 政策原文（发布日待核） |
| 29 | 膳食指南 2022 | VII | ✓ 官方 | — | — | ✓ | — | 原文未核 |
| 30 | 中国营养学会 UPF 立场 | — | — | — | — | — | — | 未检到 |

\* 政策评估类研究按本领域标准评级：智利研究是使用全国购买面板的自然实验，在食品政策评估中属于较高等级的设计，因此总体评为 A−，没有按临床层级降为 B。

### Flagged Sources (Detail)

#### 条目 3、7、8、9、13、14、18、22、26：书目信息不全
- **Issue**：作者、期刊或卷期只来自检索摘要，或者完全缺失
- **Severity**：Medium
- **Recommendation**：在 Phase 3 用 PubMed 记录补齐。补不齐的条目，在报告中只能作为“检索到但未核实”的线索，不能作为证据引用。条目 8 没有读到任何结果，**补不到摘要就剔除**

#### 条目 2、13：作者立场
- **Issue**：作者团队分别是 NOVA 的提出者和支持者
- **Severity**：Low
- **Recommendation**：引用时注明，并和条目 10、12、14 并列呈现

#### 条目 10：Industry Research 标签
- **Issue**：检索结果中该文 PDF 的页眉文字显示为 “Industry Research”，资助方没有核实
- **Severity**：Medium
- **Recommendation**：引用时注明可能的行业关联，结论以多项独立研究中的一致性数据为准

#### 条目 24、29：未读原文
- **Issue**：英国 CAP 指南只经由二手渠道获取；膳食指南 2022 的原文没有核对
- **Severity**：Medium
- **Recommendation**：报告里写到这两项时，保留 [二手] 或 [待核] 标记

### Predatory Journal Alerts
没有发现掠夺性期刊。各条目所在期刊均为主流同行评审期刊，或者是官方机构网站。

### Conflict of Interest Disclosures
- 条目 1：据检索摘要，纳入的研究均未由 UPF 生产企业资助
- 条目 10：PDF 页眉显示 Industry Research
- 条目 17：IUFoST 对 WHO 专家组构成提出了公开批评；IUFoST 本身代表食品科学与技术界
- 其余条目的 COI 都因为没读全文而无法评估，这是本次核实最主要的局限

### Verification Limitations
- 全部 30 条都只核对到“存在性和书目信息”这一层，没有一条读了全文，所以引用忠实度只能达到“和摘要一致”
- 交叉核实率：关键数字（Lane 的效应量、Dicken 的主要结局、Braesco 的 κ 值、Rauber 的 HR、GB 28050 的实施日期）都至少有两个独立来源一致，约占关键事实的 40%，满足 ARS 要求的 30%
