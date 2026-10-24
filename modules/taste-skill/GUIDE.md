---
name: design-taste-frontend
description: Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look templated. Real design systems when applicable, audit-first on redesigns, strict pre-flight check.
---

> 绘枢模块：taste v2 experimental 兼容线，作为营销页、作品集、编辑页的可选实现参考；不自动升级到上游新架构。先遵循[单入口](../../SKILL.md)和[兼容与工具规则](../../references/compatibility.md)。新建或获准完全更换视觉方向时，先走入口的方向形成分支，再按已选方向取用本模块；旧名字仅为包内文字口令，不注册独立技能，旧 frontmatter 仅作来源元数据。
>
> 适用范围：下文旧美学默认、禁用清单和数值预设均为待评估建议，包括最终 pre-flight 的重复检查项；它们不决定新方向，也不因强制措辞覆盖用户指定的具体风格、现有品牌/DS、批准参考或真实内容。字体、色彩、构图、主题和装饰按方向与内容判断；可说明适用或不适用，不为通过风格检查而改成另一套模板。可访问性、内容真实性、功能、依赖核实及已有动效安全修复仍须遵守。

# tasteskill: Anti-Slop Frontend Skill

> Landing pages, portfolios, and redesigns. Not dashboards, not data tables, not multi-step product UI.
> Every rule below is **contextual**. None of it fires automatically. First read the brief, then pull only what fits.

---

## 0. BRIEF INFERENCE (Read the Room Before Anything Else)

Before touching code or tweaking dials, **infer what the user actually wants**. Most LLM design output is bad because the model jumps to a default aesthetic instead of reading the room.

### 0.A Read these signals first
1. **Page kind** - landing (SaaS / consumer / agency / event), portfolio (dev / designer / creative studio), redesign (preserve vs overhaul), editorial / blog.
2. **Vibe words** the user used - "minimalist", "calm", "Linear-style", "Awwwards", "brutalist", "premium consumer", "Apple-y", "playful", "serious B2B", "editorial", "agency-y", "glassy", "dark tech".
3. **Reference signals** - URLs they linked, screenshots they pasted, products they named, brands they're competing with.
4. **Audience** - B2B procurement panel vs. design-conscious consumer vs. recruiter scanning a portfolio. The audience picks the aesthetic, not your taste.
5. **Brand assets that already exist** - logo, color, type, photography. For redesigns, these are starting material, not optional input (see Section 11).
6. **Quiet constraints** - accessibility-first audiences, public-sector, regulated industries, trust-first commerce, kids' products. These constraints OVERRIDE aesthetic preference.

### 0.B Output a one-line "Design Read" before generating
Before any code, state in one line: **"Reading this as: \<page kind> for \<audience>, with a \<vibe> language, leaning toward \<design system or aesthetic family>."**

Example reads:
- *"Reading this as: B2B SaaS landing for technical buyers, with a Linear-style minimalist language, leaning toward Tailwind utilities + Geist + restrained motion."*
- *"Reading this as: solo designer portfolio for hiring managers, with a project-first archive language supported by the work, leaning toward native CSS + a clear project index + direct case-study access."*
- *"Reading this as: a motion designer portfolio for art directors, with a reel-led language supported by the supplied films, leaning toward a media stage + concise project navigation + accessible playback."*
- *"Reading this as: redesign of a public-sector service site, with a trust-first language, leaning toward GOV.UK Frontend or USWDS."*

### 0.C If the brief is ambiguous, ask one question, do not guess
Ask exactly **one** clarifying question - never a multi-question dump - and only when the design read genuinely diverges. Example: *"Should this feel closer to Linear-clean or Awwwards-experimental?"*

If you can confidently infer from context, **do not ask**. Just declare the design read and proceed.

### 0.D Anti-Default Discipline
Check whether familiar patterns such as purple gradients, centered heroes, equal feature cards, glass surfaces or neutral sans type actually serve the brief. Do not select or reject them merely because they are common. Ground the design read in the content and references, rather than replacing one familiar template with another.

---

## 1. THE THREE DIALS (Optional Description of the Chosen Direction)

Choose the direction from the brief, real content and references first. If useful for implementation, describe it with these dials; they do not generate or rank directions.

* **`DESIGN_VARIANCE`** - 1 = symmetrical / predictable, 10 = strongly asymmetric / experimental.
* **`MOTION_INTENSITY`** - 1 = static, 10 = extensive choreography / physics.
* **`VISUAL_DENSITY`** - 1 = sparse, 10 = dense.

There is **no universal `8 / 6 / 4` baseline** and no automatic portfolio or marketing preset. Page category alone does not determine these values. A portfolio can be a dense index, a calm case-study sequence, a media stage or another content-led structure. Do not increase motion or variance merely because the task is a redesign.

### 1.A Descriptive Examples, Not Inference Rules
| Already chosen direction | Possible dial description | What still decides |
|---|---|---|
| Calm, compact project index | low motion, moderate density; variance as composed | Scan path and amount of real work |
| Media-led showcase | motion and density depend on playback and navigation | Supplied media, performance and access |
| Experimental spatial composition | higher variance if the layout actually uses it | Readability and responsive behavior |
| Preserve an existing site | describe the current system or omit dials | Approved scope and existing identity |

### 1.B Use-Case Presets
Legacy presets are not required. Use a numeric description only when it helps implement the selected direction, with a brief reason; otherwise omit it. Numeric novelty and changing values between projects are not quality goals.

### 1.C How the Dials Relate to Output
The names above remain available for the technical references below. A threshold is not permission to add an effect, force a split hero, change type family or remove content. If the implementation changes, update its description rather than adding decoration to satisfy the number.

---

## 2. BRIEF → DESIGN SYSTEM MAP

Once you have the design read (Section 0), pick the right foundation; dials (Section 1) are optional descriptions. Do not invent CSS for things that have an official package. Do not pretend an aesthetic trend is an official system.

### 2.A When to reach for a real design system (use official packages)
| Brief reads as… | Reach for | Why |
|---|---|---|
| Microsoft / enterprise SaaS / dashboards | `@fluentui/react-components` or `@fluentui/web-components` | Official Fluent UI, Microsoft tokens, accessibility done |
| Google-ish UI, Material-flavored product | `@material/web` + Material 3 tokens | Official, theme-able via Material Theming |
| IBM-style B2B / enterprise analytics | `@carbon/react` + `@carbon/styles` | Official Carbon, mature data-density patterns |
| Shopify app surfaces | `polaris.js` web components / Polaris React | Required for Shopify admin UI |
| Atlassian / Jira-style product | `@atlaskit/*` + `@atlaskit/tokens` | Official Atlassian DS |
| GitHub-style devtool / community page | `@primer/css` or `@primer/react-brand` | Official Primer; Brand variant for marketing |
| Public-sector UK service | `govuk-frontend` | Legally / regulatorily expected |
| US public-sector / trust-first | `uswds` | Same |
| Fast local-business / agency MVP | Bootstrap 5.3 | Boring, fast, works |
| Modern accessible React foundation | `@radix-ui/themes` | Primitives + polished theme |
| Modern SaaS where you own the components | shadcn/ui (`npx shadcn@latest add ...`) | You own the code, easy to customise; never ship default state |
| Tailwind-based modern SaaS / AI marketing | Tailwind v4 utilities + `dark:` variant | Default for indie + small team builds |

**Honesty rule:** if the brief reads as one of the systems above, install and use the **official** package. Do not recreate its CSS by hand. Do not import a system's tokens but then override 90% of them.

**One system per project.** Do not mix Fluent React with Carbon in the same tree. Do not import shadcn/ui components into a Material 3 app.

### 2.B When the brief is an aesthetic, not a system
For these directions, there is **no single official package**. Build with native CSS + Tailwind + a maintained component library. Be honest in code comments about what is borrowed inspiration vs. official material.

| Aesthetic | Honest implementation |
|---|---|
| Glassmorphism / "frosted glass" | `backdrop-filter`, layered borders, highlight overlays. Provide solid-fill fallback for `prefers-reduced-transparency`. |
| Bento (Apple-style tile grids) | CSS Grid with mixed cell sizes. No single library owns this. |
| Brutalism | Native CSS, monospace, raw borders. No library. |
| Editorial / magazine | Content-led type hierarchy and reading rhythm; serif or sans, grid and spacing follow the publication. No library. |
| Dark tech / hacker | Mono + accent neon, terminal motifs. No library. |
| Aurora / mesh gradients | SVG or layered radial gradients. No library. |
| Kinetic typography | Native CSS animations, scroll-driven animations, GSAP for hijacks. No library. |
| **Apple Liquid Glass** | Apple documents this for Apple platforms only. **There is no official `liquid-glass.css`.** Web implementations are approximations using `backdrop-filter` + layered borders + highlights. Label clearly as approximation. |

---

## 3. PROJECT ARCHITECTURE & CONDITIONAL CONVENTIONS

Read the actual project stack, dependencies and design system before choosing an implementation. No design system does not imply React, Next.js, Tailwind or Motion. Existing native HTML/CSS/JavaScript, Vue, Svelte and other project stacks remain valid; choose tools for the task rather than replacing the project to fit this reference. The React/Next-specific safeguards apply when that stack is used; RSC/client-boundary directives apply to actual RSC boundaries, not ordinary client-only React or native code.

### 3.A Stack
* **Framework:** Preserve the actual project framework. In a Next.js App Router project, use Server Components for suitable server-rendered work and Client Components where interactivity requires them; a new project selects its stack from the task, not this preset.
  * **RSC SAFETY:** Global state works ONLY in Client Components. In Next.js, wrap providers in a `"use client"` component.
  * **INTERACTIVITY ISOLATION:** Any component using Motion, scroll listeners, or pointer physics MUST be an isolated leaf with `'use client'` at the top. Server Components render static layouts only.
* **Styling:** Reuse the project's CSS approach and installed version. Native CSS and an existing design-system solution are valid; Tailwind is an option, not a requirement or an automatic v4 upgrade.
  * For v4: do NOT use `tailwindcss` plugin in `postcss.config.js`. Use `@tailwindcss/postcss` or the Vite plugin.
* **Animation:** Choose suitable native CSS/browser APIs or an existing motion library. If the project uses the Motion React package, its `motion/react` import is a reference; preserve a working installed API rather than requiring a package migration. Missing Motion or GSAP does not cancel the selected motion design.
* **Fonts:** Use the real brand fonts, available glyph coverage and loading/privacy constraints. `next/font` in Next.js or self-hosted `@font-face` with an appropriate display strategy are options; remote loading is a project decision, not a universal prohibition or permission to download fonts.

### 3.B State
* In React, use local `useState` / `useReducer` for suitable discrete UI state; other stacks use their native state model.
* Add shared state only for real cross-component requirements and prefer the existing project solution; Zustand, Jotai or context are examples, not dependencies to install by default.
* Avoid driving high-frequency continuous input through per-frame React tree renders. Use refs, CSS variables, requestAnimationFrame or suitable motion values in the actual stack; Motion's `useMotionValue` / `useTransform` / `useScroll` are options when that library is used. Verify actual performance rather than claiming every state update necessarily fails on mobile.

### 3.C Icons
* Reuse the project's icon family and assets. Phosphor, Hugeicons, Radix, Tabler and Lucide are possible choices when appropriate and available, not a priority list that overrides the project.
* A missing glyph can use suitable SVG primitives or a purpose-made accessible SVG; do not install a second library just to satisfy this reference. Code-native icons, diagrams and illustrations are valid when their roles are clear; do not present a schematic as a real screenshot or data result.
* Keep interface icon weight, scale and optical alignment coherent. Brand marks and content illustrations need not be forced into the control-icon family or one global stroke value.

### 3.D Emoji Policy
Choose symbols for the audience, content and brand. Emojis can suit playful, chat or social-native contexts without a separate per-symbol request; do not use them as an unexplained substitute for critical controls or force icon-library replacements for valid text content.

### 3.E Responsiveness & Layout Mechanics
* Use the project's responsive boundaries and actual content needs; familiar Tailwind breakpoints are examples only when Tailwind is used.
* Choose contained or edge-to-edge layouts from the composition and reading needs; 1400px / `max-w-7xl` are possible bounds, not a universal canvas.
* **Viewport Stability:** For content-led full-height sections, prefer a suitable minimum-height and viewport unit rather than clipping long content to `h-screen`. Choose dynamic/small/large viewport behavior for the actual browser chrome, then test; a deliberate fixed-height canvas is a different task.
* **Grid over fragile sizing:** Prefer Grid for two-dimensional tracks and Flexbox for suitable one-dimensional relationships. Avoid brittle percentage calculations and test wrapping; do not replace a valid layout solely because it uses `calc()` or Flexbox.

### 3.F Dependency Verification (mandatory)
Before importing ANY 3rd-party library, check the actual project dependency manifest. If missing, first consider the native/existing implementation or an appropriate alternative; add a library only when genuinely needed and covered by the task's permissions. **Never** assume a library exists.

---

## 4. DESIGN ENGINEERING DIRECTIVES (Bias Correction)

LLMs default to clichés. Override these defaults proactively. Each rule has a context-aware override path.

### 4.1 Typography
* **Display / Headlines:** Plan scale, tracking, line-height and line breaks around the actual words, typeface and composition; utility examples are starting points, not a required look.
* **Body / Paragraphs:** Use readable contrast, measure and leading for the language and viewport. Preserve the existing DS when applicable.
* **Font choice:** Serif, sans, mono and mixed-family systems are all options when their roles serve the content and selected direction. A portfolio or premium brief does not automatically require sans; an editorial brief does not automatically require serif.
* **Evaluate the actual font:** Check language/glyph coverage, available weights, license, loading cost, brand fit and display/body performance. Inter, Fraunces and Instrument Serif are not blacklisted, nor are Geist and other named alternatives preferred by default. Do not rotate fonts simply to differ from the previous project.
* **Pairings to know (examples only):** `Geist` + `Geist Mono`, `Satoshi` + `JetBrains Mono`, `Cabinet Grotesk` + `Inter Tight`, `GT America` + `IBM Plex Mono`. Verify availability and licensing before use.
* **Emphasis:** Same-family italic/bold and intentional mixed-family emphasis can both work. Choose a repeatable typographic role, rather than inserting a contrasting word solely as decoration.
* **ITALIC DESCENDER CLEARANCE (mandatory):** Inspect display italics with descenders (`y g j p q`) for clipping at the actual font and size. Provide sufficient line-height and wrapper clearance; `leading-[1.1]` plus `pb-1` is one possible fix, not a universal metric. Audit rendered headlines before shipping.

### 4.2 Color Calibration
* Build a coherent palette with explicit roles for surfaces, text, actions, emphasis and semantic states. One accent can be appropriate; multiple accents, saturated colors, neutral palettes and monochrome are also valid when the direction calls for them. No universal accent-count or saturation cap applies.
* **Purple / blue / glow:** Assess these like any other brand choice. Avoid arbitrary effects; preserve brand colors and approved references.
* **Color consistency:** Apply equivalent roles consistently across components. Different accents for different roles or section color blocks may be intentional; do not recolor success/error states to force one accent everywhere.
* **Premium-consumer palette review:** Warm paper, brass, clay, oxblood and espresso are options, not a banned family or a default. Cool neutrals, forest, cobalt, terracotta, olive, black/white and multi-color systems are options too. Choose from the product, imagery, audience and identity; do not force palette rotation between unrelated projects.
* Verify text, controls and focus contrast against each actual background, including photographic or inverted sections. Color must not be the sole carrier of meaning.

### 4.3 Layout Diversification
* Choose the composition from the content hierarchy and intended reading path. Centered, split, asymmetric, full-bleed, index/list and other structures are available; `DESIGN_VARIANCE > 4` does not forbid centering or force a split screen.
* Check the selected composition on mobile and with the actual headline, assets and navigation. Distinctiveness must come from content and composition, not a prescribed alignment.

### 4.4 Materiality, Shadows, Cards
* Use cards when grouping, interaction, hierarchy or the chosen material/spatial composition benefits from a surface. Lists, dividers and negative space are alternatives, not required replacements for flat or elevated cards.
* When a shadow is used, choose its hue, opacity and spread for the intended material and surface; black or tinted shadows are options, not mandatory treatments.
* For dense layouts, evaluate grouping, scanning and space cost with the actual content. A density number does not ban cards or require a bare metric layout.
* **Shape roles:** Use repeatable geometry for equivalent components. Mixed radii, angular panels and round controls can coexist when their roles and material language are coherent; they are not inherently broken. Reuse existing tokens where present instead of requiring a new shape specification.

### 4.5 Interactive UI States
LLMs default to "static successful state only." Always implement full cycles:
* **Loading, when present:** Choose a progress, skeleton or other honest pending-state treatment for the actual task and duration; do not fabricate a loading state for static content.
* **Empty States:** Beautifully composed; indicate how to populate.
* **Error States:** Clear, inline (forms), or contextual (toasts only for transient).
* **Tactile Feedback:** Make activation perceivable with feedback suited to the control and selected material. Translation or scale is one option; preserve keyboard, touch and reduced-motion behavior.
* **BUTTON CONTRAST CHECK (mandatory, a11y):** Before shipping any button, verify the button text is readable against the button background. White button + white text, `bg-white` CTA with `text-white` label, transparent button against the page background with no border → all banned. Audit every CTA: contrast ratio WCAG AA min (4.5:1 for body, 3:1 for large text 18px+). Same rule applies to ghost buttons over photographic backgrounds (use a backdrop, scrim, or stroke).
* **CTA label fit:** Keep action labels clear, readable and operable across widths and languages. Fix accidental clipping, awkward wrapping and undersized targets; a deliberate multiline control is valid. Do not truncate necessary meaning to meet a word-count or single-line quota.
* **CTA intent clarity:** Equivalent actions should have understandable, consistent names. Repeating an action at useful points in a long page is valid; contextual labels may differ when their destination and consequence remain clear. Remove competing or misleading duplication, not useful access paths.
* **FORM CONTRAST CHECK (mandatory, a11y):** Form inputs, placeholder text, focus rings, helper text, and error text all pass WCAG AA contrast against the section background. Light placeholders on a near-white form, white form on white page section, form labels grayer than 4.5:1 contrast → all banned. Audit every form before shipping.

### 4.6 Data & Form Patterns
* Label ABOVE input. Helper text optional but present in markup. Error text BELOW input. Standard `gap-2` for input blocks.
* No placeholder-as-label. Ever.

### 4.7 Layout Discipline (Content and Responsive Review)

* **Hero reading path:** Make the opening purpose, key work or primary action discoverable. A compact hero can fit the viewport; a long opening, immersive media stage or project index may intentionally continue below it. Do not clip content or hide essential controls to meet a viewport quota.
* **Hero scale and spacing:** Plan the actual headline, image, navigation and viewport together. Check wrapping, clearance and hierarchy at desktop and mobile. There is no universal headline-line, word-count, `pt-24` or four-element limit; preserve necessary content and remove actual clutter.
* **Hero content:** Eyebrows, summaries, proof, pricing context, project links and CTAs belong where they help the task. They do not all need to be present or moved below the hero by rule. Choose clear priority over a fixed stack or primary/secondary CTA quota.
* **Navigation:** Keep labels readable and controls reachable. Choose wrapping, collapsing or another intentional layout for the actual items; avoid accidental overlap, clipping and excessive obstruction. No universal height cap defines quality.
* **Grid content:** Use as many cells as real content needs. Do not insert empty filler tiles. Text-led grids can remain text-led; images, tint and patterns require a communicative role rather than a cell-color quota.
* **Section rhythm:** Repeated structures can make comparable projects, steps or products easier to scan. Vary the layout where the content hierarchy changes; do not impose a different-family-per-section rule, a zigzag cap or a minimum number of layout families.
* **Eyebrows and split headers:** Use labels when they add useful context, with no mechanical one-per-three quota. Headline and explanation may stack or share columns when their alignment, width and reading order work. Remove redundant labels or floating filler, rather than banning a header pattern.
* **Mobile behavior must be explicit per section.** For every multi-column layout, define and verify its small-screen reading order, sizing and fallback. No "it'll work, Tailwind handles it" assumptions.

### 4.8 Image & Visual Asset Strategy

Asset strategy follows the selected direction. Text-only and typography-led pages can be complete; fabricated product screenshots must not stand in for real product evidence.

**Priority order for visual assets:**
1. **Use the brief's assets first.** Preserve supplied photography, references and brand assets. Generate a new raster asset when the chosen design actually needs one and the task permits generation; tool availability alone does not require it. Use the right aspect ratio and do not replace an existing reference just to run generation.
2. **Existing or sourced images when needed.** If the selected medium needs photography or another raster asset, inspect suitable supplied, generated or permitted external material. Verify subject relevance, availability and licensing as appropriate; a placeholder URL is not proof of any of these.
3. **Native visual work or an honest gap.** Use CSS, SVG, canvas or actual component previews when they are the right medium for the chosen direction; they are not forbidden substitutes by origin. When an essential photographic/product asset is unavailable, identify the missing asset or a clearly labeled placeholder rather than presenting a fabricated screenshot or unrelated stock image as evidence.

**Image count follows the design.** Typography-led, text-only and no-asset directions can be complete. Use images where they communicate product, place or narrative; do not impose a minimum count or generate assets for a small existing-page fix.

**Real company logos for social proof.** When the brief calls for a "Trusted by / Used by / Customers" logo wall, do NOT default to plain text wordmarks (`<span>Acme Co</span>` styled in a row). Use real SVG logos:
* **Source: Simple Icons** (`https://cdn.simpleicons.org/{slug}/ffffff` for any color, or `simple-icons` npm package). Covers most known brands.
* **Alternative: devicon** for tech-stack logos (`@svgr/cli` or CDN).
* **Make-up the brand name? Then make-up an SVG mark too.** Generate a simple monogram (one letter in a circle, two-letter ligature, abstract glyph) rendered as an inline `<svg>` matching the page style. Plain text wordmarks for invented brand names look generic.
* Ensure logos render against every supported theme/background (white-on-dark, black-on-light, or a suitable theme variable).
* **Logo context:** Use genuine, legible marks when available. Add brand names, categories or relationship context when they help the audience interpret the row; omit redundant labels. A logo alone does not establish a customer relationship.

**Code-native illustrations and marks:** Use SVG/CSS/canvas when appropriate to the visual and technical requirements, and raster generation when a bitmap is appropriate. Inspect the actual result at target sizes, preserve brand assets and distinguish a new illustrative mark from a real company/customer logo. Tool availability does not decide the medium.

**Product previews:** Prefer actual screenshots or functional component previews for product evidence. Generated or code-built illustrative mockups are valid only when clearly identified and not presented as an actual product capture, working capability or customer proof. A native UI/diagram/illustration is not a fake screenshot merely because it uses HTML.

**Hero assets follow the chosen direction.** Use a real visual when it carries the story; an intentional typography-led hero can work without imagery.

### 4.9 Content Density

Choose density from the audience's task, real content and selected reading path. Support both first-impression scanning and the depth users need; no universal headline-word, paragraph-word, row-count or item-count quota applies.

* **Sections:** Give each section clear priority and readable grouping. Short headlines and summaries can help, but do not delete essential explanation, specifications or work merely to hit a number.
* **Lists and specifications:** A plain list or table can be the most usable presentation. For lengthy content, consider grouping, filtering, disclosure, a separate page, cards or a track only when that improves comparison and access. Do not automatically replace more than five items with a carousel, marquee or card grid.
* **Dividers:** Use borders and spacing to clarify rows and groups at the actual density. Repeated hairlines are valid for comparable data; remove redundant strokes or visual noise rather than banning the pattern.

* **COPY SELF-AUDIT (mandatory before ship):** Before declaring any task done, re-read every visible string on the page (headlines, subheads, eyebrows, button labels, body copy, captions, alt text, footer text, error messages). Flag any string that is:
  - **Grammatically broken** ("free on its past", "two plans but one is honest", "to put it on the table" out of context)
  - **Has unclear referents** ("we plan to stay that way" without prior context)
  - **Sounds like AI hallucination** (cute-but-wrong wordplay, forced metaphors that don't track, "elegant nothing" phrases)
  - **Reads like an LLM trying to sound thoughtful** (passive-aggressive humility, fake-craftsman labels, mock-poetic micro-meta)
  Rewrite every flagged string. If unsure whether a string makes sense, replace it with a plain functional sentence. AI-generated cute copy is worse than boring copy.
* **Fake-precise numbers are flagged.** Numbers like `92%`, `4.1×`, `48k`, `5.8 mm`, `13.4 lb` either:
  - Come from real data (brief, brand guidelines, public metrics) - fine
  - Are explicitly labeled as mock (`<!-- mock -->`, "example", "sample data") - fine
  - Are AI-invented spec aesthetics - banned. Don't fake engineering precision the brand doesn't claim.
* **One copy register per page.** Don't mix technical mono ("47 tasks · 0.6 ctx-switches/day"), editorial prose, and marketing punch in the same composition unless the brand voice explicitly calls for it.

### 4.10 Quotes & Testimonials

* Show quotations at a readable length for their purpose and viewport. Use a clearly indicated excerpt when appropriate; preserve the source's meaning and provide access to necessary context. Do not silently cut real quotes to a three-line quota.
* Preserve genuine wording and attribution, including names and punctuation. Do not invent a person's role or company to fill a template.
* Use typographic quotation marks appropriate to the language and existing editorial system; punctuation is not a visual failure by character count.

### 4.11 Page Theme Coherence

Choose light, dark, automatic or another intentional theme strategy from the brand, content and project requirements. Inverted sections and color-block sequences can be part of a coherent page; neither a universal no-inversion rule nor a once-per-page quota applies.

* Give each background treatment a clear compositional or semantic role and maintain readable transitions.
* Use shared semantic tokens where practical. When a section has a different surface, resolve text, controls, focus and logos against that surface.
* Preserve the existing DS theme architecture unless the task authorizes changing it. Avoid accidental local overrides, but allow purposeful section themes supported by that system.

---

## 5. CONTEXT-AWARE PROACTIVITY

These are tools, not defaults. Use them when the design read calls for them. **None of these fire automatically.**

* **Liquid Glass / Glassmorphism:** Appropriate for premium consumer, Apple-adjacent, luxury brand, or media-overlay vibes. Inappropriate for dashboards, public-sector, or "boring B2B." When used, go beyond `backdrop-blur`: add a 1px inner border (`border-white/10`) and a subtle inner shadow (`shadow-[inset_0_1px_0_rgba(255,255,255,0.1)]`) for physical edge refraction. Provide a solid-fill fallback under `prefers-reduced-transparency`.
* **Magnetic Micro-physics:** Consider when pointer attraction serves the chosen interaction, independent of a dial threshold or page category. In the React/Motion stack, use `useMotionValue` / `useTransform` outside the render cycle rather than continuous `useState`. Other stacks use their appropriate native mechanism. See Section 3.B.
* **Perpetual Micro-Interactions** (Pulse, Typewriter, Float, Shimmer, Carousel): Consider when ongoing motion communicates state, rhythm or atmosphere in the chosen direction. Informational content may remain still; loops are not a quota. Choose spring, linear or another timing model for the actual behavior, with readable content, interruption and reduced-motion alternatives.
* **"Motion claimed, motion shown."** Describe the motion actually implemented. A dial value does not require hero entry, scroll reveals or hover physics. If the direction works better static, keep it static and update or omit the dial. Never half-build motion that breaks (cut-off ScrollTriggers, jumpy enters, missing cleanups).
* **Motion purpose:** Connect motion to hierarchy, storytelling, feedback, state continuity, material behavior or the intended atmosphere/identity. Experiential expression can be a legitimate purpose; not every effect needs a conversion claim. Choose from the concept and actual interaction, then check pacing, readability and interruption in the browser. Tool availability alone is not a reason to add motion.
* **Marquee pacing:** Evaluate the combined attention, repetition and legibility of moving tracks. Multiple tracks can form one intentional composition; reduce competing or redundant motion based on actual browser experience, not a universal one-per-page count. Preserve required pause and reduced-motion behavior.
* **GSAP Sticky-Stack Pattern (when scroll-stack is used).** A "card stack on scroll" must be a REAL sticky-stack, not a sequential reveal list. See Section 5.A below for the canonical code skeleton. Common failure: trigger fires halfway through scroll instead of pinning at viewport top. Fix: `start: "top top"` not `start: "top center"` or `"top 80%"`.
* **GSAP Horizontal-Pan Pattern (when horizontal scroll-hijack is used).** See Section 5.B below for the canonical skeleton. Common failure: animation starts before the section is pinned, so the user sees half a slide. Same fix: `start: "top top"`, pin the wrapper, scrub the inner track.

### 5.A Sticky-Stack - Canonical Skeleton

```tsx
"use client";
import { useRef, useEffect, useId, type ReactNode } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useReducedMotion } from "motion/react";

gsap.registerPlugin(ScrollTrigger);

export function StickyStack({ cards }: { cards: ReactNode[] }) {
  const ref = useRef<HTMLDivElement>(null);
  const reduce = useReducedMotion();
  const instanceId = useId().replace(/:/g, "");
  const cardClass = `stack-card-${instanceId}`;
  const innerClass = `stack-card-inner-${instanceId}`;

  useEffect(() => {
    if (reduce || !ref.current || cards.length <= 1) return;
    const ctx = gsap.context(() => {
      const cardEls = gsap.utils.toArray<HTMLElement>(`.${cardClass}`);
      cardEls.forEach((card, i) => {
        if (i === cardEls.length - 1) return;
        ScrollTrigger.create({
          trigger: card,
          start: "top top",                              // pin at viewport top
          endTrigger: cardEls[cardEls.length - 1],
          end: "top top",
          pin: true,
          pinSpacing: false,
          anticipatePin: 1,
          invalidateOnRefresh: true,
        });
        const inner = card.querySelector(`.${innerClass}`);
        if (!inner) return;
        gsap.to(inner, {
          scale: 0.92,
          opacity: 0.55,
          ease: "none",
          scrollTrigger: {
            trigger: cardEls[i + 1],
            start: "top bottom",
            end: "top top",
            scrub: true,
            invalidateOnRefresh: true,
          },
        });
      });
    }, ref);
    return () => ctx.revert();
  }, [reduce, cards.length, cardClass, innerClass]);

  return (
    <div ref={ref} className="relative">
      {cards.map((card, i) => (
        <div
          key={i}
          style={{ zIndex: i + 1 }}
          className={`${cardClass} relative min-h-[100dvh] flex items-center justify-center`}
        >
          <div className={`${innerClass} w-full flex items-center justify-center`}>
            {card}
          </div>
        </div>
      ))}
    </div>
  );
}
```

Critical points: `start: "top top"`, `pin: true`, every card except the last is pinned, the scale/opacity transform is driven by the NEXT card's scroll trigger (so previous card shrinks as next one arrives). Never combine CSS `position: sticky` with `pin: true` on the same element: the native sticky engine and ScrollTrigger's `position: fixed` fight at the hand-off (judder, snapping, coordinate drift). The pinned element must also not be the element being transformed - pin the outer card and animate an inner wrapper, or the scale tween throws off the pin measurements. Scope the card class per instance (`useId`) so two stacks on one page do not cross-select; stack with ascending `zIndex`. Under `prefers-reduced-motion` the component renders a plain list: no pin, no transforms, all content reachable.

### 5.B Horizontal-Pan - Canonical Skeleton

```tsx
"use client";
import { useRef, useEffect, type ReactNode } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useReducedMotion } from "motion/react";

gsap.registerPlugin(ScrollTrigger);

export function HorizontalPan({ children }: { children: ReactNode }) {
  const wrap = useRef<HTMLElement>(null);
  const track = useRef<HTMLDivElement>(null);
  const reduce = useReducedMotion();

  useEffect(() => {
    if (reduce || !wrap.current || !track.current) return;
    const ctx = gsap.context(() => {
      const getDistance = () =>
        Math.max(0, track.current!.scrollWidth - wrap.current!.clientWidth);
      gsap.to(track.current, {
        x: () => -getDistance(),
        ease: "none",
        scrollTrigger: {
          trigger: wrap.current,
          start: "top top",                              // pin starts when section top hits viewport top
          end: () => `+=${getDistance()}`,               // scroll distance = track width minus viewport, recomputed on refresh
          pin: true,
          scrub: 1,
          anticipatePin: 1,
          invalidateOnRefresh: true,
        },
      });
    }, wrap);
    return () => ctx.revert();
  }, [reduce]);

  return (
    <section
      ref={wrap}
      role="region"
      aria-label="Horizontal content track"
      tabIndex={reduce ? 0 : undefined}
      className={`relative w-full ${reduce ? "overflow-x-auto snap-x snap-mandatory" : "overflow-hidden"}`}
    >
      <div
        ref={track}
        className="flex h-[100dvh] w-max items-center"
      >
        {children}
      </div>
    </section>
  );
}
```

Critical points: `start: "top top"`, `pin: true`, `end: "+=${getDistance()}"` (scroll length = horizontal travel needed), `scrub: 1`. The wrapper is pinned, the inner track slides horizontally as the user scrolls vertically. `x` and `end` must be function-based and paired with `invalidateOnRefresh: true`; a `distance` captured once never recomputes - after a resize it overshoots into blank space (or pans to nothing when the track fits). Keep `w-max` on the track and make each panel non-shrinking (`shrink-0` or an explicit width): without it, overflow compression collapses `scrollWidth` and the section pins without panning. Under `prefers-reduced-motion` keep every panel reachable: swap the wrapper to focusable `overflow-x-auto` instead of leaving `overflow-hidden`. Put `snap-x snap-mandatory` on that scrolling wrapper and `snap-start` on each panel; keep scrolling immediate rather than smooth.

### 5.C Scroll-Reveal Stagger - Canonical Skeleton (lighter alternative)

For simple "items appear as they enter viewport" (no pinning), prefer Motion's `whileInView` over GSAP - lighter, no ScrollTrigger needed:

```tsx
"use client";
import { motion, useReducedMotion } from "motion/react";

export function RevealStagger({ items }: { items: string[] }) {
  const reduce = useReducedMotion();
  return (
    <ul className="grid gap-6">
      {items.map((item, i) => (
        <motion.li
          key={item}
          initial={reduce ? false : { opacity: 0, y: 24 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.3 }}
          transition={{
            duration: 0.6,
            delay: i * 0.06,
            ease: [0.16, 1, 0.3, 1],
          }}
        >
          {item}
        </motion.li>
      ))}
    </ul>
  );
}
```

Use this for: feature lists, testimonial grids, logo walls, anything that just needs "enter on scroll." Save GSAP for actual pin/scrub work.

### 5.D Animation Implementation Guards

* **Scroll work:** A native scroll listener is an available tool, not inherently forbidden. Keep high-rate handlers cheap, avoid repeated layout read/write work, throttle when a lower sampling rate is appropriate, and clean up owned listeners. requestAnimationFrame can organize paint work but does not itself reduce scroll-event frequency. Choose IntersectionObserver, CSS scroll-driven animation, existing Motion/ScrollTrigger or a bounded native implementation for the actual behavior.
* **Continuous React input:** Avoid updating a broad React tree for every scroll/pointer sample. Use refs, CSS variables, a suitable native schedule or existing motion values; discrete semantic state updates remain valid. Verify actual cost instead of banning all use of `window.scrollY` or requestAnimationFrame.
* **Layout Transitions:** When using Motion, `layout` and `layoutId` can express reordering, expansion and shared elements. Other stacks may use suitable native layout/transition techniques. Do not wrap static content in measured layout machinery "for safety".
* **Staggered Orchestration:** Use a sequence only where its order serves the content; Motion's `staggerChildren` or a CSS cascade are options. When using Motion variants, keep parent and children in the required client tree; this is not a requirement to install Motion or animate every child.

Native event work and animation costs are evaluated in context; see [MDN scroll-event guidance](https://developer.mozilla.org/en-US/docs/Web/API/Document/scroll_event) and [animation performance](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Animation_performance_and_frame_rate). These support cost-aware implementation, not an extra aesthetic preset.

---

## 6. PERFORMANCE & ACCESSIBILITY GUARDRAILS

### 6.A Hardware Acceleration
* Prefer `transform` and `opacity` for frequent spatial motion. Layout interpolation, SVG, clipping, filters or other properties can serve a real behavior; bound their work and verify performance rather than globally banning the capability. Avoid unnecessary layout/paint work and preserve usable interruption/end states.
* Use `will-change: transform` sparingly - only on elements that will actually animate.

### 6.B Reduced Motion (mandatory)
* **Respect `prefers-reduced-motion` for non-essential movement regardless of the intensity dial.** Do not use a numeric threshold to skip the preference. Keep the information and main actions available in the reduced/instant alternative.
* When using Motion, `useReducedMotion()` is one way to provide the alternative; native implementations respect the same preference without requiring the library.
* In CSS: gate animations behind `@media (prefers-reduced-motion: no-preference)` or provide an override block under `@media (prefers-reduced-motion: reduce)` that disables.
* Infinite loops, parallax, scroll-hijack, and magnetic physics MUST collapse to static / instant under reduced motion.

### 6.C Theme Accessibility
* Support the modes required by the brief or existing project. A coherent light-only or dark-only page is valid; dual-mode is not mandatory merely because the page is consumer-facing.
* When multiple modes are supported, use the project's Tailwind `dark:` variant or semantic token strategy consistently. Maintain visual hierarchy, brand identity and WCAG AA contrast in each supported mode.
* Test every implemented mode and deliberate section inversion; adding an unused second theme is not an accessibility check.

### 6.D Core Web Vitals Targets
* **LCP** < 2.5s is a performance target. Identify the actual LCP element and use the project's image/loading facilities appropriately; do not assume a hero image, Next.js or unconditional preloading.
* **INP** < 200ms. Heavy work off main thread.
* **CLS** < 0.1. Reserve space for images, fonts, embeds.
* Use available performance measurements appropriate to the delivery environment. Lighthouse can help when available; distinguish lab results from field performance and report checks that were not run.

### 6.E DOM Cost
* Scope texture to the intended material using a prepared asset or bounded decorative layer that does not block input. Fixed placement is not a performance guarantee; local or scrolling texture is available when its actual paint cost and readability are acceptable. Do not force a global overlay or an arbitrary z-index.
* Consider bundle and startup cost before adding a library. Defer genuinely non-critical work when useful; viewport position alone does not determine loading priority or justify installing Motion/Three.js.

### 6.F Z-Index Restraint
Use intentional stacking contexts for navigation, overlays and compositional depth. Reuse the project's layer conventions; add tokens where useful without requiring a new constants file for a small page.

---

## 7. DIAL DEFINITIONS (Technical Reference)

The following are illustrative implementation vocabulary for an already chosen direction, not required recipes or mappings from page category. Do not add these features merely to meet a dial level.

### DESIGN_VARIANCE (Level 1-10)
* **1-3 (Predictable):** Symmetrical CSS Grid (12-col, equal fr-units), equal paddings, centered alignment.
* **4-7 (Offset):** `margin-top: -2rem` overlaps, varied image aspect ratios (4:3 next to 16:9), left-aligned headers over center-aligned data.
* **8-10 (Asymmetric):** Masonry layouts, CSS Grid with fractional units (`grid-template-columns: 2fr 1fr 1fr`), massive empty zones (`padding-left: 20vw`).
* **Mobile adaptation:** Verify content order, readable sizes, targets and reachable controls on narrow screens. Single-column, compact multi-column, a deliberate horizontal track or another responsive composition may fit; a variance number does not force one layout or spacing recipe.

### MOTION_INTENSITY (Level 1-10)
* **1-3 (Low motion):** Mostly still, with limited transitions if the direction uses them. This label describes behavior; it does not substitute reduced-motion mode for the normal experience.
* **4-7 (Fluid CSS):** `transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1)` (name the properties; never `transition: all`, which also animates layout properties off the GPU, see 6.A). `animation-delay` cascades for load-ins.
* **8-10 (Advanced Choreography):** Complex reveals, parallax or continuous choreography may use suitable native facilities or existing libraries. A bounded scroll listener is valid when appropriate; follow Section 5.D for cost, cleanup and interruption. The dial does not require Motion hooks, GSAP or every effect listed here.

### VISUAL_DENSITY (Level 1-10)
* **1-3 (Art Gallery):** Lots of white space. Huge section gaps (`py-32` to `py-48`). Expensive, clean.
* **4-7 (Daily App):** Standard web app spacing (`py-16` to `py-24`).
* **8-10 (Dense):** More information in the available space. Grouping surfaces, dividers, numeric type and tabular figures follow scanning/comparison needs and the chosen system; density does not require bare rows or monospace for every number.

---

## 8. THEME PROTOCOL

Select the supported theme mode(s) from the brand, chosen direction and actual project requirements. Light-only, dark-only and dual-mode are all valid; no print/editorial exception is needed to choose one mode.

### 8.A Token Strategy
Use the existing project's strategy. When building theme switching, either pair Tailwind color utilities with `dark:` variants or swap semantic CSS variables under the appropriate theme selector. Do not add switching solely to satisfy this guide.

### 8.B Color and Accessibility
* **Contrast** - WCAG AA minimum for text and controls, with suitable focus visibility on the actual backgrounds.
* **Hierarchy parity** - preserve useful hierarchy in each implemented mode.
* **Brand fidelity** - preserve recognizable brand expression.
* **Black and white** - pure `#000000`, pure `#ffffff`, off-black and off-white are all available. Choose for the intended contrast, imagery and material effect; pure values are not banned.

### 8.C Mode Behavior
Respect the chosen project behavior. When automatic mode is implemented, honor `prefers-color-scheme`; when a manual toggle is required, make it operable and preserve the user's selection.

### 8.D Test Implemented Modes
Inspect every supported mode and section background. Report any missing browser evidence; do not claim an unimplemented second theme was tested.

---

## 9. TEMPLATE-DEFAULT REVIEW (Contextual Patterns)

Review familiar devices against the chosen concept, content and actual browser experience. Their presence is not itself a failure, and the user need not explicitly name a technique before it can be designed. Do not replace one stereotyped template with a universal ban list.

### 9.A Visual Expression and Type
* Glows, gradients, large type, custom pointer treatments, crosshairs, grain and vertical text can be intentional. Check their compositional/material role, clarity, input alternatives and performance rather than replacing them with restrained inner borders or smaller type by default.
* Use language-appropriate font coverage and readable roles. Preserve approved brand fonts and intentional scale; no font blacklist or cross-project rotation applies.
* Decorations may establish atmosphere, rhythm or identity as well as organize content. Remove effects that compete with the task or remain visibly unfinished, not all non-functional expression.

### 9.B Labels, Navigation and Metadata
* Section numbers, image pagination, captions, overlaid tags, separator dots, progress tracks and scroll cues are available when they clarify structure, progress, content or intended exploration. Evaluate redundancy, occlusion, contrast and mobile behavior; no universal count or placement ban applies.
* Status dots, version labels, stock counters, location/time and technical metadata must be truthful when they claim real state. Real launch/version information and a genuine address may remain. Do not invent live data, availability or build status for decoration.
* Avoid adding pseudo-technical metadata to make a page appear designed. Preserve existing meaningful metadata and useful action paths.

### 9.C Content and Evidence
* Preserve real names, dates, metrics, prices, testimonials, addresses and contact details. Sample/prototype content must be identified; neither realistic names nor generated photography establish actual customers or endorsements.
* Review generated marketing clichés, poetic labels and clever copy for specificity and meaning in context. Do not mechanically erase an author's actual voice or a genuine editorial section name.
* Product evidence must come from the actual product. A functional component demo or explicitly labeled illustrative mockup is valid; do not present generated or div-built fictional UI as a real screenshot or a working capability.
* Use actual available assets or clearly identified placeholders. A seeded photo URL does not guarantee subject relevance or production availability; inspect chosen assets and report necessary missing media.

### 9.D Punctuation and Editorial Rhythm
Use punctuation appropriate to the language, actual wording and existing editorial system. Em dashes, en dashes, hyphens, quotation marks and middle dots are not automatic style failures. Remove repetitive or confusing punctuation; preserve genuine quotations, names and ranges rather than rewriting them to meet a zero-character quota.

### 9.E Implementation Fit
Reuse the project's established icon family and design-system components. Native SVG/vector work, library glyphs and generated raster assets serve different needs; choose the appropriate medium without inventing tool or dependency availability. The scope rules in the single entry take precedence over legacy stack-specific defaults.

## 10. REFERENCE VOCABULARY (Pattern Names the Agent Should Know)

This is a vocabulary, not a library. The agent should KNOW these pattern names to communicate about them, design with them in mind, and reach for them when the design read calls for them. **Implementations and code sketches live in the Block Library (Section 12), which is populated iteratively.**

### Hero Paradigms
* **Asymmetric Split Hero** - Text on one side, asset on the other, generous white space.
* **Editorial Manifesto Hero** - Large type, no asset, almost-poster.
* **Video / Media Mask Hero** - Type cut out as mask over video background.
* **Kinetic-Type Hero** - Animated typography as the primary visual.
* **Curtain-Reveal Hero** - Hero parts on scroll like a curtain.
* **Scroll-Pinned Hero** - Hero stays pinned while content scrolls behind.

### Navigation & Menus
* **Mac OS Dock Magnification** - Edge nav, icons scale fluidly on hover.
* **Magnetic Button** - Pulls toward cursor.
* **Gooey Menu** - Sub-items detach like viscous liquid.
* **Dynamic Island** - Morphing pill for status / alerts.
* **Contextual Radial Menu** - Circular menu expanding at click point.
* **Floating Speed Dial** - FAB springing into curved secondary actions.
* **Mega Menu Reveal** - Full-screen dropdown, stagger-fade content.

### Layout & Grids
* **Bento Grid** - Asymmetric tile grouping (Apple Control Center).
* **Masonry Layout** - Staggered grid, no fixed row height.
* **Chroma Grid** - Borders / tiles with subtle animating gradients.
* **Split-Screen Scroll** - Two halves sliding in opposite directions.
* **Sticky-Stack Sections** - Sections that pin and stack on scroll.

### Cards & Containers
* **Parallax Tilt Card** - 3D tilt tracking mouse coordinates.
* **Spotlight Border Card** - Borders illuminate under cursor.
* **Glassmorphism Panel** - Frosted glass with inner refraction.
* **Holographic Foil Card** - Iridescent rainbow shift on hover.
* **Tinder Swipe Stack** - Physical card stack, swipe-away.
* **Morphing Modal** - Button expands into its own dialog.

### Scroll Animations
* **Sticky Scroll Stack** - Cards stick and physically stack.
* **Horizontal Scroll Hijack** - Vertical scroll → horizontal pan.
* **Locomotive / Sequence Scroll** - Video / 3D sequence tied to scrollbar.
* **Zoom Parallax** - Central background image zooming on scroll.
* **Scroll Progress Path** - SVG line drawing along scroll.
* **Liquid Swipe Transition** - Page transition like viscous liquid.

### Galleries & Media
* **Dome Gallery** - 3D panoramic gallery.
* **Coverflow Carousel** - 3D carousel with angled edges.
* **Drag-to-Pan Grid** - Boundless draggable canvas.
* **Accordion Image Slider** - Narrow strips expanding on hover.
* **Hover Image Trail** - Mouse leaves popping image trail.
* **Glitch Effect Image** - RGB-channel shift on hover.

### Typography & Text
* **Kinetic Marquee** - Endless text bands reversing on scroll.
* **Text Mask Reveal** - Massive type as transparent window to video.
* **Text Scramble Effect** - Matrix-style decoding on load / hover.
* **Circular Text Path** - Text curving along spinning circle.
* **Gradient Stroke Animation** - Outlined text with running gradient.
* **Kinetic Typography Grid** - Letters dodging the cursor.

### Micro-Interactions & Effects
* **Particle Explosion Button** - CTA shatters into particles on success.
* **Liquid Pull-to-Refresh** - Reload indicator like detaching droplets.
* **Skeleton Shimmer** - Shifting light reflection across placeholders.
* **Directional Hover-Aware Button** - Fill enters from cursor's exact side.
* **Ripple Click Effect** - Wave from click coordinates.
* **Animated SVG Line Drawing** - Vectors drawing themselves in real time.
* **Mesh Gradient Background** - Organic lava-lamp blobs.
* **Lens Blur Depth** - Background UI blurred to focus foreground action.

### Animation Library Choice
* **Native CSS / Web Animations / project facilities** - choose for the actual behavior and existing stack. Motion (`motion/react`) is an option for suitable UI/state-change motion when available or justified, not a mandatory default.
* **GSAP + ScrollTrigger** - an option for complex scroll choreography when justified. When used in React, isolate owned effects and clean them up with the component lifecycle; native/other stacks use their corresponding teardown.
* **Three.js / WebGL** - options when the chosen concept needs real 3D/canvas rendering. Keep rendering ownership isolated and clean up owned resources; a layered or tactile interface does not inherently require them.
* Multiple animation libraries may coexist when separate elements/properties have clear ownership and lifecycle cleanup. Do not let GSAP, Three.js and Motion compete to write the same transform or frame state; use only the dependencies actually needed.

---

## 11. REDESIGN PROTOCOL

This skill handles **greenfield builds AND redesigns**. Misclassifying the mode is the single biggest source of bad redesign output.

### 11.A Detect the Mode (first action)
* **Greenfield** - no existing site, or full overhaul approved. Form the visual direction through the single entry; Section 1 dials may describe it afterward, with no baseline.
* **Redesign - Preserve** - modernise without breaking the brand. Audit first, extract brand tokens, evolve gradually.
* **Redesign - Overhaul** - form a new visual direction within the user-authorized scope. Preserve real content and required access paths; IA may change when full restructuring is authorized, while routes, tracking and legal changes follow the explicit preservation rules below.

If ambiguous, ask **once**: *"Should this redesign preserve the existing brand, or are we starting visually from scratch?"*

### 11.B Audit Before Touching
Document the current state before proposing changes:
* **Brand tokens** - primary / accent colors, type stack, logo treatment, radii.
* **Information architecture** - page tree, primary nav, key conversion paths.
* **Content blocks** - what exists, what's doing work, what's filler.
* **Patterns to preserve** - signature interactions, recognisable hero, copy voice.
* **Patterns to retire** - AI-slop tells, broken layouts, dead links, generic stock imagery, perf traps.
* **Dial reading of the existing site** - infer current `DESIGN_VARIANCE` / `MOTION_INTENSITY` / `VISUAL_DENSITY`. That's your starting point, not the baseline.
* **SEO baseline** - current ranking pages, meta titles, structured data, OG cards. **SEO migration is the #1 redesign risk.**

### 11.C Preservation Rules
* **Do not change information architecture** unless asked. Keep page slugs, anchor IDs, primary nav labels stable for SEO and muscle memory.
* **Extract brand colors before applying Section 4.2.** A brand that is already purple stays purple - apply the LILA RULE's override.
* **Preserve copy voice** unless asked for a rewrite. Visual modernisation ≠ content rewrite.
* **Honor existing accessibility wins.** Do not regress focus states, alt text, keyboard nav, contrast.
* **Respect existing analytics events.** Do not rename buttons, form fields, section IDs that downstream tracking depends on.

### 11.D Modernisation Levers (for targeted preservation work)
For preserve/targeted work, choose the smallest lever that fixes the observed issue and stop when the brief is satisfied. These are not a required sequence for an authorized overhaul:
1. **Typography refresh** - biggest visual lift per unit of risk.
2. **Spacing & rhythm** - increase section padding, fix vertical rhythm.
3. **Color recalibration** - resolve inconsistent color roles and contrast while preserving intentional brand hues and saturation.
4. **Motion layer** - add `MOTION_INTENSITY`-appropriate micro-interactions to existing components.
5. **Hero & key-section recomposition** - restructure top-of-funnel using Section 10 vocabulary.
6. **Full block replacement** - only when the existing block is unsalvageable.

### 11.E Decision Tree: Targeted Evolution vs Full Redesign
* If the user requests preservation and IA/content are sound, **targeted evolution** may fit (Levers 1-4). Existing IA quality does not cancel an explicit request for a new direction or complete reconstruction.
* Visual debt is structural (broken IA, no design system, broken mobile) → **full redesign** with strict content preservation.
* Brand itself is changing → **greenfield**.

### 11.F What Never Changes Silently
Never modify without explicit user approval:
* URL structure / route slugs.
* Primary nav labels.
* Form field names or order (breaks analytics + autofill).
* Brand logo or wordmark.
* Existing legal / consent / cookie copy.

---

## 12. THE BLOCK LIBRARY (Contract - Implementations Land Here Iteratively)

The Reference Vocabulary (Section 10) names patterns. The Block Library implements them with real props, real motion specs, and real code sketches.

**Status:** schema defined here. Blocks will be added iteratively. Do not freelance new blocks without following this schema.

### 12.A File Location
```
skills/taste-skill/blocks/
  hero/
    asymmetric-split.md
    editorial-manifesto.md
    kinetic-type.md
    ...
  feature/
    bento-grid.md
    sticky-scroll-stack.md
    zig-zag.md
    ...
  social-proof/
  pricing/
  cta/
  footer/
  navigation/
  portfolio/
  transition/
```

### 12.B Required Frontmatter
```yaml
---
name: asymmetric-split-hero
category: hero
dial_compatibility:
  variance: [6, 10]
  motion: [3, 10]
  density: [2, 5]
when_to_use: "Landing pages with one strong asset and one strong message. Default hero for SaaS, agency, premium consumer."
not_for: "Editorial / manifesto launches where the message IS the design."
stack: ["react", "next", "tailwind", "motion"]
---
```

The frontmatter above is a legacy schema example, not a default hero recommendation. Its `when_to_use` text and numeric range must be adapted to the selected block and direction.

### 12.C Required Body Sections
1. **Visual sketch** - short ASCII or description of the layout.
2. **Props API** - the component's interface.
3. **Code sketch** - minimal working implementation (Server Component default, Client island for motion).
4. **Mobile fallback** - explicit collapse rules for `< 768px`.
5. **Motion variants** - one variant per `MOTION_INTENSITY` band (1-3, 4-7, 8-10). Reduced-motion fallback explicit.
6. **Dark-mode notes** - token strategy specific to this block.
7. **Anti-patterns** - common ways this block goes wrong.
8. **References** - links to real examples in production.

### 12.D Block-Library Discipline
* One block per file. No multi-block files.
* Every block must work standalone (drop it into a page, it renders).
* Every block must pass the Pre-Flight Check (Section 14).
* Blocks that depend on a design system from Section 2.A live under `blocks/<category>/<name>--<system>.md` (e.g. `feature/bento-grid--material.md`).

---

## 13. OUT OF SCOPE

This skill is NOT for:
* Dashboards / dense product UI / admin panels (use Fluent, Carbon, Atlassian, or Polaris from Section 2.A).
* Data tables (use TanStack Table or AG Grid).
* Multi-step forms / wizards (use Form-specific patterns; this skill won't make them better).
* Code editors (use Monaco / CodeMirror with their official skinning).
* Native mobile (use Apple HIG / Material directly).
* Realtime collab UIs (presence, cursors, OT-aware - different problem class).

If the brief is one of the above, **say so explicitly**, point to the right tool, and only apply this skill's marketing-page / about-page / landing-page parts to the surfaces where they apply.

---

## 14. FINAL PRE-FLIGHT CHECK

Run this matrix before outputting code. This is the last filter.

**Review every applicable item.** Functional, accessibility and truthfulness failures must be fixed. Style items are contextual judgments against the chosen direction, not automatic bans or quotas; mark irrelevant items N/A with a brief reason when useful. Dials and legacy pattern examples do not create new requirements.

- [ ] **Brief inference** declared (Section 0.B one-liner)?
- [ ] **Dials, if used,** describe the chosen direction and actual implementation, with no universal or portfolio baseline?
- [ ] **Design system** chosen from Section 2 if applicable, or aesthetic labeled honestly?
- [ ] **Redesign mode** detected and audit performed (if applicable, Section 11)?
- [ ] **Editorial punctuation** fits the language, source text and chosen system; genuine quotes and ranges remain intact?
- [ ] **Theme coherence**: chosen mode(s) and deliberate section inversions serve the direction, with readable controls and content on each background (Section 4.11)?
- [ ] **Color roles** are coherent across components, with intentional accents and distinct semantic states; no universal single-accent rule (Section 4.2)?
- [ ] **Shape roles** are coherent for equivalent components without forcing every component to share one radius?
- [ ] **Button Contrast Check**: every CTA text is readable against its background (no white-on-white, WCAG AA 4.5:1)?
- [ ] **CTA label fit**: labels remain clear, readable and operable without clipping or arbitrary word/line quotas?
- [ ] **Form Contrast Check**: form inputs, placeholders, focus rings, labels all pass WCAG AA against the section background?
- [ ] **Typography fit**: chosen serif/sans/mixed roles support content, language, licensing and readability; no font blacklist or cross-project rotation?
- [ ] **Palette fit**: colors reflect this brand, imagery and audience; neither warm-craft colors nor alternatives are forced or banned by page category?
- [ ] **Italic descender clearance**: display italics are unclipped at their actual font, size and viewport, with sufficient line-height and wrapper reserve?
- [ ] **Hero reading path**: purpose, key work or primary action is discoverable; actual text, image scale and viewport work together without clipping or an arbitrary line/word quota?
- [ ] **Hero spacing** supports the intended composition at desktop and mobile without accidental overlap, obstruction or unexplained gaps?
- [ ] **Hero content priority** is clear; supporting context and CTAs earn their placement without a fixed element-count quota?
- [ ] **Eyebrow usefulness**: section labels add context rather than duplicate headlines; no mechanical count limit?
- [ ] **Header composition**: stacked or split content has clear alignment, measure and responsive reading order?
- [ ] **Section rhythm**: repetition supports comparable content and variation follows hierarchy, without a zigzag cap?
- [ ] **CTA intent clarity**: equivalent actions are understandable, useful repetition remains and contextual labels do not mislead?
- [ ] **Logo context**: genuine marks and any labels clarify identity/relationships without false social proof?
- [ ] **Grid treatment** follows content and selected direction; no decorative image, tint or pattern quota?
- [ ] **Social proof, if used,** is truthful, accessible and placed where it serves the reading path; invented example brands are clearly identified?
- [ ] **Copy Self-Audit**: every visible string re-read, no grammatically-broken or AI-hallucinated phrases ("free on its past" type) shipped?
- [ ] **Motion purpose** supports hierarchy, story, feedback, state, material or atmosphere, and has been assessed in normal browser interaction?
- [ ] **Moving-track pacing**: combined motion remains legible and intentional with appropriate interruption and reduced-motion behavior?
- [ ] **Navigation fit**: actual labels and controls remain readable and reachable without overlap, clipping or an arbitrary height/line cap?
- [ ] **Layout families** support the content hierarchy and scanning; repeated comparable items need no artificial per-section variety quota?
- [ ] **Bento has rhythm AND exact cell count** (N items → N cells, no empty cells in middle or at end)?
- [ ] **Lists/specifications** remain complete and easy to scan/compare; a plain list or table is valid, and any grouping/disclosure is justified?
- [ ] **Asset strategy fits the brief:** supplied assets preserved, no fake screenshots, missing required assets reported; text-only directions need no decorative image quota.
- [ ] **Image labels/captions** serve content or composition with readable contrast and no obstructed essential detail?
- [ ] **Photo attribution** is genuine; illustrative captions do not invent photographer or archival claims?
- [ ] **Technical metadata** is genuine and useful, with no invented build/version state?
- [ ] **Supporting explanations** add useful context without redundant filler?
- [ ] **Text strips** support the selected hierarchy, rhythm or identity without competing clutter?
- [ ] **Section explanations** remain aligned with their headings and readable in the chosen stacked or split layout?
- [ ] **Comparison/progress graphics** accurately represent data and remain readable in context?
- [ ] **Location/time information**, if present, is genuine and relevant to content or identity?
- [ ] **Exploration cues**, if used, support discoverability and do not obstruct the page?
- [ ] **Launch/status labels**, if present, state real information without manufactured urgency?
- [ ] **Numbering and pagination**, if used, clarify order, progress or the selected graphic system?
- [ ] **Graphic markers** support the chosen expression; markers claiming live state are truthful?
- [ ] **Dividers** clarify actual rows/groups without unnecessary stroke duplication?
- [ ] **Content density** supports scanning and necessary depth, with genuine facts and no word/row-count veto?
- [ ] **Quotes** preserve meaning and genuine attribution at a readable length, with excerpts identified?
- [ ] **Motion description** matches actual behavior; no extra effects were added to satisfy a dial threshold?
- [ ] **GSAP sticky-stack / horizontal-pan** implemented per Section 5.A / 5.B canonical skeleton (`start: "top top"`, `pin: true`, correct scrub)?
- [ ] **Scroll work** uses suitable native/existing-library facilities with bounded cost, owned-listener cleanup and usable interruption/end states (Section 5.D), without an API blacklist?
- [ ] **Reduced motion** preserves information/actions and reduces non-essential movement at every intensity; an explicit no-animation brief remains static?
- [ ] **Implemented themes** and section backgrounds have appropriate tokens and have been checked; a second mode is not mandatory?
- [ ] **Mobile adaptation** has a verified reading order, sizing and reachable controls; columns/tracks follow the chosen composition?
- [ ] **Viewport sizing** follows the actual composition and mobile browser behavior; content remains reachable without a universal full-height or utility-class requirement?
- [ ] **`useEffect` animations** have strict cleanup functions?
- [ ] **Applicable pending/empty/error states** are honest and operable; static content needs no fabricated state?
- [ ] **Grouping surfaces** serve content, interaction or material roles; neither cards nor bare rows are required?
- [ ] **Icons** reuse the actual project family or a justified native/library asset with consistent roles and accessibility?
- [ ] **Motion ownership/lifecycle** fits the actual stack; RSC projects use necessary client boundaries, without adding React directives or blanket memoization to other environments?
- [ ] **Section 9 review** distinguishes unearned stylistic defaults from intentional choices; real names/data are preserved and sample content is identified?
- [ ] **Performance evidence** records available measurements and material limits; target LCP < 2.5s, INP < 200ms, CLS < 0.1 without presenting an estimate or lab-only result as field proof?
- [ ] **One design system** per project (no Material + shadcn mixed)?

Fix applicable failures before delivering. An intentionally inapplicable style suggestion is not a failure; explain material limits in actual verification evidence without adding a new style requirement.

---

# APPENDICES - Real Source-Backed Reference Material

The sections below are vendored reference content. They give the agent real install commands, real canonical doc links, and real working starter snippets for each design system named in Section 2. Use them to ground decisions in production reality, not training-data fiction.

## Appendix A - Install Commands per Design System

```bash
# Material Web (Material 3)
npm install @material/web

# Fluent UI React (v9)
npm install @fluentui/react-components

# Fluent UI Web Components (framework-free)
npm install @fluentui/web-components @fluentui/tokens

# IBM Carbon
npm install @carbon/react @carbon/styles

# Radix Themes
npm install @radix-ui/themes

# shadcn/ui (open code, owned components)
npx shadcn@latest init
npx shadcn@latest add button card badge separator input

# Primer CSS (GitHub product/devtool UI)
npm install --save @primer/css

# Primer Brand (GitHub marketing UI)
npm install @primer/react-brand

# GOV.UK Frontend
npm install govuk-frontend

# USWDS (US Web Design System)
npm install uswds

# Atlassian Design System (Atlaskit)
yarn add @atlaskit/css-reset @atlaskit/tokens @atlaskit/button @atlaskit/badge @atlaskit/section-message @atlaskit/card

# Bootstrap 5.3
npm install bootstrap

# Shopify Polaris Web Components (Shopify apps only)
# Add this to your app HTML head:
#   <meta name="shopify-api-key" content="%SHOPIFY_API_KEY%" />
#   <script src="https://cdn.shopify.com/shopifycloud/polaris.js"></script>
```

## Appendix B - Canonical Sources (read these before reinventing)

### Material Web
- https://github.com/material-components/material-web
- https://material-web.dev/theming/material-theming/
- https://m3.material.io/develop/web

### Fluent UI
- https://fluent2.microsoft.design/get-started/develop
- https://fluent2.microsoft.design/components/web/react/
- https://github.com/microsoft/fluentui
- https://learn.microsoft.com/en-us/fluent-ui/web-components/

### Carbon
- https://carbondesignsystem.com/
- https://github.com/carbon-design-system/carbon
- https://carbondesignsystem.com/developing/react-tutorial/overview/
- https://carbondesignsystem.com/developing/web-components-tutorial/overview/

### Shopify Polaris
- https://shopify.dev/docs/api/app-home/web-components
- https://github.com/Shopify/polaris-react
- https://polaris-react.shopify.com/components

### Atlassian
- https://atlassian.design/get-started/develop
- https://atlassian.design/components/button/examples
- https://atlaskit.atlassian.com/packages/design-system/button/example/disabled
- https://atlassian.design/tokens/design-tokens

### Primer
- https://primer.style/
- https://github.com/primer/css
- https://github.com/primer/brand

### GOV.UK
- https://design-system.service.gov.uk/components/button/
- https://design-system.service.gov.uk/styles/layout/
- https://github.com/alphagov/govuk-frontend

### USWDS
- https://designsystem.digital.gov/documentation/developers/
- https://designsystem.digital.gov/components/button/
- https://designsystem.digital.gov/components/card/
- https://github.com/uswds/uswds

### Bootstrap
- https://getbootstrap.com/docs/5.3/layout/grid/
- https://getbootstrap.com/docs/5.3/components/card/

### Tailwind
- https://tailwindcss.com/docs/dark-mode
- https://tailwindcss.com/blog/tailwindcss-v4

### Radix
- https://www.radix-ui.com/themes/docs/components/theme
- https://www.radix-ui.com/themes/docs/components/card
- https://github.com/radix-ui/themes

### shadcn/ui
- https://ui.shadcn.com/docs
- https://ui.shadcn.com/docs/components/card
- https://github.com/shadcn-ui/ui

### Native CSS / W3C standards
- https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter
- https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme
- https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion
- https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout
- https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations
- https://drafts.csswg.org/scroll-animations-1/

### Apple Liquid Glass (Apple platforms only)
- https://developer.apple.com/design/human-interface-guidelines/materials
- https://developer.apple.com/documentation/TechnologyOverviews/liquid-glass
- https://developer.apple.com/documentation/TechnologyOverviews/adopting-liquid-glass
- https://developer.apple.com/documentation/SwiftUI/Material

---

## Appendix C - Apple Liquid Glass: Honest Web Approximation

Do **not** treat random CSS snippets as official Apple Liquid Glass.

### What is official
Apple documents Liquid Glass inside Apple's Human Interface Guidelines and Developer Documentation for **Apple platforms**. It is a dynamic material used across Apple platform UI. Apple's native implementation belongs to Apple platform APIs and system components, **not a public web CSS package**.

Relevant official docs:
- Apple Human Interface Guidelines → Materials
- Apple Developer Documentation → Liquid Glass
- Apple Developer Documentation → Adopting Liquid Glass
- SwiftUI → Material

### What is NOT official
There is no `liquid-glass.css` from Apple for normal websites.

A web approximation can use:
- `backdrop-filter`
- transparent backgrounds
- layered borders
- highlight overlays
- gradients
- motion
- strong contrast fallbacks

But that is **web glassmorphism / frosted-glass approximation**, not official Apple Liquid Glass. Label it as such in comments.

### Safer web approximation skeleton

```css
.liquid-glass-web-approx {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  border-radius: 999px;
  border: 1px solid rgb(255 255 255 / .32);
  background:
    linear-gradient(135deg, rgb(255 255 255 / .30), rgb(255 255 255 / .08)),
    rgb(255 255 255 / .12);
  backdrop-filter: blur(24px) saturate(180%) contrast(1.05);
  -webkit-backdrop-filter: blur(24px) saturate(180%) contrast(1.05);
  box-shadow:
    inset 0 1px 0 rgb(255 255 255 / .48),
    inset 0 -1px 0 rgb(255 255 255 / .12),
    0 18px 60px rgb(0 0 0 / .18);
}

.liquid-glass-web-approx::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  border-radius: inherit;
  background:
    radial-gradient(circle at 20% 0%, rgb(255 255 255 / .55), transparent 34%),
    linear-gradient(90deg, rgb(255 255 255 / .18), transparent 42%, rgb(255 255 255 / .14));
  pointer-events: none;
}

.liquid-glass-web-approx::after {
  content: "";
  position: absolute;
  inset: 1px;
  border-radius: inherit;
  border: 1px solid rgb(255 255 255 / .14);
  pointer-events: none;
}

@media (prefers-color-scheme: dark) {
  .liquid-glass-web-approx {
    border-color: rgb(255 255 255 / .18);
    background:
      linear-gradient(135deg, rgb(255 255 255 / .16), rgb(255 255 255 / .04)),
      rgb(15 23 42 / .42);
    box-shadow:
      inset 0 1px 0 rgb(255 255 255 / .22),
      0 18px 60px rgb(0 0 0 / .42);
  }
}

@media (prefers-reduced-transparency: reduce) {
  .liquid-glass-web-approx {
    background: rgb(255 255 255 / .96);
    backdrop-filter: none;
    -webkit-backdrop-filter: none;
  }
}
```

**Important:** `prefers-reduced-transparency` has uneven browser support; test it. Always provide enough contrast even without blur.

---

**End of appendices.** Install commands above are reality anchors. The Apple Liquid Glass skeleton is a labeled approximation, not an Apple-issued package. For canonical docs per design system, consult the system's official docs (links in Section 2 plus Appendix B).
