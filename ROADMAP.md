# Research OS — Open Source Roadmap

This roadmap describes the path to making Research OS a fully open, semantically
searchable research knowledge infrastructure. Every phase is grounded in the
project's core principles: care precedes optimization, plurality is method,
tenderness is rigor, context resists compression, binaries require defense.

---

## North Star

A research team should be able to ask any question about their collective research
history — across studies, across researchers, across time — and receive an
evidence-grounded answer with honest confidence ratings, transparent retrieval,
and explicit acknowledgment of what is not yet known.

The retrieval must be **local-first** (participant data never leaves the machine),
**transparent** (the researcher can always see why evidence was surfaced),
and **human-led** (the system amplifies judgment, it does not replace it).

---

## Phase 0 — Open Source Foundation

*Make the project ready for external contributors.*

| Issue | Title | Priority |
|-------|-------|----------|
| #5 | Add CONTRIBUTING.md with care-first contribution guidelines | High |
| #6 | Add CODE_OF_CONDUCT.md grounded in the project's epistemic stance | High |
| #7 | GitHub issue and PR templates | Medium |
| #8 | GitHub Actions CI for skill structure validation | Medium |

**Done when:** A new contributor can open the repo, understand the epistemic contract,
and submit a skill or methodology change with confidence that it will be reviewed on
the right terms.

---

## Phase 1 — RAG: Local Semantic Evidence Layer

*Replace file-traversal retrieval with semantic search. No cloud. No vendor lock-in.*

### Open source stack

| Component | Tool | License |
|-----------|------|---------|
| Vector store | [ChromaDB](https://github.com/chroma-core/chroma) | Apache 2.0 |
| Embeddings | [sentence-transformers](https://github.com/UKPLab/sentence-transformers) | Apache 2.0 |
| Default model | `all-MiniLM-L6-v2` (80MB, local) | Apache 2.0 |
| Multilingual | `paraphrase-multilingual-MiniLM-L12-v2` | Apache 2.0 |
| Keyword search | [rank_bm25](https://github.com/dorianbrown/rank_bm25) | MIT |
| NLP (noun phrases) | [spaCy](https://spacy.io/) `en_core_web_sm` | MIT |

**Dependency chain (must be built in order):**

```
#9 Evidence Unit Schema
        ↓
#10 Local Evidence Indexer (ChromaDB + sentence-transformers)
        ↓
#11 Semantic Search in querying-research-knowledge
        ↓
#12 Hybrid Retrieval (keyword + semantic via RRF)
        ↓
#13 Retrieval Transparency (vocabulary gap detection)
```

**Done when:** A researcher can ask `querying-research-knowledge` a question using
their own vocabulary and receive evidence even when the corpus uses different words
to describe the same experience. The retrieval explains itself.

---

## Phase 2 — Cross-Seed Intelligence

*Connect the dots across research studies.*

| Issue | Title | Depends on |
|-------|-------|-----------|
| #14 | Cross-seed theme similarity detector | #10 |
| #15 | Evidence traceability (quote → theme → finding → report) | #10 |
| #16 | Research gap detector | #15 |

**Done when:** A researcher can see which themes appear across multiple seeds,
trace any finding back to its source quotes, and proactively discover what questions
the corpus has not yet answered — before a stakeholder asks.

---

## Phase 3 — Evidence Quality & Integrity

*Make the epistemic health of the corpus visible.*

| Issue | Title | Depends on |
|-------|-------|-----------|
| #17 | Evidence coverage CLI report | #10 |
| #18 | Participant diversity tracker | — |
| #19 | Synthesis staleness detector | #15 |

**Done when:** A researcher running `coverage_report.py` can see exactly which
topics are well-evidenced, which are thin, which participant contexts are
underrepresented, and whether any synthesis outputs have drifted out of sync
with their source data.

---

## Phase 4 — Community & Extensibility

*Build the infrastructure for a research methods commons.*

| Issue | Title | Depends on |
|-------|-------|-----------|
| #20 | Skill plugin specification | #8 (CI) |
| #21 | Seed export/import | — |
| #22 | Public skill registry | #20 |

**Done when:** A researcher in a different organization can discover a community
skill for diary study synthesis, install it in two commands, and trust that it
meets the same epistemic standards as the core skills. A team can share their
synthesis artifacts (never raw participant data by default) with collaborators
via a seed export.

---

## Design principles for every phase

These are not guidelines — they are constraints that every implementation decision
must satisfy.

**Local-first.** Participant data cannot leave the researcher's machine. Every
component must work fully offline after initial setup. Cloud embeddings, SaaS
vector stores, and remote APIs are not acceptable defaults.

**Transparency over performance.** A slower retrieval that explains itself is
better than a faster one that doesn't. The researcher must always be able to
understand why evidence was surfaced.

**Human judgment is not automatable.** No feature should claim to make synthesis
decisions, merge themes, or invalidate findings automatically. The system detects
and flags; the researcher decides.

**Plurality is structural.** Cross-seed linking, gap detection, and coverage
reports must always present observations, not conclusions. Every flag surfaces
at least two possible interpretations.

**Consent before sharing.** Seed export defaults to synthesis-only. Raw
participant data requires explicit opt-in and an acknowledged consent prompt.
No exception.

---

## Technology choices — rationale

All dependencies are chosen against four criteria:

1. **Open source** with permissive license (MIT or Apache 2.0)
2. **Local execution** — no mandatory network calls after setup
3. **Python-native** — consistent with existing scripts in `skills/*/scripts/`
4. **Minimal footprint** — no databases requiring a running server (ChromaDB is
   file-persistent, not a server)

The stack does not include LangChain or LlamaIndex by design. Those frameworks
add abstraction layers that obscure what the retrieval system is actually doing —
which conflicts directly with the transparency principle. Direct use of
ChromaDB + sentence-transformers is more legible and more aligned with the
project's commitment to explainability.

---

## What this roadmap does not include

- A web UI or hosted dashboard (local CLI only — reduces attack surface on sensitive data)
- Automatic theme merging or finding generation (human judgment is not automatable)
- Cloud sync or collaborative real-time editing (out of scope for v1)
- Quantitative research tooling (survey analysis, A/B test interpretation) — these
  belong in community skills, not the core
