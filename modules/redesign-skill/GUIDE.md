---
name: redesign-existing-projects
description: Audit and improve an existing website or app while preserving its functionality, real content, brand assets and technology stack. Use for targeted visual redesigns or a requested design audit; a new marketing-page concept uses the relevant design workflow.
---

> 绘枢模块：已有站点或应用的审计与改造；现有品牌、真实数据、技术栈和功能优先。视觉建议是诊断选项，不自动扩写功能。 先遵循[单入口](../../SKILL.md)和[兼容与工具规则](../../references/compatibility.md)。下列保留的旧 frontmatter 仅作来源元数据；旧名字按包内模式文字口令解释，不注册独立技能。

# Redesign Skill

## How This Works

When applied to an existing project, follow this sequence:

1. **Scan** — Read the codebase. Identify the framework, styling method (Tailwind, vanilla CSS, styled-components, etc.), and current design patterns. Record the routes, forms, data, behavior and existing brand assets that must survive. When a browser is available, capture the unchanged page at representative desktop and phone widths before editing.
2. **Diagnose** — Use the audit below to identify observed problems relevant to the task. A common font, layout or component is not a defect by itself; record the actual readability, hierarchy, interaction or concept issue before changing it.
3. **Fix** — For preserve/extend work, apply targeted upgrades within the existing system. For an explicitly authorized full rebuild, follow the entry's direction-formation workflow and replace layouts/components as needed while preserving the required content, behavior, assets and stack. An existing page is not an approved visual reference merely because it exists.
4. **Verify** — Compare before and after at the same widths; check the links, forms, validation, menus and keyboard paths that worked before. For changed motion, actually trigger and observe its timing, interruption and final state in a normal browser, separately from reduced-motion checks. Report observed changes and regressions; unavailable checks remain unverified.

## Design Audit

### Typography

Check whether these patterns cause a real problem, then use the applicable remedy:

- **Typography without a clear role.** Check hierarchy, glyph coverage, readability and brand fit. Keep a working brand/system font, including Inter. A different sans or a serif/sans pairing is an option when it improves the selected direction; verify availability and language coverage first.
- **Headlines lack hierarchy.** Adjust size, weight, tracking, contrast or placement according to the content and direction. Large, heavy display type is one possible solution, not a required outcome.
- **Body text too wide.** Limit paragraph width to roughly 65 characters. Increase line-height for readability.
- **Weight does not clarify hierarchy.** Use the available weights needed by the content; two weights can be sufficient. Verify that requested intermediate weights exist before relying on them.
- **Numbers in proportional font.** Use a monospace font or enable tabular figures (`font-variant-numeric: tabular-nums`) for data-heavy interfaces.
- **Missing letter-spacing adjustments.** Use negative tracking for large headers, positive tracking for small caps or labels.
- **All-caps subheaders everywhere.** Try lowercase italics, sentence case, or small-caps instead.
- **Orphaned words.** Single words sitting alone on the last line. Fix with `text-wrap: balance` or `text-wrap: pretty`.

### Color and Surfaces

- **Dark surfaces obscure hierarchy.** Tune contrast and surface separation. Pure black, tinted darks and off-black are all valid when appropriate to the chosen medium and display.
- **Accents overwhelm content or fail contrast.** Tune their area, value and saturation to the chosen palette; there is no universal saturation ceiling.
- **Color roles are unclear.** Give accents consistent semantic or compositional roles. Multiple accents are valid when their hierarchy is deliberate and legible.
- **Neutral temperatures clash unintentionally.** Coordinate warm/cool surfaces with imagery and lighting; deliberate temperature contrast can create depth.
- **A gradient substitutes for a concept.** Check its relation to brand, content and light. Keep purple/blue or any other palette when it is justified; changing everything to neutral plus one accent is not a universal remedy.
- **Generic `box-shadow`.** Tint shadows to match the background hue. Use colored shadows (e.g., dark blue shadow on a blue background) instead of pure black at low opacity.
- **Surface treatment does not fit the concept.** Consider flat color, texture, material or imagery intentionally. Flat design is complete when it supports the content; texture is not a completion requirement.
- **Gradient form has no purpose.** Choose linear, radial, mesh or no gradient based on the intended light, material and hierarchy; do not add noise solely to avoid a common pattern.
- **Inconsistent lighting direction.** Audit all shadows to ensure they suggest a single, consistent light source.
- **Section contrast has no narrative or functional role.** Check transitions, readability and shared tokens. Light/dark chapters may coexist when their change intentionally signals content, medium or emphasis; do not force a uniformly light or dark page.
- **A section lacks a clear focal point.** Reconsider content hierarchy, spacing, imagery or depth. Plain text on a plain surface can be intentional. Prefer relevant real assets; a seeded random-photo URL does not guarantee subject matter and must not substitute for a missing real asset.

### Layout

- **Alignment obscures hierarchy or repeats without purpose.** Centered/symmetrical, offset and mixed-aspect compositions are all options; choose from the content and selected direction.
- **Card structure does not match the content.** Keep equal columns for comparable items; consider a zig-zag, asymmetric grid, horizontal scroll or masonry when order, emphasis and device behavior justify it.
- **Using `height: 100vh` for full-screen sections.** Replace with `min-height: 100dvh` to prevent layout jumping on mobile browsers (iOS Safari viewport bug).
- **Complex flexbox percentage math.** Replace with CSS Grid for reliable multi-column structures.
- **Unbounded reading width.** Constrain text and controls where needed for readability; full-bleed media and deliberate edge-to-edge compositions can remain. Choose widths from the content rather than a universal container size.
- **Card heights create empty space or disrupt comparison.** Choose aligned heights or variable heights based on item relationships; preserve a logical reading order if using masonry.
- **Corner treatment is inconsistent with nesting or the design system.** Reuse coherent tokens; adjust nested radii when needed for concentric edges. Uniform radii are valid for a deliberately flat system.
- **Spatial hierarchy is unclear.** Flat adjacency, overlap and depth are possible solutions. Use layering only when it clarifies the selected concept and keeps text, focus and touch targets unobstructed.
- **Symmetrical vertical padding.** Top and bottom padding are always identical. Adjust optically — bottom padding often needs to be slightly larger.
- **Dashboard always has a left sidebar.** Try top navigation, a floating command menu, or a collapsible panel instead.
- **Spacing hurts scanning or emphasis.** Tune density to content, task and viewport. Marketing pages may also be intentionally dense; doubling spacing is not an automatic fix.
- **Buttons not bottom-aligned in card groups.** When cards have different content lengths, CTAs end up at random heights. Pin buttons to the bottom of each card so they form a clean horizontal line regardless of content above.
- **Feature lists starting at different vertical positions.** In pricing tables or comparison cards, the list of features should start at the same Y position across all columns. Use consistent spacing above the list or fixed-height title/price blocks.
- **Inconsistent vertical rhythm in side-by-side elements.** When placing cards, columns, or panels next to each other, align shared elements (titles, descriptions, prices, buttons) across all items. Misaligned baselines make the layout look broken.
- **Mathematical alignment that looks optically wrong.** Centering by the math doesn't always look centered to the eye. Icons next to text, play buttons in circles, or text in buttons often need 1-2px optical adjustments to feel right.

### Interactivity and States

- **No hover states on buttons.** Add background shift, slight scale, or translate on hover.
- **No active/pressed feedback.** Add a subtle `scale(0.98)` or `translateY(1px)` on press to simulate a physical click.
- **Feedback is missing or poorly timed.** Use immediate state changes or a suitable transition according to the action. Do not delay essential feedback; honor static and reduced-motion requirements.
- **Missing focus ring.** Ensure visible focus indicators for keyboard navigation. This is an accessibility requirement, not optional.
- **Waiting has no useful feedback.** For real asynchronous operations, choose a progress indicator, spinner or skeleton appropriate to known duration and layout; do not add fictitious loading.
- **No empty states.** An empty dashboard showing nothing is a missed opportunity. Design a composed "getting started" view.
- **No error states.** Add clear, inline error messages for forms. Do not use `window.alert()`.
- **Dead links.** Buttons that link to `#`. Either link to real destinations or visually disable them.
- **No indication of current page in navigation.** Style the active nav link differently so users know where they are.
- **Anchor navigation loses orientation.** Choose immediate or smooth scrolling for the task; preserve focus and use immediate movement for reduced-motion/static requirements.
- **Animations using `top`, `left`, `width`, `height`.** Switch to `transform` and `opacity` for GPU-accelerated, smooth animation.

### Content

Preserve real names, dates, metrics, prices, testimonials and contact details. The sample-content suggestions below apply only to explicitly labeled prototype data. Do not invent evidence or change real data for visual variety.

- **Generic names like "John Doe" or "Jane Smith".** Use diverse, realistic-sounding names.
- **Fake round numbers like `99.99%`, `50%`, `$100.00`.** Use organic, messy data: `47.2%`, `$99.00`, `+1 (312) 847-1928`.
- **Placeholder company names like "Acme Corp", "Nexus", "SmartFlow".** Invent contextual, believable brand names.
- **AI copywriting cliches.** Never use "Elevate", "Seamless", "Unleash", "Next-Gen", "Game-changer", "Delve", "Tapestry", or "In the world of...". Write plain, specific language.
- **Exclamation marks in success messages.** Remove them. Be confident, not loud.
- **"Oops!" error messages.** Be direct: "Connection failed. Please try again."
- **Passive voice.** Use active voice: "We couldn't save your changes" instead of "Mistakes were made."
- **Publication dates:** Preserve real dates. Varied dates are appropriate only in clearly labeled sample content; do not randomize a real site's history.
- **Same avatar image for multiple users.** Use unique assets for every distinct person.
- **Lorem Ipsum.** Never use placeholder latin text. Write real draft copy.
- **Title Case On Every Header.** Use sentence case instead.

### Component Patterns

- **Card treatment lacks purpose.** Use grouping, containment, borders, color or elevation according to item relationships and the selected material. A white card with a border/shadow is valid when it clarifies the interface; cards need not imply elevation.
- **Always one filled button + one ghost button.** Add text links or tertiary styles to reduce visual noise.
- **Pill-shaped "New" and "Beta" badges.** Try square badges, flags, or plain text labels.
- **FAQ disclosure hides needed answers.** Check scan/find behavior and keyboard support; keep a working accordion or choose a list/search/inline disclosure when it improves the actual journey.
- **Testimonials are hard to read or navigate.** Keep authentic content and choose a static list, usable carousel or other composition based on quantity, reading order and supported controls.
- **Pricing table with 3 towers.** Highlight the recommended tier with color and emphasis, not just extra height.
- **Modals for everything.** Use inline editing, slide-over panels, or expandable sections instead of popups for simple actions.
- **Avatar circles exclusively.** Try squircles or rounded squares for a less generic look.
- **Theme control is unclear.** If the site supports themes, make state and labels understandable; a sun/moon switch, dropdown or settings control can all work. Do not add theme support solely for visual variety.
- **Footer link farm with 4 columns.** Simplify. Focus on main navigational paths and legally required links.

### Iconography

- **Icons lack consistency or clear meaning.** Prefer the project's existing icon set, including Lucide/Feather, when suitable. Change libraries only for a justified visual/semantic gap and verify dependencies.
- **Rocketship for "Launch", shield for "Security".** Replace cliche metaphors with less obvious icons (bolt, fingerprint, spark, vault).
- **Inconsistent stroke widths across icons.** Audit all icons and standardize to one stroke weight.
- **Missing favicon.** Always include a branded favicon.
- **Stock "diverse team" photos.** Use real team photos, candid shots, or a consistent illustration style instead of uncanny stock imagery.

### Code Quality

- **Div soup.** Use semantic HTML: `<nav>`, `<main>`, `<article>`, `<aside>`, `<section>`.
- **Styling ownership is unclear.** Follow the project's styling system; inline values for dynamic state or framework integration may be appropriate. Avoid unnecessary rewrites just to enforce one styling form.
- **Hardcoded pixel widths.** Use relative units (`%`, `rem`, `em`, `max-width`) for flexible layouts.
- **Missing alt text on images.** Describe image content for screen readers. Never leave `alt=""` or `alt="image"` on meaningful images.
- **Arbitrary z-index values like `9999`.** Establish a clean z-index scale in the theme/variables.
- **Commented-out dead code.** Remove all debug artifacts before shipping.
- **Import hallucinations.** Check that every import actually exists in `package.json` or the project dependencies.
- **Missing meta tags.** Add proper `<title>`, `description`, `og:image`, and social sharing meta tags.

### Strategic Omissions (What AI Typically Forgets)

- **Required policy information is missing.** If applicable to the actual service, link existing/approved policies; do not fabricate legal pages or add dead links just to fill a footer.
- **No "back" navigation.** Dead ends in user flows. Every page needs a way back.
- **No custom 404 page.** Design a helpful, branded "page not found" experience.
- **No form validation.** Add client-side validation for emails, required fields, and format checks.
- **No "skip to content" link.** Essential for keyboard users. Add a hidden skip-link.
- **No cookie consent.** If required by jurisdiction, add a compliant consent banner.

## Upgrade Techniques

When upgrading a project, pull from these high-impact techniques to replace generic patterns:

### Typography Upgrades
- **Variable font animation.** Interpolate weight or width on scroll or hover for text that feels alive.
- **Outlined-to-fill transitions.** Text starts as a stroke outline and fills with color on scroll entry or interaction.
- **Text mask reveals.** Large typography acting as a window to video or animated imagery behind it.

### Layout Upgrades
- **Broken grid / asymmetry.** Elements that deliberately ignore column structure — overlapping, bleeding off-screen, or offset with calculated randomness.
- **Whitespace maximization.** Aggressive use of negative space to force focus on a single element.
- **Parallax card stacks.** Sections that stick and physically stack over each other during scroll.
- **Split-screen scroll.** Two halves of the screen sliding in opposite directions.

### Motion Upgrades
- **Smooth scroll with inertia.** Consider only when the chosen spatial concept needs it and native scrolling is insufficient. Preserve keyboard, touch, anchor, focus and reduced-motion behavior; do not replace native scrolling for an incidental polish task.
- **Staggered entry.** Where sequence clarifies the story, reveal selected groups with short delays. Essential content remains visible if setup fails, and static/reduced-motion paths show the final state.
- **Spring physics.** Use springs when elastic physical response fits the chosen material; linear or other easing can suit progress, precise mechanisms and direct feedback.
- **Scroll-driven reveals.** Content entering through expanding masks, wipes, or draw-on SVG paths tied to scroll progress.

### Surface Upgrades
- **True glassmorphism.** Go beyond `backdrop-filter: blur`. Add a 1px inner border and a subtle inner shadow to simulate edge refraction.
- **Spotlight borders.** Card borders that illuminate dynamically under the cursor.
- **Grain and noise overlays.** A fixed, pointer-events-none overlay with subtle noise to break digital flatness.
- **Colored, tinted shadows.** Shadows that carry the hue of the background rather than using generic black.

## Fix Priority

Prioritize observed task/reading/interaction failures first, then the chosen concept. The following are options, not an automatic font-first sequence:

1. **Typography fit** — fix hierarchy, wrapping or glyph coverage; swap fonts only when needed
2. **Color palette cleanup** — remove clashing or oversaturated colors
3. **Hover and active states** — makes the interface feel alive
4. **Layout and spacing** — proper grid, max-width, consistent padding
5. **Replace generic components** — swap cliche patterns for modern alternatives
6. **Add loading, empty, and error states** — makes it feel finished
7. **Polish typography scale and spacing** — the premium final touch

## Rules

- Work with the existing tech stack. Do not migrate frameworks or styling libraries.
- Do not break required functionality. Run the relevant checks after a coherent change; test changed motion in the browser and report missing evidence.
- Before importing any new library, check the project's dependency file first.
- If the project uses Tailwind, check the version (v3 vs v4) before modifying config.
- If the project has no framework, use vanilla CSS.
- Keep changes reviewable and focused on the authorized scope. Prefer targeted edits for preserve/extend; an authorized replace may rebuild the layout and interaction architecture.
