---
name: planting-research-seeds
description: "Creates a new research seed in the Seeds directory. Use when a question or opportunity needs to be formally tracked as a research initiative. Generates seed.md with full metadata, a pre-filled starter research plan, and the standard phase subfolder structure. Triggers: plant a seed, new seed, create seed, new research question, track research opportunity, we should research, open a new experiment, research opportunity identified, I have a question about users."
author: "Juan Reina (they/them)"
license: "Valtech / John Deere — Internal Use Only"
last_updated: 2026-02-28
---

# Planting Research Seeds

> Apply `CORE.md` epistemic framework. Upstream handoff: seed briefs from `querying-research-knowledge` are valid inputs to this skill.

**Input**: A seed brief from `querying-research-knowledge`, or a direct description of a question or opportunity.
**Output**: A complete seed directory at `Seeds/[Seed Name]/` with `seed.md`, starter research plan, and empty phase folders ready for use.

---

## Step 1 — Gather Required Information

Collect all fields before writing any files. If a required field is missing, ask for it explicitly — do not invent values or fill with placeholders.

### Required

| Field | Description | Constraints |
|-------|-------------|-------------|
| **Seed Name** | Short, descriptive name for the seed | ≤ 64 characters; natural language with spaces (e.g., "Notification Preferences Study") |
| **Original Question** | The question or observation that triggered this seed | Stated neutrally, assumption-free — no "why do users prefer X" framing |
| **Planted By** | Name of the person planting the seed | |
| **Seed Type** | Category — see taxonomy below | |
| **Potential Impact** | What could change if this seed grows | Which product, design, or user decisions this would inform |
| **Success Recognition** | What "harvest" looks like | How will we know research is complete and findings are actionable? |

### Optional (ask if context suggests they are available)

| Field | Description |
|-------|-------------|
| **Timeline** | Urgency or rough target (e.g., "Q2 2026", "Before next sprint", "No urgency") |
| **Related Seeds** | Seed IDs of existing seeds this one connects to |
| **Related Research** | External references, prior studies, or artifacts relevant to this question |
| **Stakeholders** | Who has a stake in this question being answered |
| **Notes** | Additional context, constraints, or hypotheses to track |

### Seed Type Taxonomy

| Type | Use when |
|------|----|
| **Research Direction** | An open question about users, behaviors, or mental models — generative |
| **Feature Concept** | A design idea that needs validation before building |
| **Usability Finding** | A specific friction observed that warrants deeper study |
| **User Request** | Something participants or stakeholders directly asked for |
| **Tech Exploration** | A technical approach that needs user or feasibility research |
| **Business Opportunity** | A market or strategic hypothesis needing evidence |
| **Competitive Intelligence** | Understanding how others solve a related problem |
| **Desk Research** | Secondary research on an existing topic without primary data collection |

---

## Step 2 — Validate and Generate Identifiers

Before creating any files:

1. **Validate seed name** — Must be ≤ 64 characters. Must be unique within `Seeds/`. If it conflicts with an existing seed or is too long, propose an alternative and confirm before proceeding.

2. **Generate `seed_id`** — Format: `seed_` + 2–4 uppercase letter abbreviation from the seed name.
   - Examples: "Notification Preferences Study" → `seed_NPS`; "Admin Workflow Exploration" → `seed_AWE`
   - Read existing `Seeds/*/seed.md` frontmatter to check for ID collisions. If collision, append a number (e.g., `seed_NPS2`).

3. **Confirm both** with the person before creating files.

---

## Step 3 — Create All Files

Create the following five files. Use `TEMPLATES.md` for the exact structure of each.

```
Seeds/[Seed Name]/
├── seed.md                    ← Full metadata document
├── 01_Plan/
│   └── Research_Plan.md       ← Pre-filled starter plan
├── 02_Sessions/
│   └── README.md              ← Folder purpose guide
├── 03_Synthesis/
│   └── README.md              ← Folder purpose guide
└── 04_Evaluation/
    └── README.md              ← Folder purpose guide
```

Read `TEMPLATES.md` for the exact content templates for each file. Fill every bracketed placeholder with the values collected in Step 1.

---

## Step 4 — Confirm Creation

After all files are written, output this confirmation:

```
✓ SEED PLANTED
══════════════════════════════════════════════
Seed Name:    [name]
Seed ID:      [id]
Seed Type:    [type]
Planted By:   [name]
Date:         [YYYY-MM-DD]
Maturity:     🌱 Planted

FILES CREATED:
  Seeds/[Name]/seed.md
  Seeds/[Name]/01_Plan/Research_Plan.md
  Seeds/[Name]/02_Sessions/README.md
  Seeds/[Name]/03_Synthesis/README.md
  Seeds/[Name]/04_Evaluation/README.md

NEXT STEPS:
  1. Refine the research plan at 01_Plan/Research_Plan.md
  2. Use discussion-guide skill to write a session script when ready to collect
  3. Use querying-research-knowledge skill to check whether related seeds have partial evidence
══════════════════════════════════════════════
```

---

## Maturity Levels

Use these consistently in the `maturity` field and the Maturity Log in `seed.md`:

| Level | Emoji | Meaning |
|-------|-------|---------|
| Planted | 🌱 | Question formulated; seed created; no research designed yet |
| Planning | 🌿 | Research design in progress; plan being written |
| Growing | 🌾 | Active data collection; sessions in progress |
| Synthesizing | 🍃 | Sessions complete; analysis and synthesis in progress |
| Harvested | 🌻 | Findings complete and incorporated into design or product decisions |
| Dormant | 🌰 | Paused; not actively worked; may resume |

Update `maturity` and the Maturity Log each time the seed advances.

---

## Quality Gates

✓ Seed name ≤ 64 characters and unique within `Seeds/`
✓ Seed ID unique — checked against all existing `seed.md` files
✓ Original question stated neutrally — no embedded assumptions
✓ All 5 files created and confirmed
✓ No placeholder values left unfilled in `seed.md`
✓ Confirmation report output with next steps

---

## References

- `TEMPLATES.md` — Exact file templates for `seed.md`, `Research_Plan.md`, and folder READMEs
- `CORE.md` — Epistemic framework (required)
- `PIPELINE.md` — Research lifecycle context
- `querying-research-knowledge/SKILL.md` — Upstream: seed briefs from unanswered questions
- `discussion-guide/SKILL.md` — Downstream: write the session script once planning begins
