# Storybook Documentation — Reference

## Full MDX Template

Copy and adapt per component. Replace `ComponentName` and all placeholder content.

```mdx
import { Meta, Canvas, ArgsTable } from '@storybook/blocks';
import { ComponentName } from './ComponentName';

<Meta title="[ProductName] / Section / ComponentName" component={ComponentName} />

# ComponentName

## Intent

Why this component exists. What signal it carries in the system.
Not what it renders — what it *means*.

---

## Concept Mapping

| Dimension | Value |
|-----------|-------|
| **Entity** | The domain object this represents (e.g., Record, Asset, Event) |
| **Lifecycle Stage** | Where in its lifecycle this view applies (e.g., Discovery, Active, Deprecated) |
| **System Role** | What function this serves (e.g., Synthesis Output, Navigation Entry, Status Signal) |

---

## Anatomy

- **Element A** — purpose and behavior
- **Element B** — purpose and behavior
- **Element C** — conditional; only renders when [condition]

---

## Variants

| Variant | When Used |
|---------|-----------|
| Default | Standard rendering with complete data |
| Compact | Space-constrained contexts (list view, sidebar) |
| Expanded | Detail view with full metadata |
| Loading | Data pending; shows skeleton |
| Empty | No data available; shows fallback message |

<Canvas of={ComponentNameStories.Default} />

---

## Behavior

| Interaction | Response |
|-------------|----------|
| Hover | Reveals additional metadata / action affordances |
| Click | Navigates to entity profile or expands detail |
| Focus | Keyboard-accessible outline; same affordances as hover |
| Empty state | Displays "[Meaningful fallback message]" |
| Error state | Displays error message with recovery suggestion |

---

## Data Contract

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `title` | `string` | Yes | Primary display text |
| `status` | `StatusId` | Yes | Current lifecycle status |
| `category` | `AssetCategory` | Yes | Asset taxonomy classification |
| ... | ... | ... | ... |

<ArgsTable of={ComponentName} />

---

## Content Guidelines

**Do**
- "Rising Friction — Checkout Flow" (signal-based title)
- "A Pattern Taking Shape" (interpretive, evidence-grounded)

**Don't**
- "Feedback Analyzer Tool" (implementation label)
- "Customer Data Processor" (system-internal naming)

---

## Usage

**Use when:**
- [Primary use case]
- [Secondary use case]

**Avoid when:**
- [Anti-pattern]
- [Wrong context]

---

## Edge Cases

| Risk | What breaks |
|------|-------------|
| Missing lineage | Trust — user can't verify where data came from |
| Title overflow | Layout — long titles push metadata off-screen |
| Stale status | Meaning — status doesn't reflect current reality |
| Too many tags | Clarity — scanning cost exceeds information value |

---

## Evolution

Describe how the entity this component represents changes over time:

```
[Stage 1] → [Stage 2] → [Stage 3] → [Stage N]
```

Status transitions are driven by: [evidence volume, governance decisions, attestation, etc.]

---

## System Role

This component participates in the following flows:

- **[Flow A]** → [what it contributes]
- **[Flow B]** → [what it contributes]

---

## Lineage

**Derived from:**
- `UpstreamComponentA` — [what it provides]
- `UpstreamComponentB` — [what it provides]

**Feeds into:**
- `DownstreamComponentA` — [what it consumes]
- `DownstreamComponentB` — [what it consumes]
```

---

## Full Story Template

```tsx
import type { Meta, StoryObj } from '@storybook/react';
import { ComponentName } from './ComponentName';

const meta: Meta<typeof ComponentName> = {
  title: '[ProductName] / Section / ComponentName',
  component: ComponentName,
  parameters: {
    layout: 'centered',
    docs: { description: { component: 'One-line intent statement.' } },
  },
  tags: ['autodocs'],
};

export default meta;
type Story = StoryObj<typeof ComponentName>;

// ── Core States ──────────────────────────────────────────────

export const Default: Story = {
  args: {
    title: 'Typical Entity',
    status: 'active',
    // ... complete happy-path props
  },
};

export const Loading: Story = {
  args: {
    isLoading: true,
  },
};

export const Empty: Story = {
  args: {
    title: 'No data available',
    // ... minimal props to trigger empty state
  },
};

// ── Interaction States ───────────────────────────────────────

export const AllStates: Story = {
  render: () => (
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: 16 }}>
      <ComponentName {...Default.args} />
      {/* Hovered, Focused, Pressed, Disabled variants */}
    </div>
  ),
};

// ── Lifecycle States (entity components only) ────────────────

export const LifecyclePipeline: Story = {
  render: () => (
    <div style={{ display: 'flex', gap: 16, flexWrap: 'wrap' }}>
      {/* One card per lifecycle stage */}
    </div>
  ),
};

// ── Edge Cases ───────────────────────────────────────────────

export const LongTitle: Story = {
  args: {
    ...Default.args,
    title: 'An Extremely Long Title That Exceeds Any Reasonable Card Width and Tests Truncation Behavior',
  },
};

export const MissingOptionalFields: Story = {
  args: {
    title: 'Minimal Data',
    status: 'discovered',
    // omit all optional props
  },
};
```

---

## Worked Example: EntityCard

This is how a typical `EntityCard` component maps to the 10 sections:

| Section | EntityCard Implementation |
|---------|--------------------------|
| **Intent** | Primary discovery surface for domain entities. Communicates identity, status, and actionability at a glance. |
| **Concept Mapping** | Entity: Any domain record. Stage: All lifecycle stages. Role: Navigation entry + status signal. |
| **Anatomy** | Icon (entity type), Title, Description, Type Chip, Status Chip (conditional), Checkbox (admin), Action Buttons (bookmark, more). |
| **Variants** | Default, Hovered, Focused, Pressed, Disabled; plus per-entity-type variants based on your domain model. |
| **Behavior** | Hover → elevation + action reveal. Click → profile navigation. Checkbox → batch operations (admin only). |
| **Data Contract** | `EntityCardProps` from `EntityCard.types.ts` — title, description, statusId, entityCategory, etc. |
| **Content Guidelines** | Titles are entity names (proper nouns). Descriptions are 1–2 sentences max. No marketing language. |
| **Usage** | Use in catalog grids, search results, related entity lists. Avoid in dashboards (use summary widgets). |
| **Edge Cases** | Description overflow → 2-line clamp. Missing status → no chip shown. Too many actions → overflow menu. |
| **Evolution** | Entity lifecycle: Discovered → In Review → Active → (Deprecated / Retired). Adapt stages to your domain. |

---

## MDX Helper Components

If your project defines shared MDX helpers, use them in your docs. Common patterns:

| Helper | Usage |
|--------|-------|
| `<Note>` | Callout for design notes |
| `<Callout color="...">` | Colored callout for warnings or emphasis |
| `<Evidence id="..." quote="..." source="..." />` | Research evidence citation |
| `<DosDonts dos={[...]} donts={[...]} />` | Content guideline table |

Extract helpers into a shared MDX file and import from there rather than inlining.

---

## Checklist Before PR

- [ ] `.docs.mdx` has all 10 sections filled
- [ ] `.stories.tsx` has Default, Loading, Empty stories minimum
- [ ] Entity components have System Role and Lineage sections
- [ ] `npx tsc --noEmit` passes
- [ ] Storybook renders without console errors
- [ ] No explicit `import React from 'react'` in MDX files
- [ ] Storybook title uses `[ProductName] / ...` hierarchy
