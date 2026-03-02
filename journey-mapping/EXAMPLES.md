# Journey Mapping Examples

## Example 1: New Employee Onboarding to a Data Tool

**Scenario**: A mid-market software company (50–200 employees) has just hired a data analyst. The company uses an internal analytics platform. We mapped the analyst's first month experience based on three interview sessions and observation during onboarding.

**Persona**: Sarah, Data Analyst
- **Background**: 5 years in analytics, first time at this company, previous tool was Tableau
- **Context**: Hired to support marketing and product teams; sits in a hybrid role between engineering and product
- **Goal**: Get to productivity within 2 weeks; understand the company's data architecture and key dashboards

---

### Sarah's Onboarding Journey

| Stage | Touchpoint | User Action | Thought/Quote | Emotion | Pain Point | Opportunity | Confidence |
|---|---|---|---|---|---|---|---|
| **Awareness** | Welcome email from HR | Opens email, skims onboarding agenda, clicks link to company wiki | "There's a lot of information here. Where do I start?" | Overwhelmed | Email contains 8 links and no clear priority order | Restructure welcome email with single CTA: "Start with this onboarding checklist" | 3 |
| **Orientation** | In-person office tour and IT setup | Receives laptop, gets desk assigned, meets team members briefly | "Everyone seems friendly but I'm meeting too many names at once." | Anxious+ | No written guide for where things are (data docs, code repos, analytics dashboards); relies entirely on colleague memory | Provide a printed map of tools, repos, and key resources with one-page guide | 2 |
| **Tool Discovery** | First visit to analytics platform dashboard | Logs in, sees 47 existing dashboards, searches for "marketing" to narrow scope | "Oh, there are a lot of dashboards here already. Are these live or sample?" | Curious | No dashboard tagging or categorization; difficult to distinguish critical operational dashboards from experiments | Add tags ("production", "experimental", "template") and brief ownership metadata to each dashboard | 3 |
| **Learning** | Scheduled tutorial with data engineer (Carlos) | Attends 90-minute session on platform architecture, SQL conventions, data refresh schedule; takes notes | "I understand the schema now, but I'm not sure which tables to use for marketing analysis." | Confident, Slightly Anxious | Tutorial is comprehensive but lacks hands-on practice; no recorded version; Sarah's notes are incomplete on SQL naming patterns | Record the tutorial and create a templated "first query" walkthrough with comments explaining each part | 3 |
| **Hands-On Practice** | First independent query creation | Opens SQL editor, copies a previous dashboard query, modifies WHERE clause to test, gets stuck on joining tables | "I know Tableau syntax, but this SQL is different. The join keys aren't obvious." | Frustrated+ | Documentation exists but is in three separate places (wiki, Slack thread, code comments); no searchable index of table relationships | Create a single-page "Table Relationships Cheat Sheet" with ERD diagram and example joins for common use cases | 3 |
| **Validation & Integration** | Review first analysis with product manager (Diego) | Shares query results in a Google Doc, Diego asks clarifying questions about data freshness and filters | "I wasn't sure if my data was correct, so this feedback is really valuable." | Relieved, Satisfied | No standard for how to document data sources and transformations in shared analysis; data lineage is unclear | Create a reusable "Data Source Template" that analysts fill in to document origin, refresh rate, filters, and limitations | 2 |
| **Mastery** | Creates first stakeholder-facing dashboard | Builds a retention cohort dashboard in the platform, adds filters and drill-downs, presents to product leadership | "I can now answer the questions people ask me without waiting for Carlos." | Confident++ | Takes 4 hours longer than expected because color-coding and legend conventions aren't documented | Document and share the "Analytics Style Guide" (colors, fonts, naming conventions) early; link from the dashboard creation template | 2 |

---

## Example 2: Role Variant – Data Engineer Onboarding to the Same Analytics Platform

**Persona**: Marcus, Data Engineer
- **Background**: 8 years in data engineering, just joined the company, coming from a larger tech company with mature data infrastructure
- **Context**: Responsible for data pipeline maintenance, schema design, and platform performance optimization
- **Goal**: Understand the current architecture, identify technical debt, and run first optimization

---

### Marcus's Onboarding Journey (Key Divergence Points)

| Stage | Touchpoint | User Action | Thought/Quote | Emotion | Pain Point | Opportunity | Confidence |
|---|---|---|---|---|---|---|---|
| **Awareness** | Welcome email + systems access request | Opens email, immediately checks which systems are mentioned; navigates to GitHub to find data infrastructure code | "The email is HR-focused. Let me go straight to the code repo." | Neutral | Welcome email is generic; no tech-specific onboarding track for engineers | Create a separate technical onboarding track with links to: GitHub repos, architecture docs, incident playbooks, and performance dashboards | 2 |
| **Architecture Discovery** | Code repository exploration and system diagrams | Reads data pipeline code (Python/Airflow), looks for system architecture documentation, finds scattered README files | "The pipeline is more complex than the docs suggest. There's a lot of legacy code here." | Skeptical | Documentation is outdated; architecture diagram doesn't match the current DAG structure; no changelog explaining technical decisions | Update architecture diagram and add a "How We Got Here" doc explaining design decisions and known limitations | 1 |
| **Technical Setup** | Local development environment setup | Sets up Python virtual environment, pulls airflow repo, tries to run a test DAG; encounters missing database credentials in README | "The setup instructions assume I already know the password schema location." | Frustrated+ | Setup script is incomplete; credential management is manual and not documented | Create an automated setup script that pulls secrets from the company secret manager and validates all connections before returning to user | 3 |
| **Knowledge Mapping** | Meets with outgoing data engineer for handoff (2-hour pairing session) | Watches outgoing engineer run queries to diagnose a pipeline issue, asks about performance metrics, requests list of known issues | "There's a lot of context I won't get from just reading the code." | Engaged+ | No formal knowledge transfer document; key insights live in institutional memory only | Create a "Data Engineer Playbook" with common troubleshooting steps, performance metrics to monitor, and contact info for different platform domains | 2 |
| **Hands-On Work** | First independent task: Optimize a slow query (given by team lead) | Profiles query execution, identifies missing index, implements change, runs performance test, documents change in a commit message | "I can optimize this, but I'm not sure if there's a gate review process or performance testing standard." | Confident, Slightly Anxious | No documented code review standards for data engineers; no performance benchmarking framework | Document the code review checklist (what to check for schema changes, performance impact, backward compatibility) and share the perf testing framework | 2 |
| **Integration** | Pushes first DAG change through the review and deployment process | Creates a PR, requests review from Carlos, waits 48 hours for feedback, makes one revision, merges to main, verifies deployment in staging | "The review process is slow. I don't know if this is normal." | Patient, Slightly Impatient | No SLA or expected turnaround time for code reviews; no clear deployment checklist | Document the review SLA (e.g., "Reviews within 24 hours for urgent, 3 days for standard") and create a deployment checklist | 1 |
| **Ownership** | Assigned to on-call rotation (first week) | Monitors alerts via Slack, receives notification of a pipeline failure at 2 AM, reads incident playbook, executes recovery steps, posts to #data-incidents channel | "I had to figure out which systems to check first. The playbook helped but it's incomplete for this type of failure." | Alert+, Competent | Incident playbook covers 70% of failure types; no escalation path for unknown failures | Expand incident playbook with decision tree for "unknown errors" and establish clear escalation path (e.g., "Page Carlos if resolution > 15 min") | 2 |

---

## Cross-Persona Observations

### Convergence Points (Same Experience)
1. **Awareness stage**: Both Sarah and Marcus found the generic welcome email insufficient and had to ask colleagues for direction.
2. **Tool Discovery / Architecture Discovery**: Both needed more structured guidance to navigate the platform's scope and complexity.
3. **Integration stage**: Both benefited from having a clear review process and feedback channel.

### Divergence Points (Different Needs)
1. **Learning approach**: Sarah needed visual tutorials and SQL templates; Marcus went straight to code and system design docs.
2. **Pain areas**: Sarah struggled with syntax and conventions; Marcus struggled with institutional knowledge gaps and process clarity.
3. **Timeline to productivity**: Sarah reached productivity in 3–4 weeks (hands-on practice required); Marcus reached productivity in 1 week (technical foundation already strong, just needed context).

### Unified Opportunities
- Create separate onboarding tracks for analysts vs. engineers
- Improve documentation indexing and discoverability across the platform
- Establish clear SLAs and expectations for reviews, on-call, and support
- Record knowledge transfer sessions and maintain a living "lessons learned" doc

---

## Example 3: Service Blueprint Variant – Customer Support Chat Onboarding

This example shows how to expand a journey map into a service blueprint when you have data about both user actions and behind-the-scenes processes.

**Scenario**: A SaaS company provides customer support via chat. We mapped both the customer's experience and the support agent's parallel experience for a customer's first support interaction.

### Customer Journey + Service Blueprint

| Stage | **Customer Touchpoint** | **Customer Action** | **Emotion** | **Behind-the-Scenes Action** | **Support Process** | Confidence |
|---|---|---|---|---|---|---|
| **Need Recognition** | Help icon in product UI | Customer clicks "?" icon next to confusing feature | Confused | Agent receives ticket notification in queue management system | SLA: First response within 2 minutes during business hours | 3 |
| **Initiation** | Chat window opens with pre-filled context (product name, feature, user ID) | Customer types: "I don't know how to export my data." | Hopeful | Agent sees customer profile, recent session activity, and previous tickets (if any); system suggests 3 most relevant help articles | Agents trained to reference knowledge base within first 30 seconds; escalation available if customer dismisses KB articles | 3 |
| **Exploration** | Agent sends two help articles and asks clarifying question | Customer reads article 1, clicks "This helped!" button; agent continues chat | Satisfied+ | Agent logs interaction, adds tags (e.g., "data-export", "resolved-self-serve"), closes ticket if marked helpful | Agents incentivized for "self-serve resolution rate"; tickets marked helpful automatically add to knowledge base analytics | 2 |
| **Resolution** | Customer finds the answer, completes the action | Customer exports data, returns to chat to confirm | Confident, Grateful | Agent marks ticket as resolved, sends follow-up email with transcript and direct link to used article | Follow-up email sent from support system; ticket data feeds into product analytics to identify features with high support volume | 2 |
| **Feedback** | Post-chat survey appears with 3 questions (1-5 star, "Would you use chat again?", free text) | Customer rates 5 stars, types "Very helpful, thanks!" | Satisfied++ | Survey responses logged in CRM; tagged "positive"; agent receives recognition in team Slack | Positive surveys are shared in team standups; agent performance metrics track resolution rate and CSAT | 2 |

### Key Behind-the-Scenes Insights
- **Support process gap**: No direct integration between chat resolution and product improvements; article effectiveness is tracked but not actionable
- **Opportunity**: Implement monthly review where product team analyzes high-volume help topics and prioritizes UX improvements

---

## How to Use These Examples

1. **Adapt the structure** for your own research. Use the same column headers and confidence scale.
2. **Vary the granularity** based on available research. If you have minimal data, 5 stages are fine. If you have detailed transcripts, 7–8 stages are appropriate.
3. **Reference role divergence** when creating multi-persona maps. Show where personas' experiences differ and why.
4. **Consider the service blueprint** when you have operational data. It's especially useful when designing organizational improvements, not just product changes.
5. **Export to CSV** using the provided script for further analysis or comparison across multiple personas or research phases.

---

## CSV Export Example

The Sarah onboarding journey above, exported to CSV:

```
Stage,Touchpoint,User Action,Thought/Quote,Emotion,Pain Point,Opportunity,Confidence
Awareness,Welcome email from HR,"Opens email, skims onboarding agenda, clicks link to company wiki","There's a lot of information here. Where do I start?",Overwhelmed,Email contains 8 links and no clear priority order,Restructure welcome email with single CTA: Start with this onboarding checklist,3
Orientation,In-person office tour and IT setup,"Receives laptop, gets desk assigned, meets team members briefly","Everyone seems friendly but I'm meeting too many names at once.",Anxious+,No written guide for where things are; relies entirely on colleague memory,Provide a printed map of tools and one-page guide,2
Tool Discovery,First visit to analytics platform dashboard,"Logs in, sees 47 existing dashboards, searches for marketing to narrow scope","Oh, there are a lot of dashboards here already. Are these live or sample?",Curious,No dashboard tagging or categorization; difficult to distinguish critical operational dashboards from experiments,Add tags and brief ownership metadata to each dashboard,3
Learning,Scheduled tutorial with data engineer,"Attends 90-minute session on architecture, SQL conventions, refresh schedule; takes notes","I understand the schema now, but I'm not sure which tables to use for marketing analysis.",Confident + Slightly Anxious,Tutorial is comprehensive but lacks hands-on practice; no recorded version,Record the tutorial and create templated first query walkthrough,3
Hands-On Practice,First independent query creation,"Opens SQL editor, copies previous query, modifies WHERE clause, gets stuck on joining tables","I know Tableau syntax, but this SQL is different. The join keys aren't obvious.",Frustrated+,Documentation exists in three places; no searchable index of table relationships,Create single-page Table Relationships Cheat Sheet with ERD diagram,3
Validation & Integration,Review first analysis with product manager,"Shares query results in Google Doc, manager asks clarifying questions about data freshness and filters","I wasn't sure if my data was correct, so this feedback is really valuable.",Relieved + Satisfied,No standard for documenting data sources and transformations; data lineage is unclear,Create reusable Data Source Template for shared analysis,2
Mastery,Creates first stakeholder-facing dashboard,"Builds retention cohort dashboard, adds filters and drill-downs, presents to product leadership","I can now answer the questions people ask me without waiting for Carlos.",Confident++,Takes 4 hours longer than expected because color-coding and legend conventions aren't documented,Document and share Analytics Style Guide early,2
```

To convert markdown to CSV:
```bash
python format_journey_map.py --input onboarding_journey.md --output onboarding_journey.csv --direction md2csv
```

To convert back:
```bash
python format_journey_map.py --input onboarding_journey.csv --output onboarding_journey.md --direction csv2md
```
