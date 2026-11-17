✦︎✦︎✦︎ Meta Apollo Logos //

# 🖳 OPERATE // SCROLL VIEWPORT AND TRACK OWNERSHIP

> **STATE //** operator-directed contract proposal, pending independent review/merge
> **OWNER //** Syntagma for cross-widget behavior; The-Post-Apollo-Project for QML component and runtime evidence
> **SOURCE //** Finance Market narrow-layout screenshots (2026-11-17); Post-Apollo PR #2019, existing `NeonScrollBar` contract, Finance Budget PR #2016
> **SCOPE //** Post-Apollo scrollable widget panes, indicators, layout policies, and UI acceptance
> **EXCEPTION //** intentional split, fixed and specialized Git/Hospital/CPU++ rails are preserved until individually reviewed

## Rule // one scroll viewport owns one indicator

A scrollbar track spans the **usable edge of the viewport whose content it scrolls**, with only deliberate endpoint clearance. Its **thumb** remains proportional to that viewport's visible fraction of its content. Do not stretch a list scrollbar across an unrelated fixed header, chart or detail panel to make it look longer. Do not let a track stop early **inside its own viewport** because of an arbitrary indicator height.

The owner of a list/detail layout must allocate the list's height first. The track then follows that allocation; it must never independently decide the list's height.

## Layout policy // choose the viewport, not a fake track

For a pane whose content scrolls vertically, an explicit layout policy may be:

- **fill**: the list receives the full available content-body height (the usual preferred default when the operator expects a full-height list). Any independently scrollable details must move to their own view, tab or side panel; provide an accessible return path.
- **split**: list and selected-item details are simultaneous, each receiving an intentionally declared portion. The list track ends at the list viewport, even if it occupies only part of the window.
- **fixed**: the list receives a declared height, clamped within the actual available area. Document why it is fixed and what consumes the remaining area.

An intentionally narrow split viewport is **not** automatically a scrollbar defect. Preserve established split/fixed layouts unless the operator authorizes a change.

## Component geometry // no invisible second positioning authority

Prefer a shared pane/container which owns a `Flickable` and its `NeonScrollBar` as children of the **same stable non-positioning host**. Use that host's live width/height and normal visual family/style. Preserve source-specific star/bar identity, glow and tested hit geometry.

Where a parent `Column`, `Row`, `Grid` or other positioning container must place the viewport, an overlay must not become another positioned child. It must follow **explicit observable** viewport position and size bindings; a computed coordinate function without verified change notifications is not enough.

A shared scroll component may expose a recommended/implicit extent; it must **not** silently resize the outer widget, take ownership of unrelated service data, override the parent layout's choice, or alter existing scroll semantics.

Reserve a visible content gutter beside the track so text, interactive controls and charts do not overlap it. When an entire pane is hidden, its rail must also be hidden and unable to intercept input. When content does not exceed its viewport, default to hiding the indicator rather than inventing scroll capacity.

## Verification // acceptance is layered

A scroll geometry change needs separate evidence for:

1. **Source contract:** correct target, style, mounting owner, declared policy and no unexpected second rail.
2. **Real Qt component runtime:** actual viewport and rail top/bottom/width, thumb position/ratio, resize, changed header heights, mode visibility, short/long content, and non-overlap (within an explicitly documented pixel tolerance).
3. **Target-widget host:** the **real** widget's narrow and wide layouts, list/detail switching, wheel/drag interaction, focus/hit testing, overflow, hidden panes and existing user controls.
4. **Operator native acceptance:** visual evidence in the running Post-Apollo surface, as a separate decision from technical tests and from permission to merge.

A green source or isolated Qt test alone does **not** certify the full target widget's native geometry. Native screenshots and operator corrections are acceptance evidence, not automatic approval to merge or change production.

## Adoption and exceptions

The technical implementation is currently staged in [Post-Apollo PR #2019](https://github.com/kudokudo1/The-Post-Apollo-Project/pull/2019). That source introduces `NeonScrollPaneV2` for the Finance Market trial; it is **not** evidence that every widget already uses the contract. Do not mass-migrate unrelated Git/Hospital, CPU++, Weather, Camera, Publisher or AppControl files under this single task. Coordinate owners and preserve bespoke audited rails.

For each future adoption record: owning widget/room, explicit viewport policy, geometry host, style family, special exceptions, source/Qt/native checks, and the operator's final acceptance.
