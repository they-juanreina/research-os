---
scope: all-skills
author: "Juan Reina (they/them)"
license: "MIT"
---

# Skills Pipeline — Composability Model

Skills compose in research lifecycle order. Each skill's outputs feed downstream skills.

---

## Research Lifecycle

```
PLAN              COLLECT                    SYNTHESIZE                                EVALUATE           REPORT
────────────      ────────────────────       ──────────────────────────────────────    ──────────────────────────────────────────────────────
Discussion   →    Session Note-Taking   →    Thematic Coding   →    Journey Mapping →  Saturation Analysis
Guide                    ↓                          ↓               HMW Extraction     Success Criteria   →  Synthesis Reporting
                    Issue Log ←────────────────────┘──────────────────────────────────→ Tracking
```

## Heuristic Evaluation Track

Heuristic evaluation runs as a parallel track — independent of moderated sessions but
feeding its outputs back into the core lifecycle via Phase 4 (Handoff).

```
EVAL TRACK        PHASE                         CONNECTS TO
──────────        ────────────────────────────  ─────────────────────────────────────────────
Product URL  →    01 Scope & Discovery       →  Discovery Brief
Brief        →    02 Evidence Collection     →  heuristic-findings.json + screenshots
Findings     →    03 Heuristic Synthesis     →  Evaluation Report
Report       →    04 Designer Actions &      →  Action Briefs
                  Research Initiatives          Issue Log   → issue-log skill
                                                HMW list    → hmw-extraction skill
                                                Seed briefs → planting-research-seeds skill
```

---

## Skill Handoffs

| Phase | Skill | Key Outputs | Fed Into |
|-------|-------|-------------|----------|
| Plan | Discussion Guide | session script, topic tracker | Session Note-Taking (session framing) |
| Collect | Session Note-Taking | `observations`, `quotes`, `pain_points`, `timing_data` | Thematic Coding, Issue Log |
| Collect | Issue Log | `issues[]` — ID, severity, role, frequency, effort | Success Criteria Tracking (behavioral evidence) |
| Synthesize | Thematic Coding | `codebook` (themes + definitions), `coded_dataset` (evidence units + codes) | Journey Mapping, HMW Extraction, Saturation Analysis, Issue Log |
| Synthesize | Journey Mapping | `stages[]` — touchpoint, emotion, pain point, opportunity | HMW Extraction (pain points → opportunities) |
| Synthesize | HMW Extraction | `hmw_statements[]` — ID, statement, priority, evidence | Design handoff; ideation input |
| Evaluate | Saturation Analysis | `recommendation` (Continue / Pause / Conclude) | Decision to run more sessions |
| Evaluate | Success Criteria Tracking | `go_no_go`, per-criterion status + confidence | Research completion decision |
| Evaluate | Heuristic Eval — Phase 4 | `action_briefs[]`, `hmw_statements[]`, `issue_entries[]`, `seed_briefs[]` | Design team; issue-log; hmw-extraction; planting-research-seeds |
| Report | Synthesis Reporting | `report-[seed].md` — executive summary, theme narratives, journey arc, opportunity map, limitations, next steps | Stakeholder distribution; design team handoff; follow-up seed planning |

---

## Field Mapping

| From Skill | Output Field | → | To Skill | Input Field |
|------------|-------------|---|----------|-------------|
| Session Note-Taking | `observations[]`, `quotes[]`, `pain_points[]` | → | Thematic Coding | evidence units (raw input) |
| Thematic Coding | `codebook` (themes + definitions) | → | Saturation Analysis | theme list for tracking table |
| Thematic Coding | `coded_dataset` (pain-point themes) | → | HMW Extraction | pain point list with evidence |
| Thematic Coding | `coded_dataset` (behavioral themes) | → | Journey Mapping | raw research data with codes |
| Thematic Coding | `coded_dataset` (friction/blocker themes) | → | Issue Log | session data |
| Session Note-Taking | `observations + pain_points` | → | Issue Log | session data (direct path, when thematic coding is skipped) |
| Session Note-Taking | all session notes (corpus) | → | Saturation Analysis | session corpus |
| Research Plan | success criteria definitions | → | Success Criteria Tracking | criterion list |
| Session Note-Taking | session outcomes | → | Success Criteria Tracking | per-session scores |
| Issue Log | `issues[]` | → | Success Criteria Tracking | behavioral evidence |
| Heuristic Eval Ph4 | `issue_entries[]` | → | Issue Log | heuristic-sourced issue rows |
| Heuristic Eval Ph4 | `hmw_statements[]` | → | HMW Extraction | opportunity statements |
| Heuristic Eval Ph4 | `seed_briefs[]` | → | Planting Research Seeds | new seed from evaluation gap |
| Discussion Guide | topic tracker | → | Session Note-Taking | coverage checklist |
| Thematic Coding | `codebook`, `coded_dataset` | → | Synthesis Reporting | theme narratives + evidence basis |
| Journey Mapping | `stages[]` | → | Synthesis Reporting | experience arc section |
| HMW Extraction | `hmw_statements[]` | → | Synthesis Reporting | opportunities section |
| Issue Log | `issues[]` | → | Synthesis Reporting | severity context for limitations |
| Saturation Analysis | `recommendation` | → | Synthesis Reporting | study scope / limitations framing |
| Success Criteria Tracking | `go_no_go` | → | Synthesis Reporting | study conclusion status |

---

## Invocation Pattern

For any task:

1. **Always load `CORE.md`** — epistemic framework, language policy, and guardrails apply to all skills.
2. **Load the relevant `SKILL.md`** — specific workflow, output format, and quality gates.
3. **Load `REFERENCE.md` only when needed** — edge cases, detailed methodology, pitfall avoidance.
4. **Load `EXAMPLES.md` only for onboarding or format uncertainty** — not needed for routine tasks.

**Minimum viable invocation**: `CORE.md` + `SKILL.md`
**Full invocation**: `CORE.md` + `SKILL.md` + `REFERENCE.md`
**Onboarding / format unclear**: `CORE.md` + `SKILL.md` + `EXAMPLES.md`

---

## Knowledge Gap Loop

When `querying-research-knowledge` returns **Confidence: None**, it emits a seed brief. That brief is the direct input for `planting-research-seeds`, which creates a formal seed. This closes the loop between consuming knowledge and generating new research:

```
Question asked
    ↓
querying-research-knowledge
    ↓ (if Confidence: None)
Seed brief output
    ↓
planting-research-seeds
    ↓
New seed in Seeds/ → follows standard lifecycle → future harvest
```

---

## Concurrent vs. Sequential Skills

Some skills run concurrently after sessions; others gate the next phase:

- **Sequential gate**: Run Saturation Analysis before recruiting more participants. Its `recommendation` field determines whether to continue collecting.
- **Sequential gate**: Success Criteria Tracking's `go_no_go` determines whether research is complete.
- **Sequential prerequisite**: Thematic Coding runs before Journey Mapping and HMW Extraction. Its coded dataset and codebook are the recommended input for those synthesis skills. Journey Mapping and HMW Extraction can run directly from session notes when thematic coding is skipped (faster but less rigorous).
- **Concurrent**: Journey Mapping, HMW Extraction, and Issue Log can all run from the Thematic Coding output simultaneously.
- **Independent**: Discussion Guide runs before sessions; Saturation Analysis and Success Criteria Tracking run after all sessions.
- **Parallel track**: Heuristic Evaluation runs independently of moderated sessions. It can precede sessions (to generate hypotheses), run alongside them, or follow them (to cross-validate findings). Phase 4 outputs re-enter the core lifecycle at Issue Log, HMW Extraction, and Planting Research Seeds.
- **Terminal skill**: Synthesis Reporting runs after all synthesis and evaluation skills are complete. It consumes outputs; it produces nothing for other skills to consume. Its output (`report-[seed].md`) is the lifecycle's external-facing deliverable.
