# 绘枢维护映射

统一维护入口为 `huishu/SKILL.md`，模块维护单位为 `huishu/modules/<原目录>/GUIDE.md`。保持单入口，不重新创建已合并的独立技能。正文旧名作为文字口令；宿主发现、自动选择、模块读取及业务成功分别取证。

| 模块 | 兼容线 / 已核实上游 | 保留重点 |
|---|---|---|
| art-direction / impeccable | pbakaus/impeccable，skill/SKILL.src.md 与选定 skill/reference | 1.2补入new-work/shape与概念审稿；1.3本地补入材质/空间/运动及真实时序验收；中文改编的方向形成、批评、排版/空间/色彩与精修；纯文本工作流，不导入二进制、hooks、官方检测器或live会话 |
| ui-ux-pro-max | nextlevelbuilder/ui-ux-pro-max-skill，src/ui-ux-pro-max/data 与 scripts | 完整检索数据及5个标准库脚本，GUIDE单独适配；不导入平台模板/入口/安装器；数据建议不能盖过现有DS |
| taste-skill | Leonxlnx/taste-skill-classics，skills/taste-skill-v2-experimental | v2 experimental 可选兼容/实现参考；1.2弱化默认风格锁，工程定制与代码样例保留；上游新 taste 架构只参考，不自动替换 |
| taste-skill-v1 | Leonxlnx/taste-skill-classics，skills/taste-skill-v1 | 明确 v1 依赖才读取；正文与样例完整保留，不混 v2 |
| brutalist-skill / gpt-tasteskill / minimalist-skill / soft-skill / stitch-skill | Leonxlnx/taste-skill-classics，对应 skills 目录 | 各自风格边界、静态/减动效、Stitch 语义文档与模板 |
| brandkit / imagegen-frontend-mobile / imagegen-frontend-web | Leonxlnx/imagegen-skills，对应 skills 目录 | 现有品牌优先、尺寸诚实、只图阶段、分节与移动框规则 |
| image-to-code-skill | Leonxlnx/imagegen-skills，skills/image-to-code | 已有 / 新建参考 / 直接实现三路分流 |
| redesign-skill | 历史 taste-skill 本地保留；新主线已合并，非同路径自动升级 | 真实内容、原栈、功能与改造前后同宽度回归 |

来源详单、固定 commit 与此前采用/拒绝理由保存在 [upstreams.json](upstreams.json)。旧模块的classics/imagegen来源沿用2026-10-21核实基线；本次2026-10-23只新增Impeccable与UI UX Pro Max固定源核对，并重新评估Taste主线。Taste `6010f91a9935f1c167dfc500fb1a475681892e6b` 与此前记录相同，不自动取代本机 v2 兼容线；classics 为 `5e08c9383dc4ad7fc0df70e1ac8cfa09ec356305`，imagegen-skills 为 `beb16b0d0f4dae9a6f5cb04ea41e97b93a54ab8e`。

历史2026-10-21整合的13个来源文件、哈希及插入段保留在 [coverage.json](coverage.json)，Stitch DESIGN.md未改。原始清单见 [source-inventory.json](source-inventory.json)，历史结构检查见 [static-validation.json](static-validation.json)。这些文件保留历史身份，不冒充当前新增模块的检查记录。原快照在当时任务工作区 `work/skill-consolidation-20261021/snapshots/<原目录>/`；1.1快照与检查在当时任务的 `work/huishu-merge/run/`；1.2基线/候选在 `work/huishu-v12/run/`，不复制进安装包。

2026-10-23新增来源：Impeccable固定 `5cb95eea9c96479f57afe0732a45470d30183326`，逐文件依据与改编声明见[来源](../modules/impeccable/references/provenance.md)；UI UX Pro Max固定 `d14efff8ed1faa4187f004f79926f428c8074ec7`，数据/脚本原件哈希见[整合来源](integration-20261023.json)。Taste[新主线评估](taste-mainline-assessment.md)仅作决策依据，未导入其运行时/默认风格。

2026-10-24的1.2前期创作链与v2风格适配见[整合记录](integration-20261024.json)。固定源未变，新增new-work/shape的逐文件哈希进入Impeccable来源表；原数据、脚本、许可与非v2旧模块保持1.1原件。只保留一个SKILL入口；开放方向先检索/校准/比较/审稿，精确参考、DS延展、小修、只读审计保持短路由。方法执行与业务审美效果分别验收。

1.3的本地补充见[整合记录](integration-20261024-v13.json)：针对静态版式偏重的用户纠正，将表达选择接入候选、承诺、审稿与浏览器过程验收。不是新增上游导入；不改色彩/字体全局禁令，不添加运行时、依赖或入口。1.3基线/候选在当时任务的 `work/huishu-v13/run/`，实际业务和宿主触发另验。

1.4的[规则审计记录](integration-20261024-v14.json)对应 `work/huishu-v14/run/` 的1.3基线：对实际会否决授权方案的正文、路由和文档输出骨架作选择性修正，不仅依赖顶层例外覆盖。预设身份可保留，但不自动锁某库、字体、色板、布局和数量；主动创作与减动效保障分别执行。1.3的暗场金属个人站是业务产物，未加入本包作为模板或默认色板。保护taste工程段和可运行代码围栏、v1兼容线、Stitch原模板、UIUX44文件、许可、现有审计准则与历史来源更新；新旧文案差异不应在未来上游同步时被整包覆盖。

两个新增族及前期流程的后续维护目标均在 `huishu/modules/` 内：Impeccable及art-direction只更新所选方法并保留中文适配与前期/成品审稿分工，UI UX Pro Max的脚本与数据按一致固定版本更新，保留GUIDE中的查询/平台/只读边界。同步外部 `sources.json` 的 huishu-visual 维护单元；不得按仓库名重新安装独立Skill、插件或覆盖根路由。

未来更新先定位具体模块和当前修复，建立快照，再选择性合并。保持品牌资产/尺寸处理、图到代码分流、真实内容保护、减动效以及 taste StickyStack / HorizontalPan 修复；不按上游新描述覆盖本机自动触发。结构检查通过只支持结构兼容；真实图像、代码、浏览器、远程生成与自动加载另验。完整许可与归属见 [CREDITS.md](../CREDITS.md)。

1.5的[Agency选择性整合记录](integration-20261024-agency.json)固定 `msitarzewski/agency-agents@4e3ac3ca6604c75113f52c695dbddcc7af928b46` 的 `design/design-persona-walkthrough.md`。维护目标仅为 `modules/impeccable/references/review.md` 的“咨询与转化路径：按需走查”短节、其 GUIDE 分流及根路由/描述；仅在营销页咨询/转化审计时触发。未来先比较记录中的采用段和当前中文适配，不整包恢复上游角色、心理归因、固定设备/双声部/每屏 CTA/结果数量或门禁，不引入 UX 研究模板和无数据收益承诺。保留 1.4 的开放方向、材质/空间/运动、真实浏览器过程验收、品牌/DS 与精确参考短路径及所有既有工程代码；既有历史来源记录不改写。完整新增 MIT 见[许可](../licenses/agency-agents-MIT.txt)，本次不改外部来源注册或自动化。

1.6的[Elaya整合记录](integration-20261026-elaya.json)固定 `elayadesign/ai-design-skills@a2735a3eaf092eaaffb6dc17df25de33ef3bd048`。维护目标为 `modules/design-to-motion` 与既有营销策略短节；保留中文分流、源图/品牌、真实内容、按请求格式、静态/交互短路径及所有既有工程定制。上游只取所列方法，逐帧检查脚本与测试为本地实现；不按上游description恢复全Web触发、固定审美、三件套或假定工具。完整MIT及间接归属保留；未来在同一huishu-visual维护单元选择性追踪。
