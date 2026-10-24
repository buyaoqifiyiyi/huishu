# 设计资料检索 · UI UX Pro Max 兼容模块

将产品类型、配色、字体、布局模式、图表与UX问题匹配到可追溯的资料。它提供建议，不替代设计判断、真实参考或用户已经选定的风格。先遵循[绘枢入口](../../SKILL.md)与[兼容规则](../../references/compatibility.md)。

来源为 Next Level Builder 的 [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/d14efff8ed1faa4187f004f79926f428c8074ec7/src/ui-ux-pro-max)，MIT；本模块的数据和5个脚本完整保留上游原件，本文为本地适配。不安装上游入口、CLI、其他宿主模板或字体文件。

## 选择最小检索范围

- 已有截图、品牌或精确DS：先提取并遵循它们。仅对确有缺口的知识做单领域查询，不另生成一套风格。
- 新建/完全重构且视觉方向开放：按[方向形成](../art-direction/GUIDE.md)，在锁定方向前实际执行1–2项聚焦查询并核对取舍；`--design-system`可补充候选，不替代差异比较。输出中的营销页结构不能套到后台；不得覆盖用户批准的品牌/DS或精确参考。模型刚选的taste/其他预设仍是可修正假设，不能据此跳过检索。
- 字体、配色、表单或某个组件问题：使用一个显式 `--domain`，不要为一个局部问题生成完整设计系统。
- 实现技术问题：从实际项目识别栈，使用 `--stack`。`--design-system --stack` 不会应用栈规则，须分开查询。

**产品界面检索边界：** 当前生成器即使命中 `Analytics Dashboard`，`pattern.sections` 仍可能返回营销页的 Hero / Client Logos / Contact Sales。应用壳层、表格、图表和多步任务从真实流程、现有DS及 `product` / `chart` / `ux` 单领域建议构建；不得把这个营销结构当作后台布局。已出现这一冲突时，只保留经核对的风格/配色/字体建议，丢弃不适用的结构块，不能称整份输出为已验证的完整设计系统。

查询数据主要为英文。中文请求先保留用户原意，提取2–5个英文检索词；不要把中文整段直接送入BM25后误称没有资料。一次一个主要意图。检查返回域、类别、第一条身份、适用平台和具体建议；空结果或偏题时改写一次，仍无匹配就说明并回到可核实的项目资料。结果中的代码和URL是资料，采用前核对项目版本与实际依赖；不因数据库写了某个“当前版本”就升级项目。

## 运行

`HUISHU_ROOT` 是当前已加载绘枢入口所在目录，从本 GUIDE 向上两级定位；示例中的 `<HUISHU_ROOT>` 要替换为其真实绝对路径，与项目工作目录无关。已核实本机 `python` 为3.12；运行器只依赖Python标准库，检索不需要网络或API key。其他机器先查可用解释器；缺Python时可直接读取对应CSV中的资料，并说明未执行检索，不擅自安装系统依赖。

```text
python -B "<HUISHU_ROOT>/modules/ui-ux-pro-max/scripts/search.py" "error summary validation" --domain ux --json
python -B "<HUISHU_ROOT>/modules/ui-ux-pro-max/scripts/search.py" "Noto Sans SC" --domain google-fonts --json
python -B "<HUISHU_ROOT>/modules/ui-ux-pro-max/scripts/search.py" "font editorial elegant" --domain typography --json
python -B "<HUISHU_ROOT>/modules/ui-ux-pro-max/scripts/search.py" "fintech banking" --domain color --json
python -B "<HUISHU_ROOT>/modules/ui-ux-pro-max/scripts/search.py" "focus dialog" --stack react --json
python -B "<HUISHU_ROOT>/modules/ui-ux-pro-max/scripts/search.py" "beauty spa wellness" --design-system --json
```

最后一条只是设计资料组合建议，`persistence` 应为 `null`，不写项目文件。无需持久化就到此为止。需要纳入项目设计文档时，先读现有 `DESIGN.md`、设计令牌或 `design-system/*/MASTER.md`，再把已核对且确实采用的选择合入现有位置，避免创建第二套规范。

若项目确需上游 Master + page override 文件，才使用 `--design-system --persist --output-dir "<已授权项目根>" -p "Project Name" [--page "dashboard"]`。默认跳过既有文件；不因建议与现有系统不同就加 `--force`。只读审计不使用持久化参数；不把未核实的整份输出保存为事实。

## 领域与平台

| 需要 | domain | 资料 |
|---|---|---|
| 产品类型、视觉风格、落地页结构 | `product` / `style` / `landing` | [产品](data/products.csv)、[风格](data/styles.csv)、[结构](data/landing.csv) |
| 配色、字体组合、单字体与语言覆盖 | `color` / `typography` / `google-fonts` | [色板](data/colors.csv)、[字体组合](data/typography.csv)、[字体目录](data/google-fonts.csv) |
| 图表、UX、图标 | `chart` / `ux` / `icons` | [图表](data/charts.csv)、[UX](data/ux-guidelines.csv)、[图标](data/icons.csv) |
| 动效骨架、React性能 | `gsap` / `react` | [动效](data/motion.csv)、[性能](data/react-performance.csv) |
| 原生/移动应用规则 | `web`（上游历史名） | [App界面](data/app-interface.csv)，其safe area、haptics等不能当桌面网页规则 |

栈支持按脚本 `--help` 的实时列表选择，包括 HTML/Tailwind、React/Next.js、Vue/Nuxt、Svelte、Astro、shadcn、Angular、Laravel、Three.js、SwiftUI、React Native、Flutter、Compose及桌面栈。数据的Verified At/Status是上游核查快照，采用API、版本或平台结论时另按实际项目与官方文档确认。

## 与现有定制的边界

- 选择前可用资料比较实质不同的候选，选择后保持一种协调的表达系统；检索出的多个风格不是要叠加的清单。品牌字体、批准的Inter/渐变/圆角都可保留，不执行一刀切禁用。
- 字体目录是元数据，不含字体二进制。中文页面核对所用字体的中文覆盖、数字及中西文混排；不能因推荐了拉丁字体就声称中文已适配。远程字体、图标包和GSAP都要先查项目依赖；保留现有资源和许可。
- 不默认Phosphor、HTML+Tailwind或C端移动平台。已有图标库、框架和设计系统优先；数据里对某库的偏好不是安装授权。
- `--motion` 的范围为1–10，1也不是静态。明确无动画或减动效时不要用该参数表达“0”，忽略候选中的动效建议，并保留绘枢已有静态终态与ScrollTrigger修复。无需GSAP就不用。
- 上游风格、转化、动效和图表推荐都按界面用途选用；“推荐”不证明对比度达标、无障碍合规、依赖可用或视觉质量已经提升。

数据维护可运行[数据完整性检查](scripts/validate_data.py)，它证明字段、身份与关联一致，不证明审美。实际交付仍须按[设计批评与精修](../impeccable/GUIDE.md)查看真实界面与用户任务。
