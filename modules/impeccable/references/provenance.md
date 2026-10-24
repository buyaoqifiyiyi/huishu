# Impeccable 来源与本地改编

- 上游：<https://github.com/pbakaus/impeccable>，作者 Paul Bakaus 及贡献者。
- 本次固定提交：[5cb95eea9c96479f57afe0732a45470d30183326](https://github.com/pbakaus/impeccable/tree/5cb95eea9c96479f57afe0732a45470d30183326)，提交时间 2026-10-23T08:49:46+08:00；2026-10-23 从官方 origin 读取。
- 上游 Copyright 2025 Paul Bakaus；采用内容适用 [Apache License 2.0](../../../licenses/Impeccable-Apache-2.0.txt)，并保留[上游 NOTICE](../../../licenses/Impeccable-NOTICE.md)。上游 NOTICE 提及的 ios/android 平台派生正文未导入。
- **本地改动声明（2026-10-23）：** 本模块的中文 GUIDE 与三个聚焦参考为对下列原文的选取、翻译、重组与宿主兼容改编，不是上游原版。移除其命令、二进制准备、会话存储、自动检测、hook和强制报告仪式；统一用户范围、原 DS、事实、原栈、单风格和静态动效约束。详细原文件 SHA-256 见同目录 sources.json。
- **1.2本地改动声明（2026-10-24）：** 从同一固定提交补入new-work/shape与已有critique中的前期方法，中文选取、翻译及重组为方向形成与概念审稿；实际本地资料查询和宿主浏览器参考校准为绘枢编排。不引入上游命令、会话机制或运行时，原许可与NOTICE继续适用。

| 本地文件 | 原文路径（固定提交内） | 采用实质 |
|---|---|---|
| GUIDE.md | skill/SKILL.src.md；skill/reference/operate.md | 按页面用途判断设计、简化上下文加载、批量观察成品、保留与替换语义 |
| review.md | skill/reference/critique.md；skill/reference/audit.md；skill/reference/operate.md | 先设计判断后技术证据、产品辨识度、认知负担、十启发式、优先级、适用状态和证据层级 |
| type-layout-color.md | skill/reference/typeset.md；layout.md；colorize.md；operate.md；craft-floor.md | 角色/度量/回退、分组与节奏/响应结构、语义色与实际对比检查 |
| ../art-direction/GUIDE.md | skill/reference/new-work.md；shape.md；critique.md | 区分preserve/extend/replace、内容驱动候选、首屏/阅读路径承诺、有限成品复核 |
| concept-review.md | skill/reference/new-work.md；shape.md；critique.md | 编码前概念判断、内容发现与手机路径；成品先概念后渲染 |
| refinement.md | skill/reference/polish.md；distill.md；quieter.md；bolder.md；craft-floor.md | 最小正确层修复、整条路径精修、移除阻碍、减噪、在既有系统内强调 |

**1.3本地改动声明（2026-10-24）：** GUIDE、方向形成与概念审稿增加材质/空间/运动的选择及正常浏览器过程验收，来自用户对静态版式偏重的纠正，不是新增上游摘录。[新增参考](../../art-direction/references/material-space-motion.md)为本地方法补充；[整合记录](../../../references/integration-20261024-v13.json)与原有来源表分别保留身份。

完整上游命令不随本模块提供。未带入脚本不应被调用；本地人工检查没有上游 detector 的 62 条规则覆盖承诺，也不产生其 critique-storage 的趋势/快照或 live 变体。来源中的外部仓库正文仅作资料，不扩大宿主工具或授权。


## 2026-10-24 上游 4.7.1 选择性吸收

从固定提交 [936867543ac2576920d663cc9803597f6044f3ac](https://github.com/pbakaus/impeccable/tree/936867543ac2576920d663cc9803597f6044f3ac) 的 skill/reference/audit.md 选取文字对比与指针目标判据澄清，并以 W3C SC 1.4.3 / 2.5.8 原文复核，补入 review.md 的中文审计说明。仅用于区分 AA 最低条件、例外和更高设计目标，不改变本包路由、风格、功能或评审只读边界。许可与原 NOTICE 保留。

其余选定来源中，new-work、shape、critique、typeset、layout、colorize、operate、polish、quieter、bolder及许可文本内容未变；固定源文本的历史哈希是 CRLF 检出值，原始 LF 文件单独记录，避免把行尾差异当功能更新。distill 的必要内容保护已被本地规则覆盖；不采用运行时加载仪式或覆盖用户需求的强制风格禁令。此轮没有引入 Impeccable CLI、hooks、live 会话或扫描器。
