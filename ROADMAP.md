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

## Anthropic's guidelines informing this roadmap

Anthropic's ["Building Effective Agents"](https://www.anthropic.com/research/building-effective-agents)
and ["Equipping Agents for the Real World with Agent Skills"](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
establish three principles that every phase of this roadmap must satisfy:

**Start with the simplest solution that works.** Only add complexity when a
simpler approach demonstrably fails. The current file-traversal retrieval is simple
and correct for small seed libraries. Before adding RAG, evals must show where it
actually breaks down — not where we assume it does.

**Design skills for agents, not developers.** Skills must be dense enough to work
with the minimum invocation (`CORE.md` + `SKILL.md`). `REFERENCE.md` and
`EXAMPLES.md` are loaded only when needed. This progressive disclosure pattern
keeps context windows lean without sacrificing depth.

**Human oversight is the invariant.** Every automated feature — retrieval, gap
detection, staleness flags, eval scoring — surfaces findings for a researcher to
act on. Nothing decides autonomously.

---

## Phase 0 — Open Source Foundation ✓

*Make the project ready for external contributors.*

| Issue | Title | Status |
|-------|-------|--------|
| #5 | Add CONTRIBUTING.md with care-first contribution guidelines | Done |
| #6 | Add CODE_OF_CONDUCT.md grounded in the project's epistemic stance | Done |
| #7 | GitHub issue and PR templates | Done |
| #8 | GitHub Actions CI for skill structure validation | Done |

---

## Phase 0.5 — Skill Evals

*Before building more, understand how well what exists actually works.*

This phase exists because of a direct Anthropic recommendation: run evaluations
before adding complexity. The 16 core skills have never been systematically tested
against their own quality gates. That gap is a risk — skills may formally apply
`CORE.md` principles without structurally enforcing them. Evals make that visible.

This is also the **best starting point for collaboration.** Running evals requires
no engineering background — just a Claude Code session, a research artifact, and
the rubric. Friends and collaborators can contribute eval findings before the
codebase is ready for code contributions. Every eval finding improves the skills
directly and creates a benchmark against which future changes (including RAG) are
measured.

| Issue | Title | Priority |
|-------|-------|----------|
| #23 | Build eval infrastructure — directory structure, rubric format, and LLM-as-judge runner | High |
| #24 | Write eval cases for all 16 core skills (normal, edge, adversarial) | High |
| #25 | Collaborative eval guide — how to run evals and submit findings | High |
| #26 | Add eval gate to CI for community skill submissions | Medium |

**Done when:** Every core skill has a passing eval suite covering normal, edge, and
adversarial cases. Systematic failure modes are documented. Collaborators can run
evals independently using only Claude Code. The eval suite becomes the baseline
against which every future change is measured.

---

## Phase 1 — RAG: Local Semantic Evidence Layer

*Replace file-traversal retrieval with semantic search. No cloud. No vendor lock-in.*

**Prerequisite: Phase 0.5 must be complete.** The eval baseline is what tells us
whether RAG actually improves retrieval quality — or just adds complexity.

### Open source stack

| Component | Tool | License |
|-----------|------|---------|
| Vector store | [ChromaDB](https://github.com/chroma-core/chroma) | Apache 2.0 |
| Embeddings | [sentence-transformers](https://github.com/UKPLab/sentence-transformers) | Apache 2.0 |
| Default model | `all-MiniLM-L6-v2` (80MB, local) | Apache 2.0 |
| Multilingual | `paraphrase-multilingual-MiniLM-L12-v2` | Apache 2.0 |
| Keyword search | [rank_bm25](https://github.com/dorianbrown/rank_bm25) | MIT |
| Document ingestion | [LlamaIndex](https://github.com/run-llama/llama_index) (lower-level APIs only) | MIT |
| NLP (noun phrases) | [spaCy](https://spacy.io/) `en_core_web_sm` | MIT |

**Dependency chain (must be built in order):**

```
#9  Evidence Unit Schema
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
to describe the same experience. The retrieval explains itself. Eval scores are
equal to or better than Phase 0.5 baseline — if they aren't, the RAG layer is
adding noise, not signal.

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

### On LangChain — excluded

LangChain's chain and agent abstractions obscure execution in ways that conflict
directly with the transparency principle. Debugging why a chain produced a
particular result requires stepping through several abstraction layers — which
makes it difficult to understand, audit, or explain retrieval behavior to a
researcher. It also has a pattern of frequent breaking changes between major
versions, which increases maintenance burden without proportional benefit for a
focused, file-based RAG system like this one.

### On LlamaIndex — used selectively

LlamaIndex is purpose-built for document ingestion and RAG, and the blanket
exclusion in earlier drafts of this roadmap was too broad. The concern about
abstraction applies to its high-level orchestration APIs — not to its lower-level
document utilities. Research OS uses LlamaIndex for:

- **Document ingestion** (`SimpleDirectoryReader`, `MarkdownReader`) — loading
  session notes, synthesis artifacts, and CSV files into the indexing pipeline
  without reimplementing file parsing for each format
- **Chunking** (`SentenceWindowNodeParser`) — splitting session notes into
  evidence-sized units with surrounding context preserved
- **RAG evaluation** (`FaithfulnessEvaluator`, `RelevancyEvaluator`) — measuring
  retrieval quality against the eval baseline from Phase 0.5

The vector store (ChromaDB), the embedding model (sentence-transformers), and the
retrieval logic remain direct and explicit. LlamaIndex handles only the document
lifecycle between raw files and indexed evidence units — the part where using a
well-maintained library is genuinely simpler than building it ourselves.

This position is consistent with Anthropic's simplicity principle: use maintained
libraries where they reduce complexity; build directly where transparency is
non-negotiable.

---

## What this roadmap does not include

- A web UI or hosted dashboard (local CLI only — reduces attack surface on sensitive data)
- Automatic theme merging or finding generation (human judgment is not automatable)
- Cloud sync or collaborative real-time editing (out of scope for v1)
- Quantitative research tooling (survey analysis, A/B test interpretation) — these
  belong in community skills, not the core
