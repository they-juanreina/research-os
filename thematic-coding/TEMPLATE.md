# Thematic Coding Templates

---

## Template 1 — Codebook Entry

Copy one block per theme. Fill all fields before second-pass coding begins.

```
---
THEME: [Short label — 2–5 words, participant-frame pattern]
ID: TC-[NN]
Confidence target: [High / Medium / Low — based on expected evidence]
Added: [First-pass / Post-second-pass residual]
---

Definition:
[1–2 sentences. What does this theme capture, from the participant's frame?
State what they experience or believe — not what the design does wrong.]

Inclusion criteria:
[What qualifies as this theme? Be specific enough to decide a borderline case.
List behavioral signals, verbal markers, and contextual conditions.]

Exclusion criteria:
[What is NOT this theme? Especially: name adjacent themes this one could be confused with
and draw the line explicitly.]

Examples (fill after first-pass clustering):
- [Evidence unit verbatim]
- [Evidence unit verbatim]
- [Evidence unit verbatim — optional third]

Negative cases (fill after second-pass coding):
- [Any evidence unit that contradicts the dominant pattern — or write "None found — search documented [date]"]

Role concentration: [Distributed / Concentrated: [role] / Single-role: [role]]
```

---

## Template 2 — Coded Dataset (CSV headers)

```
Unit_ID,Session_ID,Participant_ID,Role,Type,Evidence_Unit,Theme_Codes,Multi_Code,Confidence,Notes
```

**Field definitions**:

| Column | Format | Description |
|--------|--------|-------------|
| Unit_ID | U-001, U-002, … | Sequential across full dataset |
| Session_ID | S01, S02, … | Matches session note filenames |
| Participant_ID | P1, P2, … | Consistent with session notes |
| Role | Text | Participant's job title or role label |
| Type | observation / quote / pain_point | Source field in session notes |
| Evidence_Unit | Text | Verbatim or near-verbatim unit |
| Theme_Codes | TC-01 or TC-01,TC-02 | Comma-separated if multi-coded |
| Multi_Code | — or TC-01+TC-02 | Only populate when multi-coding |
| Confidence | High / Medium / Low / — | Low or — for RESIDUALs |
| Notes | Text | Anything relevant to downstream use |

**Special values for Theme_Codes**:
- `RESIDUAL` — does not fit any current theme
- `CONTRADICTS:TC-[NN]` — actively contradicts the named theme; record under that theme's negative cases

---

## Template 3 — Theme Summary Table

```markdown
## Theme Summary

| Theme ID | Theme Name | Evidence Count | Sessions | Participants | Roles | Confidence | Negative Cases | Feeds Into |
|----------|-----------|---------------|----------|--------------|-------|------------|----------------|------------|
| TC-01 | | | | | | | | |
| TC-02 | | | | | | | | |
| TC-03 | | | | | | | | |

**Edge and variance scan notes**:
[Who is absent from each theme? Which themes are role-concentrated?
Which participants contributed to no theme's evidence?]

**Negative case search notes**:
[How was the search conducted? What was found and not found?
What does the absence of negative cases mean given this sample size?]

**Residuals**:
[List unresolved RESIDUAL units here. Note count and whether any cluster was identified.]
```

---

## Template 4 — Codebook Header (file-level)

Place at the top of `themes-[seed].md` before individual theme entries.

```markdown
---
document type: thematic codebook
seed: [Seed Name]
seed_id: [seed_ID]
date: [YYYY-MM-DD]
researcher: [name]
sessions coded: [S01, S02, …]
total participants: [N]
total evidence units: [N]
coding mode: [Affinity mapping → formalized / Thematic coding / Hybrid]
inter-rater check: [Yes — N% agreement / No — single coder]
version: 1.0
---

# Thematic Codebook: [Seed Name]

## Codebook evolution log
- v1.0 [date]: Initial codebook — [N] themes from first-pass affinity mapping
- [future entries as themes are added or revised]

## Sessions coded
| Session ID | Date | Participants | Roles | Notes |
|-----------|------|--------------|-------|-------|
| S01 | | | | |

## Exclusions
[Any sessions excluded from coding and reason]

---
```
