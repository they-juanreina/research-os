---
name: hmw-extraction
description: "Transforms research pain points and findings into prioritized How Might We opportunity statements. Use when converting qualitative research insights, usability findings, or user complaints into actionable design challenges. Produces clustered, evidence-grounded HMW statements with priority scores. Triggers: how might we, HMW, opportunity statements, design opportunities, reframe pain points, ideation input."
author: "Juan Reina (they/them)"
license: "MIT"
last_updated: 2026-03-02
---

# HMW Extraction

> Apply `CORE.md` epistemic framework before extracting. See `PIPELINE.md` for upstream/downstream handoffs.

**Input**: Research findings, pain points, session notes, or usability observations.
**Output**: Clustered, evidence-grounded HMW statements with priority scores.

---

## Template Formula

```
How might we [help/allow/enable/empower/teach]
             [specific user/persona]
          to [goal or benefit]
             [in context / when / with constraints]?
```

**Scope check**: Can this HMW inspire 3–5 diverse design approaches?
- No → too narrow or solution-biased. Broaden.
- Yes → proceed to prioritization.

---

## Workflow

1. **Identify pain points** — Flag moments where users struggle, repeat manual work, abandon workflows, or express frustration (explicit or implicit).

2. **Document workarounds** — How users currently cope: invented solutions, tools strung together, skipped steps. Workarounds signal the barrier's location and severity.

3. **Extract the core barrier** — Ask: *What would need to change for this to stop being a problem?* This is the reframing lever.

4. **Name the user role** — Specific persona, not "users." Example: "project managers coordinating cross-team sprints" not "managers."

5. **Define the benefit** — Success from the user's perspective: save time, reduce cognitive load, increase confidence, enable a new behavior.

6. **Add context** (optional) — Constraints, scenarios, or conditions that matter (e.g., "for organizations with 50+ employees," "in low-connectivity environments").

7. **Cluster and prioritize** — Group HMWs by theme. Score using:

   ```
   Priority = Impact × Urgency
   ```
   Each factor 1–5. Score ≥ 15: High · 8–14: Medium · < 8: Low.

   **Feasibility** is a separate column — a planning input, not a priority filter. A high-impact, low-feasibility opportunity is your most important design challenge, not one to defer. Use the 2×2 matrix in `REFERENCE.md` to decide *when* and *how* to address it after priorities are set.

---

## Output Format

| HMW_ID | Pain Point | Current Workaround | HMW Statement | Personas | Priority | Feasibility | Evidence | Design Implications |
|--------|------------|-------------------|---------------|----------|----------|-------------|----------|---------------------|
| HMW-01 | summary | workaround | statement | list | High/Med/Low | High/Med/Low | quote or observation | 2–3 design prompts |

---

## Quality Gates

✓ Human-centered — focuses on user needs, not technical solutions
✓ Framed as "How might we..." not "Can we build..." or "We should..."
✓ Grounded in evidence — traceable to a quote or specific observation
✓ Scope-appropriate — not "improve UX"; not "add a red button"
✓ Actionable — a team can move from this toward ideation and prototyping

---

## References

- `REFERENCE.md` — formula breakdown, anti-patterns, clustering methodology, prioritization matrix
- `EXAMPLES.md` — five domain-specific examples with evidence linking and design implications
- `scripts/hmw_generator.py` — Python templating utility
