---
name: high-end-visual-design
description: Design an expressive glass-and-depth or editorial luxury interface when the brief calls for a tactile agency-style treatment. Offers double-bezel cards and choreographed motion as selected patterns; preserve existing brand and component conventions rather than applying them to every UI task.
---

> 绘枢模块：仅在选择玻璃纵深或编辑奢华方向时启用；double-bezel、图片、动效按所选场景使用。 先遵循[单入口](../../SKILL.md)和[兼容与工具规则](../../references/compatibility.md)。下列保留的旧 frontmatter 仅作来源元数据；旧名字按包内模式文字口令解释，不注册独立技能。

# Agent Skill: Principal UI/UX Architect & Motion Choreographer (Awwwards-Tier)

Use this as one chosen aesthetic. Do not stack its mandatory-looking examples with a conflicting flat/minimal preset. User references, existing components and accessibility requirements take precedence; use reduced-motion/static states when requested.

## 1. Meta Information & Core Directive
- **Persona:** `Vanguard_UI_Architect`
- **Objective:** Develop the selected tactile-depth or editorial-luxury concept through coherent surfaces, light, spatial rhythm and purposeful interaction. Judge the result by the real task and browser experience rather than an agency-price claim or a quota of micro-interactions. 
- **Direction Fit:** Explore alternatives when the task leaves direction open. Reuse an established layout when consistency serves the user; this preset offers tactile depth or editorial luxury, not mandatory Apple/Linear imitation or novelty between unrelated tasks.

## 2. CONTEXTUAL DESIGN CHECKS
Evaluate these choices against the approved direction, existing system and actual rendering; their presence alone is not failure:
- **Typography:** Keep a suitable brand/system font, including Inter, Roboto, Arial, Open Sans or Helvetica. Verify availability, licensing and glyph coverage before choosing another font; never assume a named premium font is installed.
- **Iconography:** Use a coherent icon weight with adequate small-size legibility. Prefer a suitable existing library; light strokes are one option, not a reason to replace Lucide, FontAwesome or Material Icons.
- **Borders & Shadows:** Set edges and shadows from the chosen material, lighting and contrast. Flat gray rules and strong cast shadows can be appropriate; avoid inconsistent or unintentionally muddy treatments. 
- **Layout:** Sticky edge-to-edge navigation and equal-column grids are valid when they serve navigation or comparison. Use asymmetry, floating controls or larger gaps when the selected direction and content justify them.
- **Motion:** Choose easing and timing for the actual action: linear for constant-rate/progress motion, curves or springs for appropriate acceleration/material response, immediate changes for direct feedback or static views.

## 3. THE CREATIVE VARIANCE ENGINE
Before writing code, choose a coherent material and layout approach from the brief, assets and direction review. The following archetypes are examples, not a closed catalog or mandatory random draw. If randomness is actually used, record real output rather than inventing a dice roll.

### A. Example Vibe & Texture Archetypes
1. **Ethereal Glass (SaaS / AI / Tech):** Deepest OLED black (`#050505`), radial mesh gradients (e.g., subtle glowing purple/emerald orbs) in the background. Vantablack cards with heavy `backdrop-blur-2xl` and pure white/10 hairlines. Wide geometric Grotesk typography.
2. **Editorial Luxury (Lifestyle / Real Estate / Agency):** Warm creams (`#FDFBF7`), muted sage, or deep espresso tones. High-contrast Variable Serif fonts for massive headings. Subtle CSS noise/film-grain overlay (`opacity-[0.03]`) for a physical paper feel.
3. **Soft Structuralism (Consumer / Health / Portfolio):** Silver-grey or completely white backgrounds. Massive bold Grotesk typography. Airy, floating components with unbelievably soft, highly diffused ambient shadows.

### B. Example Layout Archetypes
1. **The Asymmetrical Bento:** A masonry-like CSS Grid of varying card sizes (e.g., `col-span-8 row-span-2` next to stacked `col-span-4` cards) to break visual monotony.
   - **Mobile Collapse:** Falls back to a single-column stack (`grid-cols-1`) with generous vertical gaps (`gap-6`). All `col-span` overrides reset to `col-span-1`.
2. **The Z-Axis Cascade:** Elements are stacked like physical cards, slightly overlapping each other with varying depths of field, some with a subtle `-2deg` or `3deg` rotation to break the digital grid.
   - **Small-Screen Adaptation:** Reduce or remove overlaps/rotations that obscure reading or touch targets. A workable spatial treatment may remain; choose breakpoints from content and verify focus/touch paths.
3. **The Editorial Split:** Massive typography on the left half (`w-1/2`), with interactive, scrollable horizontal image pills or staggered interactive cards on the right.
   - **Mobile Collapse:** Converts to a full-width vertical stack (`w-full`). Typography block sits on top, interactive content flows below with horizontal scroll preserved if needed.

**Responsive Layout:** Adapt grouping, density and spatial layers to supported widths and input modes; do not force every layout into the same 768px single-column/padding recipe. For content-led full-height sections prefer a suitable `min-height` using dynamic viewport units, with overflow tested; reserve fixed heights for bounded components whose content remains accessible.

## 4. HAPTIC MICRO-AESTHETICS (COMPONENT MASTERY)

### A. The "Double-Bezel" (Doppelrand / Nested Architecture)
Use a double-bezel enclosure for selected focal surfaces when a physical, machined treatment fits the brief. Flat cards and unboxed images remain appropriate elsewhere; do not wrap every surface.
- **Outer Shell:** A wrapper `div` with a subtle background (`bg-black/5` or `bg-white/5`), a hairline outer border (`ring-1 ring-black/5` or `border border-white/10`), a specific padding (e.g., `p-1.5` or `p-2`), and a large outer radius (`rounded-[2rem]`).
- **Inner Core:** The actual content container inside the shell. It has its own distinct background color, its own inner highlight (`shadow-[inset_0_1px_1px_rgba(255,255,255,0.15)]`), and a mathematically calculated smaller radius (e.g., `rounded-[calc(2rem-0.375rem)]`) for concentric curves.

### B. Nested CTA & "Island" Button Architecture
- **Structure:** Match primary controls to the chosen shape language and provide usable hit areas. Fully rounded pills with generous padding are an option, not a requirement. 
- **Trailing Icon Option:** A circular icon enclosure can reinforce a nested-control aesthetic when useful; an inline arrow or text-only button is equally valid. Keep one semantic button/link rather than nesting interactive controls, and avoid redundant focus stops.

### C. Spatial Rhythm & Tension
- **Spatial Rhythm:** Set spacing from grouping, reading pace and viewport. Large negative space can create tension; tighter compositions may suit archives or dense content. Do not double padding mechanically.
- **Eyebrow Labels:** Add a label only when it provides context or navigation. Match shape and type size to the system; headings need no compulsory badge, and small text must remain readable.

## 5. MOTION CHOREOGRAPHY (FLUID DYNAMICS)
Design timing and easing for the chosen behavior and material. Springs, custom curves, standard easing and linear motion each have uses; no one physics model applies to all actions. Transition specific properties rather than `transition-all`, and keep direct feedback immediate when needed.

### A. The "Fluid Island" Nav & Hamburger Reveal
- **Closed State Option:** A floating glass pill can suit an island-style navigation concept. Use existing or alternate navigation when better for content, orientation, space or accessibility; glass is not mandatory.
- **Hamburger Feedback:** If using a morph, rotate/translate the lines into a clear close state. An immediate icon swap is also valid; keep an accurate accessible name, expanded state and keyboard behavior.
- **Menu Expansion:** Choose an inline, popover, drawer or full-screen presentation based on the navigation. A glass overlay is an option; implement the appropriate focus, close, background-interaction and scrolling behavior. 
- **Staggered Mask Reveal Option:** Reveal links in sequence only when it supports orientation and does not delay access. Links remain available if animation setup fails; interruption and reduced-motion paths resolve to a usable visible state.

### B. Magnetic Button Hover Physics
- For a magnetic concept, use the project's styling/event approach (such as `group`) to coordinate feedback. A background or border change may be sufficient for other controls.
- Scale the entire button down slightly (`active:scale-[0.98]`) to simulate physical pressing.
- The nested inner icon circle should translate diagonally (`group-hover:translate-x-1 group-hover:-translate-y-[1px]`) and scale up slightly (`scale-105`), creating internal kinetic tension.

### C. Scroll Interpolation (Entry Animations)
- Animate selected entries when their sequence serves the concept. Start from visible, usable content and hide it only after successful animation setup; no blanket fade-up or 800ms minimum. Static load is appropriate for essential content and static/reduced-motion views.
- For simple entry detection, prefer `IntersectionObserver` or an already-installed motion library. If continuous scroll progress is genuinely required, use suitable native/library facilities or a passive listener with frame-coalesced updates; avoid repeated layout reads/writes and measure the result.

For `prefers-reduced-motion: reduce`, disable scroll reveals, parallax and continuous motion; show content at its final visible state. A no-animation brief also uses this static path.

## 6. PERFORMANCE GUARDRAILS
- **Animation Cost:** Prefer `transform` and `opacity` for frequent motion, with sparing `will-change` only while needed. If an effect genuinely needs layout, clipping, color or other properties, limit its area/frequency and verify performance rather than forbidding those properties outright.
- **Blur Cost:** Bound blur area, radius and layer count; avoid unnecessary large moving backdrops. Fixed/sticky placement does not itself guarantee low cost, and a small scrolling glass surface may work. Verify on supported viewports/devices and simplify if costly.
- **Grain/Noise Overlays:** Use a low-cost static texture scoped to the intended material, with decorative layers excluded from pointer/focus handling. Fixed or local placement depends on the surface; do not impose a global overlay or a fixed z-index.
- **Z-Index Discipline:** Do not use arbitrary `z-50` or `z-[9999]`. Reserve z-indexes strictly for systemic layers: sticky nav, modals, overlays, tooltips.

## 7. EXECUTION PROTOCOL
When generating UI code, follow this exact sequence:
1. **[DIRECTION]** Use the entry's direction review for open creation/replacement work. State the selected material, spatial and motion approach; Section 3 offers examples, not a mandatory random template.
2. **[SCAFFOLD]** Establish content hierarchy, surface/light relationships, responsive spacing and typography appropriate to the chosen direction.
3. **[ARCHITECT]** Apply Double-Bezel to selected focal surfaces only when it supports the chosen aesthetic; reuse the project's existing component structure for other cards, inputs and grids.
4. **[CHOREOGRAPH]** Implement selected behaviors and their triggers, interruption and final states. Use only effects that support the concept and retain usable static/reduced-motion paths.
5. **[OUTPUT]** Deliver code in the project's actual stack; verify dependencies before imports and retain necessary progressive enhancement. Exercise normal motion, keyboard/touch behavior, interruption and reduced-motion states in a real browser; report unavailable checks honestly.

## 8. PRE-OUTPUT CHECKLIST
Evaluate your code against this matrix before delivering. This is the last filter.
- [ ] Typography, icons, edges, layout and timing support the selected direction and the existing system; no assumed font/library dependency
- [ ] Material, space and motion choices are deliberate; Section 3 examples were adapted or rejected as appropriate
- [ ] Selected Double-Bezel surfaces justify their extra wrapper; other surfaces follow the brief without decorative nesting
- [ ] Controls have clear meaning, usable targets and coherent feedback; optional icon enclosures do not create nested interactive elements
- [ ] Responsive spacing supports grouping and reading rhythm without a minimum padding quota
- [ ] Timing/easing fit the behavior; only intended properties transition, and direct feedback is not needlessly delayed
- [ ] Motion serves the chosen brief; static or reduced-motion views keep content visible at rest
- [ ] Layout adapts at content-appropriate breakpoints and preserves reading, focus and touch paths
- [ ] Frequent motion favors low-cost properties; other required effects are bounded and actually checked for performance
- [ ] Blur/texture layers are scoped to the chosen surface and tested for cost, legibility and interaction
- [ ] The result fulfills the content/concept commitments and has normal-motion browser evidence, not only a static screenshot or an unsupported quality label
