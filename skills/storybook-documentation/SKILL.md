---
name: storybook-documentation
description: "Generates structured Storybook documentation for UI components — MDX docs, stories, and system-level metadata. Produces intent-driven documentation that encodes data contracts, lifecycle evolution, lineage, and behavioral states, not just props and visuals. Triggers: document component, storybook docs, component documentation, MDX docs, write stories, component contract, design system docs, describe component."
author: "Juan Reina (they/them)"
license: "MIT"
last_updated: 2026-04-09
---

# Storybook Documentation

> Apply `CORE.md` epistemic framework before documenting. See `PIPELINE.md` for upstream/downstream handoffs.

**Input**: A component (`.tsx`), its types (`.types.ts`), and the asset/entity context it represents.
**Output**: Three files — `*.docs.mdx` (structured documentation), `*.stories.tsx` (state stories), and updated barrel export (`index.ts`).

---

## Why This Exists

If a component isn't documented in Storybook, it dies in Figma.
This skill treats documentation as a **contract between design, research, and engineering** — not a reference page.

A component library shows props, variants, visuals.
A **system** shows intent, data contracts, evolution, and relationships.
This skill produces the latter.

---

## Documentation Sections

Every documented component must include **all ten sections**. No skipping.

| # | Section | Purpose |
|---|---------|---------|
| 1 | **Intent** | Why this component exists. What signal it carries. |
| 2 | **Concept Mapping** | Entity, lifecycle stage, and system role it represents. |
| 3 | **Anatomy** | Named sub-elements the component renders. |
| 4 | **Variants** | Named visual/behavioral variations (Default, Compact, Loading, Empty, etc.). |
| 5 | **Behavior** | Interaction states — hover, click, empty, error, loading. |
| 6 | **Data Contract** | Prop table with types, required/optional, and descriptions. |
| 7 | **Content Guidelines** | Do/Don't examples for labels, titles, descriptions. |
| 8 | **Usage** | When to use / when to avoid. |
| 9 | **Edge Cases** | Known limits — overflow, missing data, trust breakdowns. |
| 10 | **Evolution** | How the entity this component represents changes over time. |

### System Layer (required for entity-level components)

Components that represent a **domain entity** (not a generic button or chip) must also include:

| Section | Purpose |
|---------|---------|
| **System Role** | Flows this component participates in (e.g., Evidence → Insight → Decision). |
| **Lineage** | Upstream components it derives from; downstream components it feeds into. |

---

## Workflow

### Phase 1 — Gather Context

1. **Read the component source** — `.tsx` file, understand render logic and conditional branches.
2. **Read the types** — `.types.ts` file, extract all props, enums, and interfaces.
3. **Identify the entity** — What domain concept does this component represent? (e.g., Record, Asset, Model, Issue, Event).
4. **Check for existing docs** — Does an `.mdx` or `.stories.tsx` already exist? If so, this is an update, not a creation.
5. **Check the schema** — If a JSON schema exists for this entity, align the Data Contract section with it.
6. **Check the status registry** — If the component uses lifecycle statuses, reference your project's status token file.

### Phase 2 — Write the MDX Doc

7. **Create `ComponentName.docs.mdx`** — In the same directory as the component.
8. **Fill all 10 sections** — Use the template in `REFERENCE.md`.
9. **Add System Layer sections** if the component represents a domain entity.
10. **Use existing MDX helper components** — `Note`, `Callout`, `Evidence`, `DosDonts` from the project's doc utilities when available.

### Phase 3 — Write the Stories

11. **Create or update `ComponentName.stories.tsx`** — State-driven stories, not just visual demos.
12. **Required stories**: Default, Loading, Empty, Error/Edge state.
13. **Entity stories**: Each lifecycle stage if the component represents an entity with state transitions.
14. **Interaction stories**: Hover, focus, disabled where applicable.

### Phase 4 — Quality Check

15. Run quality gates below before finalizing.

---

## File Structure Convention

```
src/components/ComponentName/
  ComponentName.tsx           ← implementation
  ComponentName.types.ts      ← type definitions
  ComponentName.stories.tsx   ← state stories
  ComponentName.docs.mdx      ← structured documentation
  index.ts                    ← barrel export
```

For entity-level asset stories (lifecycle walkthroughs):

```
src/assets/EntityName/
  EntityName.stories.tsx      ← lifecycle + entity-specific stories
```

---

## Storybook Hierarchy Convention

Use domain-based paths, not generic names. Structure by your product name and feature area:

```
[ProductName] / Cards / [EntityCard]
[ProductName] / Assets / [EntityType]
[ProductName] / Design System / Reference / Asset Types
[ProductName] / Design System / Reference / Lifecycle Statuses
```

Never use: `Card1`, `ComponentX`, `Misc / Thing`.

---

## Story Requirements

Stories document **states of reality**, not just visual snapshots.

### Minimum story set per component

| Story | Purpose |
|-------|---------|
| `Default` | Happy-path rendering with typical data |
| `Loading` | Skeleton / spinner state |
| `Empty` | No data / null state with meaningful fallback message |
| `AllStates` | Grid showing all interaction states (hover, focus, pressed, disabled) |

### Additional for entity components

| Story | Purpose |
|-------|---------|
| `LifecyclePipeline` | Visual walkthrough of all lifecycle stages |
| `EdgeStates` | Overflow, truncation, missing optional fields |
| `WithRelationships` | Shows lineage / parent-child / downstream connections |

---

## MDX Technical Rules

1. **Never `import React from 'react'`** in MDX files — MDX3 with Storybook 8.x auto-injects React. Explicit imports cause `Identifier 'React' has already been declared` errors.
2. Use `import { Meta, Canvas, ArgsTable } from '@storybook/blocks'` for Storybook primitives.
3. Use `<Meta title="..." component={...} />` to link the doc to the component.
4. Use `<Canvas>` to embed live stories.
5. Use `<ArgsTable of={Component} />` to auto-generate the props table from TypeScript types.

---

## Content Guidelines for Docs

### Titles and descriptions

**Do** — write from the entity's perspective:
- "Surfaces emerging signals from distributed feedback"
- "Tracks lifecycle state from discovery through certification"

**Don't** — write implementation-speak:
- "A card component that renders data"
- "Wrapper around MUI Card with custom props"

### Edge Cases section

Every Edge Cases section must answer:
- What breaks trust? (e.g., missing lineage, overstated confidence)
- What breaks layout? (e.g., too many tags, long titles)
- What breaks meaning? (e.g., stale status, ambiguous state)

---

## Quality Gates

✓ All 10 sections present — no skipping
✓ Data Contract matches the component's TypeScript interface exactly
✓ If a JSON schema exists for the entity, Data Contract aligns with schema fields
✓ Stories cover Default, Loading, Empty at minimum
✓ Entity components include System Role and Lineage sections
✓ MDX file does not import React explicitly
✓ Storybook title uses domain hierarchy (`[ProductName] / ...`), not generic names
✓ Content guidelines use entity-voice, not implementation-voice
✓ Edge Cases section addresses trust, layout, and meaning
✓ TypeScript compiles cleanly: `npx tsc --noEmit`
✓ Storybook builds without errors: `npm run storybook`

---

## References

- `REFERENCE.md` — Full MDX template, story template, and worked example
- `CORE.md` — Epistemic framework (load with every invocation)
- `PIPELINE.md` — How this skill connects to the research lifecycle
