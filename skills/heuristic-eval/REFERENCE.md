---
name: heuristic-eval
description: >
  Deep methodology, epistemic considerations, and downstream integration guidance
  for the heuristic-eval skill. Load when encountering edge cases, calibrating severity,
  or integrating findings into the Research OS pipeline.
license: "Valtech / John Deere — Internal Use Only"
metadata:
  author: "Juan Reina (they/them)"
  document_type: reference
  depends_on: CORE.md, SKILL.md
---

# Heuristic Evaluation — Reference

Deep methodology, epistemic considerations, and downstream integration guidance.
Load this file when encountering edge cases, calibrating severity judgment, or
integrating findings into the broader Research OS pipeline.

---

## Methodological Foundation

### What heuristic evaluation is (and is not)

Heuristic evaluation is an **expert inspection method** — a set of trained eyes examining an
interface against established usability principles. It is:

- Fast and low-cost relative to usability testing
- Useful for identifying structural, systemic, and standards-based violations
- Strong at finding *potential* problems before user testing

It is not:

- A measurement of actual user behavior or task success rates
- A representative sample of the diversity of your user population
- A substitute for moderated sessions, especially for complex workflows
- A guarantee that identified issues are the *most important* ones to users

The deep-research-report in this skill folder provides authoritative synthesis of the academic and
practitioner evidence base. Refer to it for literature-grounded defenses of methodology choices.

---

## Applying Plural Epistemology to Heuristic Findings

`CORE.md` requires ≥ 2 interpretations of significant findings. For heuristic evaluation, this
means resisting the reflex to assign a single cause to every violation.

### Example of plural interpretation in practice

**Finding:** The error message on failed file upload reads only "Upload failed."

| Interpretation | Lens | Implication |
|----------------|------|-------------|
| 1. Feedback gap — the system cannot distinguish error types and surfaces a generic fallback | Technical root cause | Fix requires engineering: differentiate error cases (file size, format, server error) |
| 2. Localization constraint — the product supports 12 languages and specific error text was not translated for this locale | Localization root cause | Fix is a content and translation workflow problem, not a UI architecture problem |
| 3. Intentional brevity — early product decision to surface minimal error text based on user research that found verbose errors caused anxiety, but that research is now outdated | Historical decision root cause | Fix requires revisiting earlier research assumptions, not just writing better copy |

The evaluator does not need to determine which interpretation is correct — that is exactly the
work that a research seed would do. Flag the uncertainty explicitly.

### Categories of finding where plural interpretation is mandatory

- Any finding assigned Severity 3 or 4
- Any finding involving language, labels, or terminology (H2)
- Any finding involving accessibility (H6, H8, H10)
- Any finding that involves a pattern across multiple screens (systemic vs. incidental)
- Any finding where the evaluator is uncertain whether the issue reflects the product's design
  intent or a bug

---

## Severity Calibration

Severity ratings in this skill follow the 0–4 NNG scale (see `references/nng-heuristics-guide.md`
for per-heuristic examples). Additional calibration guidance for this context:

### Calibration factors

**Increase severity by 1 when:**
- The affected workflow is a primary, high-frequency task
- The finding disproportionately affects users with assistive technology, lower digital literacy,
  or non-primary language contexts
- The violation blocks task completion entirely (not just creates friction)
- The issue appears across ≥ 3 distinct screens or flows (systemic)

**Decrease severity by 1 when:**
- The affected workflow is edge-case or infrequent
- The product has a highly expert, homogeneous user base with shared mental models
- A workaround exists that a typical user would discover within ≤ 2 attempts
- The evaluator has low confidence in the finding (evidence is ambiguous)

**Never adjust severity below 1 for any finding that:**
- Blocks access to any user using assistive technology
- Exposes personally identifiable data or causes data loss
- Could cause a user to complete an irreversible action unintentionally

### Severity as a spectrum reminder

`CORE.md` requires justifying binary classifications. The 0–4 scale is itself a compression.
Where a finding sits at a severity boundary (e.g., strong 2 / possible 3), note the ambiguity
explicitly rather than forcing a single number.

---

## Coverage Limitations Model

Every evaluation covers a fraction of the possible evaluation space. The report must
enumerate what was *not* evaluated.

**Standard coverage gaps to document:**

| Category | Common exclusions |
|----------|-------------------|
| User population | Non-English speakers, assistive technology users, low-bandwidth environments, older adult users |
| Authentication state | Logged-in states, multi-role UIs, permission-restricted views |
| Device coverage | Tablet viewports, Android-specific rendering, specific OS/browser combinations |
| Content variation | Empty states, error states, maximum-data states, first-time-use states |
| Temporal states | Loading states, timeout states, offline/degraded modes |
| Competitive benchmarking | H4 (Consistency/Standards) requires external comparison — mark findings where no benchmark was available |

**When a finding's validity depends on coverage:**
Flag it as "conditional" — e.g., "This is a Severity 3 finding *if* the product serves users on
mobile as a primary device. If the primary use case is desktop-only, reassign to Severity 1."

---

## Evaluator Bias Acknowledgment

Expert reviews reflect the evaluator's own knowledge, cultural context, and assumptions.
Required acknowledgments per evaluation:

1. **Evaluator identity** — Background, domain expertise, and context that shaped what was
   noticed and what was not.

2. **Methodological limitation** — A single-evaluator review (automated + AI) will surface
   20–40% of usability problems on average. Multiple independent evaluators improve coverage.
   Note in the report when only one evaluator pass was performed.

3. **Assumption audit** — Before finalizing any Severity 3–4 finding, ask:
   - "Am I assuming a particular type of user?" (e.g., a "standard" Western user with
     particular norms around form interaction)
   - "Am I applying a heuristic in a context it wasn't designed for?"
   - "What would change about this finding if the primary user were a power user, a new user,
     or a user in an assistive technology context?"

---

## Downstream Integration in Research OS

### → issue-log

Heuristic findings map directly to issue-log entries. Use Phase 4 (handoff) to generate
issue-log-compatible rows. Key field mappings:

| Heuristic report field | Issue log field |
|------------------------|-----------------|
| Finding title | `issue_title` |
| Severity (0–4) | `severity` (map to issue-log scale) |
| H# category | `category` |
| Affected journey | `context` |
| Recommended fix | `recommendation` |

### → hmw-extraction

Pain points surfaced by heuristic findings (especially H1–H5 and H9) are direct inputs to
`hmw-extraction`. Phase 4 generates a ready-to-use pain point list in the format the
hmw-extraction skill expects.

### → planting-research-seeds

When a finding reveals a question heuristic evaluation cannot answer, Phase 4 outputs a
seed brief. Seed-worthy conditions:

- The evaluator assigns plural interpretations with meaningfully different implications
- The impact of a violation depends on actual user behavior (not just expert judgment)
- The finding surfaces a gap in existing research (no prior sessions addressed this)
- The finding involves a population group that has not been represented in prior sessions
  (see Sessions coverage in the relevant seed)

### Severity alignment with issue-log

The issue-log skill uses a different severity vocabulary. Map as follows when creating
issue entries from heuristic findings:

| Heuristic severity | Issue log severity |
|--------------------|--------------------|
| 4 — Catastrophic | Critical |
| 3 — Major | High |
| 2 — Moderate | Medium |
| 1 — Cosmetic | Low |
| 0 — Not a problem | (omit from log) |

---

## Standards References

| Standard | What it contributes |
|----------|---------------------|
| ISO 9241-11 | Usability outcomes in context: effectiveness, efficiency, satisfaction — use as business-readable impact language |
| ISO 9241-110 | Interaction principles (formerly dialogue principles); priority depends on purpose, users, tasks, environment — use to contextualize and justify severity adjustments |
| ISO 9241-210 | HCD across lifecycle — use when evaluations need to connect to iterative design process governance |
| WCAG 2.2 / ISO 40500:2025 | Accessibility heuristics; treat as mandatory heuristic extension when any user population includes people with disabilities |
| NNG 10 Heuristics | Primary heuristic set; see `references/nng-heuristics-guide.md` |

---

## Anti-Patterns to Avoid

| Anti-pattern | Why it's a problem | What to do instead |
|--------------|-------------------|-------------------|
| Severity assigned during finding — before full set is known | Relative severity requires seeing the full picture; first-pass ratings are inflated | Collect all findings first, then calibrate severity across the set |
| "No violations detected" = "Passed" | Absence of automated evidence is not positive evidence | Mark as "Not evaluated" or "No violations detected — visual review recommended" |
| Generic recommendations ("improve error messages") | Cannot be actioned by design or engineering | Write specific, buildable recommendations ("Add aria-live='polite' to the .status-message container and ensure text describes the specific error condition") |
| Findings without audience | A developer needs different information than a product manager | Phase 4 handoff explicitly separates designer action briefs from stakeholder summary framing |
| "The user" as a homogeneous subject | Collapses diversity of experience | Always specify *which* user, in *which* context, is affected |
