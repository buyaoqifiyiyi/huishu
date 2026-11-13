# 现代 Web 实现参考

本模块选择性吸收 GoogleChrome/modern-web-guidance，提供本地按需指南；它是实现参考，不决定视觉方向或扩大改动范围，也不自行启动方向形成或概念审稿。中文入口为本地改编，guides 内为固定提交原文，来源见 [provenance.json](provenance.json)，完整许可见 [Apache-2.0](../../licenses/Modern-Web-Guidance-Apache-2.0.txt)。

## 何时使用

实现或修复 Web 弹层、响应式布局、交互动画、输入法提交、表单反馈、前端性能或不可信 HTML 处理时，若需要选择平台能力或核对已知陷阱，先按下表读取匹配指南。一般编码由 Yanlu 管理；视觉方向仍走绘枢现有路线。只改文案、颜色或间距、已有明确实现的小修、纯设计图、后端/API/数据库任务不强制读取。

## 本地工作流

1. 先读目标组件和现有设计系统，确认行为、框架及项目已有浏览器支持范围；将需求转成具体平台问题，如 confirmation dialog 或 IME enter submit。按索引选相关文件，或在本模块 guides 目录用 `rg` 搜索；不一次加载全部正文。
2. 阅读命中指南的实现及完整 fallback 段。按需求选最简单的可用能力；已有组件或 GSAP 等动效方案满足需求时继续复用，不为了“原生化”替换整套库。已有动画仅补减动效时直接沿用现有动效模块，不转向 View Transitions。原生 dialog 的自动归还焦点只在触发元素仍存在且浏览器行为满足任务时可依赖；SPA 重渲染、触发元素移除或自绘弹层应核实实际焦点去向并提供合理落点，不机械套用示例的禁止手动归还规则。指南中的 MANDATORY、默认模态、字体比例和样例样式均限定于对应示例，不能覆盖用户要求、项目约束或批准设计。
3. 固定快照里的 Baseline 状态和版本表可能过时。项目有支持矩阵时以其为准；没有时优先广泛可用能力，较新特性在采用前从官方兼容资料核实并做特性检测/渐进增强。不要默认用户只用 Chrome；目标环境显著影响行为且无法从项目确认时才澄清。必要降级保留功能、键盘与可访问性，不能为减少代码删除现有可靠回退。
4. 框架适配检查 SSR 的 DOM 访问、实例 ID、ref 与框架管理的节点边界。不要照抄原文的类型强转、全局 CSS 或升级构建目标建议；只有真实项目需要时调整。输入法场景检查完整 Safari 降级说明；静态检查不代表真实输入法通过。
5. 验证当前变更涉及的打开/关闭、键盘焦点、减动效、窄屏与降级路径。动效在真实浏览器触发并观察，保留绘枢的过程验收；未测设备或浏览器明确标注。汇报实际采用的指南及其影响即可，不强制增加标题、逐条引文或无关说明。

上游原文中的 `npx ... retrieve` 是其在线 CLI 用法，不是本模块自动执行指令。先在本地按 ID 找文件；未收录的主题可按当前联网规则读取上游固定版本或官方文档，不能声称本地完整收录。此模块没有安装 CLI、扫描器、插件、后台服务或 Node 依赖；不隐式执行 `@latest`、申请全局权限或安装 polyfill。用户要求全仓现代化时另行评估扫描工具，具体功能任务不全仓扫描。

## 本地索引

| ID | 指南 |
|---|---|
| `dialog` | [Dialog](guides/ui-components/dialog.md) |
| `navigation-drawer` | [Navigation Drawer](guides/ui-components/navigation-drawer.md) |
| `declarative-dialog-popover-control` | [Declarative Dialog and Popover Control](guides/ui-behaviors/declarative-dialog-popover-control.md) |
| `prevent-page-scroll-under-modal-dialog` | [Prevent the Page Underneath a Modal Dialog from Scrolling](guides/ui-behaviors/prevent-page-scroll-under-modal-dialog.md) |
| `light-dismiss-a-dialog` | [Light-Dismiss a Dialog](guides/ui-behaviors/light-dismiss-a-dialog.md) |
| `responsive-design` | [Responsive design](guides/css/responsive-design.md) |
| `css-layout` | [CSS Layouts and Responsive Design](guides/css/css-layout.md) |
| `size-aware-styling` | [Size Aware Styling](guides/css/size-aware-styling.md) |
| `animate-to-intrinsic-sizes` | [Animate to Intrinsic Sizes](guides/css/animate-to-intrinsic-sizes.md) |
| `same-document-transitions` | [Same Document Transitions](guides/ui-behaviors/same-document-transitions.md) |
| `ime-safe-enter-submit` | [IME-safe enter-to-submit](guides/forms/ime-safe-enter-submit.md) |
| `validate-input-after-interaction` | [Validate Input After Interaction](guides/forms/validate-input-after-interaction.md) |
| `performance` | [Performance](guides/performance/performance.md) |
| `accessibility` | [Accessibility Coding Guidelines](guides/accessibility/accessibility.md) |
| `sanitize-untrusted-html` | [Sanitizing Untrusted HTML](guides/security/sanitize-untrusted-html.md) |
