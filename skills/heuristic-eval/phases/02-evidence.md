---
name: heuristic-eval
description: >
  Phase 2 — Evidence Collection. Translates the discovery brief into Playwright test scripts
  that capture screenshots, accessibility scans, and structured heuristic findings. Use after
  completing Phase 1 or when a discovery brief already exists.
license: "MIT"
metadata:
  author: "Juan Reina (they/them)"
  phase: "02-evidence"
  phase_name: "Evidence Collection"
  inputs: discovery brief (from phases/01-scope.md)
  outputs: Playwright project, heuristic-findings.json, screenshots
  feeds_into: phases/03-synthesis.md
---

# Phase 2 — Evidence Collection

**Goal:** Translate the discovery brief into repeatable, runnable Playwright scripts that
capture evidence for each user journey. The output is an auditable evidence package —
not a one-time capture. Scripts should be structured so the team can re-run them after
fixes to measure improvement over time.

> **Load `references/heuristic-assertions.md`** when writing assertion patterns for specific heuristics.

---

## What you are building

A self-contained Playwright TypeScript project:

```
ux-evidence-[product-name]/
├── package.json
├── playwright.config.ts
├── README.md
├── tests/
│   ├── 01-onboarding.spec.ts
│   ├── 02-primary-task.spec.ts
│   ├── 03-error-paths.spec.ts
│   └── 04-mobile.spec.ts
└── artifacts/            ← created at runtime
    ├── screenshots/
    ├── accessibility/
    └── heuristic-findings.json
```

---

## Step 1: Read the discovery brief

If the user provides a path to the discovery brief from Phase 1, read it. Extract:

- Target URL (base URL)
- The four user journeys (steps, start/end points)
- The heuristic hypotheses (what to specifically look for)
- Notes about auth, loading patterns, or viewports

If no brief is provided, ask for: URL, a primary journey description, and any known problem areas.
Proceed with the default journey set from Phase 1 as a fallback.

---

## Step 2: Project scaffolding

### package.json

```json
{
  "name": "ux-evidence-[product-name]",
  "version": "1.0.0",
  "description": "Playwright UX evidence collection for heuristic evaluation",
  "scripts": {
    "test": "playwright test",
    "test:headed": "playwright test --headed",
    "test:mobile": "playwright test --project=mobile-chrome",
    "report": "playwright show-report"
  },
  "devDependencies": {
    "@playwright/test": "^1.41.0",
    "fs-extra": "^11.2.0"
  }
}
```

### playwright.config.ts

```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  outputDir: './artifacts',
  timeout: 30000,
  retries: 1,
  use: {
    baseURL: process.env.PLAYWRIGHT_BASE_URL || '[BASE_URL_FROM_BRIEF]',
    screenshot: 'on',
    video: 'on-first-retry',
    trace: 'on-first-retry',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'], viewport: { width: 1280, height: 800 } },
    },
    {
      name: 'mobile-chrome',
      use: { ...devices['iPhone 13'] },
    },
  ],
});
```

### README.md for the evidence project

```markdown
# UX Evidence: [Product Name]

Playwright evidence collection for heuristic evaluation.
Generated: [date]

## Quick start

\`\`\`bash
npm install
npx playwright install chromium
npm test
\`\`\`

## Override target URL

\`\`\`bash
PLAYWRIGHT_BASE_URL=https://staging.example.com npm test
\`\`\`

## Artifacts

After running, find:
- `artifacts/screenshots/` — screenshots at each test step
- `artifacts/accessibility/` — axe accessibility scan results
- `artifacts/heuristic-findings.json` — structured findings for Phase 3 synthesis

## Re-running after fixes

Re-run scripts after design changes to compare findings. The `heuristic-findings.json`
is appended on each run; clear it before a new evaluation cycle.
\`\`\`
```

---

## Step 3: Core test file pattern

Use this pattern in every `.spec.ts` file.

```typescript
import { test, expect } from '@playwright/test';
import fs from 'fs';
import path from 'path';

const ARTIFACTS_DIR = path.join(__dirname, '../artifacts');
const SCREENSHOTS_DIR = path.join(ARTIFACTS_DIR, 'screenshots');
const A11Y_DIR = path.join(ARTIFACTS_DIR, 'accessibility');

[ARTIFACTS_DIR, SCREENSHOTS_DIR, A11Y_DIR].forEach(d =>
  fs.mkdirSync(d, { recursive: true })
);

function saveFinding(finding: {
  heuristic: string;
  severity: number;
  evidence: string;
  url: string;
  type: string;
  journey?: string;
  notes?: string;
}) {
  const filePath = path.join(ARTIFACTS_DIR, 'heuristic-findings.json');
  const existing = fs.existsSync(filePath)
    ? JSON.parse(fs.readFileSync(filePath, 'utf-8'))
    : [];
  existing.push({ ...finding, timestamp: new Date().toISOString() });
  fs.writeFileSync(filePath, JSON.stringify(existing, null, 2));
}
```

---

## Step 4: Heuristic listeners — embed in every test

```typescript
test('journey: [name]', async ({ page }) => {
  const consoleErrors: string[] = [];
  const networkErrors: { url: string; status: number }[] = [];

  // H1: Visibility — capture console errors as evidence of silent failures
  page.on('console', msg => {
    if (msg.type() === 'error') consoleErrors.push(msg.text());
  });

  // H5/H10: Error prevention / Help — capture failed network requests
  page.on('response', res => {
    if (res.status() >= 400)
      networkErrors.push({ url: res.url(), status: res.status() });
  });

  // --- journey steps go here ---

  // At end: save accumulated findings
  consoleErrors.forEach(text => saveFinding({
    heuristic: 'H1 Visibility of system status',
    severity: 2,
    evidence: `Console error: ${text}`,
    url: page.url(),
    type: 'console-error',
    journey: '[journey name]'
  }));

  networkErrors.forEach(({ url, status }) => saveFinding({
    heuristic: 'H1 Visibility of system status',
    severity: status >= 500 ? 3 : 2,
    evidence: `Network error ${status}: ${url}`,
    url: page.url(),
    type: 'network-error',
    journey: '[journey name]'
  }));
});
```

---

## Step 5: Journey-specific test files

Write one `.spec.ts` per journey from the discovery brief.
Refer to `references/heuristic-assertions.md` for per-heuristic assertion patterns.

### Key assertions to include in every journey file

**H3 — User control (modals with no close):**
```typescript
const dialogs = page.locator('[role="dialog"]');
const count = await dialogs.count();
for (let i = 0; i < count; i++) {
  const dialog = dialogs.nth(i);
  const hasClose = await dialog.locator(
    '[aria-label*="close" i], button:has-text("Cancel"), button:has-text("Close")'
  ).count() > 0;
  if (!hasClose) {
    saveFinding({
      heuristic: 'H3 User control and freedom',
      severity: 3,
      evidence: 'Dialog found with no visible close button or cancel option',
      url: page.url(),
      type: 'missing-close',
      journey: '[journey name]'
    });
  }
}
```

**H5 — Error prevention (forms with no validation):**
```typescript
// Try submitting a form with blank required fields
await page.fill('input[type="email"]', 'notanemail');
await page.click('button[type="submit"]');
const errorVisible = await page.locator(
  '[role="alert"], .error, .form-error, [aria-invalid="true"]'
).isVisible().catch(() => false);
if (!errorVisible) {
  saveFinding({
    heuristic: 'H5 Error prevention',
    severity: 4,
    evidence: 'Form submitted with invalid email — no inline validation shown',
    url: page.url(),
    type: 'missing-validation',
    journey: '[journey name]'
  });
}
```

**H6 — Recognition (inputs without visible labels):**
```typescript
const inputs = page.locator(
  'input:not([type="hidden"]):not([type="submit"]):not([type="button"])'
);
const inputCount = await inputs.count();
for (let i = 0; i < inputCount; i++) {
  const input = inputs.nth(i);
  const id = await input.getAttribute('id');
  const hasLabel = id
    ? await page.locator(`label[for="${id}"]`).count() > 0
    : false;
  const hasAriaLabel = !!(await input.getAttribute('aria-label'));
  if (!hasLabel && !hasAriaLabel) {
    saveFinding({
      heuristic: 'H6 Recognition over recall',
      severity: 2,
      evidence: `Input field missing visible label and aria-label`,
      url: page.url(),
      type: 'missing-label',
      journey: '[journey name]'
    });
  }
}
```

**H8 — Mobile horizontal overflow:**
```typescript
// Only run in mobile project
const hasHorizontalScroll = await page.evaluate(
  () => document.body.scrollWidth > window.innerWidth
);
if (hasHorizontalScroll) {
  saveFinding({
    heuristic: 'H8 Aesthetic and minimalist design',
    severity: 3,
    evidence: `Horizontal overflow detected: scrollWidth=${
      await page.evaluate(() => document.body.scrollWidth)
    }px, innerWidth=${await page.evaluate(() => window.innerWidth)}px`,
    url: page.url(),
    type: 'horizontal-overflow',
    journey: '[journey name]'
  });
}
```

**H2 — Technical language in labels:**
```typescript
const technicalLabels = await page.locator(
  'label, [placeholder]'
).filter({ hasText: /[_][a-z]|uuid|uid|hash|id\b/ }).count();
if (technicalLabels > 0) {
  saveFinding({
    heuristic: 'H2 Match between system and real world',
    severity: 2,
    evidence: `${technicalLabels} label(s) contain technical naming (snake_case, uuid, etc.)`,
    url: page.url(),
    type: 'technical-language',
    journey: '[journey name]'
  });
}
```

---

## Step 6: Accessibility scan (H6, H8, H10 support)

If the target product is expected to serve users with assistive technology, add an
axe accessibility scan to each journey. Install `@axe-core/playwright`:

```typescript
import AxeBuilder from '@axe-core/playwright';

const accessibilityResults = await new AxeBuilder({ page })
  .withTags(['wcag2a', 'wcag2aa'])
  .analyze();

if (accessibilityResults.violations.length > 0) {
  accessibilityResults.violations.forEach(violation => {
    saveFinding({
      heuristic: 'H6 Recognition over recall / Accessibility',
      severity: violation.impact === 'critical' ? 4 : violation.impact === 'serious' ? 3 : 2,
      evidence: `${violation.id}: ${violation.description} — ${violation.nodes.length} instance(s)`,
      url: page.url(),
      type: 'accessibility-violation',
      journey: '[journey name]',
      notes: violation.helpUrl
    });
  });
  fs.writeFileSync(
    path.join(A11Y_DIR, `${journey-name}-axe.json`),
    JSON.stringify(accessibilityResults, null, 2)
  );
}
```

---

## What automation cannot cover

For these heuristics, note findings as "Requires visual review" — do not mark as passed:

| Heuristic | Why automation is insufficient |
|-----------|-------------------------------|
| H2 Match with real world | Jargon vs. plain language requires domain knowledge |
| H7 Flexibility and efficiency | "Appropriate shortcuts" requires knowing user expertise levels |
| H8 Aesthetic and minimalist | Visual hierarchy and cognitive load require human judgment |
| H9 Error recovery | Whether error messages are *helpful* (not just present) requires reading them |
| H10 Help and documentation | Whether help content is adequate requires reading and evaluating it |

For each of these, include a screenshot capture + a `notes` field indicating "manual review required."

---

## Handoff to Phase 3

After scripts run successfully:

1. Confirm with the user that `heuristic-findings.json` is populated and screenshots are captured.
2. Note the finding count and any immediately notable patterns.
3. Say: "Phase 3 will synthesize these findings into an evaluation report with severity ratings
   and plural interpretations. Load `phases/03-synthesis.md` with the brief and findings JSON to continue."
