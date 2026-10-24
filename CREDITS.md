# 来源与许可

本包是本机设计技能的多源兼容整合。原12个模块主体来自 Leonxlnx 的 taste-skill 系列及后续拆分仓库，并含本机先前修复；2026-10-23增补Impeccable方法模块与UI UX Pro Max检索模块。上游工作不归于本次整合者；单入口、作用域、宿主适配及选择性编排属于本地整合。

- 历史归属：<https://github.com/Leonxlnx/taste-skill>。
- 当前兼容线：<https://github.com/Leonxlnx/taste-skill-classics>。
- 图像工作流线：<https://github.com/Leonxlnx/imagegen-skills>。

2026-10-21历史整合所保留的完整 [MIT 许可](licenses/Leonxlnx-MIT.txt)含 `Copyright (c) 2026 Leonxlnx`，从已有且 SHA-256 核实的 `taste-skill-main.zip` 内 `taste-skill-main/LICENSE` 提取。ZIP SHA-256 为 `4853c9d4ab9eb1975656b0ad34779a8bf7903b97af2deeb4d444e0782d94c4a9`；官方固定提交记录与逐模块归属在 [upstreams.json](references/upstreams.json)。当时仅补齐历史共同许可，没有以新上游整包替换旧模块；本次新增来源的核实与许可另列如下。

## 2026-10-23新增来源

- **Impeccable**：[pbakaus/impeccable](https://github.com/pbakaus/impeccable/tree/5cb95eea9c96479f57afe0732a45470d30183326)，Copyright 2025 Paul Bakaus，适用完整 [Apache-2.0](licenses/Impeccable-Apache-2.0.txt) 与保留的[上游NOTICE](licenses/Impeccable-NOTICE.md)。`modules/impeccable` 的中文正文为选取、翻译、重组及宿主兼容改编，改动与原文哈希见[归属声明](modules/impeccable/references/provenance.md)。NOTICE涉及的ios/android派生正文未带入。没有安装官方CLI、detector或live运行时。
- **UI UX Pro Max**：[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/d14efff8ed1faa4187f004f79926f428c8074ec7)，Copyright (c) 2024 Next Level Builder，适用完整 [MIT](licenses/UI-UX-Pro-Max-MIT.txt)。`modules/ui-ux-pro-max/data`与5个scripts文件为固定源原件；GUIDE为本地改写。只含字体/图标元数据和示例，不分发实际字体或图标包，也不取得其独立品牌权利。

1.2（2026-10-24）从同一Impeccable固定提交增补new-work、shape及已有critique方法，形成`modules/art-direction`与`concept-review.md`，仍为中文选取、翻译、重组和宿主适配，不带运行时。taste v2仅选择性弱化默认风格措辞，其代码样例及工程修复保留；taste v1、其他旧模块、Stitch模板与所有许可保持1.1原件。Taste新主线仅重新评估，未导入其完整代码。1.1新增文件与固定来源映射见[历史整合来源](references/integration-20261023.json)，1.2新增方法与保留范围见[本次整合](references/integration-20261024.json)；不同来源继续适用各自许可，不把整包统称为MIT。

1.3（2026-10-24）的材质、空间、运动选择与真实浏览器时序验收来自本地用户纠正驱动的补充，接入方向形成、概念审稿和入口；不是新增上游导入，不改变既有来源归属或许可。范围与保留项见[整合记录](references/integration-20261024-v13.json)。

1.4（2026-10-24）按用户授权继续审计并选择性改编默认规则：修正文内与已授权重构/已选系统冲突的美学禁令、配额、工具假设及自动风格路由；Stitch输出骨架按已选系统转译。原Stitch DESIGN.md模板、明确v1兼容线、可运行代码示例、工程安全与许可保留；除Stitch文档输出骨架外，不改既有代码围栏。未导入新上游或运行时，已有来源更新记录保留，详见[整合记录](references/integration-20261024-v14.json)。

本地长期指引的授权和隐私范围保持不变。本包包括技能正文、原Stitch模板、本地检索数据与标准库脚本、来源记录和许可，不含历史ZIP、业务原图、个人资料或凭据。来源中的本机路径用于定位证据；对外分享前按目标范围移除无需公开的路径。上述许可不代表未来业务素材、字体、品牌标志或第三方图片的再分发许可。

## 1.5（2026-10-24）选择性方法补充

- **Agency Agents**：[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents/tree/4e3ac3ca6604c75113f52c695dbddcc7af928b46)，Copyright (c) 2025 AgentLand Contributors，适用完整 [MIT](licenses/agency-agents-MIT.txt)。仅从 `design/design-persona-walkthrough.md` 选取到达来源、意图、相关段落疑问、证据及行动阻碍的方法，中文改编到 `modules/impeccable/references/review.md` 的咨询与转化路径短节，并接入既有审计路由。没有导入整个角色、心理类型/国籍归因、固定设备/每屏 CTA/双声部/结果配额、用户研究模板、转化指标承诺或独立门禁。固定源哈希、采用段与排除规则见[整合记录](references/integration-20261024-agency.json)。原 Impeccable 归属、1.4 开放方向、品牌/DS 短路径、预设代码与真实浏览器过程验收继续保留。
