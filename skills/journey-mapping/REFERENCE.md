# Journey Mapping Reference

## Journey Map Table Schema

### Column Definitions

**Stage**
- The phase or cycle in the user's experience journey
- Examples: Awareness, Discovery, Evaluation, Adoption, Integration, Mastery, Offboarding
- Stages should be mutually exclusive and collectively exhaustive for the experience being mapped
- Typically 5–8 stages per journey

**Touchpoint**
- The specific interaction point where the user encounters the product, service, team, or environment
- Can be digital (UI element, email, documentation), human (conversation, support ticket, meeting), or environmental (physical space, artifact, tool)
- Multiple touchpoints can exist within a single stage; list each in its own row if they have different actions or emotions
- Format: Concise noun phrase, e.g., "Signup form", "First team standup", "Onboarding checklist"

**User Action**
- The concrete behavior the user performs at this touchpoint
- Use active verbs: clicks, reads, types, asks, searches, explores, submits, compares, tests, shares
- Ground all actions in research evidence; do not infer beyond what transcripts or observations show
- Example: "Clicks 'Get Started' button and enters email address"
- Avoid vague terms like "interacts" or "engages"

**Thought/Quote**
- A direct quote from the research data, or an inferred thought grounded in behavior and context
- Direct quotes are preferred and should be wrapped in quotation marks with a confidence flag
- Inferred thoughts should be clearly labeled as such and should only represent obvious, well-supported interpretations
- Format: `"[Direct quote from interview]"` or `[Inferred: user appears to be assessing...]`
- Maximum one thought per row; if multiple exist, create additional rows for the same stage/touchpoint

**Emotion**
- The user's emotional state at this moment, with intensity indicator
- Use a scale: Satisfied, Neutral, Frustrated, Confused, Excited, Overwhelmed, Confident, Anxious, etc.
- Add intensity as +/++ (mild, strong) for clarity: "Frustrated+", "Excited++"
- Emotions should be grounded in vocal tone, word choice, body language, or explicit statements from research
- Multiple emotions can coexist; separate with comma if appropriate: "Confident, Slightly anxious"

**Pain Point**
- A specific point of friction, dissatisfaction, or unmet need
- Pain points must be concrete and tied to the research (not generic complaints)
- Good: "Form validation error message appears after 3-second delay, user submitted twice"
- Bad: "Slow form", "Bad UX"
- One pain point per row; if multiple exist for the same touchpoint, create additional rows
- Leave blank if this touchpoint contains no friction

**Opportunity**
- A potential intervention, design change, process improvement, or policy shift that would address a pain point or enhance satisfaction
- Opportunities must be grounded in research findings and user goals
- Be specific and actionable: "Add real-time validation feedback to form inputs" not "Make form better"
- Can also identify opportunities to amplify positive moments: "Expand the feature that surprised users with its intuitiveness"
- Link each opportunity to a corresponding pain point or emotional highlight

**Confidence**
- A 1–3 scale reflecting the evidence strength for this row
- **1 (Low)**: Inferred from indirect signals, single mention, or contextual clues only
- **2 (Medium)**: Mentioned explicitly or shown in behavior; observed in one persona or session
- **3 (High)**: Explicitly stated by multiple participants, observed across sessions, clear behavioral evidence, direct quote available
- Use this to flag areas needing additional research or validation

---

## CSV Export Format

Journey maps can be exported to CSV for analysis in spreadsheets or analysis tools.

### CSV Structure
```
Stage,Touchpoint,User Action,Thought/Quote,Emotion,Pain Point,Opportunity,Confidence
```

### Rules for CSV Export
1. **Column order**: Must match the order above exactly
2. **Escaping**: Wrap any cell containing commas, quotes, or newlines in double quotes. Escape internal quotes with double quotes (`""`).
3. **Newlines in cells**: Use literal newlines (CRLF or LF) within quoted cells, or replace with `\n` if line breaks cause parsing issues.
4. **Empty cells**: Leave blank (two consecutive commas) for null values. Do not use "N/A" unless it is semantically meaningful.
5. **Confidence values**: Use numeric format (1, 2, 3) in CSV; can be text ("Low", "Medium", "High") in markdown.

### Example CSV Row
```
Awareness,"Homepage",Lands on website and reads value proposition,"I want to see if this fits our workflow",Curious,None,Add customer testimonial above fold,3
Discovery,"Feature documentation",Reads FAQ and searches for specific use cases,"Does it integrate with our existing tools?",Skeptical,Documentation lacks integration examples,Add integration matrix to docs,2
```

---

## Journey Scope

Before mapping, define the scope explicitly. Unscoped maps sprawl across too many stages or stop short of a meaningful end.

### Three scope types

**Epic journey** — Covers a multi-stage lifecycle spanning weeks, months, or years. Use when the question is: *How does the user's relationship with this product evolve over time?* Examples: onboarding through mastery, first purchase through retention, initial problem awareness through ongoing resolution.

**Micro-story** — Covers a single task or feature flow, typically 3–7 steps, completing in one session. Use when the question is: *Why are users dropping off at this step?* or *Does this feature flow work end-to-end?* Micro-stories should have a clear trigger and a resolution.

**Serial journey** — A repeating cycle of use (e.g., weekly reporting workflow, recurring approval loop). Use when the question is: *Why don't users return?* Map one episode of the cycle first; then note what drives repetition into the next episode.

### When to use a service blueprint vs. a standard journey map

Use a **service blueprint** when:
- The user's experience is directly shaped by backstage processes (approval workflows, data handoffs, support escalations, fulfillment pipelines)
- Research data includes operational observations or backstage walkthroughs, not just user behavior
- The core question is: *What organizational or process change would most improve this experience?*

Use a **standard journey map** when:
- The question is: *What does the user experience at each stage?*
- Research data comes primarily from sessions, interviews, or user observations
- Backstage complexity is out of scope or unresearched

### Start and end points

State explicitly before mapping:
- **Start**: The first moment the user enters this experience (e.g., "User receives a task assignment notification")
- **End**: The moment the user's goal is met, or the point they exit the experience (e.g., "User submits the final report and sees a confirmation")

A journey that ends without resolution — where the user exits before meeting their goal — is a **cliffhanger**. Name it as such. See Story Structure Analysis below.

---

## Multi-Persona Journeys

### Approach 1: Separate Tables per Persona
Create a complete journey map table for each persona. Use a header and brief persona description before each table.

Example structure:
```
## Persona 1: Data Analyst

**Profile**: Needs quick insights, high technical literacy, time-constrained

| Stage | Touchpoint | ... |
| --- | --- | ... |
```

### Approach 2: Persona Overlay / Comparison Table
Create a single journey with a "Persona" column, or create a separate comparison matrix showing:
- **Convergence points**: Stages where personas have identical or nearly identical experiences
- **Divergence points**: Stages where personas' emotions, actions, or needs differ significantly
- **Priority stages**: Stages where one persona's experience is notably more critical or problematic

Example comparison row:
```
| Stage | Analyst Experience | Manager Experience | Divergence | Notes |
| Adoption | "This is quick to set up" | "I need to brief my team first" | Yes | Analyst wants speed; manager needs stakeholder buy-in |
```

### Best Practice
- Map primary persona(s) first (highest user count, highest impact, most complex journey)
- Add secondary personas only if their journeys diverge materially from primary
- Use persona comparison to identify "jobs to be done" that vary by user role

---

## Coverage Assessment

### Completeness Check
After mapping, verify:
1. **Stage coverage**: Does the map represent the full lifecycle or defined scope? (e.g., from awareness to mastery, or just onboarding?)
2. **Touchpoint saturation**: For each stage, are major and minor touchpoints identified? A stage should have 1–4 touchpoints on average.
3. **Research saturation**: Have you reached diminishing returns in themes? (i.e., no new pain points or opportunities emerging)
4. **Confidence distribution**: Aim for >70% of rows at confidence level 2 or 3. Rows with confidence 1 should be few and explicitly marked as research gaps.

### Coverage Gap Indicators
- Stages with blank pain point and opportunity columns (may indicate under-explored area)
- Multiple confidence-1 rows in sequence (suggests thin research for that phase)
- Stages mentioned in research but without detailed touchpoint/action data
- Missing persona perspective on a shared touchpoint

### When to Flag for Additional Research
- If >30% of rows are confidence 1 or lower
- If critical decision points or high-emotion moments lack direct quotes
- If service blueprint rows have no "behind-the-scenes actions" (suggests lack of operational data)
- If two personas show identical journeys (may indicate insufficient segmentation)

---

## Common Pitfalls and How to Avoid Them

### Pitfall 1: Confusing Stages with Touchpoints
**Problem**: Creating rows like "Email" or "Dashboard" as stages instead of actual experience phases.
**Solution**: Stages are *when*, touchpoints are *where*. Ask: "What is the user trying to accomplish in this phase?" The answer is the stage (e.g., "Learning the tool"). Touchpoints are the tools or channels used within that stage.

### Pitfall 2: Inferring Emotions Without Evidence
**Problem**: Guessing emotional state based on assumptions about user intent.
**Solution**: Ground emotions in explicit statements ("I was frustrated"), tone and language cues, or behavioral signals (e.g., user abandoned the task, came back repeatedly). Mark inferred emotions clearly. If confidence is uncertain, use confidence level 1 and flag for follow-up.

### Pitfall 3: Generic Pain Points
**Problem**: Writing "Poor UX" or "Confusing interface" without specificity.
**Solution**: Always answer: *What* was confusing? *When* did the user notice it? *What did they do* as a result? Example: "Text color contrast on the 'Submit' button was too low; user clicked 'Cancel' instead and restarted the form."

### Pitfall 4: Opportunities Divorced from Research
**Problem**: Suggesting features or changes that sound good but lack grounding in actual user needs.
**Solution**: Every opportunity should link back to a pain point or positive moment in the research. Ask: "Where in the research does a user hint at this need?" If you can't answer, it's speculation.

### Pitfall 5: Over-Segmenting Stages
**Problem**: Creating 12+ stages because each action feels distinct.
**Solution**: Group actions into logical phases. Aim for 5–8 stages. If you have many, consider whether you're describing one journey in too much detail, or whether you should split into separate journeys (e.g., onboarding vs. ongoing use).

### Pitfall 6: Ignoring Outliers or Minority Experiences
**Problem**: Creating a "happy path" journey and ignoring users who struggled or deviated.
**Solution**: If multiple personas or a notable minority experienced a stage differently, create separate journey maps or add divergence rows. Minority experiences often reveal critical friction points.

### Pitfall 7: Forgetting the "Why" in Opportunities
**Problem**: Listing feature ideas without explaining their impact.
**Solution**: Frame opportunities as "Why": e.g., "Add tooltips to hidden settings *so users don't accidentally disable notifications*."

### Pitfall 8: Treating Journeys as Finished
**Problem**: Creating a map and treating it as final truth.
**Solution**: Journey maps are research artifacts. Update them as you gather more data. Version them. Highlight areas of uncertainty. Use them as hypotheses to test, not conclusions to defend.

---

## Integration with Service Blueprints

If your research includes data about *behind-the-scenes processes*, expand the journey map into a service blueprint:

**Add two meta-rows above the main journey**:

1. **Frontstage (User-Facing)**: The journey map as described above
2. **Backstage (Internal Actions)**: What the team does to enable each touchpoint (e.g., backend processing, support ticket routing, data preparation)
3. **Support Processes**: Policies, systems, training, or tools that enable backstage actions (e.g., "Customer support SLA: 4-hour response time")

**Example Blueprint Row**:

| Stage | Touchpoint | User Action | Emotion | **Backstage Action** | **Support Process** |
|---|---|---|---|---|---|
| Adoption | Onboarding call | Joins video call to get set up | Anxious | Specialist reviews account setup, screen-shares configuration guide | Training: All specialists pass certification in account setup workflows |

This variant is useful when mapping organizational capability or operational efficiency alongside user experience.

---

## Exporting and Sharing

### Markdown Format
- Best for: Internal collaboration, Git version control, documentation sites
- Use the table format specified in SKILL.md
- Include persona description and map context as headers

### CSV Format
- Best for: Data analysis, cross-referenced with quantitative metrics, large-scale comparison across many journeys
- Use the CSV export script (`format_journey_map.py`) to ensure consistency
- Tag rows with persona, research phase, or domain for filtering

### PDF/Visual Format
- Best for: Stakeholder presentations, printable reference
- Use design tools to add visual elements (emotional arc graph, icons, colors by stage)
- Ensure all text from the table is preserved in the visual version

---

## Quality Checklist for Final Review

Before sharing a journey map:
- [ ] All stages have at least one touchpoint with a corresponding user action
- [ ] Every emotion is grounded in evidence (quote, explicit statement, or clear behavioral cue)
- [ ] Pain points are specific and tied to research data
- [ ] Opportunities are actionable and connected to pain points
- [ ] Confidence levels are assigned and defensible
- [ ] If multi-persona, divergence points are explicitly noted
- [ ] No assumptions or inferences appear without being labeled as such
- [ ] Stages are in logical (chronological or process) order
- [ ] Terminology is consistent across all rows
- [ ] Persona description (if applicable) appears at the top
- [ ] Research sources are cited or accessible to readers
- [ ] CSV export (if used) has been validated against markdown original
- [ ] Story structure analysis complete: climax identified, story shape named

---

## Story Structure Analysis

After completing a journey map, run a story structure analysis as a diagnostic check. This lens (from Donna Lichaw's storymapping framework, *The User's Journey*, 2016) identifies structural problems that column-by-column mapping may miss. It does not replace the evidence-grounded workflow — it runs after it.

### The narrative arc

Every user experience has a story shape. Map the 7 plot points onto your journey stages:

| Plot Point | What it represents in a journey map |
|---|---|
| **Exposition** | User's starting context — who they are, what they want, what's already in place |
| **Inciting incident** | The trigger that starts this journey (task assigned, notification, problem encountered) |
| **Rising action** | The sequence of steps; engagement and effort should build stage by stage |
| **Crisis** | The moment of maximum friction — a required action, a paywall, a cognitive hurdle, a dead end |
| **Climax / value peak** | The stage where the user most clearly experiences the product's value — the "aha" moment |
| **Falling action** | What happens after the peak — the user wraps up, downloads output, closes the flow |
| **End** | The user arrives in a better state than when they started |

Map each plot point to a stage in your journey. If a stage doesn't correspond to any plot point, question whether it belongs. If a plot point has no stage, flag the gap.

### Diagnosing the story shape

**Story with climax (ideal)** — Emotional engagement rises through the journey, peaks at a high-value moment, and winds down to a clear end. The user leaves having accomplished something meaningful.

**Flat journey** — Emotions and effort remain roughly constant throughout. No stage stands out as a peak. The experience is functional but unmemorable. Intervention: identify a moment that could be elevated (a confirmation, a result reveal, a completion signal, an unexpected capability).

**Anticlimactic journey** — Value is delivered too early. The user experiences the product's best moment in the first or second stage; the rest feels like aftermath. Intervention: resequence steps so effort and tension build before resolution arrives.

**Cliffhanger** — The journey ends without resolution. The user exits before meeting their goal (drop-off, error, dead end, forced handoff to another channel). Visible in analytics as funnel abandonment; visible in research as task non-completion or expressed frustration at exit. Intervention: identify the crisis stage driving the drop-off and redesign the path from crisis to climax.

### Identifying the climax (value peak)

Ask:
- At which stage does the user most clearly experience the product's value?
- At which stage would a user smile, say *"Oh — that's what this does"*, or feel their effort was worthwhile?
- Which moment do users mention spontaneously in interviews when asked "what worked?"

If you cannot identify a climax, the journey has no moment of value delivery — a critical design gap regardless of how smooth individual steps are.

### Peak-end rule

Users remember two moments disproportionately: **the peak** (highest emotional moment, positive or negative) and **the end**. Duration barely registers.

Implications for prioritization:
- Improving the climax stage has more impact on memory and repeat use than smoothing mid-journey friction
- The end must feel resolved — an unresolved ending is remembered as badly as a painful peak
- A painful crisis that is never resolved (cliffhanger) will define the user's memory of the experience, even if earlier stages were positive

When ranking opportunities, apply the peak-end rule: improvements to the climax and ending stages outweigh improvements to middle stages of comparable evidence strength.

### Opposing forces formula

For each opportunity, articulate it as: **A × B → C**

- **A** (forward momentum): The user's goal and their effort to reach it
- **B** (opposing force): The crisis or pain point blocking completion
- **C** (climax): The design solution that resolves the tension

Example: *"User wants to submit the weekly report quickly (A) but must re-enter data already in the system (B) → Pre-populate known fields from prior week so the submission takes under 2 minutes and feels effortless (C)."*

This framing makes opportunities more persuasive to stakeholders because it shows the arc from problem to resolution, not a disconnected list of improvements.

---

## Story Structure Pitfalls

*(Extends the Common Pitfalls section above.)*

### Pitfall 9: Flat journey — no discernible peak
**Problem**: Every stage is mapped at roughly the same emotional intensity. The map looks complete but has no value peak.
**Solution**: Before closing the map, identify one stage as the climax. If no stage qualifies, that is itself a finding: the product may not be delivering a clear moment of value. Flag it in the opportunity column.

### Pitfall 10: Treating a cliffhanger as a scope choice
**Problem**: A journey that ends mid-task is framed as "we only mapped onboarding" when it actually reveals that users cannot complete the experience.
**Solution**: Name the drop-off explicitly as a cliffhanger in the map. Mark the last-reached stage with Opportunity: "Resolve cliffhanger — user exits without meeting goal." Do not reframe structural abandonment as a deliberate scope boundary.

### Pitfall 11: Scoping mismatch
**Problem**: Mapping a multi-year lifecycle at the same granularity as a 5-minute task, or mapping a micro-task with so few stages that the journey loses meaning.
**Solution**: Declare the scope type (Epic / Micro / Serial) before mapping. Epic journeys tolerate 5–8 high-level stages. Micro-stories may have as few as 3, each with rich detail. Serial journeys should map one episode fully before considering the cycle.
