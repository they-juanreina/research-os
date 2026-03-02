# Heuristic Assertion Patterns

Playwright detection patterns for each of Nielsen's 10 heuristics. Specifies what
can be detected automatically vs. what requires visual or AI judgment.

Use this reference when writing or customizing Phase 2 test scripts.

---

## H1 — Visibility of System Status
*Keep users informed about what is going on, through appropriate feedback within a reasonable time.*

**Playwright can detect:**
- No loading indicator after click (check for visible element within 3s)
- No success or error message after form submit
- Console errors suggesting silent failures
- Network requests returning 4xx/5xx without corresponding UI feedback
- Loading state persisting > 5 seconds without change

**Selector patterns:**
```typescript
// Loading / progress indicators
text=/loading|spinner|processing|saving|saved|success|error|failed/i
[aria-label*="loading"], [role="progressbar"], .loading, .spinner

// Check for feedback after critical action
await page.waitForSelector('[role="alert"], .success, .notification', { timeout: 3000 })
  .catch(() => saveFinding({ heuristic: 'H1', severity: 3, evidence: 'No feedback after action' }));
```

**Severity guide:**
- Severity 4: Submit with no feedback at all for > 5s
- Severity 3: Submit with no feedback for 3–5s
- Severity 2: Generic "something went wrong" with no specifics
- Severity 1: Feedback exists but is easy to miss (low contrast, small text)

---

## H2 — Match Between System and the Real World
*Speak the users' language. Use words, phrases, and concepts familiar to the user.*

**Playwright can detect:**
- Form field labels with technical IDs (snake_case, uuid, hash)
- Error messages referencing HTTP status codes or raw exceptions
- Date formats inconsistent with locale

**Requires visual/AI judgment:**
- Jargon vs. plain language in body copy and navigation
- Icons that don't match their intended meaning
- Confusing terminology in instructions or tooltips

**Selector patterns:**
```typescript
// Labels that look like database field names
page.locator('label').filter({ hasText: /[_][a-z]|uuid|uid|hash|\bid\b/i })

// Error messages with technical content
page.locator('[role="alert"], .error').filter({
  hasText: /400|404|500|Internal Server Error|undefined|null|exception/i
})
```

**Mark all H2 findings as:** `Source: Visual review` unless they match an automated selector.

---

## H3 — User Control and Freedom
*Users often choose system functions by mistake and need clearly marked "emergency exits."*

**Playwright can detect:**
- Modal dialogs without a visible close button or Cancel option
- Multi-step forms without a Back button
- Destructive action buttons without a confirmation step
- No undo option after significant destructive action

**Selector patterns:**
```typescript
// Modal without close control — test BOTH close button AND Escape key
const dialogs = page.locator('[role="dialog"]');
for (let i = 0; i < await dialogs.count(); i++) {
  const dialog = dialogs.nth(i);
  const hasClose = await dialog.locator(
    '[aria-label*="close" i], button:has-text("Cancel"), button:has-text("Close"), button:has-text("×")'
  ).count() > 0;
  if (!hasClose) {
    saveFinding({ heuristic: 'H3', severity: 3, evidence: 'Modal lacks visible close/cancel control' });
  }
  // Escape-key dismissal test
  await page.keyboard.press('Escape');
  const stillVisible = await dialog.isVisible().catch(() => false);
  if (stillVisible) {
    saveFinding({ heuristic: 'H3', severity: 2, evidence: 'Modal does not close on Escape key press' });
  }
}

// Multi-step form without Back
page.locator('[data-step], .step-form, .wizard').filter({
  hasNot: page.locator('button:has-text("Back"), button:has-text("Previous")')
})
```

---

## H4 — Consistency and Standards
*Users should not have to wonder whether different words, situations, or actions mean the same thing.*

**Playwright can detect:**
- Primary CTA button labels that differ across pages for the same action
- Multiple icon library sources mixed in the same UI (conflicting SVG paths)
- Inconsistent heading capitalization across navigation elements

**What to collect:**
Track all primary CTA labels across pages and compare. Track heading and nav label
capitalization (Title Case vs Sentence case — look for inconsistencies in the same surface).

```typescript
// Collect all primary button labels across pages for comparison
const primaryButtons = await page.locator('button[type="submit"], .btn-primary').allTextContents();
// Compare across test runs — flag if same action has different labels

// Store per-page for cross-page comparison at the end of the run
buttonLabelsPerPage[currentPageName] = primaryButtons;
```

**Requires visual/AI judgment:**
- Whether navigation structure is consistent between sections
- Whether the interaction model is consistent (drag in one place but button in another)

---

## H5 — Error Prevention
*Better to prevent errors in the first place. Check for problematic conditions before users commit.*

**Playwright can detect:**
- Forms that submit with empty required fields
- No client-side validation on email, phone, or URL fields
- Password fields without inline requirements before submission attempt
- Irreversible actions reachable in a single click
- Network errors (4xx) triggered by foreseeable user input

**Test approach:** Submit forms with deliberately bad data and observe.

```typescript
// Test missing validation
await page.fill('input[type="email"]', 'notanemail');
await page.click('button[type="submit"]');
const errorShown = await page.locator(
  '[role="alert"], .form-error, [aria-invalid="true"], .field-error'
).isVisible().catch(() => false);
if (!errorShown) {
  saveFinding({
    heuristic: 'H5 Error prevention',
    severity: 4,
    evidence: 'Form accepted invalid email format without inline validation'
  });
}

// Check for confirm dialog on destructive action
page.once('dialog', dialog => {
  if (dialog.type() === 'confirm') return; // good
  saveFinding({
    heuristic: 'H5 Error prevention',
    severity: 3,
    evidence: `Destructive action triggered dialog of type "${dialog.type()}" — not a confirm`
  });
});
await page.click('button:has-text("Delete")').catch(() => {});
```

---

## H6 — Recognition Over Recall
*Minimize memory load. Objects, actions, and options should be visible.*

**Playwright can detect:**
- Inputs without associated visible labels (not aria-label — actual `<label>` elements)
- Icon-only buttons without `aria-label` or `title` (inaccessible to screen readers and unclear to sighted users)
- Navigation items without text labels

**Selector patterns:**
```typescript
// Inputs missing visible labels
const inputs = page.locator(
  'input:not([type="hidden"]):not([type="submit"]):not([type="button"]):not([type="reset"])'
);
for (let i = 0; i < await inputs.count(); i++) {
  const input = inputs.nth(i);
  const id = await input.getAttribute('id');
  const hasLabel = id ? await page.locator(`label[for="${id}"]`).count() > 0 : false;
  const hasAriaLabel = !!(await input.getAttribute('aria-label') || await input.getAttribute('aria-labelledby'));
  if (!hasLabel && !hasAriaLabel) { /* save finding */ }
}

// Icon-only buttons
page.locator('button:not([aria-label]):not([title])').filter({
  hasNot: page.locator(':has-text(/.+/)')
})
```

---

## H7 — Flexibility and Efficiency of Use
*Accelerators, unseen by novice users, may speed up interaction for experts.*

**Playwright can detect:**
- Absence of search functionality on content-heavy pages
- No `accesskey` attributes (limited proxy for keyboard shortcuts)
- Lack of bulk operation when list items are present

**Mostly visual/AI judgment** for this heuristic.  
Note the absence of efficiency features as findings rather than violations
unless the product is explicitly targeted at expert/power users.

---

## H8 — Aesthetic and Minimalist Design
*Dialogues should not contain irrelevant or rarely needed information.*

**Playwright can detect:**
- Mobile: touch targets < 44×44px
- Mobile: horizontal overflow (`scrollWidth > innerWidth`)
- Body text < 14px font size
- More than 3–4 different font sizes on a single page
- Cookie banners / entry modals blocking main content on first visit

**Viewport checks (mobile project only):**
```typescript
const hasHorizontalScroll = await page.evaluate(
  () => document.body.scrollWidth > window.innerWidth
);
if (hasHorizontalScroll) {
  saveFinding({
    heuristic: 'H8 Aesthetic and minimalist design',
    severity: 3,
    evidence: `Horizontal overflow — scrollWidth: ${
      await page.evaluate(() => document.body.scrollWidth)
    }px vs innerWidth: ${await page.evaluate(() => window.innerWidth)}px`
  });
}
```

---

## H9 — Help Users Recognize, Diagnose, and Recover from Errors
*Error messages should be in plain language, indicate the problem, and suggest a solution.*

**Playwright can detect:**
- Error messages containing only a code or icon (text length < 20 chars is a proxy)
- Error messages with generic phrases ("Something went wrong")
- Form validation that clears all field values on error

**Test approach:** Trigger errors deliberately and inspect message content.

```typescript
const errorText = await page.locator('[role="alert"], .error, .form-error').textContent()
  .catch(() => '');
if (errorText && errorText.trim().length < 20) {
  saveFinding({
    heuristic: 'H9 Error recovery',
    severity: 3,
    evidence: `Error message too vague: "${errorText.trim()}"`
  });
}
```

**Requires visual review:**
- Whether the message actually suggests an actionable fix (not just names the problem)
- Whether field values are preserved after a validation error

---

## H10 — Help and Documentation
*Even when the system can be used without documentation, help should be available.*

**Playwright can detect:**
- Broken help/support links (HTTP 404 on `/help`, `/docs`, `/support`, `/faq`)
- No help or FAQ link in navigation or footer
- No `title` or `aria-label` (tooltip proxy) on complex or technical fields
- Support chat widget that fails to load (console error on widget script)

**Selector patterns:**
```typescript
// Check all help/support links resolve
const helpLinks = page.locator('a[href*="help"], a[href*="support"], a[href*="docs"], a[href*="faq"]');
const hrefs = await helpLinks.evaluateAll(links => links.map(l => l.href));
for (const href of hrefs) {
  const response = await page.request.get(href).catch(() => null);
  if (!response || response.status() >= 400) {
    saveFinding({
      heuristic: 'H10 Help and documentation',
      severity: 4,
      evidence: `Help link broken (${response?.status() ?? 'no response'}): ${href}`
    });
  }
}
```

---

## Accessibility Snapshot

Capture Playwright's accessibility tree for each evaluated page.
The snapshot surfaces roles, names, values, and focus state — useful across
multiple heuristics (H1 feedback, H6 labels, H10 help presence).

```typescript
const snapshot = await page.accessibility.snapshot();
// Flatten the tree and check for:
// - buttons/links with empty name → H6
// - role="alert" presence after actions → H1
// - aria-describedby on complex fields → H10
// Save the full snapshot for reference in synthesis.
```

If the page renders in a single-page-app framework, run the snapshot after
the main content has loaded (`waitForLoadState('networkidle')`).

---

## Severity Scale (0–4)

| Level | Label | Description |
|-------|-------|-------------|
| 0 | Not a problem | Cosmetic — fix only if time allows |
| 1 | Cosmetic | Minor issue, low priority |
| 2 | Moderate | Causes friction; address in next cycle |
| 3 | Major | Impedes task completion for many users; fix soon |
| 4 | Catastrophic | Prevents task completion; fix before next release |

See `references/nng-heuristics-guide.md` for per-heuristic severity examples and the
overall quality score formula.
