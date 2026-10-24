---
name: gpt-taste
description: Design cinematic marketing or portfolio pages when the brief calls for GSAP scroll storytelling, expressive typography, and an Awwwards-style motion treatment. Preserve an existing design system; ordinary UI fixes and static or reduced-motion briefs do not require this preset.
---

> 绘枢模块：仅在选择电影式营销或作品集方向时启用 GSAP/AIDA；明确静态与 reduced-motion 走可读终态。 先遵循[单入口](../../SKILL.md)和[兼容与工具规则](../../references/compatibility.md)。下列保留的旧 frontmatter 仅作来源元数据；旧名字按包内模式文字口令解释，不注册独立技能。

# CORE DIRECTIVE: AWWWARDS-LEVEL DESIGN ENGINEERING

Use one coherent visual preset for the current brief. The motion and AIDA guidance below applies to this selected cinematic direction, not to every UI task. User references, required content, brand fonts, accessibility and explicit static/no-animation constraints take precedence.
Work as a frontend design engineer responsible for concept and execution. Diagnose accidental wrapping, unplanned grid holes, meaningless labels, unreadable controls and repetitive composition using the actual content; those observations do not ban deliberate multiline type, negative space or chapter identifiers. 

Develop the selected cinematic direction from the actual content, assets and intended experience. Use motion, spacing, typography and media where they support that direction; a preset is not a quota of effects or assets.

DO NOT USE EMOJIS IN YOUR CODE, COMMENTS, OR OUTPUT. Maintain strictly professional formatting.

## 1. CHOOSE A COHERENT DIRECTION
Choose a layout from the brief and the available assets. If sampling alternatives is useful, actually run a seeded Python selection and record its real output; otherwise make an intentional design choice and label it as such. Never simulate tool execution or present invented RNG output as evidence. Possible choices:
- An opening composition appropriate to the content; Section 3 offers examples rather than a closed catalog
- An available typography system with suitable language coverage; retain a supplied brand font
- Components and motion patterns needed by the story, from Sections 5–6 or the project's existing system, without numerical quotas
Use these choices as a compatible direction, not a reason to override the brief or force new dependencies.

## 2. AIDA STRUCTURE & SPACING
Provide navigation appropriate to the page and user journey. A conventional header, contextual controls, a works index or an immersive opening may all fit; a floating glass navbar is not required.
For a conversion-oriented marketing page, AIDA is a useful default; adapt or omit stages that do not fit the requested content:
- **Attention (Hero):** Cinematic, clean, wide layout.
- **Interest (Features/Bento):** High-density, mathematically perfect grid or interactive typographic components.
- **Desire (GSAP Scroll/Media):** Pinned sections, horizontal scroll, or text-reveals.
- **Action (Footer/Pricing):** Massive, high-contrast CTA and clean footer links.
**SPACING:** Set spacing from reading rhythm, grouping and the supported viewport. Large gaps can distinguish cinematic chapters; close continuity can serve sequences or dense archives. Verify actual scroll length instead of applying a padding quota.

## 3. OPENING COMPOSITION & READABILITY
The opening must establish the content and intended next action. It may be led by media, an index, typography or an interaction; it need not be a conventional hero.
- **Heading Measure:** Set heading width and size using the real text, script and font. Wide display headings are one option; do not sacrifice readability or the chosen composition to force a particular width.
- **Wrapping:** Inspect real wrapping at supported desktop and phone widths. Fix accidental orphaning, clipping and loss of hierarchy; longer intentional headlines or narrow-screen wrapping are not failures merely because they exceed a line count.
- **Hero Layout Options (Selected for the Brief):**
  1. *Cinematic Center:* A centered composition with appropriate type width, media treatment and actions. Use the actions required by the journey; no mandatory pair of CTAs or dark radial wash.
  2. *Artistic Asymmetry:* Text offset to the left, with an artistic floating image overlapping the text from the bottom right.
  3. *Editorial Split:* Text left, image right, but with massive negative space.
- **Button Contrast:** Button labels and states must remain legible against their actual surfaces; verify contrast rather than inferring it solely from a light/dark label.
- **Opening Content:** Avoid arbitrary decoration that obscures the message. Badges, labels and real data may lead when they are meaningful to the task; do not remove necessary information because it occupies the opening.

## 4. GRID COMPOSITION
- **Intentional Grid Occupancy:** Check spans and responsive layouts for accidental holes, clipping and misleading grouping. Deliberate negative space can serve hierarchy. Use `grid-auto-flow: dense` only if its visual reordering preserves a logical DOM, keyboard and reading order; it is not required on every grid.
- **Card Count:** Use as many items as the real content and navigation require. Group, paginate or change the representation when scanning becomes difficult; do not invent or omit items to satisfy a 3–5 card quota.

## 5. ADVANCED GSAP MOTION & HOVER PHYSICS
Use real GSAP/ScrollTrigger when the selected direction needs their choreography and the project supports them; `@gsap/react` applies only to React projects. Verify installed dependencies before imports, reuse existing suitable tools, and use native CSS/JS for simpler transitions. Keep requested static views static; this preset does not authorize a framework migration.
- **Interactive Feedback:** Make actionable items distinguishable and provide suitable pointer, keyboard and touch feedback. Scaling within a clipped container is an option, not a requirement for every card or image.
- **Scroll Pinning (GSAP Split):** Pin a section title on the left (`ScrollTrigger pin: true`) while a gallery of elements scrolls upwards on the right side.
- **Image Scale & Fade Scroll:** If the story calls for a spatial approach or exit, interpolate scale and opacity through a suitable range. Keep essential media visible and avoid hiding content before successful setup; use the static visible state when disabled.
- **Scrubbing Text Reveals:** Use word-by-word emphasis only when sequence is meaningful; preserve readable contrast, selectable text and a visible static path rather than dimming every paragraph by default.
- **Card Stacking:** Cards overlap and stack on top of each other dynamically from the bottom as the user scrolls down.
- **Reduced Motion (mandatory):** Every animation above MUST honor `prefers-reduced-motion: reduce`. Gate ScrollTrigger/GSAP setup behind a reduced-motion check (`gsap.matchMedia()` or `useReducedMotion()`), and under `(prefers-reduced-motion: reduce)` collapse scroll-pinning, scrubbing, image scale/fade, card stacking, and marquees to their static end-state (full opacity, `scale: 1`, no auto-scroll). Motion is the default for this selected cinematic preset, not a requirement for static or reduced-motion briefs.

## 6. COMPONENT ARSENAL & CREATIVITY
Select relevant components from this arsenal for the chosen direction:
- **Inline Typography Images:** Embed small, pill-shaped images directly INSIDE massive headings. Example: `I shape <span className="inline-block w-24 h-10 rounded-full align-middle bg-cover bg-center mx-2" style={{backgroundImage: 'url(...)'}}></span> digital spaces.`
- **Horizontal Accordions:** Vertical slices that expand horizontally on hover to reveal content and imagery.
- **Infinite Marquee (Trusted Partners):** If useful, show real partner marks or meaningful typography using the actual stack/assets. Do not substitute a React icon package for authentic partner evidence; provide pause/static behavior where needed.
- **Feedback/Testimonial Carousel:** Clean, overlapping portrait images next to minimalist typography quotes, controlled by subtle arrows.

## 7. CONTENT & ASSET FIT
- **Labels:** Remove meaningless repeated labels when they add noise. Keep real chapter numbers, navigation names and archive identifiers when they orient the user; wording and visual treatment should fit the content.
- **Image Context & Style:** Prefer relevant real assets and verify their subject matter, rights and crop. A random-photo seed does not provide semantic image search. Apply filters only when they support the selected direction and preserve necessary color/content; label prototype placeholders.
- **Backgrounds:** Choose flat color, material, image, gradient or ambient motion deliberately. The background must support content and the selected lighting system; neither dark overlays nor grain are required.
- **Horizontal Overflow:** Fix the element causing accidental document overflow. Clip decorative layers locally when appropriate; keep intentional horizontal panels operable and do not crop focus indicators, sticky content or controls with a blanket page-level overflow rule.

## 8. DESIGN PLAN AND FINAL CHECKS
Before implementation, briefly state the chosen direction and planned checks. After implementation, perform the relevant rendered-layout and motion checks where tools are available. The items below guide that work; planned checks are not completed measurements:
1. **Direction:** State the selected layout, typography and motion approach briefly. Include RNG output only if it was actually executed.
2. **Story check:** Use the AIDA stages relevant to this marketing brief; do not add sections solely to satisfy the preset.
3. **Hero layout:** Check heading wrapping at the supported viewports with the actual text and font; a max-width class alone does not guarantee a line count.
4. **Grid Verification:** Inspect responsive grouping, spans, intended negative space and reading/focus order; use dense flow only when those checks support it.
5. **Labels & Controls:** Confirm labels carry meaning, actions remain discoverable, and text/focus contrast works on actual surfaces. Trigger selected motion and observe its process, interruption and final state in a normal browser, separately from reduced-motion checks.
Deliver the implementation and actual verification results. Report unavailable checks accurately; a CSS class or an unexecuted plan is not proof of wrapping, contrast or grid behavior.
