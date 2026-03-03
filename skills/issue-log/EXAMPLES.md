# Issue Log Examples

## Complete Example: Issue Log Table

This is a realistic issue log from a multi-session research cycle exploring an e-commerce checkout flow.

### Sample Issue Log (issue_log_MASTER.csv)

```
ID | Severity | Title | Description | Role Affected | Frequency | Effort | Status | Notes
TC-01 | Blocker | Shipping address field rejects valid ZIP codes | User entered ZIP code "90210" multiple times. Form repeatedly rejected with message "Invalid ZIP format." User tried with hyphens, spaces, and extra digits. Address could not be saved. User abandoned checkout. | Developer | 2x | Medium | Open | Session: 2025-02-10-TC; Session: 2025-02-12-TC; Timestamp: 14:33, 15:12; Appears to be regex validation bug
MB-01 | Major | Promo code input requires exact match syntax | User attempted to enter promo code "SAVE20" but received error "Invalid code." Code visible on website banner but system required "SAVE-20" with hyphen. User discovered correct format only after third attempt. | Designer | 1x | Low | In Design | Session: 2025-02-10-MB; Timestamp: 13:47; Design ticket: DS-1204
TC-02 | Major | Cart item quantity updates don't reflect in real-time | User increased item quantity from 1 to 3. Total price in cart header remained unchanged for 5 seconds. User clicked update button twice, unsure if change registered. Quantity eventually updated to 5 after second click. | Developer | 2x | Medium | In Build | Session: 2025-02-10-TC, Session: 2025-02-11-TC; Timestamp: 14:56, 10:23; Race condition in cart state management; PR pending: gh-1847
MB-02 | Minor | Shipping method descriptions are truncated on mobile | User viewed shipping options. "Express 2-day" label was cut off to "Express 2-d..." on mobile view. User tapped label to expand but hesitated briefly. Label full text appeared in tooltip after tap. | Designer | 1x | Low | Open | Session: 2025-02-10-MB; Timestamp: 16:04; Mobile-only issue; affects clarity of shipping choice
KL-01 | Minor | Form validation error icons don't match error text location | User encountered required field validation error. Red icon appeared next to street address label. Error message appeared in footer. User looked back and forth between fields before understanding which field had error. | Designer | 1x | Low | Resolved | Session: 2025-02-11-KL; Timestamp: 11:30; Fixed in release v2.3.1
MB-03 | Polish | Payment method selector could use loading state | User clicked payment method option. Selected state updated instantly (correct). Spinner doesn't appear during payment processing initiation. Experience feels unresponsive even though data loads in <200ms. | Developer | 1x | Low | Backlog | Session: 2025-02-12-MB; Timestamp: 15:45; Low priority; minor polish; could improve perceived performance
```

---

## Issue Severity Distribution

This example log contains:
- **1 Blocker** (TC-01) — Prevents checkout completion
- **2 Major** (MB-01, TC-02) — Significant friction; workarounds required
- **2 Minor** (MB-02, KL-01) — Confusion/inefficiency; task completes
- **1 Polish** (MB-03) — Cosmetic/delight improvement

---

## Priority Calculation Example

Using the Priority Formula: `(Frequency × Severity Weight + Role Impact) / Effort`

### Issue: TC-01 (Blocker: Shipping address ZIP code rejection)

```
Frequency: 2x = 2
Severity: Blocker = 4
Role Impact: High (core to checkout) = +2
Effort: Medium = 2

Priority Score = (2 × 4 + 2) / 2 = 10 / 2 = 5.0 (HIGHEST PRIORITY)
```

### Issue: MB-02 (Minor: Truncated shipping labels)

```
Frequency: 1x = 1
Severity: Minor = 2
Role Impact: Medium (affects choice clarity) = +1
Effort: Low = 1

Priority Score = (1 × 2 + 1) / 1 = 3 / 1 = 3.0 (MEDIUM PRIORITY)
```

### Issue: MB-03 (Polish: Missing loading state)

```
Frequency: 1x = 1
Severity: Polish = 1
Role Impact: Low (cosmetic) = +0
Effort: Low = 1

Priority Score = (1 × 1 + 0) / 1 = 1 / 1 = 1.0 (LOWEST PRIORITY)
```

**Priority Ranking:**
1. TC-01: 5.0 (Blocker) — Address immediately
2. TC-02: 4.0 (Major, 2x frequency) — Address before launch
3. MB-01: 3.5 (Major, 1x) — Design before launch
4. MB-02: 3.0 (Minor) — Backlog; fix next cycle
5. KL-01: 2.0 (Minor, already resolved) — Closed
6. MB-03: 1.0 (Polish) — Backlog; nice-to-have

---

## Issue Summary Snapshot

### By Severity

| Severity | Count | Critical Path | Examples |
|----------|-------|----------------|----------|
| Blocker | 1 | Prevent checkout | ZIP code validation failure |
| Major | 2 | High friction | Promo code syntax, cart quantity sync |
| Minor | 2 | Confusion | Truncated labels, error icon placement |
| Polish | 1 | Delight | Loading state animation |

### By Status

| Status | Count | Action Required |
|--------|-------|-----------------|
| Open | 4 | Design or engineering review |
| In Design | 1 | Awaiting design specification |
| In Build | 1 | In active development (PR pending) |
| Resolved | 1 | Released in v2.3.1 |
| Backlog | 1 | Deferred; low priority |

### By Effort

| Effort | Count | Avg Priority | Notes |
|--------|-------|--------------|-------|
| Low | 4 | 2.5 | Quick wins; UI/UX fixes |
| Medium | 2 | 4.5 | Logic or state management changes |
| High | 0 | — | No architectural changes identified |

### By Role Impact

| Role | Count | Primary Issues | Severity Mix |
|------|-------|----------------|--------------|
| Developer | 3 | Checkout flow bugs, state management | 1 Blocker, 1 Major, 1 Polish |
| Designer | 3 | Mobile UX, error messaging, promo clarity | 1 Major, 2 Minor |

---

## Session Metadata

### Sessions Included in This Log

| Session ID | Participant | Role | Date | Focus Area | Issues Found |
|------------|-------------|------|------|-----------|--------------|
| 2025-02-10-TC | Thomas Chen | Developer | 2025-02-10 | Checkout & payments | 3 (TC-01, TC-02, MB-01*) |
| 2025-02-10-MB | Maya Barrera | Designer | 2025-02-10 | Visual design & mobile | 2 (MB-01*, MB-02) |
| 2025-02-11-TC | Thomas Chen | Developer | 2025-02-11 | Cart updates | 1 (TC-02*) |
| 2025-02-11-KL | Kevin Lin | QA Engineer | 2025-02-11 | Form validation | 1 (KL-01) |
| 2025-02-12-TC | Thomas Chen | Developer | 2025-02-12 | Regression testing | 0 new |
| 2025-02-12-MB | Maya Barrera | Designer | 2025-02-12 | Mobile checkout | 1 (MB-03) |

*Asterisk indicates issue observed with multiple participants

---

## Description Quality Examples

### Example 1: Blocker Issue

**Poor Description:**
"ZIP code validation is broken."

**Better Description:**
"User entered valid 5-digit ZIP code '90210' in shipping address field. Form submitted but returned generic error 'Invalid ZIP format.' User attempted 4 different formats (90210, 90210-0000, 90-210, etc.) without success. After 8 minutes, user stated 'I can't get past this step' and abandoned checkout."

### Example 2: Major Issue

**Poor Description:**
"Promo codes are hard to use."

**Better Description:**
"User saw promotional banner offering 'SAVE20' discount. Entered 'SAVE20' in promo code field. System rejected with message 'Invalid code.' User tried variations: 'SAVE-20', 'save20', 'SAVE 20'. Only 'SAVE-20' (with hyphen) was accepted. User discovered correct format through trial-and-error after 3 failed attempts."

### Example 3: Minor Issue

**Poor Description:**
"Text is cut off on mobile."

**Better Description:**
"User viewed shipping method selection on mobile device (375px width). Shipping option label 'Express 2-day delivery' displayed as 'Express 2-d...' due to text truncation. User tapped label; full text appeared in tooltip. User said, 'I need to click to see what this means,' indicating label alone was insufficient."

### Example 4: Polish Issue

**Poor Description:**
"Add a loading spinner."

**Better Description:**
"User clicked payment method option. Selected state updated immediately (correct behavior). No visual loading indicator appears during payment processing, even though backend request takes ~150ms. User said the interaction 'feels instant but uncertain whether anything is happening.'"

---

## Aggregation Example: Deduplication

When the same issue appears with multiple participants, consolidate into single log entry:

### Before Aggregation (Two Session Logs)

**Session-A (Thomas Chen):**
| ID | Severity | Title | Description |
|----|----------|-------|-------------|
| TC-01 | Blocker | Shipping address ZIP validation fails | [full description] |

**Session-B (Maya Barrera):**
| ID | Severity | Title | Description |
|----|----------|-------|-------------|
| MB-01 | Blocker | Shipping address ZIP validation fails | [full description] |

### After Aggregation (Master Log)

| ID | Severity | Title | Description | Frequency | Notes |
|----|----------|-------|-------------|-----------|-------|
| ZIP-VALIDATION-001 | Blocker | Shipping address ZIP validation fails | [full description] | 2x | Observed with TC (2025-02-10), MB (2025-02-11); Affects all users; likely regex bug |

---

## Exporting and Sharing

### CSV Format (Plain Text, Pipe-Delimited)
Copy the issue log table directly into shared document or GitHub issue tracker.

### Markdown Format
Use this skill's EXAMPLES.md as template to create GitHub wiki page or Confluence documentation.

### JSON Export (Optional)
```json
{
  "issue_log": [
    {
      "id": "TC-01",
      "severity": "Blocker",
      "title": "Shipping address field rejects valid ZIP codes",
      "description": "User entered ZIP code '90210'...",
      "role_affected": "Developer",
      "frequency": "2x",
      "effort": "Medium",
      "status": "Open",
      "priority_score": 5.0,
      "sessions": ["2025-02-10-TC", "2025-02-12-TC"],
      "timestamps": ["14:33", "15:12"]
    }
  ]
}
```
