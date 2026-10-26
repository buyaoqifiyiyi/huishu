---
name: huishu
description: 网页和应用UI设计的统一入口：新建或完全重构时发散方向、检索参考，考虑材质、空间与动效并实际体验审稿；现有界面精修、营销页咨询/转化路径审计、按截图实现、设计稿演示动画与按需MP4/GIF导出、图像参考、品牌板及Stitch DESIGN.md。保留品牌、技术栈和现有设计系统；小修走短路径，普通后端或逻辑修复不加载视觉预设。
license: MIT AND Apache-2.0; source-specific terms and notices in CREDITS.md
metadata:
  version: "1.6.0"
---

# 绘枢 · Huishu

先确定用户要交付的产物、已有参考与设计系统，再从下表选当前工作所需模块。自然任务可自动触发；旧文件夹名与旧 frontmatter 名均作为文字口令理解，宿主选择器使用 `$huishu`。这些模块不是独立技能，不全量加载。

先区分 preserve（按批准参考/DS保留）、extend（在既有系统内延展）与 replace（新建或授权完全重构）。新建或完全重构且视觉方向开放时，先读[方向形成](modules/art-direction/GUIDE.md)：基于真实内容实际检索资料、在允许联网时查看外部参考、比较结构不同的候选，把[材质、空间与运动](modules/art-direction/references/material-space-motion.md)纳入取舍，再写首屏、桌面/手机路径和关键行为时序承诺，做[概念审稿](modules/impeccable/references/concept-review.md)后实现。不要先加载 taste 全篇替默认方向补理由。精确参考、既有DS延展、小修与只读审计保留短路径。成品先验概念承诺，再按[设计批评与精修](modules/impeccable/GUIDE.md)检查渲染与交互；动态体验须在真实浏览器正常模式实际触发和观察过程，不能仅凭静态/禁动画截图验收。缺少浏览器证据时说明，不能以构建通过代替验收。

| 当前产物或情境 | 读取模块 | 分流依据 |
|---|---|---|
| 界面不好看、模板感、审美评审；Impeccable / critique / polish | [设计批评与精修](modules/impeccable/GUIDE.md) | critique/audit只读；明确要求改造才修改；按排版、布局、色彩等具体问题精修 |
| 访问多但咨询少、客户不信任；营销页/服务详情的咨询或转化路径审计 | [设计批评与精修](modules/impeccable/GUIDE.md) → [到达意图走查](modules/impeccable/references/review.md#咨询与转化路径按需走查) | 对应到达意图、疑问、可见证据、阻碍和下一步；只读审计不修改，不把推演当用户研究；字号小修、精确参考实现不触发 |
| 配色、字体、图表、UX或技术栈资料；UI UX Pro Max | [设计资料检索](modules/ui-ux-pro-max/GUIDE.md) | 本地Python检索；建议须核对语义与平台，不覆盖用户参考或现有DS |
| 后台、工具与多步骤产品界面 | 方向开放的新建/完全重构先[方向形成](modules/art-direction/GUIDE.md)，再按需[检索](modules/ui-ux-pro-max/GUIDE.md)与[精修](modules/impeccable/GUIDE.md) | 既有系统优先真实组件/DS；内容与任务决定表达，不因产品类别强制灰色、平面或静态，也不套营销页结构 |
| 新建网页/应用，或完全重构且没有已批准精确参考 | [方向形成](modules/art-direction/GUIDE.md) → [概念审稿](modules/impeccable/references/concept-review.md) | 检索/校准 → 不同候选及材质/空间/运动取舍 → 首屏/路径/时序承诺 → 浏览器实际体验；选定后按需读实现参考 |
| 材质、光照、纵深、动效或交互节奏的设计与验收 | [材质、空间与运动](modules/art-direction/references/material-space-motion.md) | 按任务选择表达及触发/变化/终态，验证正常、中断与适用替代；不把局部效果扩大成重设计 |
| taste-skill / design-taste-frontend；需要经典 v2 实现参考 | [taste v2](modules/taste-skill/GUIDE.md) | v2 experimental 兼容线可选；开放方向仍先走方向形成，v2不再是新建默认风格；明确复现旧版兼容行为时按其范围执行 |
| 项目明确依赖 taste v1；taste-skill-v1 / design-taste-frontend-v1 | [taste v1](modules/taste-skill-v1/GUIDE.md) | 保留完整 v1 正文；同一任务不混入 v2 |
| 已有网站或应用的视觉审计、针对性改造；redesign-existing-projects | [改造](modules/redesign-skill/GUIDE.md) | 先审计，保留真实内容、功能、品牌与栈；只要求审计则只读；授权完全重构且方向开放时先接方向形成 |
| 设计稿/截图/Figma 的演示动画、功能卡片叙事循环，或相关 MP4/GIF 导出 | [设计稿演示动画](modules/design-to-motion/GUIDE.md) | 保留源画面与背景，区分独立展示和网站区域；格式按请求；普通菜单/悬停交互、静态截图实现不触发 |
| 根据截图或设计稿实现；image-to-code | [图到代码](modules/image-to-code-skill/GUIDE.md) | 已有参考直接检查和提取；新参考才先生成；精确 DS 或小修直接实现 |
| 只要网页设计参考图；imagegen-frontend-web | [网页图像](modules/imagegen-frontend-web/GUIDE.md) | 每节一张独立横图，统一视觉系统；此阶段只图不代码 |
| 只要 iOS / Android App 屏幕、流程概念；imagegen-frontend-mobile | [移动图像](modules/imagegen-frontend-mobile/GUIDE.md) | 只图不代码；按要求决定手机框与多屏展示 |
| 品牌标志、识别系统、品牌总览板；brandkit | [品牌板](modules/brandkit/GUIDE.md) | 先判定新品牌、现有延展或授权重塑；品牌板可在一图内分格 |
| 给 Google Stitch 写语义设计系统；stitch-design-taste | [Stitch](modules/stitch-skill/GUIDE.md) | 产物 DESIGN.md；[原模板](modules/stitch-skill/DESIGN.md)按需适配 |
| 已选工业/瑞士印刷方向，或显式 industrial-brutalist-ui | [工业参考](modules/brutalist-skill/GUIDE.md) | print / telemetry是可选表达；不因题材词自动锁色板或整套构图 |
| 已选电影式方向，或显式 gpt-taste | [电影参考](modules/gpt-tasteskill/GUIDE.md) | 按需借鉴叙事和运动方法，不因“作品集/电影”自动锁GSAP、AIDA或固定Hero；保留正常与减动效路径 |
| 已选极简方向，或显式 minimalist-ui | [极简参考](modules/minimalist-skill/GUIDE.md) | 按内容取舍字体、留白、平面和用色，不因“文档/温暖”自动套一套外观 |
| 已选触感/纵深方向，或显式 high-end-visual-design | [纵深参考](modules/soft-skill/GUIDE.md) | 材质、层次和运动按角色选择；double-bezel、玻璃和胶囊不是必选套件 |

用户明确需求、批准参考、现有品牌/DS、真实内容、技术栈与可访问性优先于模块的风格默认。候选阶段允许比较不同方向；交付时形成协调的表达系统，不必选命名预设，也不要求每个章节同色、同材质、同构图。预设是按需参考，工程技巧可以复用，互相冲突的风格硬规则不同时强加。已有精确参考决定视觉，无需另选预设；普通软件界面或小修也无需套营销页结构。要求某风格时在其边界内设计，不另加载 taste 施加第二套规则。仅供校准的外部网站不等于用户批准的精确目标；上次成功的页面、配色、材质和动效也不是下一任务的默认模板。

生成图像、切换阶段或遇到模块强制措辞冲突时，读[兼容与工具规则](references/compatibility.md)。图像调用使用实际宿主图像工具和系统 imagegen 指引；尺寸、次数、依赖及验证按真实能力报告。只要求图像或 DESIGN.md 时完成该产物；代码实现与远程 Stitch 执行按用户实际任务进入。

完成后检查用户要求的真实终点：设计图可见、代码可运行及适配、改造前后功能，或 DESIGN.md 可读与令牌一致；分别报告已执行、静态检查和未验部分。维护与来源见[维护映射](references/maintenance.md)和[归属许可](CREDITS.md)。

新增两族仅为包内模块，没有注册 Impeccable/UI UX Pro Max 独立入口，也不代表安装了上游运行时。Taste新主线的[评估结论](references/taste-mainline-assessment.md)保留历史决策；1.2的前期创作链来自选择性方法整合，1.3的材质/空间/运动补充来自本地用户纠正，不切换主线或新增入口。
