---
name: discussion-guide
description: "Generates a teleprompter-ready facilitator script for moderated research sessions. Use when planning a usability test, discovery interview, concept validation, or expert interview. Produces a fully scripted guide with timestamped parts, rationale, topic tracker, facilitator speech, stage directions, probes, and transition prompts. Triggers: discussion guide, moderator guide, facilitator script, interview guide, usability script, session script, interview protocol."
author: "Juan Reina (they/them)"
license: "MIT"
last_updated: 2026-02-28
---

# Discussion Guide

> Apply `CORE.md` epistemic framework before writing. **Ask for participant pronouns before finalizing; default to they/them.** See `PIPELINE.md` for upstream/downstream handoffs.

**Input**: Research plan, session type, participant persona, session duration, P0 research questions, optional session start time.
**Output**: Production-ready facilitator script — every word spoken is written out, stage directions in brackets, probes labeled, timestamps explicit.

---

## Workflow

1. **Read the research plan** — Identify session type, persona, duration, and the full P0/P1/P2 question list. Every P0 must map to a designated section. None left to chance or improvisation.

2. **Build the topic tracker first** — List all themes by priority (P0/P1/P2). This is used by the note-taker during the live session as a real-time coverage checklist.

3. **Plan the time budget** — Parts must sum to total session duration. Budget guidance: consent + intro ≈ 8–10 min; tasks almost always run 20% over; debrief is frequently cut. Flag any part at risk of overrun.

4. **Follow canonical section order**:
   - `PART 0` — Pre-session checklist *(not read aloud)*
   - `PART 1` — Introduction & setup
   - `PART 2` — Consent & ground rules
   - `PART 3` — Warm-up (current experience only; no prototype mention)
   - `PART 4–N` — Tasks or topic areas
   - `PART N+1` — Debrief & hypothesis validation
   - `PART N+2` — Close

5. **Write for the spoken word** — Short sentences. Transitions written explicitly. No academic vocabulary. Anyone on the team should be able to pick this up and run the session.

6. **Separate speech from direction** — Format is strict:
   - Facilitator speech → `> blockquote`
   - Stage directions → `[BRACKETS IN CAPS]`
   - Probes → `→ PROBE:` *(optional; select 1–2 based on what participant shares; not sequential)*
   - Conditional paths → `⚑ IF [SCENARIO]:`
   - Note-taker actions → `📋 NOTE-TAKER:`

7. **Write section rationale** — 2–3 sentences before each part explaining what this section achieves and why it's placed here.

8. **Frame warm-up questions for the present** — Past tense ("Tell me about the last time..."), tool-agnostic ("How do you currently..."), no prototype mention.

9. **Write probes as options** — 3–5 per main question. Facilitator selects 1–2. Mark clearly as optional.

10. **Include a transition prompt for every part** — Last line closes the section and opens the next. Never leave the facilitator to improvise a segue.

11. **Tone requirements** — Clear, polite, appreciative, slightly hesitant. Prefer invitations over commands:
    - Avoid: "Tell me about X." / "What do you think of this?"
    - Prefer: "I'd love to hear about X, if you're open to sharing." / "I'm curious what's going through your mind right now."
    - Use natural hedges: "I wonder if..." / "Just whenever you're ready..." / "There's no rush."

12. **Quality check** — Run all quality gates below before delivering.

---

## Required Consent Elements (PART 2)

Every guide must include all of the following:

| Element | Purpose |
|---------|---------|
| Recording consent (voice, screen, video) | Legal and ethical baseline |
| Ground rule: honesty | Reduce social desirability bias |
| Ground rule: ask for clarification freely | Reduce misunderstood questions |
| Ground rule: designs not you | Reduce performance anxiety |
| Ground rule: questions welcome | Reduce participant passivity |
| Confidentiality statement | Build trust |
| Anonymity opt-in | Respect participant autonomy |
| Silence / note-taking acknowledgment | Prevent awkward silence from derailing session |
| "Any questions before we start?" | Final check before research begins |

---

## Part Block Structure

```
## PART [N] — [SECTION NAME]
**⏱ Duration:** X min | **Elapsed:** HH:MM–HH:MM | **Clock:** HH:MM–HH:MM

**🎯 Covers:** [research questions or topics addressed]

**💡 Rationale:** [2–3 sentences]

---

[PRE-SECTION STAGE DIRECTIONS IF ANY]

> [FACILITATOR SPEECH — verbatim, as blockquote]

→ PROBE: [optional follow-up]
→ PROBE: [optional follow-up]

⚑ IF [SCENARIO]: [conditional path]

📋 NOTE-TAKER: [observation instruction]

> [TRANSITION — last line that opens the next section]
```

*Clock times assume a 10:00 AM start. Update the `Session Start Time` header field before each session.*

---

## Output

Save as `Discussion_Guide_[SESSION_TYPE].md` in the seed's `01_Plan/` directory.

---

## Quality Gates

✓ Every P0 question maps to a specific part and question number
✓ Time budget sums to total session duration
✓ Consent covers recording (voice + screen + video), 4 ground rules, confidentiality, anonymity, silence note
✓ Warm-up questions are prototype-agnostic and answerable in current tools
✓ Every task framed as a scenario ("Imagine you need to..."), not a command
✓ Probes labeled optional; not numbered sequentially
✓ Every part has a rationale block and a transition prompt
✓ Tone is polite, appreciative, and slightly hesitant throughout
✓ Pronouns confirmed or defaulted to neutral
✓ File saved to the correct seed's `01_Plan/` directory

---

## References

- `REFERENCE.md` — probe types, pacing rules, handling difficult moments, note-taker coordination, topic tracker format
- `TEMPLATE.md` — blank template structure for producing new guides
