---
name: querying-research-knowledge-agent-team
description: "Multi-agent architecture for parallelized research corpus querying. Replaces sequential seed-by-seed searching with concurrent dispatching."
author: "Juan Reina (they/them)"
license: "MIT"
last_updated: 2026-03-06
---

# Agent Team — Querying Research Knowledge

> This team replaces the monolithic SKILL.md execution with a coordinated multi-agent workflow. The epistemic rules in `CORE.md` and the zero-extrapolation constraints in `SKILL.md` apply to **every agent** in the team — no agent is exempt.

---

## Why an Agent Team?

The single-agent workflow bottlenecks at **Step 2 — Search the Research Corpus**. With 8+ seeds, each containing 4 phase directories with multiple files, a sequential search is slow and context-heavy. The agent team solves this by:

1. **Parallelizing corpus search** — one agent per seed, all running concurrently
2. **Isolating concerns** — each agent handles one well-scoped responsibility
3. **Reducing context window pressure** — each searcher only loads one seed's data
4. **Maintaining rigor** — evidence classification and anti-bias checks run on the merged dataset, not piecemeal

---

## Team Roster

| Agent | File | Role | Concurrency |
|-------|------|------|-------------|
| **Orchestrator** | `orchestrator.md` | Receives the question, decodes it, dispatches searchers, coordinates handoffs, delivers the final answer | 1 (singleton) |
| **Corpus Searcher** | `corpus-searcher.md` | Searches a single seed across all 4 phases; returns a structured evidence packet | N (one per seed, **parallel**) |
| **Evidence Assessor** | `evidence-assessor.md` | Classifies all collected evidence, rates confidence, runs anti-bias checks | 1 (after all searchers complete) |
| **Answer Composer** | `answer-composer.md` | Assembles the final structured answer or generates a seed brief | 1 (after assessor completes) |

---

## Execution Flow

```
                    ┌─────────────────────────┐
                    │      ORCHESTRATOR        │
                    │  1. Load CORE.md         │
                    │  2. Decode question       │
                    │  3. List Seeds/           │
                    │  4. Dispatch searchers    │
                    └────────┬────────────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
     ┌────────────┐  ┌────────────┐  ┌────────────┐
     │  SEARCHER   │  │  SEARCHER   │  │  SEARCHER   │   ← N agents in parallel
     │  Seed A     │  │  Seed B     │  │  Seed N     │
     │             │  │             │  │             │
     │ → evidence  │  │ → evidence  │  │ → evidence  │
     │   packet    │  │   packet    │  │   packet    │
     └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
            │                │                │
            └────────────────┼────────────────┘
                             │
                    ┌────────▼───────────────┐
                    │   EVIDENCE ASSESSOR     │
                    │  1. Merge packets       │
                    │  2. Classify evidence   │
                    │  3. Rate confidence     │
                    │  4. Anti-bias checks    │
                    └────────┬───────────────┘
                             │
                    ┌────────▼───────────────┐
                    │    ANSWER COMPOSER      │
                    │  1. Formulate answer    │
                    │  2. Or: seed brief      │
                    │  3. Quality gates       │
                    └────────────────────────┘
```

---

## Handoff Contracts

### Orchestrator → Corpus Searcher
Each searcher receives:
```yaml
question: "the decoded, assumption-stripped question"
seed_path: "Seeds/[Seed Name]"
seed_name: "[Seed Name]"
search_focus: "keywords and concepts extracted from the question"
```

### Corpus Searcher → Evidence Assessor
Each searcher returns:
```yaml
seed_name: "[Seed Name]"
seed_status: "Complete | In Progress | No Relevant Data"
evidence_items:
  - type: "verbatim_quote | observed_behavior | coded_theme | researcher_note"
    content: "the evidence text"
    source_file: "path/to/file"
    participant_id: "P-XX or null"
    session_id: "Session N or null"
    phase: "01_Plan | 02_Sessions | 03_Synthesis | 04_Evaluation"
    relevance_note: "why this evidence relates to the question"
files_searched: ["list of files examined"]
```

### Evidence Assessor → Answer Composer
The assessor passes:
```yaml
confidence: "High | Medium | Low | None"
confidence_justification: "why this rating"
classified_evidence:
  - # same as evidence_items but with verified type classification
contradictions: ["list of contradictory evidence pairs"]
minority_findings: ["evidence that runs counter to the majority pattern"]
bias_flags: ["any anti-bias check warnings"]
seeds_consulted: ["all seed names — including those with no findings"]
embedded_assumptions: ["assumptions detected in the original question"]
gaps: ["aspects of the question not addressed by any evidence"]
```

---

## Invocation

The orchestrator is the entry point. To run the agent team:

1. Load `CORE.md` (epistemic framework)
2. Load `SKILL.md` (rules — zero-extrapolation, language policy, output format)
3. Load `agents/orchestrator.md` (team coordinator)
4. The orchestrator handles loading and dispatching all other agents

**Minimum invocation**: `CORE.md` + `SKILL.md` + `orchestrator.md`

---

## Constraints Inherited by All Agents

Every agent in the team must:

- Follow the **zero-extrapolation rule** (SKILL.md)
- Use **required language patterns** only (SKILL.md)
- Apply the **CORE.md epistemic framework** — plural interpretations, edge & variance scan, care check
- Never invent, hallucinate, or infer evidence
- Return structured data in the handoff contract format
- Report "no relevant data found" rather than stretching a partial match

---

## Error Handling

| Condition | Agent | Action |
|-----------|-------|--------|
| Seed directory is empty or missing phases | Corpus Searcher | Return `seed_status: "No Relevant Data"`, list expected-but-missing directories |
| No evidence items found in any seed | Orchestrator | Skip Evidence Assessor, route directly to Answer Composer with `confidence: None` |
| Contradictory evidence across seeds | Evidence Assessor | Surface both sides in `contradictions`; do not resolve |
| Anti-bias check fails | Evidence Assessor | Include `bias_flags` with specific warnings; Answer Composer must surface them |
| Single seed returns ambiguous match | Corpus Searcher | Include with `relevance_note` explaining ambiguity; let Assessor decide |
