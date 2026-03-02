# Session Notes Examples

## Example 1: Usability Test Session

# Session Notes: Task Management App – Prototype A Testing

## Session Meta

| Field | Value |
|-------|-------|
| **Session ID** | UST-001-2024 |
| **Date** | February 10, 2024 |
| **Time (Start)** | 2:00 PM EST |
| **Duration** | 47 minutes |
| **Session Type** | Usability Test |
| **Location** | Remote |
| **Platform** | Zoom |
| **Facilitator(s)** | Alex Chen |
| **Observer(s)** | Jordan Lee, Sam Rodriguez |
| **Recorder** | Video + Audio |

---

## Participant Info

| Participant ID | Name/Handle | Role | Background | Experience Level |
|---|---|---|---|---|
| P1 | Sarah M. | Participant | Product Manager at fintech startup | Intermediate (uses 2-3 task apps) |

**Participant Demographics**:
- Age Range: 28–32
- Industry/Domain: Financial technology
- Product Experience: Heavy task manager user (Asana, Monday.com, Notion)
- Technical Proficiency: Advanced

**Known Context**:
- First time seeing our prototype
- Has requested better task filtering in previous user research
- Works in an agile team with 8 members

---

## Scenario / Task

**Research Objective**: Evaluate whether users can intuitively filter and prioritize tasks in Prototype A without training.

**Research Question(s)**:
- Can users discover and use the filter feature?
- Do users understand the priority system?
- What mental model do users have for task organization?

**Task Description**:
"You have just joined a new team project. You need to find all tasks assigned to you that are due this week, and mark the three most urgent ones as high priority. Assume you can do anything a task management app would let you do."

**Background Framing**:
"This is an early prototype we're testing. Not everything is finished, and we want your honest feedback. There's no right or wrong way to use it."

**Success Criteria**:
- User can identify and access the filter feature within 3 minutes
- User successfully marks at least one task as high priority
- User articulates their mental model for task organization

---

## First Actions

**What did the participant do immediately upon encountering the stimulus?**

**Time**: 0:15

**Action**: Clicked directly on the search/filter icon in the top navigation bar.

**Quote**: "I'm looking for the filter. That's usually where it is."

**Context**: User was familiar with similar patterns from Asana and Monday.com. No hesitation—immediately went to the expected location.

---

## Chronological Observations

### Phase 1: Orientation and Filter Discovery
**Time**: 0:15–2:10
- User scanned the entire interface from left to right in 30 seconds
- Immediately identified the search bar but not the filter button initially
- After 45 seconds, user found the filter icon (three horizontal lines) in the header
- User clicked filter; a dropdown menu appeared with options: "Assigned to Me," "Due This Week," "Priority," "Status"
- User commented: "Oh nice, these are pre-built filters. That's helpful."
- User clicked "Assigned to Me" first, which filtered the task list correctly

### Phase 2: Additional Filtering
**Time**: 2:10–4:35
- User then clicked "Due This Week" to apply a second filter
- System displayed 7 filtered tasks (correctly narrowed from the full list)
- User paused for 5 seconds, reading the task list
- User did NOT recognize a "Priority" column and asked: "Where do I set the priority on these?"
- Facilitator responded: "Good question. What would you expect to do?"
- User said: "Usually I'd click on the task to open it, or there'd be a priority flag or tag visible in the list"

### Phase 3: Task Opening and Priority Assignment
**Time**: 4:35–7:45
- User clicked on the first task ("Design homepage mockup")
- Task detail panel opened on the right side
- User immediately found a "Priority" dropdown field (set to "Normal")
- User changed it to "High" and confirmed the change
- User closed the detail panel by clicking the X button
- User repeated this process for two more tasks
- Third task: User hesitated. The task detail panel took 2 seconds to load. User said: "Is it loading?"
- User successfully marked three tasks as high priority

### Phase 4: Review and General Comments
**Time**: 7:45–9:30
- User returned to the main task list to see the updated priorities
- User expected to see a "High Priority" indicator next to each marked task but didn't initially notice the change
- Facilitator asked: "How do you know which tasks are high priority now?"
- User scrolled back to the task detail view and confirmed the priority had been saved
- User said: "I think there should be a visual indicator on the list view. Like a red flag or bold text. Right now I have to open each task to verify it's marked as high priority."

---

## Key Quotes

| Time | Participant | Quote | Context |
|---|---|---|---|
| 0:30 | P1 | "I'm looking for the filter. That's usually where it is." | User had strong expectations from prior tools |
| 2:15 | P1 | "Oh nice, these are pre-built filters. That's helpful." | Positive reaction to filter options |
| 4:50 | P1 | "Usually I'd click on the task to open it, or there'd be a priority flag or tag visible in the list" | User expressed mental model for priority visibility |
| 6:10 | P1 | "Is it loading?" | Concerned about slow task detail panel |
| 8:00 | P1 | "I think there should be a visual indicator on the list view. Like a red flag or bold text." | Clear UX feedback |
| 8:45 | P1 | "Everything else feels pretty intuitive, honestly." | Overall satisfaction signal |

---

## Pain Points

| # | Issue | Severity | Context | Participant(s) | Observed Behavior | Potential Root Cause |
|---|---|---|---|---|---|---|
| 1 | Priority not visually indicated in list view | Moderate | User had to open each task to confirm priority was saved | P1 | Repeated navigation to detail view; expressed frustration | UI doesn't show priority status in main list; users expect visual cue |
| 2 | Task detail panel has 2-second load time | Minor | User noticed delay and asked "Is it loading?" | P1 | Brief hesitation; mild concern about responsiveness | Possible API latency or component rendering issue |
| 3 | "Priority" field not immediately visible in first glance | Minor | User had to ask facilitator where to set priority | P1 | Asked facilitator; had to explore task detail panel | Priority field location is not obvious; may need clearer label or positioning |

---

## Timing Data

| Task / Phase | Duration | Notes |
|---|---|---|
| Orientation and filter discovery | 1:55 | User confident; found filters quickly |
| Applying multi-filter (Assigned to Me + Due This Week) | 0:45 | Smooth; correct results |
| Opening first task and marking as high priority | 1:15 | Quick; user found the field easily |
| Opening second task and marking as high priority | 0:50 | Smooth repetition |
| Opening third task and marking as high priority | 1:00 | Included pause for loading concern |
| Reviewing changes and confirming visual feedback | 1:15 | User expected visual indicator; had to verify manually |

---

## Non-Verbal Observations

- **Confidence Level**: High overall, with brief dips
  - Evidence: User moved quickly through the interface; no mouse hovering or exploration. Brief pause at task load (6:10). Resumed high confidence after understanding the task.

- **Emotional Tone**: Positive, with a moment of mild frustration
  - Evidence: User said "Oh nice" when discovering pre-built filters (positive tone). Said "I think there should be..." when noting the lack of visual priority indicator (constructive, not angry). Overall engaged.

- **Engagement**: Highly interested throughout
  - Evidence: Leaning into the screen; speaking freely; asked clarifying questions; made unsolicited suggestions. Did not seem bored or fatigued during the 9:30 session.

- **Other Signals**:
  - Nodding when filters appeared ("That's helpful")
  - Slight frown when task detail took 2 seconds to load
  - Spoke quickly and with authority about expected patterns from other tools
  - Made eye contact with facilitator during Q&A

---

## Mini-Survey Results

### Satisfaction / Usability Ratings

| Question | Rating | Comments |
|---|---|---|
| Overall satisfaction | 4/5 | "Good foundation. Needs the visual priority indicator." |
| Ease of use | 4/5 | "Filters are great. Priority system works but could be more visible." |
| Likelihood to recommend | 4/5 | "Yes, after you fix the priority visual feedback." |
| Would you use this instead of Asana? | Maybe | "If you add more filtering options and better priority visibility." |

### Open-Ended Feedback

- **What was the best part of your experience?**
  - "The pre-built filters. I didn't have to create custom filters or learn a complex UI. It just works."

- **What was the most frustrating?**
  - "Not seeing the high priority indicator on the main list. I had to open each task to confirm. That's inefficient."

- **What would you change?**
  - "Add a priority icon or color indicator next to each task in the list view. Make it obvious which tasks are high priority at a glance."

- **Any other comments?**
  - "The app is mostly intuitive. I'd switch to this if you keep iterating on these details. Your competitor (Asana) has had 10 years to polish, so you're not far behind."

---

## Post-Session Debrief

**Facilitator Notes**:
- User was a strong participant. She had clear expectations based on prior experience with professional tools.
- The priority visibility issue is actionable and aligns with our hypothesis that users need visual status indicators.
- The 2-second load time on task detail was unexpected. Should investigate backend performance.
- User's suggestion about priority icons is a direct, implementable recommendation.

**Observer Notes** (Jordan Lee):
- Participant P1 is a power user. Her feedback is high signal because she knows what she's looking for.
- The filter feature succeeded. Users will find it and use it intuitively.
- Priority visibility failure is a quick win—could be fixed with a simple visual indicator (icon or color tag).

**Observer Notes** (Sam Rodriguez):
- Noted that the user defaulted to opening tasks to check priority. This is a workaround, not the intended flow.
- The pre-built filters are a strong differentiator compared to competitors. Keep emphasizing this.

**Unexpected Findings**:
- User expected the priority visual indicator to be present in the list view by default. This is a stronger UX expectation than we anticipated.
- The 2-second load time was noticeable enough for the user to ask about it. This may be a technical blocker for confidence in the product.

**Revised Assumptions**:
- ❌ REVISED: We thought users would click into task details to see priority status. Instead, users expect priority to be visible at a glance in the list.
- ✓ CONFIRMED: Users with task management experience will quickly adopt our filter system.

---

## Key Insights

### Insight 1: Pre-Built Filters are a Clear Strength
**What we learned**: Users with experience in professional task management tools immediately recognize and appreciate pre-built filters. This is a key differentiator.

**Evidence**:
- "Oh nice, these are pre-built filters. That's helpful." (2:15)
- User did not try to create custom filters; she used the pre-built ones correctly on first try.
- Post-survey: "The pre-built filters. I didn't have to create custom filters or learn a complex UI."

**Implication**: Emphasize the pre-built filter feature in marketing and onboarding. This is a competitive advantage. Consider expanding the pre-built filters to address more use cases.

### Insight 2: Priority Status Must Be Visible in the List View
**What we learned**: Users expect to see task priority status (and other key metadata) in the main list view. Burying this information in the detail panel is a UX friction point.

**Evidence**:
- User had to open each task multiple times to verify priority was saved.
- "I think there should be a visual indicator on the list view. Like a red flag or bold text."
- User expected a visual cue without prompting; this is an unstated mental model expectation.

**Implication**: Add a priority icon or color indicator to the task list (low effort). This will reduce friction and align with user expectations. Consider what other metadata should be visible in the list view (status, due date, assignee).

### Insight 3: Task Load Time is Noticeable and Concerning
**What we learned**: A 2-second delay in opening the task detail panel triggered user concern about system responsiveness. Even power users expect snappiness.

**Evidence**:
- "Is it loading?" (6:10) — User noticed the delay and expressed concern.
- Brief hesitation in workflow; disrupted the task completion flow.

**Implication**: Investigate backend API latency or component rendering performance. Aim for <500ms task detail load time. This is not a critical blocker, but it undermines confidence in the product's performance.

### Insight 4: User Mental Models Are Formed by Existing Tools
**What we learned**: Users transfer expectations from tools like Asana and Monday.com to our prototype. Strong prior experience creates both an advantage (users know what to do) and a challenge (users notice when we deviate).

**Evidence**:
- "I'm looking for the filter. That's usually where it is." (0:30) — User knew where to look before exploring.
- "Usually I'd click on the task to open it, or there'd be a priority flag or tag visible in the list" (4:50) — User articulated her mental model explicitly.

**Implication**: Design with pattern consistency in mind. Don't innovate on UX patterns that users already understand. Save innovation for workflow improvements, not navigation.

---

## Notes for Future Sessions

- **Task Wording**: The task was clear and achievable. No changes needed. Consider testing "managing a large list" (50+ tasks) to see if filter and priority features scale.

- **Follow-Up Questions**:
  - Ask participants how they currently prioritize tasks in their existing tools.
  - Ask participants what other metadata they'd want visible in the list view (due date, assignee, tags, status).
  - Test with non-power users. Will they discover the filters as easily?

- **Recruitment Criteria**:
  - Include at least 3–4 power users (like P1) who use professional task management tools daily.
  - Include 2–3 novices who may not have strong prior expectations.
  - Vary by role (PM, engineer, designer, operations) to understand different mental models.

- **Environmental/Setup Changes**:
  - Monitor task detail load times during future testing. If it's consistently >1 second, investigate performance before next test round.
  - Consider recording screen sharing to see where users' eyes go (heat map analysis could help with visual hierarchy).

- **Other Considerations**:
  - The app appears to handle the filter + sort workflow well. Consider testing more complex scenarios (nested filters, saving filter presets).
  - User mentioned wanting more filtering options. Explore which filters are most requested in a survey before building.

---

---

## Example 2: Discovery Interview Session

# Session Notes: Healthcare Provider Scheduling – Discovery Interview

## Session Meta

| Field | Value |
|-------|-------|
| **Session ID** | DI-001-2024 |
| **Date** | February 8, 2024 |
| **Time (Start)** | 10:00 AM EST |
| **Duration** | 53 minutes |
| **Session Type** | Discovery Interview |
| **Location** | In-Person |
| **Platform** | In-Lab (Conference Room B) |
| **Facilitator(s)** | Maya Patel |
| **Observer(s)** | Chris Wright |
| **Recorder** | Audio |

---

## Participant Info

| Participant ID | Name/Handle | Role | Background | Experience Level |
|---|---|---|---|---|
| P1 | Dr. James T. | Participant | Family medicine physician | Experienced (20 years practice) |

**Participant Demographics**:
- Age Range: 55–60
- Industry/Domain: Healthcare (Primary Care)
- Product Experience: Uses EHR system (Epic) and handwritten paper scheduling; minimal consumer tech outside work
- Technical Proficiency: Intermediate (comfortable with EHR; uncomfortable with consumer apps)

**Known Context**:
- Manages a small practice with 3 other physicians and 5 support staff
- Spends 30–40 minutes daily on scheduling and rescheduling
- Has been asking staff for alternative scheduling solutions for 6 months
- Never used a dedicated scheduling app; relies on paper and EHR

---

## Scenario / Task

**Research Objective**: Understand pain points in current healthcare provider scheduling workflows and uncover high-priority needs for a scheduling solution.

**Research Question(s)**:
- What is the current scheduling workflow (manual, hybrid, software)?
- What are the biggest friction points and time drains?
- What would the ideal scheduling experience look like?
- Are there blockers (regulatory, cultural, technical) to adopting new tools?

**Task Description**:
"Walk me through a typical day of your scheduling. How do you handle new appointment requests, cancellations, and rescheduling? What's most frustrating about the current process?"

**Background Framing**:
"We're exploring whether a dedicated scheduling tool could improve workflows for independent and small-practice physicians. Your honest perspective is invaluable. This is exploratory—no pitch coming."

**Success Criteria**:
- Participant describes a complete day-in-the-life of scheduling
- Participant articulates at least 3 pain points and their frequency
- Participant describes ideal workflow or workaround attempts

---

## First Actions

**What did the participant do immediately upon encountering the stimulus?**

**Time**: 0:15

**Action**: Asked a clarifying question before answering.

**Quote**: "Are you looking at this for just scheduling, or do you want to know about the whole patient management workflow? Because scheduling doesn't happen in a vacuum for us."

**Context**: Physician immediately contextualized the question within the broader ecosystem. This signals systems thinking and importance of integration. Not a user who wants point solutions.

---

## Chronological Observations

### Phase 1: Current Workflow Overview
**Time**: 0:15–8:30
- Participant described the scheduling system: A combination of Epic EHR, phone calls, and paper logbooks
- Morning routine includes checking Epic for the day's appointments (5 minutes)
- Review of cancellations and no-shows from previous day (3–5 minutes)
- Manual rescheduling of cancelled appointments by calling patients (10–20 minutes, depending on day)
- Office staff (medical assistant) also handles inbound appointment requests and rescheduling
- Epic is the "single source of truth," but staff use paper notes to track requests that come in throughout the day
- Participant said: "I trust Epic with the record, but the workflow is clunky. By the time something gets into Epic, I've already written it on paper three times."

### Phase 2: Pain Points Deep Dive
**Time**: 8:30–22:00
- Facilitator asked: "What's the most frustrating part?"
- Participant: "Double entry. I get a call. I write down the request. My MA checks with the patient. I write it again. Then we enter it into Epic. That's a minimum of three times I or someone on my team is writing down the same information."
- Discussed the frequency: "This happens 20–30 times a day. It adds up."
- Noted that cancellations are especially chaotic: Patient calls the office → MA notes it on paper → MA tells physician → Physician updates Epic → Physician looks for a replacement patient → Calls other patients
- Participant said: "The worst part is not knowing in real time. I might see a cancellation hours later. I could have already called another patient or shuffled my schedule."
- Mentioned a regulatory pain point: "We have to keep all those paper notes for compliance. It's a legal requirement. So we're creating duplicates for years."

### Phase 3: Attempted Workarounds and Tools
**Time**: 22:00–33:15
- Participant described trying to use a shared Google Calendar with staff but abandoned it after 2 weeks
- Reason: "Epic is the legal record. Google Calendar didn't integrate with Epic. We'd have to double-enter data anyway."
- Tried texting with staff but realized it created communication gaps and no audit trail
- Currently relies on a color-coded paper schedule on the front desk and oral handoffs
- Participant: "We bought a big wall calendar. That's 2024 for us. I know it sounds low-tech, but it works for quick visual scanning."
- Asked: "Why not use a more integrated solution?" Participant said: "Cost is one factor. But honestly, integration with our EHR is the deal-breaker. If it doesn't talk to Epic, it's just another thing we have to maintain separately."

### Phase 4: Ideal Workflow and Motivations
**Time**: 33:15–45:00
- Facilitator asked: "Describe your ideal scheduling day."
- Participant described: "Phone rings. My MA tells me there's a request. I see it appear in my app immediately. I can see my availability, propose times to the patient in real time, and once the patient confirms, it auto-populates into Epic and sends a confirmation to the patient. No re-entry. One shot."
- Participant emphasized the real-time aspect: "The biggest time saver would be not waiting. We lose time because we're batching these tasks. Do it as it comes in, and it's gone."
- Discussed willingness to adopt new tech: "If it saves my staff and me 30 minutes a day, that's 2.5 hours a week. I'd pay for that."
- Noted cultural resistance: "My partners might not adopt it immediately. I'd have to prove it works for me first, then evangelize it to them."

### Phase 5: Regulatory and Technical Constraints
**Time**: 45:00–53:00
- Participant raised regulatory requirements: HIPAA compliance, audit trails, patient consent documentation
- Emphasized the importance of the audit trail: "Every change has to be logged. If a patient claims we didn't call them, I need proof that we did."
- Technical concern: "Our Epic system is managed by a hospital network. I don't have direct control over integrations. Any tool we use has to work with the Epic API or standard HL7 integration."
- Mentioned data silos: "We also have insurance verification, prior auth tracking, and billing. These are all separate systems. I'd love a unified solution, but I know that's pie in the sky."
- Said: "Start with scheduling. Get that right. Then we can talk about bigger integration."

---

## Key Quotes

| Time | Participant | Quote | Context |
|---|---|---|---|
| 0:20 | P1 | "Are you looking at this for just scheduling, or do you want to know about the whole patient management workflow? Because scheduling doesn't happen in a vacuum for us." | Participant's systems thinking |
| 4:30 | P1 | "I trust Epic with the record, but the workflow is clunky. By the time something gets into Epic, I've already written it on paper three times." | Core frustration: data re-entry |
| 10:15 | P1 | "Double entry. I get a call. I write down the request. My MA checks with the patient. I write it again. Then we enter it into Epic. That's a minimum of three times." | Quantified pain point |
| 12:00 | P1 | "This happens 20–30 times a day. It adds up." | Volume and frequency |
| 14:30 | P1 | "The worst part is not knowing in real time. I might see a cancellation hours later. I could have already called another patient or shuffled my schedule." | Time lag friction |
| 24:30 | P1 | "We bought a big wall calendar. That's 2024 for us. I know it sounds low-tech, but it works for quick visual scanning." | Current workaround; effectiveness despite primitiveness |
| 27:00 | P1 | "If it doesn't talk to Epic, it's just another thing we have to maintain separately." | Integration as non-negotiable requirement |
| 36:45 | P1 | "Phone rings. My MA tells me there's a request. I see it appear in my app immediately. I can see my availability, propose times to the patient in real time, and once the patient confirms, it auto-populates into Epic and sends a confirmation to the patient. No re-entry. One shot." | Ideal workflow vision |
| 38:15 | P1 | "If it saves my staff and me 30 minutes a day, that's 2.5 hours a week. I'd pay for that." | Value proposition and ROI motivation |
| 48:00 | P1 | "Every change has to be logged. If a patient claims we didn't call them, I need proof that we did." | Regulatory/compliance imperative |
| 50:30 | P1 | "Start with scheduling. Get that right. Then we can talk about bigger integration." | Prioritization and realistic expectations |

---

## Pain Points

| # | Issue | Severity | Context | Participant(s) | Observed Behavior | Potential Root Cause |
|---|---|---|---|---|---|---|
| 1 | Data re-entry across paper, EHR, and manual tracking | Critical | Happens 20–30 times daily; eats up 10–20 minutes per day | P1, Staff | Participant described as "clunky"; expressed frustration multiple times | Lack of integrated workflow; Epic requires manual data entry |
| 2 | Time lag in cancellation notifications | Critical | Physician may not learn of cancellation for hours; prevents real-time rescheduling | P1 | Participant cited this as "the worst part"; leads to inefficient call-backs | Paper/phone-based communication not real-time |
| 3 | Regulatory compliance overhead (paper trail for audit) | Moderate | All scheduling changes must be logged and paper records retained for legal protection | P1, Practice | Participant mentioned as necessary but burdensome | HIPAA and malpractice liability requirements |
| 4 | Lack of real-time visibility for staff | Moderate | Medical assistant and physicians don't have simultaneous view of availability and requests | P1, Staff | Mentioned as a source of double-bookings and confusion | No shared, real-time scheduling system |
| 5 | Manual patient communication (phone calls) | Minor | Requesting appointments by phone is slow; no automation for confirmations | P1 | Participant noted but accepted as industry norm | Healthcare norms and patient preference; regulatory requirements for verbal confirmation |

---

## Timing Data

| Task / Phase | Duration | Notes |
|---|---|---|
| Current workflow overview | 8:15 | Participant provided detailed walkthrough; contextualized within broader patient management |
| Pain points exploration | 13:30 | Longest phase; participant elaborated on frequency, impact, and workarounds |
| Attempted workarounds and tools discussion | 11:15 | Participant described prior attempts (Google Calendar, texting) and why they failed |
| Ideal workflow and motivations | 11:45 | Participant articulated a clear vision; discussed ROI and adoption barriers |
| Regulatory and technical constraints | 8:00 | Participant raised non-negotiable requirements (Epic integration, HIPAA, audit trails) |

---

## Non-Verbal Observations

- **Confidence Level**: High and steady
  - Evidence: Participant spoke clearly and decisively about his pain points and requirements. No hesitation when discussing needs. Spoke authoritatively about practice operations.

- **Emotional Tone**: Frustrated but not angry; pragmatic and solution-focused
  - Evidence: Sighed when describing data re-entry ("By the time something gets into Epic..."). Did not express anger. Suggested workarounds he's already tried. Practical about constraints ("I know that's pie in the sky").

- **Engagement**: Highly engaged; leaned forward during pain points discussion
  - Evidence: Participant asked clarifying questions about scope upfront. Elaborated beyond facilitator prompts. Discussed trade-offs and technical constraints without being asked. Took the conversation seriously.

- **Other Signals**:
  - Nodded when discussing the wall calendar ("It works for quick visual scanning") — indicating acceptance of pragmatic solutions
  - Spoke quickly and with energy when describing the ideal workflow — evident enthusiasm
  - Mentioned "my partners" when discussing adoption — signals organizational dynamics and potential resistance
  - Used precise language ("audit trail," "HL7 integration," "HIPAA compliance") — demonstrates technical literacy and regulatory awareness

---

## Mini-Survey Results

*No formal survey; participant answered open-ended questions during the interview.*

### Open-Ended Feedback

- **What would a successful scheduling solution look like?**
  - "Real-time visibility. No re-entry. Integration with Epic. And it has to be compliant with HIPAA and produce an audit trail. If it does all that, I'm in."

- **How likely would you be to adopt a new scheduling tool?**
  - "High, if it meets those requirements. I'd pilot it myself, prove it works, then pitch it to my partners. I estimate it would take 2–3 months to get buy-in across the practice."

- **What would prevent you from adopting it?**
  - "Cost (if it's >$500/month for our practice). Lack of Epic integration. If it doesn't have an audit trail. If adoption takes more than a month of training."

- **Who else would need to sign off?**
  - "My office manager and one of my partners (the tech-forward one). The other two partners would follow once they see it working."

---

## Post-Session Debrief

**Facilitator Notes** (Maya Patel):
- Excellent, articulate participant. He's done the thinking already. His pain points are specific and quantified (20–30 re-entries/day; 30 minutes saved/day ROI).
- Integration with Epic is non-negotiable. This is a hard constraint. Any product roadmap must prioritize this from day one.
- The wall calendar comment is insightful. He's not against technology; he's against solutions that require workarounds (like Google Calendar creating duplicate entry).
- His ideal workflow vision is clear and specific. We should use his wording to inform the product spec.
- Adoption barrier: organizational inertia. He'd champion it, but his partners need to buy in. Sales and implementation need to account for multi-stakeholder decision-making in small practices.

**Observer Notes** (Chris Wright):
- Participant is a primary care physician with a small practice. He's a likely early adopter for a healthcare-specific scheduling tool.
- The volume of re-entries (20–30/day) is our largest opportunity. A tool that eliminates this would save real time and money.
- Regulatory and compliance concerns (audit trail, HIPAA) are not negotiable. We need to ensure our product is built from the ground up for healthcare compliance, not bolted on after.
- The practice has a technical decision-maker (the "tech-forward" partner), but adoption still requires consensus. Consider targeting the office manager as a secondary user for buy-in.

**Unexpected Findings**:
- The wall calendar is still a critical tool in 2024. This surprised me. It signals that practices still value analog, tangible solutions alongside digital tools. There may be an opportunity for a hybrid approach (digital + print exports).
- The participant did not ask about cost until prompted. This suggests the value prop is strong enough that cost is secondary to functionality. However, we should still price competitively with Epic add-ons (~$200–300/month).

**Revised Assumptions**:
- ❌ REVISED: We thought automation (auto-confirming appointments) was a priority. Instead, the participant emphasized integration and real-time visibility. Automation is secondary to removing re-entry friction.
- ✓ CONFIRMED: Healthcare providers will adopt new tools if they integrate with their existing EHR. Integration is table stakes, not a nice-to-have.
- ✓ CONFIRMED: Small practices (3–5 physicians) are a viable market segment with acute pain points and budget availability.

---

## Key Insights

### Insight 1: Data Re-entry Across Systems is the #1 Pain Point
**What we learned**: Physicians and staff spend 20–30 minutes daily re-entering the same scheduling data across paper, EHR, and manual systems. This is not just a UX friction point; it's a workflow architecture failure.

**Evidence**:
- "Double entry. I get a call. I write down the request. My MA checks with the patient. I write it again. Then we enter it into Epic." (10:15)
- "This happens 20–30 times a day. It adds up." (12:00)
- Participant estimated this consumes 10–20 minutes of a 9-hour clinical day.

**Implication**: Any scheduling solution must integrate seamlessly with Epic (or the user's EHR). A standalone scheduling tool will create the same problem it's meant to solve. Epic integration is a prerequisite, not an add-on feature.

### Insight 2: Real-Time Visibility is Critical, Not Automation
**What we learned**: Participants prioritize real-time visibility of cancellations, requests, and availability over automated workflows. The ability to see and act on information immediately is more valuable than automating actions.

**Evidence**:
- "The worst part is not knowing in real time. I might see a cancellation hours later." (14:30)
- When describing ideal workflow, participant emphasized seeing information immediately: "I see it appear in my app immediately." (36:45)
- Participant did not request automation for patient confirmations; he requested real-time notification and manual control.

**Implication**: Design for real-time push notifications and live updates, not for automation. Automation can come later if participants request it. The immediate priority is visibility and rapid decision-making.

### Insight 3: Regulatory Compliance is Non-Negotiable and Shapes Adoption
**What we learned**: Healthcare providers operate under strict HIPAA, audit trail, and liability requirements. Any solution must be built with compliance as a core feature, not a compliance checkbox.

**Evidence**:
- "Every change has to be logged. If a patient claims we didn't call them, I need proof that we did." (48:00)
- Participant mentioned retaining paper records for years due to legal requirements.
- When describing ideal workflow, participant did not mention compliance. He assumed it would be a given.

**Implication**: Build compliance into the product architecture from day one. Audit trails, HIPAA encryption, and data retention policies should be core features. Marketing should emphasize compliance as a selling point, not a burden.

### Insight 4: EHR Integration is the Deal-Breaker (or Deal-Maker)
**What we learned**: Solutions that don't integrate with the existing EHR (Epic) are dead on arrival. Participants will not use a scheduling tool that requires duplicate data entry.

**Evidence**:
- "If it doesn't talk to Epic, it's just another thing we have to maintain separately." (27:00)
- Participant tried Google Calendar but abandoned it because it didn't integrate with Epic.
- When discussing ideal workflow, participant assumed Epic would be involved: "It auto-populates into Epic." (36:45)

**Implication**: Epic integration is not a feature request; it's a market requirement. Any roadmap must prioritize HL7/FHIR integration or direct Epic API access. This is a technical blocker, not a sales objection.

### Insight 5: Small Practices Have Acute Needs and Budget, but Multi-Stakeholder Adoption is Required
**What we learned**: Independent and small-practice physicians (3–5 providers) have significant scheduling pain points and are willing to invest in solutions. However, adoption requires buy-in from multiple stakeholders (office manager, partners).

**Evidence**:
- "If it saves my staff and me 30 minutes a day, that's 2.5 hours a week. I'd pay for that." (38:15)
- Participant indicated willingness to pilot and evangelize: "I'd pilot it myself, prove it works, then pitch it to my partners." (Post-survey)
- Participant mentioned needing sign-off from office manager and at least one partner.

**Implication**: Sales and implementation strategy should account for multi-stakeholder decision-making. Target the champion (the tech-forward physician) but also engage the office manager (the workflow expert). Consider offering a pilot period or ROI guarantee to reduce adoption risk.

---

## Notes for Future Sessions

- **Follow-Up Questions**:
  - How does the practice currently handle scheduling conflicts and double-bookings? (Participant didn't elaborate on this.)
  - What's the breakdown of time spent on each scheduling task (inbound requests vs. cancellations vs. rescheduling)?
  - Does the practice use any integration tools (middleware) to connect paper/Epic/external systems?
  - What's the team structure for scheduling? Is the office manager a secondary decision-maker?

- **Recruitment Criteria**:
  - Include at least 1–2 office managers or administrative staff. They may have different priorities (patient communication, compliance tracking).
  - Include 1–2 practices that already use an EHR other than Epic (e.g., Medidata, Nextgen, Cerner) to understand integration requirements across systems.
  - Include 1–2 larger practices (10+ physicians) to understand how pain points scale.
  - Recruit at least one "late adopter" or resistance figure to understand organizational barriers.

- **Environmental/Setup Changes**:
  - Consider doing one in-person observation of a scheduling workflow (visit a practice, shadow the office manager for 2 hours) to see the pain points firsthand.
  - Request a copy of the practice's typical daily schedule (de-identified) to understand volume, patterns, and edge cases.

- **Product Research**:
  - Validate Epic API access and integration feasibility with Epic's integration team.
  - Research HL7/FHIR standards for healthcare scheduling to ensure compatibility with multiple EHRs.
  - Investigate HIPAA compliance requirements and audit trail implementation (consider consulting with healthcare compliance lawyer).
  - Explore whether a wall calendar export feature (print-friendly schedule) could be a quick win for adoption.

- **Other Considerations**:
  - The "wall calendar as a secondary tool" insight suggests there may be a hybrid opportunity (digital + print). Explore this in future interviews.
  - Consider partnerships with EHR vendors or practice management companies to accelerate adoption and integration.
  - The small-practice market is fragmented and price-sensitive. Explore subscription pricing tiers or per-provider models to reduce barrier to entry.
