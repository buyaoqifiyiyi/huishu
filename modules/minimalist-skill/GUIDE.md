---
name: minimalist-ui
description: Design warm monochrome, flat editorial interfaces when the brief requests restrained minimalist styling. Use typography, thin dividers and muted pastel accents; preserve an existing design system and do not combine this preset with cinematic glass or maximal motion rules.
---

> 绘枢模块：仅在选择温暖、平面、克制极简风格时启用；不叠加玻璃、强动效或强制图片。 先遵循[单入口](../../SKILL.md)和[兼容与工具规则](../../references/compatibility.md)。下列保留的旧 frontmatter 仅作来源元数据；旧名字按包内模式文字口令解释，不注册独立技能。

# Protocol: Premium Utilitarian Minimalism UI Architect

Apply this as the chosen visual direction, not as a second style layered onto another preset. Existing brand requirements and explicit no-image/no-animation requests take precedence.

## 1. Protocol Overview
Name: Premium Utilitarian Minimalism & Editorial UI
Description: An advanced frontend engineering directive for generating highly refined, ultra-minimalist, "document-style" web interfaces analogous to top-tier workspace platforms. This protocol strictly enforces a high-contrast warm monochrome palette, bespoke typographic hierarchies, meticulous structural macro-whitespace, bento-grid layouts, and an ultra-flat component architecture with deliberate muted pastel accents. It actively rejects standard generic SaaS design trends.

## 2. Absolute Negative Constraints (Banned Elements)
The AI must strictly avoid the following generic web development defaults:
- Select typefaces for this restrained direction, actual language coverage and available licensed resources. Inter, Roboto and Open Sans are valid when they fit; preserve existing brand fonts.
- Reuse the project's existing icon family. Choose weight and scale for this flat composition; thin-line icons are not inherently generic and do not require a library replacement.
- DO NOT use Tailwind's default heavy drop shadows (e.g., `shadow-md`, `shadow-lg`, `shadow-xl`). Shadows must be practically non-existent or heavily customized to be ultra-diffuse and low opacity (< 0.05).
- DO NOT use primary colored backgrounds for large elements or sections (e.g., no bright blue, green, or red hero sections).
- DO NOT use gradients, neon colors, or 3D glassmorphism (beyond subtle navbar blurs).
- DO NOT use `rounded-full` (pill shapes) for large containers, cards, or primary buttons.
- DO NOT use emojis anywhere in code, markup, text content, headings, or alt text. Replace with proper icons or clean SVG primitives.
- Preserve real content. Identify prototype/sample content clearly; realistic names do not establish real people, customers or endorsements.
- DO NOT use AI copywriting clichés: "Elevate", "Seamless", "Unleash", "Next-Gen", "Game-changer", "Delve". Write plain, specific language.

## 3. Typographic Architecture
The interface must rely on extreme typographic contrast and premium font selection to establish an editorial feel.
- Primary Sans-Serif (Body, UI, Buttons): Use clean, geometric, or system-native fonts with character. Target: `font-family: 'SF Pro Display', 'Geist Sans', 'Helvetica Neue', 'Switzer', sans-serif`.
- Editorial Serif (Hero Headings & Quotes): Target: `font-family: 'Lyon Text', 'Newsreader', 'Playfair Display', 'Instrument Serif', serif`. Apply tight tracking (`letter-spacing: -0.02em` to `-0.04em`) and tight line-height (`1.1`).
- Monospace (Code, Keystrokes, Meta-data): Target: `font-family: 'Geist Mono', 'SF Mono', 'JetBrains Mono', monospace`.
- Text Colors: Off-black/charcoal (`#111111` or `#2F3437`) and muted secondary gray are sample roles for this palette. Pure black is valid when the selected system uses it. Verify contrast and leading with the actual font, language and surface.

## 4. Color Palette (Warm Monochrome + Spot Pastels)
Color is a scarce resource, utilized only for semantic meaning or subtle accents.
- Canvas / Background: Pure White `#FFFFFF` or Warm Bone/Off-White `#F7F6F3` / `#FBFBFA`.
- Primary Surface (Cards): `#FFFFFF` or `#F9F9F8`.
- Structural Borders / Dividers: Ultra-light gray `#EAEAEA` or `rgba(0,0,0,0.06)`.
- Accent Colors: Exclusively use highly desaturated, washed-out pastels for tags, inline code backgrounds, or subtle icon backgrounds.
  - Pale Red: `#FDEBEC` (Text: `#9F2F2D`)
  - Pale Blue: `#E1F3FE` (Text: `#1F6C9F`)
  - Pale Green: `#EDF3EC` (Text: `#346538`)
  - Pale Yellow: `#FBF3DB` (Text: `#956400`)

## 5. Component Specifications
These are references for components the actual page needs, not a required inventory of bento grids, badges, FAQ, shortcuts or software previews.
- Bento Box Feature Grids:
  - Utilize asymmetrical CSS Grid layouts.
  - Use fine, low-contrast structural borders where they help group content; adapt color and thickness to the selected tokens and actual contrast rather than requiring one exact declaration.
  - Border-radius must be crisp: `8px` or `12px` maximum.
  - Internal padding must be generous (e.g., `24px` to `40px`).
- Primary Call-To-Action (Buttons):
  - Solid background `#111111`, text `#FFFFFF`. 
  - Slight border-radius (`4px` to `6px`). No box-shadow. 
  - Hover state should be a subtle color shift to `#333333` or a micro-scale `transform: scale(0.98)`.
- Tags & Status Badges:
  - Pill-shaped (`border-radius: 9999px`), very small typography (`text-xs`), uppercase with wide tracking (`letter-spacing: 0.05em`).
  - Background must use the defined Muted Pastels.
- Accordions (FAQ):
  - Strip all container boxes. Separate items only with a `border-bottom: 1px solid #EAEAEA`.
  - Use a clean, sharp `+` and `-` icon for the toggle state.
- Keystroke Micro-UIs:
  - Render shortcuts as physical keys using `<kbd>` tags: `border: 1px solid #EAEAEA`, `border-radius: 4px`, `background: #F7F6F3`, using the Monospace font.
- Software Previews:
  - Show actual product surfaces or clearly identified illustrative mockups. Use platform chrome only when it matches the depicted product; do not automatically add macOS controls to web, Windows or mobile interfaces.

## 6. Iconography & Imagery Directives
- System Icons: Phosphor (Bold/Fill) and Radix are examples for a slightly thicker aesthetic, not required dependencies. Reuse the actual project family and keep weight/size coherent across equivalent roles.
- Illustrations: Monochromatic, rough continuous-line ink sketches on a white background, featuring a single offset geometric shape filled with a muted pastel color.
- Photography: Preserve supplied imagery and its intended color. Desaturation, warm grading or subtle grain are optional treatments when compatible with the work; do not process assets merely to force the palette. If required imagery is missing, use an inspected, clearly identified placeholder or report the gap; seeded photo URLs do not guarantee relevance or availability.
- Hero & Section Backgrounds: Plain warm surfaces and intentional whitespace are valid. Where the brief needs extra texture, use restrained imagery or minimal geometric line patterns; keep the no-gradient constraint.

## 7. Subtle Motion & Micro-Animations
Motion should feel invisible — present but never distracting. The goal is quiet sophistication, not spectacle.
- Scroll Entry: Optional when it supports the reading sequence; `translateY(12px)` + opacity over `600ms` is an example, not a per-element requirement. Use `IntersectionObserver` for visibility-triggered entry; keep content reachable when animation is disabled or unsupported.
- Hover States: Cards lift with an ultra-subtle shadow shift (`box-shadow` transitioning from `0 0 0` to `0 2px 8px rgba(0,0,0,0.04)` over `200ms`). Buttons respond with `scale(0.98)` on `:active`.
- Staggered Reveals: Use a short cascade only where sequence matters. Static lists and simultaneous rendering are valid; avoid cumulative delays that obstruct scanning or access.
- Background Ambient Motion: Optional only when requested by the visual direction. Use a faint solid geometric shape, without gradients, on a `position: fixed; pointer-events: none` layer. Static backgrounds remain valid.
- Performance: Prefer `transform` and `opacity` for frequent spatial motion. Other properties can support the chosen behavior; bound their area/frequency and verify cost instead of banning the capability. Use `will-change` sparingly and only while useful.
- Reduced Motion (mandatory): Gate scroll-entry, staggered reveals, and ambient background motion behind `@media (prefers-reduced-motion: no-preference)`, and add a `@media (prefers-reduced-motion: reduce)` block that disables them so content appears instantly at rest. Keep meaningful hover/focus/active feedback, but make non-essential spatial movement instant or static under reduced motion; an explicit no-animation brief stays static.

## 8. Execution Protocol
When tasked with writing frontend code (HTML, React, Tailwind, Vue) or designing a layout:
1. Establish hierarchy and readable spacing for the actual task and viewport. Generous macro-whitespace is available; `py-24`/`py-32` are examples, not minimums or a reason to stretch compact content.
2. Choose readable text measures and layout widths from the content and selected composition; narrow reading columns and wider project/data regions can coexist.
3. Apply the custom typographic hierarchy and monochromatic color variables immediately.
4. Keep fine borders and dividers coherent with their roles and actual tokens; inspect contrast on the chosen surface instead of enforcing one hex value everywhere.
5. Add restrained scroll-entry animation only where it serves the brief; keep no-animation and reduced-motion views static.
6. Use typography, spacing, dividers and optional subtle textures for hierarchy. Flat or text-only sections can be complete; do not force imagery or gradients.
7. Provide code that reflects this high-end, uncluttered, editorial aesthetic natively without requiring manual adjustments.
