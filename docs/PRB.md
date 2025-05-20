# PRB Rejected - Callback Schedule Flow

## 🧾 Overview

This SOP defines the process for handling PRB-rejected leads, including identification, callback scheduling, lead assignment, and exclusions. It also incorporates guidelines for V2 enhancements and dynamic lead management.

---

## 👤 Customer Identification

- From the go-live date `{{ vars.go_live_date }}`, all customers marked as PRB will be tracked.
- Leads with the following exclusion criteria will **not** be considered:
  - PRB Lead Source: `{{ vars.prb_lead_source_exclusion }}`
  - PRB UTM Source: `{{ vars.prb_utm_source_exclusion }}`

---

## 📆 Callback Process

- The job runs at `{{ vars.callback_job_time }}` every night.
- Callback setting starts at `{{ vars.callback_setting_start_time }}`.
- Callbacks will be scheduled every `{{ vars.callback_interval_minutes }}` minutes for agents with multiple PRB callbacks.

---

## 🚫 Exclusions

- For leads dated between `1st` and `15th` of any month:
  - Booked leads, callbacks, or those with ≥ `{{ vars.min_talk_time_seconds }}` seconds talk time will be excluded from PRB creation.

---

## ❌ Rejected Lead Handling

- **Unassigned:** No action taken.
- **Assigned:** Rejected lead is reassigned to the last assigned agent.

---

## 🔁 Callback on Parent Lead

- For active **Marine** leads of the client:
  - Set callback on the open parent lead.
  - No new leads created.
- Callback Message Display: `{{ vars.callback_message }}`

---

## ☎️ Dialer & Prioritization

- If a callback is **not** scheduled, it won't be prioritized in the dialer.
- Max `{{ vars.max_consecutive_callbacks }}` consecutive callbacks per lead.

---

## 🧾 Lead Creation & Rejection

- No new PRB lead creation if the source or UTM matches rejection criteria.
- Rejected leads will **not** be counted toward `{{ vars.daily_lead_limit }}`.

---

## ⏰ Callback Schedule

- Callback Time Window: `{{ vars.callback_start_time }} to {{ vars.callback_end_time }}`
- Callback Frequency: Every `{{ vars.callback_gap_minutes }}` minutes

---

## 👥 Lead Assignment

- Leads assigned only to agents **tagged with PRB**.
- Agent selection based on:
  - Agent with max bookings on the Customer ID.
  - If no agents available: Assign to any agent with `{{ vars.min_tenure_months }}`+ months in Marine ST group.

---

## 🛑 Dialing Rejection Logic

- First day dial from system.
- Post-first-day, only manual dials allowed.
- System will not include in auto dialer priority.

---

## 🌙 Cool-Off Period

- Cool-off period: `{{ vars.cool_off_days }}` days from last callback for the same lead.

---

## ❓ Open Questions

- **If callbacks exceed 6** → What is the fallback process?
  - Action needed: Prevent further callbacks or reroute to a senior agent?

- **Job Rejection Logic for Callback Feature**:
  - SOP pending to define actions when rejection logic is triggered due to thresholds.

---

# PRB V2 Enhancements

## 📊 Insights

- **Rejected PRB Leads:**
  - Low conversion rates → Recommend monthly outreach.
- **Booked PRB Leads:**
  - High conversion → Continue prioritizing at scheduled CB time.
  - Manual call option remains enabled for agents.

---

## ✅ Action Items

- **Auto-Reopen Rejected PRB:** Every `{{ vars.reopen_interval_days }}` days.
- **Referral/Upsell PRB Tagging:**
  - All non-AO customers with > `{{ vars.min_policy_count_fy25 }}` policies tagged as PRB.
  - Reopened every 30 days.

- **Unmark as PRB Option:**
  - Agents can unmark PRB via rejection disposition: `{{ vars.unmark_prb_disposition }}`

- **HH Occupancy Exclusion:**
  - Prevent HH occupancy from being auto-tagged as PRB.

- **Call Audits:**
  - Enable audit request process for PRB leads.

- **PRB Communication:**
  - WhatsApp comms monthly via `{{ vars.virtual_number }}`.
  - New messaging every time.

---

## 🧠 Arpita’s Observations

- Customers with > `{{ vars.min_policy_count_fy25 }}` policies (non-AO) tagged as PRB.
- No year-round comms once AO is bought.
- Monthly callback by system every `{{ vars.system_callback_interval_months }}` months.
- Use MatrixGo Virtual Number: `{{ vars.virtual_number }}`.
- Agent assignment based on:
  - Highest sales count.
  - TL verification if needed.
