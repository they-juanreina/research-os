---
name: thematic-coding
document type: reference
description: Methodology depth — affinity mapping vs. thematic coding, atomic decomposition rules, codebook writing, negative cases, inter-rater reliability, and cross-persona analysis.
---

# Thematic Coding — Methodology Reference

---

## 1. Affinity Mapping vs. Thematic Coding — When Each Applies

These are two distinct but related practices. The SKILL.md uses affinity mapping as the default entry point because most UX research studies are exploratory. Understanding the difference matters when the study design calls for the other.

### Affinity Mapping (bottom-up)

**How it works**: Evidence units are grouped physically (digital board or cards) by one researcher who moves freely until patterns emerge. Themes are named *after* clustering, not before.

**When it's appropriate**:
- Generative or exploratory study — you do not know what to expect
- Early-stage research — first study on a product or user group
- Discovery interviews, contextual inquiry, diary study synthesis
- Team analysis sessions where multiple researchers co-cluster

**Strengths**: Resists confirmation bias; allows genuinely unexpected patterns to surface; collaborative process builds shared understanding.

**Limitations**: Dependent on who is doing the clustering; labels are post-hoc and may oversimplify; harder to replicate across different researchers; does not naturally surface negative cases.

### Thematic Coding (structured)

**How it works**: A codebook is written (or borrowed from prior studies) before coding begins. Each evidence unit is systematically evaluated against the codebook.

**When it's appropriate**:
- Theory-informed research — specific hypotheses to test or frameworks to apply
- Cross-study synthesis — comparing findings from multiple seeds
- High-stakes studies requiring replicability (e.g., regulatory, longitudinal)
- When a prior codebook exists from a related seed and is being extended

**Strengths**: Replicable; supports inter-rater reliability checks; good for cross-study comparison; explicit about analytical decisions.

**Limitations**: Can suppress unexpected findings if codebook is too rigid; requires more setup time; risk of forcing data to fit pre-existing categories.

### Hybrid (recommended for most studies)

Start with affinity mapping (Steps 3–4) to let patterns emerge without constraint. Then formalize the clusters into a codebook (Step 5) and apply it systematically in a second pass (Step 6). This captures the discovery value of affinity mapping and the rigor of thematic coding.

---

## 2. Atomic Decomposition — Edge Cases

The goal is evidence units small enough to code independently. These cases require judgment:

### When NOT to split

**Embedded context**: If splitting removes the context that gives the observation meaning, keep together.
- `"She found it confusing — but said she would figure it out eventually"` — two thoughts, but the second qualifies the first. Keep as one unit; note the qualification in the Confidence column.

**Verbatim quotes**: Never split a participant's direct quote. A long quote with multiple ideas is still one quote — code it to all relevant themes.

**Causal observations**: `"Clicked the wrong button because the labels looked the same"` — splitting loses the causal link. Keep as one unit; it belongs to both a "labeling" theme and a "selection error" theme via multi-coding.

### When to definitely split

**Sequential actions**: `"Read the instructions, then ignored them and tried anyway"` → two units: (1) read instructions, (2) bypassed instructions. These may code to different themes.

**Compound pain points**: `"The export is slow and the format options are limited"` → two units. Slow export and limited format are independent problems.

**Multiple participants in one note**: `"Both P1 and P2 struggled to find the save button"` → two units, one per participant, to preserve individual attribution for coverage analysis.

---

## 3. Writing Good Theme Definitions

The codebook definition is the analytical instrument. A weak definition produces inconsistent coding. A strong definition produces coding decisions anyone on the team can replicate.

### Structure of a strong definition

```
[What the participant experiences or believes], expressed as [evidence type: behavior / statement / emotional signal], in the context of [task or situation where it appears].
```

**Example — weak**: `"Users have trouble with navigation."` — too broad, topic-framed, no inclusion criteria.

**Example — strong**: `"Participants cannot locate a previously visited or saved item without retracing steps from the beginning of the session. Expressed as backward navigation, explicit verbal confusion, or repeated attempts to reach the same location. Distinct from 'search failure' (TC-04), which concerns not finding new information — this theme concerns losing access to work already done."`

### Inclusion criteria specificity

Include enough specificity to decide the hard case, not just the obvious one.

**Weak inclusion**: `"Participant seems frustrated"`
**Strong inclusion**: `"Participant explicitly names frustration ('this is frustrating', 'this makes no sense'), or exhibits behavioral signals — repeated failed attempts, audible sighs, abandonment of task — attributable to the product experience and not to the study situation"`

### Exclusion criteria — the most important and most skipped part

Every theme should be defined partly by what it is *not* — especially against its closest neighbor theme.

**Example**: Theme `"Cannot trust system state"` vs. theme `"System behaves unexpectedly"`:
- Trust theme: participant doubts the *accuracy* of what they see (did my save go through? is this number right?)
- Unexpected behavior theme: participant is surprised by *what happened* (that was not what I expected it to do)
- Exclusion for trust: `"Surprise or confusion about behavior — code to TC-07 unless the participant explicitly questions accuracy or reliability"`

---

## 4. Multi-Coding — When and How

Multi-coding is not a failure to decide — it is an accurate representation of the data.

### When to multi-code

- The evidence unit contains two independently meaningful elements that code to different themes
- A quote about one theme explicitly reveals a second theme as context: `"I didn't save it because I didn't think it would let me"` — codes to both a "save behavior" theme and a "low system confidence" theme
- A behavioral observation spans two stages of a journey that map to different themes

### When NOT to multi-code

- The themes overlap because the codebook definitions are too broad — fix the codebook instead
- You are uncertain which theme it belongs to — assign the best-fit theme and note the uncertainty in the Confidence column; don't resolve uncertainty by assigning both

### Recording multi-codes

In the coded CSV, the `Theme_Codes` column holds a comma-separated list: `TC-02,TC-05`. The `Multi_Code` column confirms the pairing: `TC-02+TC-05`. Both columns are required when multi-coding — do not use one without the other.

### Analysis implication

When counting evidence per theme for the theme summary, a multi-coded unit counts toward *both* themes in their evidence totals. Do not count a multi-coded unit twice in the total evidence unit count across the dataset.

---

## 5. Negative Cases — How to Find Them

Negative cases are evidence that contradicts or meaningfully complicates a theme's dominant pattern. They are the primary check against confirmation bias in thematic analysis.

### Why researchers miss them

- The instinct is to build cohesive themes; contradictory evidence feels like noise
- Session notes often record notable moments; neutral or counter-evidence is underrecorded
- Post-hoc rationalization is easy when you are both the collector and the analyst

### How to find them deliberately

After second-pass coding, for each theme:

1. Write the dominant pattern in one sentence: `"Most participants distrusted save state because the system gave no feedback after saving."`
2. Ask: which evidence units show a participant who *did* trust save state, *did not* need feedback, or *found feedback but still had issues*?
3. Search the full coded dataset for evidence matching any of those counter-patterns
4. Review sessions where the participant was notably different from the sample majority (different role, more experience, different workflow)

### What to do with negative cases

- **Revise the theme definition** if the negative case reveals an overgeneralization
- **Add an alternative theme** if multiple negative cases cluster into a pattern
- **Retain the dominant pattern and document the exception** if the negative case is genuinely atypical (note what makes it atypical — do not dismiss based on its inconvenience)
- **Raise confidence on the main theme** if the search was thorough and genuine negative cases are rare

---

## 6. Minority Themes

A minority theme is a theme with low evidence count (≤ 2 units) that does not meet the confidence threshold for a Full theme but cannot be ethically suppressed.

### When to keep a minority theme

- The evidence is strong (verbatim quote, strong behavioral observation) even if rare
- The participant who provided the evidence is from an underrepresented population in the study
- The finding would change a significant design decision if confirmed in a larger sample
- The theme contradicts a high-confidence majority theme

### When to fold a minority theme into an adjacent theme

- The minority theme is conceptually subsumed by a larger theme (it is a nuance, not a distinct pattern)
- The exclusion criteria of an existing theme would have to be violated to separate them

### How to document minority themes

Add a `Low confidence` flag in the theme summary's Confidence column. Add a note in the codebook: `"Minority theme — appears in 1 session. Meets inclusion criteria but evidence is insufficient for high confidence. Recommend probing in future sessions."`

Do not present minority themes as equivalent to high-confidence themes in downstream handoffs (journey mapping, HMW) without flagging their evidential status.

---

## 7. Inter-Rater Reliability

Most UX research does not require formal IRR. It becomes important when:
- The study is high-stakes (regulatory, legal, or organizational policy decisions)
- Multiple researchers are coding independently and their findings will be merged
- The codebook is being validated for reuse across studies

### Lightweight IRR for practitioner use

1. Both researchers code the same 20% sample independently using the shared codebook
2. Count agreements and disagreements per theme
3. Compute percent agreement: `agreements / (agreements + disagreements) × 100`
4. Target: ≥ 80% agreement before proceeding
5. Resolve disagreements by discussion; revise codebook definitions where patterns of disagreement reveal ambiguity

### What disagreements reveal

Disagreements on inclusion/exclusion → codebook definitions need sharpening
Disagreements on whether to multi-code → multi-code policy needs explicit rules
Systematic disagreements on one theme → that theme may be conflating two concepts

---

## 8. Codebook Evolution — Adding Themes After Second Pass

The codebook should be treated as stable during the second-pass coding so that decisions are consistent. After the second pass is complete, residuals are the input for evolution.

**Protocol for adding new themes from residuals:**

1. Group all `RESIDUAL` units. Count them. If fewer than 3 residuals, document them as "uncodeable outliers" — do not force a theme.
2. If ≥ 3 residuals appear to share a pattern, write a candidate theme definition.
3. Apply the candidate theme to the residuals. If all 3 fit cleanly, add the theme to the codebook.
4. Return to the full dataset and check whether any previously coded units should be re-coded or multi-coded with the new theme.
5. Document the evolution: note in the codebook header that this theme was added post-second-pass and list the residuals that prompted it.

Do not add themes to confirm a prior hypothesis. If a new theme only emerged because you went looking for it, flag that explicitly.

---

## 9. Cross-Persona Analysis

When participant roles differ meaningfully (designers vs. administrators, new users vs. power users), thematic analysis must account for role as a moderating variable.

### How to conduct cross-persona analysis

After completing the theme summary, for each theme:
1. Filter the coded dataset to show evidence by role
2. Identify themes where evidence comes predominantly from one role
3. Identify whether the theme name and definition still hold across roles — or whether the same surface behavior has different root causes by role

**Example**: A theme `"Cannot locate previous work"` may appear in both designer and admin evidence. But for designers, it relates to file organization; for admins, it relates to permission scoping. These are different problems named by the same theme. The theme should either be split or the definition updated to hold the distinction.

### Documenting role concentration

Add a `Role concentration` field to the theme summary:
- `Distributed` — evidence from ≥ 3 roles
- `Concentrated` — > 60% of evidence from one role
- `Single-role` — evidence exclusively from one role (flag as low generalizability)

A concentrated or single-role theme is not invalid — but it should not be treated as a universal finding in downstream handoffs. Journey maps and HMW statements derived from it should specify the role explicitly.

---

## 10. Common Pitfalls

| Pitfall | What it looks like | How to catch it |
|---------|-------------------|-----------------|
| **Galaxy-brained themes** | A theme that subsumes 40% of the dataset | No theme should hold > 25% of evidence. If it does, split it. |
| **Dust-bin themes** | A theme called "Miscellaneous" or "Other" | Resolve or dissolve — never ship a dust-bin theme to downstream skills |
| **Solution-themed themes** | `"Needs better onboarding"` as a theme name | Theme names must describe experience, not design response |
| **One-voice themes** | All evidence from the same session or participant | Documented and flagged, but not presented as a generalizable pattern |
| **Premature saturation** | Naming themes before finishing the full first-pass cluster | Hold naming until all units are clustered |
| **Unchecked inference** | Theme definition says "users feel..." without behavioral evidence | Match definition type to evidence type (quote vs. observation vs. inferred) |
| **Conflating categories with themes** | Treating a category label (`"TC-02: Cannot locate work"`) as an interpretive finding | Ask: does this make a claim or just name a pattern? Names are categories; claims are themes. See Section 11. |
| **Skipping analytic memos** | No record of why coding decisions were made; analysis cannot be audited | Write one memo entry per clustering and naming decision. See Section 12. |
| **Undifferentiated coding method** | All evidence coded the same way regardless of data type | Behavioral observations, quotes, and pain points call for different methods. See Section 13. |

---

## 11. Saldaña's Three Levels — Code, Category, Theme

*Source: Saldaña, J. (2021). The Coding Manual for Qualitative Researchers (4th ed.). SAGE.*

### Code

A code is a label assigned to a single datum — a word or short phrase that captures what the datum is about.

- `SAVE UNCERTAINTY` — applied to: `"I never know if my changes saved"`
- `BACKWARD NAVIGATION` — applied to: *Clicked back button three times without reaching previous screen*
- `PERMISSION BARRIER` — applied to: `"I can't export without admin access"`

Codes name; they do not interpret. They are applied to individual evidence units.

### Category

A category groups codes that share a conceptual similarity. **This is what the skill calls "themes" (TC-XX).**

- TC-02 ("Cannot locate previous work") groups: `BACKWARD NAVIGATION`, `SESSION STATE LOSS`, `REPEATED PATH-TRACING`

Categories summarize patterns. They are descriptive at a higher level than individual codes.

**Touch test** (Saldaña): Can you physically touch what this code or category represents? If yes, you are at a concrete/descriptive level. If no, you are approaching a conceptual level. "Navigation button" (touchable) vs. "Loss of agency" (not touchable — conceptual). Use the touch test to gauge when a category has reached a conceptual depth worth interpreting.

### Theme

A theme is an interpretive, propositional statement that emerges from categorization. It is not a label — it is a claim.

- Category: `TC-02 "Cannot locate previous work"`
- Theme: *"Users' sense of competence in the product depends on trusting that their work persists — and that trust is systematically undermined by the absence of visible state feedback."*

Saldaña: *"A theme is an outcome of coding, categorization, or analytic reflection, not something that is, in itself, coded."*

### Why the distinction matters

Confusing categories with themes produces pattern lists instead of interpretive insights. Category-level analysis answers *what*. Theme-level analysis answers *why it matters* and *what it reveals about the user's experience*.

For most UX deliverables, category-level analysis (TC-XX) is the right stopping point — it directly feeds journey mapping, HMW extraction, and issue logging. Themeing is appropriate when producing a synthesis report or design principles document. Apply Step 9 of SKILL.md to move from categories to interpretive themes.

---

## 12. Analytic Memos

*Source: Saldaña, J. (2021). The Coding Manual for Qualitative Researchers (4th ed.). SAGE.*

Saldaña calls analytic memos the "engine" of qualitative analysis. They are concurrent records of the researcher's reasoning — not post-hoc documentation.

### What an analytic memo captures

- **Coding decisions**: Why this code was assigned; what alternatives were considered; why a unit was placed in one category and not another
- **Emerging patterns**: What seems to be taking shape across multiple sessions; what surprises you; what you expected but are not finding
- **Hypotheses**: Tentative interpretations to test against remaining data
- **Methodological notes**: Why you split or merged categories; why you added a theme post-second-pass
- **Ethical observations**: Moments where participant wellbeing, power dynamics, or representation issues surfaced in the data

### When to write memos

Write at every analytical decision point, not at the end:
- When you name a cluster — why this name over the alternatives?
- When you write a codebook definition — why is the inclusion boundary here?
- When you find a negative case — does it revise the theme or stay as a documented exception?
- When you multi-code — why both codes, not just one?
- When you are stuck — articulating the blockage often resolves it

### Format

No required structure. A dated, freeform markdown note is sufficient:

```
[2026-03-01] — Cluster naming — TC-02
Named "Cannot locate previous work" over "Navigation issues" because the pattern
is specifically about *returning* to prior state, not general wayfinding. Three
units (U-007, U-012, U-023) all describe a participant who *had* found a screen,
then could not return — not participants who couldn't find something new. Keeping
"navigation" in the name would merge this with TC-04 (search failure).
```

### Where to store memos

Save to `memos-[seed].md` in the seed's `03_Synthesis/` directory alongside the codebook. One file; append as analysis progresses.

### What memos are not

- Not session notes — memos are about the analysis, not the research event
- Not the codebook — memos explain decisions; the codebook records outcomes
- Not optional for high-stakes projects — memos are the audit trail for every coding decision, regardless of project scale

---

## 13. Coding Method Selection

*Source: Saldaña, J. (2021). The Coding Manual for Qualitative Researchers (4th ed.). SAGE. Adapted for UX research contexts.*

Saldaña documents 32 coding methods across two cycles. The seven most applicable to UX research:

### First Cycle Methods

**Descriptive Coding** — Summarizes the topic of a datum as a noun or noun phrase.
- Format: `TOPIC PHRASE` (concise noun phrase)
- Example: `EXPORT LIMITATION`, `ONBOARDING CONFUSION`, `PERMISSION BARRIER`
- Best for: Any UX research; creates a general-purpose codebook; good starting point when the research question is open
- Limitation: Describes topics, not experience — may not capture the *quality* or stakes of an experience

**In Vivo Coding** — Uses the participant's own words as the code, preserved in quotes.
- Format: `"participant's exact phrase"`
- Example: `"figured it out eventually"`, `"I never know if it saved"`, `"it feels like guessing"`
- Best for: Preserving participant language; grounding the codebook in participant voice; avoiding analyst-imposed framing
- Note: In Vivo codes are often collapsed into Descriptive codes at the categorization stage, but should be preserved through first-pass coding

**Process Coding** — Uses gerunds (-ing words) to capture actions, interactions, and states.
- Format: `VERB-ING NOUN` (gerund phrase)
- Example: `SEARCHING FOR SAVED WORK`, `AVOIDING COMPLEX FEATURES`, `RETRACING STEPS`
- Best for: Behavioral observations; user actions for journey mapping; identifying recurring behavioral patterns

**Emotion Coding** — Identifies participant emotional states.
- Format: `EMOTION` — pair with Magnitude Coding for intensity
- Example: `FRUSTRATION`, `RELIEF`, `ANXIETY`
- Best for: Studies where emotional experience is part of the research question; feeds directly into journey mapping
- Note: Emotion codes require behavioral or verbal evidence. If inferred, label `[INFERRED: FRUSTRATION]`

**Values Coding** — Captures participant values, attitudes, and beliefs.
- Format: `VALUE:`, `ATTITUDE:`, or `BELIEF:` prefix
- Example: `VALUE: CONTROL OVER OWN WORKFLOW`, `ATTITUDE: DISTRUSTS AUTOMATION`, `BELIEF: SYSTEM IS UNRELIABLE`
- Best for: Understanding *why* users behave as they do; grounding design principles in user values

**Versus Coding** — Captures binary oppositions, tensions, and conflicts in the data.
- Format: `X VS. Y`
- Example: `EFFICIENCY VS. CONTROL`, `SPEED VS. ACCURACY`, `INDIVIDUAL WORKFLOW VS. TEAM NORMS`, `SYSTEM LOGIC VS. USER MENTAL MODEL`
- Best for: UX friction that arises from competing constraints; identifying design tensions that a single feature cannot resolve; naming the core conflict driving multiple pain points
- UX application: Versus codes often name the design problem more precisely than descriptive codes. A cluster of units about "confusing navigation," "unexpected behavior," and "lost trust" may all instantiate `SYSTEM LOGIC VS. USER MENTAL MODEL`
- Note: Versus codes name a tension; the theme emerges when you explain what that tension reveals about the user's experience

**Simultaneous Coding** — Formally assigns two codes to one datum when it genuinely belongs to both.
- This is the formal version of multi-coding (documented in Section 4)
- Simultaneous coding signals that the datum is analytically significant precisely because it straddles two categories

### Additional Techniques

**Subcoding** — A secondary tag applied after a primary code for finer-grained categorization.
- Format: `PRIMARY CODE > subcode`
- Example: `NAVIGATION CONFUSION > BACKWARD NAVIGATION`, `NAVIGATION CONFUSION > DEAD END`
- Use when a category is internally heterogeneous and the subcategory distinction changes downstream decisions. Do not subcode routinely — only when the distinction matters.

**Magnitude Coding** — An intensity modifier added to any other code.
- Format: `CODE +` (mild intensity), `CODE ++` (strong intensity), `CODE -` (attenuated)
- Example: `FRUSTRATION+`, `FRUSTRATION++`, `RELIEF-`
- Use alongside Emotion Coding and Values Coding; enables intensity comparison across participants and sessions

**N/A Coding** — Explicitly marks administrative or non-substantive passages as out of scope.
- Format: `N/A` or `N/A: [reason]`
- Example: `N/A: session intro/consent language`, `N/A: off-topic tangent`
- Why: Prevents silently skipped passages from creating ambiguity in audit; makes the coded corpus complete

### Choosing a method

| If your data primarily contains… | Start with… |
|---|---|
| Behavioral observations | Process Coding |
| Interview responses about experience | Descriptive + In Vivo Coding |
| Emotional moments | Emotion + Magnitude Coding |
| User motivations and mental models | Values Coding |
| Product friction and competing constraints | Versus Coding |
| Mixed data from multiple session types | Descriptive as baseline; add In Vivo for notable quotes |

Most studies benefit from combining methods. A common UX combination: Descriptive for the codebook backbone + In Vivo for memorable participant language + Versus for friction identification + Emotion for journey mapping input.

---

## 14. Code Mapping — Iterative Reduction

*Source: Saldaña, J. (2021). The Coding Manual for Qualitative Researchers (4th ed.). SAGE.*

Code mapping is the reduction process that moves from a full first-cycle code list to the named categories of the codebook. It is the intermediate step between Step 3 (first-pass clustering) and Step 5 (codebook writing).

### The reduction sequence

```
Full first-cycle code list
        ↓
Initial groupings (similar codes together)
        ↓
Named categories (TC-XX — what SKILL.md Step 5 produces)
        ↓  [optional]
Higher-level meta-categories (if categories themselves cluster)
        ↓  [optional, Step 9]
Interpretive themes (propositional statements)
```

### How to perform code mapping

1. **Produce the full code list** — after first-pass coding, list every code used (including multi-codes and Versus codes). This is your raw material.
2. **Sort by similarity** — group codes that address the same phenomenon. Do this visually if possible. This is the Step 3 clustering process made explicit.
3. **Name the groups** — produces TC-XX categories (Step 4). Apply the naming rules from SKILL.md.
4. **Check for redundancy** — two codes in the same group that mean the same thing are candidates for merging. Two groups with overlapping inclusion criteria are candidates for merging.
5. **Check for over-inclusion** — one group containing > 25% of all codes is likely a galaxy-brained category. Split it.
6. **Iterate** — most analyses need 2–3 reduction passes before the category structure stabilizes.

### When to stop reducing

Stop when: every code has a category home; no two categories have overlapping inclusion criteria; the categories collectively answer the research question.

### Pattern types to look for during mapping

Go beyond frequency. Frequency indicates prevalence; other pattern types indicate structure:

| Pattern type | What it looks like | Analytical value |
|---|---|---|
| **Similarity** | Multiple participants share the same experience at the same touchpoint | Confirms a pain point or strength as generalizable |
| **Difference** | Different roles have opposite experiences with the same feature | Reveals that one solution will not work for all users |
| **Frequency** | A code appears across many sessions | Indicates a widespread issue — but frequency alone doesn't establish importance |
| **Sequence** | One experience consistently follows another | Suggests a causal chain or a predictable user pathway |
| **Correspondence** | Two themes co-occur — when one appears, so does the other | Suggests a shared root cause or a compound problem |
| **Causation** | One theme is cited as causing another (by participants explicitly, or clearly implied by behavioral evidence) | Strongest basis for a specific design intervention |

Low-frequency sequence or causation patterns are often more actionable than high-frequency descriptive patterns. Do not filter by frequency alone.
