# Thematic Coding — Worked Example

This example walks through a complete thematic coding run: from raw session notes across three sessions to a finished codebook and coded dataset. The study is a discovery interview series about a B2B document management tool.

---

## Starting point: raw evidence from session notes

Three sessions. Evidence extracted from `observations[]`, `quotes[]`, and `pain_points[]` fields.

**Session S01** — P1, Content Manager, experienced user
**Session S02** — P2, Legal Analyst, occasional user
**Session S03** — P3, Content Manager, new user (3 weeks)

---

## Step 2 output — Atomic decomposition

| Unit_ID | Session | Participant | Role | Type | Evidence Unit |
|---------|---------|-------------|------|------|---------------|
| U-001 | S01 | P1 | Content Manager | quote | "I keep a spreadsheet on the side because I can never find what I uploaded last week." |
| U-002 | S01 | P1 | Content Manager | observation | Opened "Recent" tab, scrolled without finding the file, navigated to four folders before locating the document. |
| U-003 | S01 | P1 | Content Manager | pain_point | Cannot search by upload date — only by file name or tag. |
| U-004 | S01 | P1 | Content Manager | quote | "I'm never sure if my version is the latest one. I'll just email the author to double-check." |
| U-005 | S01 | P1 | Content Manager | observation | Downloaded a document, then immediately re-opened the web version to compare modification dates. |
| U-006 | S02 | P2 | Legal Analyst | quote | "The sharing dialog is — I genuinely do not understand what 'view' vs. 'edit' does in practice." |
| U-007 | S02 | P2 | Legal Analyst | pain_point | Cannot tell which colleagues currently have access to a document after sharing it. |
| U-008 | S02 | P2 | Legal Analyst | observation | Attempted to restrict access by removing their own name from the share list. Restored after 90 seconds of confusion. |
| U-009 | S02 | P2 | Legal Analyst | quote | "Every time I export to PDF the formatting breaks. I send Word files instead." |
| U-010 | S02 | P2 | Legal Analyst | pain_point | PDF export loses table formatting; workaround is always Word. |
| U-011 | S03 | P3 | Content Manager | observation | Spent 4 minutes looking for a "Save" button before discovering the system autosaves. |
| U-012 | S03 | P3 | Content Manager | quote | "Wait — did that just save? How do I know?" |
| U-013 | S03 | P3 | Content Manager | pain_point | No visible save confirmation; new user assumed data would be lost. |
| U-014 | S03 | P3 | Content Manager | observation | Created two identical documents on separate days, unaware the first already existed. |
| U-015 | S03 | P3 | Content Manager | quote | "I feel like I'm always starting from scratch. I don't know if something is already in here." |

---

## Step 3 output — First-pass clusters (affinity mapping)

```
Cluster A: U-001, U-002, U-003, U-014, U-015
"Can't find things" — navigation, retrieval, duplicate creation

Cluster B: U-004, U-005, U-012, U-013
"Doesn't know if state is accurate" — save state, version currency, system feedback

Cluster C: U-006, U-007, U-008
"Doesn't understand permissions" — sharing, access control, permission semantics

Cluster D: U-009, U-010
"Export breaks things" — PDF formatting, workaround adoption

Outliers: none — all units found a cluster
```

---

## Step 4 output — Cluster names

| Cluster | Name |
|---------|------|
| A | Lost previous work — can't relocate or recognize |
| B | Can't confirm system followed through |
| C | Sharing and access feel opaque |
| D | Export fails; workarounds become default |

---

## Step 5 output — Codebook

---

### TC-01: Lost previous work — can't relocate or recognize

**Definition**: Participant cannot locate a document, version, or result of previous work without significant effort, or does not recognize that their previous work already exists in the system. Expressed as folder navigation, workaround filing systems (external spreadsheets), or duplicate creation.

**Inclusion**: Folder searching that ends in the wrong location or takes > 3 navigation steps; maintaining external lists to compensate for in-system findability; creating a duplicate without realizing an original exists; verbal statements about inability to find prior work.

**Exclusion**: Difficulty finding *new* information or content from others — that is a search/discovery problem distinct from relocating one's own work. Confusion about file organization systems not caused by the product (e.g., organizational naming conventions).

**Examples**:
- U-001: "I keep a spreadsheet on the side because I can never find what I uploaded last week."
- U-002: Opened "Recent" tab, scrolled without finding the file, navigated to four folders.
- U-014: Created two identical documents on separate days, unaware the first existed.

---

### TC-02: Can't confirm system followed through

**Definition**: Participant cannot determine whether an action they took (saving, submitting, sharing) was successfully completed by the system. Expressed as verification behaviors (checking a second source), explicit uncertainty statements, or searching for feedback the system does not provide.

**Inclusion**: Repeated or redundant actions to verify a single intended action; downloading and re-opening to confirm version; searching for a save button that doesn't exist; verbal expressions of uncertainty about action completion or data accuracy.

**Exclusion**: Confusion about *how* to perform an action (that is TC-03 or a usability finding). Distrust stemming from a confirmed bug or data loss — this theme applies when the system performed correctly but feedback was absent.

**Examples**:
- U-004: "I'm never sure if my version is the latest one. I'll just email the author to double-check."
- U-005: Downloaded a document, then re-opened the web version to compare modification dates.
- U-012: "Wait — did that just save? How do I know?"

---

### TC-03: Sharing and access feel opaque

**Definition**: Participant cannot determine what permissions they are granting, have granted, or currently hold, when using the sharing and access control features. Expressed as confusion about permission labels, inability to verify current access state, or incorrect actions taken based on misunderstanding.

**Inclusion**: Verbal confusion about permission semantics ("I don't know what 'edit' means in practice"); inability to see current access recipients after sharing; unintended changes to own access during permission modification; workarounds that bypass sharing features entirely.

**Exclusion**: General discomfort with sharing (organizational policy concern, not product usability). Document search — if the issue is finding a document someone shared *with* the participant, code to TC-01.

**Examples**:
- U-006: "I genuinely do not understand what 'view' vs. 'edit' does in practice."
- U-007: Cannot tell which colleagues currently have access after sharing.
- U-008: Attempted to restrict access by removing own name from the share list.

---

### TC-04: Export fails; workaround becomes default

**Definition**: Participant's intended output format (typically PDF) produces a degraded result, causing them to adopt a workaround output format (typically Word/DOCX) as their permanent default workflow. The workaround is not an occasional fix — it has replaced the intended workflow.

**Inclusion**: Statements that a workaround is "what I always do now"; behavioral evidence of sending/exporting in a non-preferred format; explicit description of the export failure and its consequence (formatting break, data loss, etc.).

**Exclusion**: One-time export failure without behavioral adaptation. Feature requests for new export formats (different from a failing existing format).

**Examples**:
- U-009: "The formatting breaks. I send Word files instead."
- U-010: PDF export loses table formatting; workaround is always Word.

*Note: This theme has only 2 evidence units, both from P2 (S02). Treat as Medium confidence — minority theme. Single-session, single-participant. Recommend probing in future sessions.*

---

## Step 6 output — Coded dataset

| Unit_ID | Session | Participant | Role | Type | Evidence Unit | Theme_Codes | Multi_Code | Confidence | Notes |
|---------|---------|-------------|------|------|---------------|-------------|------------|------------|-------|
| U-001 | S01 | P1 | Content Manager | quote | "I keep a spreadsheet on the side because I can never find what I uploaded last week." | TC-01 | — | High | Classic TC-01; workaround behavior |
| U-002 | S01 | P1 | Content Manager | observation | Opened "Recent" tab, scrolled without finding, navigated four folders. | TC-01 | — | High | Behavioral evidence |
| U-003 | S01 | P1 | Content Manager | pain_point | Cannot search by upload date. | TC-01 | — | High | Root cause of TC-01 pattern for P1 |
| U-004 | S01 | P1 | Content Manager | quote | "I'm never sure if my version is the latest one. I'll just email the author." | TC-02 | — | High | Compensatory communication behavior |
| U-005 | S01 | P1 | Content Manager | observation | Downloaded doc, re-opened web version to compare dates. | TC-02 | — | High | Dual-source verification behavior |
| U-006 | S02 | P2 | Legal Analyst | quote | "I genuinely do not understand what 'view' vs. 'edit' does in practice." | TC-03 | — | High | Explicit permission confusion |
| U-007 | S02 | P2 | Legal Analyst | pain_point | Cannot see who has access after sharing. | TC-02,TC-03 | TC-02+TC-03 | Medium | TC-03 primary (permission opacity); also TC-02 (can't confirm share succeeded) |
| U-008 | S02 | P2 | Legal Analyst | observation | Tried to restrict access by removing own name. Restored after 90 seconds. | TC-03 | — | High | Behavioral evidence of permission model mismatch |
| U-009 | S02 | P2 | Legal Analyst | quote | "Every time I export to PDF the formatting breaks. I send Word files instead." | TC-04 | — | Medium | Minority theme; single session |
| U-010 | S02 | P2 | Legal Analyst | pain_point | PDF export loses table formatting; always use Word as workaround. | TC-04 | — | Medium | Minority theme; corroborates U-009 |
| U-011 | S03 | P3 | Content Manager | observation | Spent 4 minutes looking for "Save" button before discovering autosave. | TC-02 | — | High | Missing feedback at moment of expectation |
| U-012 | S03 | P3 | Content Manager | quote | "Wait — did that just save? How do I know?" | TC-02 | — | High | Direct verbal expression of TC-02 |
| U-013 | S03 | P3 | Content Manager | pain_point | No visible save confirmation; assumed data would be lost. | TC-02 | — | High | Behavioral consequence of absent feedback |
| U-014 | S03 | P3 | Content Manager | observation | Created two identical documents, unaware the first existed. | TC-01 | — | High | Duplicate creation = findability failure |
| U-015 | S03 | P3 | Content Manager | quote | "I feel like I'm always starting from scratch. I don't know if something is already in here." | TC-01,TC-02 | TC-01+TC-02 | High | TC-01 (can't locate prior work) + TC-02 (uncertain what the system holds) |

---

## Step 8 output — Theme summary

| Theme ID | Theme Name | Evidence Count | Sessions | Participants | Roles | Confidence | Negative Cases | Feeds Into |
|----------|-----------|---------------|----------|--------------|-------|------------|----------------|------------|
| TC-01 | Lost previous work — can't relocate or recognize | 6 | S01, S03 | P1, P3 | Content Manager only | High | 0 found | journey-mapping, hmw-extraction |
| TC-02 | Can't confirm system followed through | 7 | S01, S02, S03 | P1, P2, P3 | Content Manager, Legal Analyst | High | 0 found | journey-mapping, hmw-extraction, issue-log |
| TC-03 | Sharing and access feel opaque | 3 | S02 | P2 | Legal Analyst only | Medium — single-session, single-role | 0 found | hmw-extraction, issue-log |
| TC-04 | Export fails; workaround becomes default | 2 | S02 | P2 | Legal Analyst only | Low — minority theme | 0 found | issue-log |

**Edge and variance scan notes**: TC-01 and TC-02 are strong themes with cross-session support. TC-03 and TC-04 originate entirely from S02/P2 (Legal Analyst). Content Managers are not represented in TC-03 and TC-04; Legal Analysts are not represented in TC-01. These are role-specific patterns — downstream skills should not generalize them to all users without additional sessions with Legal Analysts.

**Negative case search results**: No contradicting evidence found in this dataset. All three Content Managers expressed TC-01 or TC-02 behaviors. However: this study has only 3 sessions and 3 participants. Absence of negative cases may reflect homogeneous sample and small N, not robust saturation. Recommend additional sessions before treating TC-01 and TC-02 as confirmed high-confidence themes.

---

## What feeds downstream

| Theme | → Journey Mapping | → HMW Extraction | → Saturation Analysis |
|-------|------------------|------------------|----------------------|
| TC-01 | Stage: "Returning to prior work" — high friction, negative emotion | HMW: How might we help content managers resume previous work without rebuilding context? | Theme: "Retrieval and findability" |
| TC-02 | Stage: "Completing an action" — low confidence, verification loop | HMW: How might we confirm every consequential action so users can trust the system's state? | Theme: "System feedback and trust" |
| TC-03 | Stage: "Sharing a document" — confusion, risk of error | HMW: How might we make permission changes legible before and after they are applied? | Theme: "Permission model opacity" |
| TC-04 | Stage: "Exporting for external use" — workaround adoption | HMW: How might we ensure exported documents preserve their intended formatting without intervention? | Theme: "Export reliability" |
