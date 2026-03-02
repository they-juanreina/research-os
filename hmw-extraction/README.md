# HMW Extraction Skill

A complete skill for transforming research pain points into actionable How Might We (HMW) opportunity statements following Anthropic's canonical skill structure.

## Files

### 1. SKILL.md (135 lines)
**The canonical skill file that Claude executes.**

- **YAML frontmatter:** Skill name, description, and trigger keywords
- **Agent-directive tone:** Instructive steps Claude follows to extract and reframe HMW statements
- **Seven-step workflow:** Identify → Document → Extract → Define → Benefit → Context → Cluster & Prioritize
- **HMW template formula:** `How might we [help] [user] to [benefit] [in context]?`
- **Output format:** Standard table with HMW_ID, Pain Point, Workaround, HMW Statement, Personas, Priority, Evidence, Design Implications
- **Prioritization scoring:** Impact × Urgency / Feasibility matrix
- **Quality gates:** Five validation checkpoints to ensure well-formed HMW statements

### 2. REFERENCE.md (295 lines)
**Detailed reference guide for deep understanding.**

- **Formula breakdown:** Action verb, User specification, Benefit, Context—with examples and anti-patterns
- **Common anti-patterns:** Too narrow, too broad, solution-biased, vague users, missing evidence
- **Clustering methodology:** By domain, user role, pain frequency, or effort level
- **Prioritization matrix:** 2-axis (Impact × Feasibility) and 3-axis (Impact × Urgency / Feasibility) approaches
- **Persona-specific variants:** How to tailor HMW statements to different users
- **Scope validation:** The "3-5 approaches" test to ensure HMW statements are well-scoped
- **Evidence linking:** Types of evidence, documentation template
- **Quality checklist:** 10-point validation before finalizing

### 3. EXAMPLES.md (123 lines)
**Five complete, real-world HMW examples covering different themes.**

Examples include:
1. **Navigation & Findability** (HMW-01): Content editor duplicate prevention
2. **Trust & Security** (HMW-02): Compliance auditing and access verification
3. **Terminology & Mental Models** (HMW-03): Domain language understanding for new users
4. **Permissions & Access Control** (HMW-04): Simplified permission granting at team level
5. **Automation & Repetitive Tasks** (HMW-05): No-code task automation for analysts

Each example shows the complete table structure with all required fields, demonstrating how to write evidence-grounded, well-scoped HMW statements.

### 4. hmw_generator.py (189 lines)
**Python utility to transform raw pain points into structured HMW templates.**

**Input:** CSV with columns: Pain Point, Workaround, Quote, Persona, Theme

**Output:** CSV with columns: HMW_ID, Pain_Point, Workaround, HMW_Statement, Personas, Theme, Priority, Evidence, Design_Implications, Confidence

**Features:**
- Auto-generates HMW IDs (HMW-01, HMW-02, etc.)
- Clusters pain points by Theme
- Leaves HMW_Statement and Design_Implications as placeholders for Claude to fill
- Preserves Evidence (Quote) from input
- Sets default Priority and Confidence levels
- Includes clustering summary output

**Usage:**
```bash
python hmw_generator.py --input pain_points.csv --output hmw_statements.csv --show-clusters
```

## Workflow

### For Claude/Analysts:
1. Start with SKILL.md for the canonical extraction process
2. Use REFERENCE.md to validate HMW statements and resolve edge cases
3. Study EXAMPLES.md to understand output format and quality standards
4. Apply the seven-step workflow to your research findings

### For Data Processing:
1. Export research findings (pain points, workarounds, quotes, personas) to CSV
2. Run `hmw_generator.py` to create the structured template
3. Share output CSV with Claude for HMW statement generation
4. Claude fills in HMW_Statement and Design_Implications
5. Team assigns Priority and Confidence scores
6. Validate against quality checklist

## Key Principles

✓ **Human-centered:** Focus on user needs, not technical solutions

✓ **Evidence-grounded:** Every HMW rooted in specific research findings

✓ **Well-scoped:** Each HMW should inspire 3-5 distinct design approaches

✓ **Actionable:** Teams move directly from HMW to ideation and prototyping

✓ **Prioritized:** Use Impact × Urgency / Feasibility to focus effort

## Integration

This skill integrates with:
- **User research:** Findings, interviews, usability tests, surveys
- **Ideation:** HMW statements feed directly into divergent thinking workshops
- **Prototyping:** Design implications guide solution direction
- **Prioritization:** Ranked HMW statements guide roadmap sequencing

---

**Last Updated:** 2026-02-12
**Canonical Version:** 1.0
**Structure:** Anthropic Skill Standard
