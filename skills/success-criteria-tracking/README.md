# Success Criteria Tracking Skill

A comprehensive agent instruction skill for tracking research success criteria against session outcomes.

## Files

### Documentation

1. **SKILL.md** (149 lines)
   - Canonical Anthropic skill structure
   - YAML frontmatter with name, description, and trigger keywords
   - Agent-directive tone
   - Quick Start and Core Workflow (8 steps)
   - Criterion Types: Quantitative, Qualitative, Behavioral
   - Output Format and Quality Gates
   - References to REFERENCE.md and EXAMPLES.md

2. **REFERENCE.md** (367 lines)
   - Detailed reference guide for criterion types with measurement examples
   - Threshold-setting strategies (realistic vs aspirational)
   - Confidence level tables (sample size requirements)
   - Root-cause analysis framework
   - Must-have vs nice-to-have distinction
   - Go/no-go decision framework
   - Edge cases: conditional criteria, role-specific criteria, outliers

3. **EXAMPLES.md** (307 lines)
   - Complete worked example: Collaborative Research Dashboard Study
   - 5 sessions with 6 criteria (mix of Q, B, C types)
   - Per-session scoring matrices
   - Aggregate tracking matrix
   - Root-cause analysis for each failure
   - Full go/no-go recommendation with decision logic

### Utility

4. **scripts/track_criteria.py** (334 lines)
   - Python 3 utility for automated tracking computation
   - Loads criteria CSV and session result CSVs
   - Computes pass rates, confidence levels, trends
   - Generates tracking matrix CSV and text summary
   - Implements go/no-go decision logic

**Usage:**
```bash
python track_criteria.py --criteria criteria.csv --sessions ./session_results/ --output tracking_matrix.csv
```

## Key Features

- **Canonical Skill Structure**: Matches Anthropic's agent instruction format
- **Agent-Directive Tone**: Tells Claude exactly what to do
- **Three Criterion Types**: Quantitative, Qualitative, Behavioral with clear measurement guidance
- **Confidence Assessment**: Based on sample size, consistency, and data quality
- **Root-Cause Analysis**: Framework for investigating failures
- **Go/No-Go Framework**: Decision logic based on must-haves, confidence, and trends
- **Edge Case Coverage**: Conditional criteria, role-specific success, outliers, missing data
- **Automated Computation**: Python script handles complex aggregation and scoring
- **No Experiment-Specific References**: Generalizable to any research domain

## How to Use This Skill

1. **Extract Criteria**: Read research plan; list all success criteria with IDs, types, and thresholds
2. **Define Indicators**: For each criterion, specify the exact metric or evidence
3. **Score Sessions**: Measure each criterion per session; record result and status
4. **Aggregate**: Use Python utility or manually compute pass rates, confidence, trends
5. **Analyze Failures**: Root-cause analysis for unmet criteria
6. **Recommend**: Synthesize into Go/Caution/No-Go decision

See SKILL.md for the complete 8-step workflow.
