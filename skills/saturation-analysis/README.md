# Saturation Analysis Skill

This directory contains a comprehensive skill for analyzing thematic saturation in qualitative research datasets. Use this skill to determine whether your research has gathered sufficient data or if additional sessions are needed.

## Files in This Skill

- **SKILL.md** (158 lines)
  - Core skill definition with agent-directive tone
  - 7-step workflow for assessing saturation
  - Quick Start guide and decision thresholds
  - Quality gates before finalizing recommendations
  - Academic references

- **REFERENCE.md** (261 lines)
  - Detailed guidance on theme definition (new vs. variant vs. confirmation)
  - Saturation curve interpretation (early spike, growth, plateau phases)
  - Role-specific analysis when participant types vary
  - Edge case handling (outliers, homogeneous samples, small populations)
  - Minimum session requirements and confidence levels (High/Medium/Low)
  - Practical interpretation scenarios
  - Coding and documentation standards

- **EXAMPLES.md** (214 lines)
  - Complete 8-session saturation analysis report with fictional mobile app study
  - Theme tracking table, metrics, curve narrative, and recommendation
  - 4 additional scenario examples: early termination, continuation, outliers, and mixed role-based results

- **scripts/compute_saturation.py** (362 lines)
  - Python utility for automated saturation computation
  - Input: CSV with columns (Session_Number, Session_Date, Participant_Role, Theme, Is_New)
  - Output: Saturation metrics CSV + text summary with recommendation
  - Supports three threshold levels: conservative, moderate, aggressive
  - Usage: `python compute_saturation.py --input theme_tracking.csv --output saturation_report.csv --threshold moderate`

## Quick Start

1. **Read SKILL.md** for the 7-step workflow and decision thresholds
2. **Prepare your data** as a CSV (see Example in EXAMPLES.md)
3. **Run the Python script** or manually follow the workflow
4. **Consult REFERENCE.md** for edge cases and clarifications
5. **Use EXAMPLES.md** to understand output format and confidence levels

## When to Use This Skill

- You've completed 6+ qualitative research sessions and want to know if saturation is reached
- Your findings are becoming repetitive and you're unsure whether to continue
- You need to justify stopping data collection to stakeholders
- You have heterogeneous participant types and want to assess per-role saturation
- You want to objectively measure whether your dataset covers research question comprehensively

## Key Concepts

**Thematic Saturation**: The point where additional data collection yields diminishing returns. New themes stop emerging at meaningful rates.

**Theme vs. Variant**: A new theme is conceptually distinct. A variant is a reframing of an existing theme (not counted as new emergence).

**Saturation Curve**: A plot of cumulative unique themes vs. session number. Saturation is reached when the curve plateaus.

**Three Thresholds**:
- **Conservative** (≥12 sessions, 5+ sessions without new themes): High confidence
- **Moderate** (≥8 sessions, 3+ sessions without new themes): Balanced thoroughness & resources
- **Aggressive** (≥6 sessions, 2+ sessions without new themes): For timeline pressure

## Output Recommendation Levels

- **SATURATED**: Stop collecting data; proceed to analysis
- **LIKELY_SATURATED**: Consider pausing; 1-2 more sessions recommended
- **APPROACHING_SATURATION**: Continue; monitor emergence rate
- **CONTINUE**: Significant novelty still emerging; more sessions needed

## Contact & Updates

This skill follows the canonical Anthropic skill structure. For questions about thematic saturation methodology, consult the references in SKILL.md.
