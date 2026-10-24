---
name: stitch-design-taste
description: Translate a selected visual system into a semantic DESIGN.md for Google Stitch, preserving its actual palette, typography, material, spatial and motion decisions with precise values and responsive behavior.
---

> 绘枢模块：交付 Google Stitch 可理解的 DESIGN.md；同目录 DESIGN.md 是可选旧模板，生成文档与远程 Stitch 执行分开取证。先遵循[单入口](../../SKILL.md)和[兼容与工具规则](../../references/compatibility.md)。下列保留的旧 frontmatter 仅作来源元数据；旧名字按包内模式文字口令解释，不注册独立技能。

# Stitch — Semantic Design System Translation

## Overview
Generate a `DESIGN.md` that translates the project's selected visual system into descriptive rules, exact values and component behaviors. It is the source of truth for that project's screen generation, not a new aesthetic preset.

Read the brief, approved references, existing DS and selected concept first. If a new or fully rebuilt project still has an open direction, return to the single entry's direction formation before fixing tokens. When a direction is already chosen, preserve it rather than choosing another style here.

## Prerequisites and Output Boundary
- Writing a local `DESIGN.md` requires the project inputs, not Google login or a Stitch connection.
- Remote screen generation or submission requires an available Stitch connection and authorization for that operation. Do not imply remote execution from a local document.
- [DESIGN.md](DESIGN.md) is a preserved optional legacy example. Adapt its structure only as useful; its dial values, colors, font bans, layout bans and motion recipe are not inherited defaults. An existing DS or selected concept may legitimately use none of them.

## The Goal
Encode the actual system:
1. **Visual atmosphere** — content, audience, energy, density, material and spatial intent.
2. **Color roles** — exact tokens, semantic use and contrast behavior.
3. **Typography** — real font availability, language coverage, scale and hierarchy.
4. **Components** — shape, material, depth and interaction states.
5. **Layout** — reading path, grouping, responsive strategy and intended overlap.
6. **Motion** — triggers, transitions, timing, interruption and suitable alternatives.
7. **Project anti-patterns** — actual constraints and observed failures to avoid.

## Analysis & Synthesis Instructions

### 1. Describe the Selected Atmosphere
Express the project's mood, density and energy in concrete visual terms. Describe material and spatial choices when adopted, including flat surfaces or no depth when appropriate. Numeric dials are optional communication aids derived from the selected concept; there is no 8/6/4 baseline.

Do not equate premium with quiet, neutral, sparse, asymmetrical or dark. Explain the meaning and content job of the chosen expression.

### 2. Map Color Roles
For each color provide **Descriptive Name + Exact Value + Functional Role**, including semantic states and contrast requirements. Hex, RGB/RGBA or other supported values may be appropriate.

Preserve a coherent palette rather than enforcing one accent or a saturation cap. Multicolor systems, saturated colors, purple, pure black, gradients and glow are valid when selected deliberately and remain legible. Record how color behaves over imagery and across supported modes; do not invent another theme merely to complete a pair.

### 3. Establish Typography
Record selected fonts and fallbacks, availability or licensing limitations, language/glyph coverage, size, weight, leading, tracking and line-length behavior. Use expressive display, serif, system sans or monospace when the task calls for it; no font family is banned by name. Dashboards need readable labels and numbers, not a universal serif prohibition. Tabular numbers or monospace should serve comparison when useful, rather than follow a density threshold.

### 4. Describe the Opening and Components
Describe the actual first-view promise and next actions. A hero is optional for an application. Centered compositions, image-backed type, asymmetry, text-led openings and intentional layering are available choices, not a variance formula. Preserve readable contrast and discoverable actions when layers overlap.

For each applicable component document normal, hover, focus, active, loading, empty and error states. Specify material, edge, shadow and lighting behavior only where used. Keep labels and recovery paths clear. Choose real loading feedback for known or unknown progress; skeletons and spinners are both valid when appropriate. Use supplied components and icons before inventing replacements.

### 5. Define Layout and Responsive Behavior
Describe grouping, reading order, grid or flex rules, spacing, containment and purposeful overlaps. A repeated equal-column comparison can be useful; there is no forced split, bento or three-column ban.

Adapt to the content at narrow widths. A single column, compact comparison grid, discoverable horizontal gallery or suitable task-specific arrangement may be appropriate. Prevent accidental whole-page overflow, clipped actions and unusable hit areas. Specify touch and keyboard behavior appropriate to the platform; test important breakpoints rather than claiming all sizes work from a mockup. Use fluid sizing and dynamic viewport units where appropriate, without prescribing one CSS class or forcing every section full-height.

### 6. Encode Actual Motion and Interaction
For adopted motion, specify **trigger → visible change → timing/easing → settled state**, repeat/interruption handling, input method and reduced-motion behavior. Springs, linear movement, easing curves and discrete changes each have uses; there is no universal physics setting or motion quota. Static components remain valid.

Prefer `transform`/`opacity` for efficient movement. If layout interpolation, clipping, filters, SVG or other properties express a real behavior, specify the needed effect and verify its performance rather than banning the capability. Keep heavy work isolated and clean up owned listeners, timelines and triggers. Respect the preserved local animation safety fixes.

Stitch screens are static. This document records temporal intent for implementation; a generated screen cannot prove the animation works. When the task includes code, verify normal motion in a real browser, including an appropriate interrupted path and usable reduced-motion state; static screenshots and a build alone do not prove it.

### 7. Record Project Anti-Patterns
List project-specific constraints, genuine usability failures and observed habits that would weaken the selected concept. Keep real content, data, links and asset provenance honest; label examples rather than inventing proof. Do not substitute arbitrary organic-looking numbers for actual round data.

Do not turn font names, colors, centered layouts, overlays, grids, cursors or effect categories into universal NEVER rules. A concrete failure such as hidden text, obstructed controls, purposeless repetition or inaccessible interaction should name what fails and why.

## Output Format — Preserve These Seven Sections

```markdown
# Design System: [Project Title]

## 1. Visual Theme & Atmosphere
[Selected concept, audience, content job, energy and density. Material and spatial
choices or deliberate flatness. Reference/DS constraints and meaningful tradeoffs.]

## 2. Color Palette & Roles
- **[Token Name]** ([exact value]) — [semantic role and applicable state/surface]
[Supported modes and contrast rules; the actual number of accents follows the system.]

## 3. Typography Rules
- **[Role]:** [available font + language-aware fallback], [exact size/weight/leading/tracking]
[Responsive wrapping, line length and numeric alignment appropriate to the content.]

## 4. Component Stylings
* **[Component]:** [shape/material/depth tokens and normal/hover/focus/active behavior]
[Applicable loading, empty and error states with usable labels and recovery paths.]

## 5. Layout Principles
[Reading path, grouping, grid/flex, spacing values, containment and intended overlap.
Narrow-screen rearrangement, touch/keyboard behavior and accidental-overflow limits.]

## 6. Motion & Interaction
[For each adopted behavior: trigger → change → timing/easing → settled state;
repeat/interruption handling and appropriate reduced-motion alternative.
Static behavior is valid. Identify which temporal behavior still needs live browser proof.]

## 7. Anti-Patterns (Project Constraints)
[Actual project prohibitions and concrete failures to avoid, with reasons.
No copied aesthetic bans from the legacy example; honest data and asset boundaries.]
```

## Completion Check
- Use consistent semantic names with exact values where the implementation needs them.
- Trace decisions to the existing DS, selected concept or real task, not the legacy example.
- Include only applicable components and behaviors; do not add a hero, theme or motion to fill a document slot.
- Keep descriptive language understandable to Stitch without losing precision.
- Distinguish local document creation, static screen generation, code implementation and actual browser verification in the delivery report.
