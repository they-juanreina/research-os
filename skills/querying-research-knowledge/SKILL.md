---
name: querying-research-knowledge
description: "Answers questions about users, workflows, design decisions, and the platform by querying completed research seeds. Returns evidence-grounded summaries with confidence ratings and verbatim citations. Never extrapolates beyond available data. Flags embedded assumptions in the question itself. When a question has no research backing, generates a seed brief for future study instead of guessing. Use when asking what research shows, what users said, what we know about user behavior, pain points, mental models, platform use, or design rationale."
author: "Juan Reina (they/them)"
license: "MIT"
last_updated: 2026-02-28
---

# Querying Research Knowledge

> Apply `CORE.md` epistemic framework throughout. This skill answers **only from evidence**. It does not guess, extrapolate, or fill gaps with inference — even when that would feel more helpful.

**Input**: Any question about users, design, workflows, or the platform.
**Output**: Evidence-grounded summary with confidence rating and citations — or a seed brief if evidence is absent.

---

## Step 1 — Decode the Question

Before searching, examine the question itself:

- **What is actually being asked?** Separate the question from any assumption embedded in it.
- **What does the question presuppose?** Name embedded assumptions explicitly. Example: "Why do users prefer X?" assumes they do — flag that first.
- **What research question(s) does this map to?** Which seeds might have addressed this topic?

If the question contains a strong embedded assumption, state it before answering:

> ⚠️ **Embedded assumption detected**: This question assumes [X]. The research will be searched for evidence that supports or contradicts this assumption — not to confirm it.

---

## Step 2 — Search the Research Corpus

Navigate `Seeds/` and check each seed directory in order:

1. `Seeds/[Seed]/01_Plan/` — Does the research plan include a question that maps to this topic?
2. `Seeds/[Seed]/02_Sessions/` — What do transcripts and session notes say? Look for verbatim quotes and observed behaviors.
3. `Seeds/[Seed]/03_Synthesis/` — What do journey maps, HMW statements, and thematic analyses show?
4. `Seeds/[Seed]/04_Evaluation/` — What do issue logs and success criteria results record?

Search all relevant seeds. Do not stop at the first partial match.

---

## Step 3 — Classify Evidence

For each piece of evidence found, classify by type:

| Type | Definition | Weight |
|------|-----------|--------|
| **Verbatim quote** | Participant said it, word for word | Strongest |
| **Observed behavior** | Researcher recorded it happening during a session | Strong |
| **Coded theme** | Researcher identified a pattern across sessions | Moderate |
| **Researcher note** | Analyst interpretation — may include inference | Weakest; flag clearly |

Discard anything that is pure inference without direct backing. If evidence is researcher-interpreted, label it as such.

---

## Step 4 — Rate Confidence

Assign one confidence level to the overall answer:

| Level | Criteria |
|-------|----------|
| **High** | ≥ 3 independent sessions; consistent evidence; verbatim quotes available |
| **Medium** | 2 sessions or coded themes only; some supporting quotes |
| **Low** | 1 session; observer inference; or indirect evidence only |
| **None** | No evidence in the corpus — question is unanswered by current research |

If evidence exists but contradicts itself across sessions or personas, state that explicitly. Do not resolve the contradiction — surface it.

---

## Step 5 — Formulate the Answer

Structure every response in this format:

```
CONFIDENCE: [High / Medium / Low / None]
SEEDS CONSULTED: [list all seeds checked, not just those with findings]

WHAT THE RESEARCH SHOWS:
[Evidence-grounded summary. Every claim is followed by an inline citation: (Seed, Session ID or Participant ID).]

EVIDENCE:
[Verbatim quotes or behavior descriptions. Format: "[Quote]" — Participant [ID], [Seed], Session [N]]

CONTRADICTIONS AND MINORITY FINDINGS:
[Any evidence that cuts against the main finding. Do not suppress this.]

WHAT WE DON'T KNOW:
[Explicit gaps — aspects of the question the research didn't address. Every gap is named, not papered over.]

EMBEDDED ASSUMPTIONS FLAGGED:
[Any assumption in the original question that the research does not support, contradicts, or simply hasn't tested.]
```

If the question is fully answered with high confidence, all sections still appear. "We don't know" and "Contradictions" sections may be brief but must not be omitted.

---

## Zero-Extrapolation Rule

**Never state or imply what is not directly in the data.**

Prohibited language patterns:
- "Users probably..." / "Users likely..." / "Users tend to..."
- "This suggests that..." (without a direct evidence citation)
- "Based on similar contexts..." / "It's reasonable to assume..."
- "The data implies..." / "One could infer..."
- Generalizing from N=1 without stating it is N=1

Required language patterns:
- "In [Seed], [Participant ID] stated: '[verbatim quote]'"
- "[N] of [total] participants in [Seed] exhibited [specific behavior]"
- "The [Seed] issue log records [N] instances of [specific issue] across [N] sessions"
- "No evidence in the current corpus addresses this aspect of the question"

If the honest answer is "we don't know," that is the answer.

---

## Anti-Bias Protocol

Before returning any answer, run this check:

- **Confirmation check**: Does this answer confirm what the questioner seems to want to hear? If so, re-examine the evidence more critically. Look for contradicting data first.
- **Majority-perspective check**: Does this evidence come only from dominant personas or user types? Flag if so. State which roles and sessions the evidence comes from.
- **Sample-size check**: Is a pattern from a small sample being treated as a general finding? State the exact sample size for every pattern cited.
- **Contradiction suppression check**: Is there any minority finding or edge-case evidence being left out? Include it.

---

## Step 6 — If Confidence is None: Plant a Seed

When no evidence exists for the question, do not guess. Output a seed brief instead:

```
NO RESEARCH EVIDENCE FOUND
════════════════════════════════════════════
The current research corpus does not address: [restate the question neutrally, stripped of assumptions]

PROPOSED SEED BRIEF
────────────────────────────────────────────
Title: [descriptive name — what is being studied - max. 64 characters]
Research Question: [the question, reframed as open-ended and assumption-free]
Why This Matters: [1–2 sentences: what design decision or product understanding this would inform]
Suggested Method: [interview / usability test / diary study / survey / secondary research]
Suggested Participant Criteria: [who would need to be recruited and why]
Related Seeds: [existing seeds whose findings border this question]
────────────────────────────────────────────

Next step: Use the planting-research-seeds skill to open this as a formal research seed.
```

Do not offer a guess alongside the seed brief. The brief is the complete response when evidence is absent.

---

## Quality Gates

Before delivering any answer:

✓ Every claim in the summary has a citation (seed name + session or participant ID)
✓ Confidence level matches evidence quantity and quality — not optimism
✓ Contradictory and minority evidence is surfaced, not suppressed
✓ Gaps explicitly named — no gap is filled with inference
✓ Embedded assumptions in the question identified and named
✓ Sample sizes stated for every pattern cited
✓ Zero use of probabilistic language without quantitative backing ("probably", "likely", "tends to")
✓ All seeds checked, not just the first match

---

## Agent Team (Recommended for Complex Queries)

For questions requiring search across multiple seeds, an agent team can execute the workflow in parallel for significantly faster results. The team splits Steps 2–5 across specialized agents:

| Agent | What it handles | Equivalent SKILL.md steps |
|-------|----------------|--------------------------|
| Orchestrator | Question decoding, dispatching, coordination | Steps 1, 6 (routing) |
| Corpus Searcher (×N) | Searches one seed in parallel with others | Step 2 |
| Evidence Assessor | Classification, confidence, anti-bias checks | Steps 3, 4 |
| Answer Composer | Final structured answer or seed brief | Steps 5, 6 |

**When to use the agent team**: Multi-seed questions, broad queries, any question where sequential searching would be slow.

**When single-agent is fine**: Targeted questions about a specific seed, or quick factual lookups.

Agent team prompts: `agents/TEAM.md` (start here), then `agents/orchestrator.md`, `agents/corpus-searcher.md`, `agents/evidence-assessor.md`, `agents/answer-composer.md`.

---

## References

- `CORE.md` — epistemic framework (load with every invocation)
- `PIPELINE.md` — research lifecycle and seed structure context
- `Seeds/` — the research corpus (navigate directly; do not assume contents)
- `agents/TEAM.md` — agent team overview and orchestration model
- `agents/orchestrator.md` — orchestrator agent prompt
- `agents/corpus-searcher.md` — corpus searcher agent prompt
- `agents/evidence-assessor.md` — evidence assessor agent prompt
- `agents/answer-composer.md` — answer composer agent prompt
