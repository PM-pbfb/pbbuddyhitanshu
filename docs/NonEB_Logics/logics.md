# Non-EB Allocation Logic 🚀

---

## Marine ⚓

### Adhoc Leads

* If leads are created under the **annual open category** (from CJ), they are assigned only to advisors with at least **`{{vars.marine_adhoc_leads_min_experience_months}}` months** of total experience.
* For **single transit leads**, assignments are made on a **round-robin basis**, following a **Last In, First Out (LIFO)** approach.

### Lead Assignment

* **Single transit leads** are assigned to the logged-in advisor on a **round-robin basis**.
* **Annual open leads** are assigned to advisors with more than **`{{vars.marine_annual_open_leads_min_tenure_months}}` months** of tenure in the system.

### Agent Reassignment Logic 🔄

If a lead is created and assigned to an agent, and the lead has a talk time of **`{{vars.agent_reassignment_min_talk_time_minutes}}` minutes**, then:

* If the assigned agent is unavailable for a particular day (e.g., on leave or a week off), the lead is reassigned to another available agent.
* Once the original agent returns, the lead is reassigned back to them.
* However, if the call duration between the **new agent** and the customer exceeds the call duration between the **original agent** and the customer, the lead remains with the new agent.

### Assignment TAT ⏱️

* **`{{vars.marine_assignment_tat_minutes}}` minutes** after lead creation.

### Qualification ✅

* **Pmax**: Quotes page landed.
* **YouTube**: Quotes page landed.

### Offline Advertisement 📺

* **Toll-Free Number on Auto and Trucks**: Leads are assigned directly to the **“Marine Insurance”** group. If no advisor is available, such calls are directed to the **Saleib group**.

## Workmen Compensation 👷

---

### Lead Assignment

* Leads are assigned on a **round-robin basis** to the logged-in advisor, following a **LIFO** approach.

### Winback Leads 🔙

* For **Winback leads**, the system first checks if the agent who previously booked the policy is active. If available, the lead is assigned to that agent.
* If the previous agent is not active, the lead is assigned to available agents on a **round-robin basis**, provided they have more than **`{{vars.wc_winback_min_experience_months}}` months** of experience.
* These leads do not count towards the daily limit.

### Qualification ✅

* **Pmax WC**: On quotes page landed.
* **Demand Gen WC**: On quotes page landed.
* **Mobile App**: Round-robin basis.

### Assignment TAT ⏱️

* **`{{vars.wc_assignment_tat_minutes}}` minutes** after lead creation.

## Professional Indemnity 🧑‍💼

---

### Lead Assignment

* If a PI lead comes from the **Mobile App**, the lead is only assigned if the user has selected **‘Call Now,’** edited the specialization, or clicked on the **Premium** option.
* From **`{{vars.pi_mobile_app_go_live_date}}`**, all leads from the Mobile App are assigned.
* **Influencer campaign**: All leads are assigned to the team.

### Assignment TAT ⏱️

* **`{{vars.pi_assignment_tat_minutes}}` minutes** after lead creation.

### Qualification ✅

* **Mobile App Leads**: Assigned if either the plan ID is selected, **‘Call Us’** tile is clicked, or **‘Edit SI’** is clicked.

## Liability Insurance ⚖️

---

### Lead Assignment

* Leads are assigned on a **round-robin basis** to the logged-in advisor, following a **LIFO** approach.

### Assignment TAT ⏱️

* **`{{vars.liability_assignment_tat_minutes}}` minutes** after lead creation.

## Cyber Individual Insurance 💻

---

* Individual cyber leads **will not be assigned**.
* From **`{{vars.cyber_individual_assignment_go_live_date}}`**, all leads are assigned to one agent.

## Engineering 🏗️

---

### Lead Assignment

* Leads are assigned on a **round-robin basis** to the logged-in advisor, following a **LIFO** approach.

### Assignment TAT ⏱️

* **`{{vars.engineering_assignment_tat_minutes}}` minutes** after lead creation.

### Qualification ✅

* **CPM**: If RTO option is selected on CJ, such leads will not be assigned.

## Property 🏡

---

### Office Package Policy (7)

* Any lead with **sub-product ID 7** is assigned to **Group ID `{{vars.property_office_package_group_id}}`** on a **round-robin basis**.

### Fire & Burglary Insurance (5) 🔥

* Any lead with **sub-product ID 5** is redirected to **Group ID `{{vars.property_fire_burglary_group_id}}`**.

### Shop Owner Insurance (8) 🛍️

* Any lead with **sub-product ID 8** is assigned to **Group ID `{{vars.property_shop_owner_group_id}}`** on a **round-robin basis**.
* Any lead with **sub-product ID 5** and **occupancy ID** in ('3135', '3253') is assigned to **Group ID `{{vars.property_shop_owner_group_id}}`** on a **round-robin basis**.

### Lead Assignment

* Leads are assigned to the logged-in advisor on a **round-robin basis**, following a **LIFO** approach.

### Assignment TAT ⏱️

* **`{{vars.property_assignment_tat_minutes}}` minutes** after lead creation.

### Offline Advertisement 📰

* **Toll-Free Number on Pamphlet**: Leads are assigned directly to the **Shop Owner Insurance group**. If no advisor is available, such calls are directed to the **Saleib group**.

## Generic 📋

---

### Working Hours ⏰

* **`{{vars.working_hours_start}}`** to **`{{vars.working_hours_end}}`** (Last lead assignment time: **`{{vars.last_lead_assignment_time}}`**)

### Non-Working Hours 🌙

* **`{{vars.non_working_hours_start}}`** to **`{{vars.non_working_hours_end}}`**

### Lead Age ⏳

* If a lead has a status of "New" or "Valid" and no contact has been made within the next **`{{vars.lead_age_auto_reject_days}}` days**, the system automatically marks the lead as "Rejected."

### Future Prospect 🔮

* If the talk time on a particular lead is **`{{vars.future_prospect_min_talk_time_minutes}}` minutes**, the agent cannot mark the lead as a "Future Prospect."
* If a lead in Sub-product A is rejected as a "Future Prospect" and the user (at the customer ID level) purchases any sub-product across SME before the specified date, no lead will be created on that specific date.
* The minimum start date for a "Future Prospect" is **D+`{{vars.future_prospect_min_start_date_days}}` days**.

### Winback Logic 🔄

* **WC Expired Leads**: Created before **`{{vars.wc_expired_leads_days_before_expiry}}` days** of policy expiry.
* **PI Last Year Lost Cases/Renewal**: Created before **`{{vars.pi_lylr_days_before_expiry}}` days** of policy expiry.
* **Marine Winback**: For last year's lost renewals.
* **Liability Winback**: For last year's lost renewals.

### Lead (Call) Status 📞

* **New**: A new lead in the system. If a user creates a new child ID while having an existing parent lead with a status other than "New," the child ID will be marked as "New," but the call will always be initiated on the parent ID. After booking, the status of the call will be marked as "Parent/Child Booked."
* **Valid**: The customer didn’t pick up the call (i.e., there is a ring time available), or the number was switched off, or the call duration was less than **`{{vars.valid_call_duration_threshold_seconds}}` seconds**.
* **Interested**: Call duration is **`{{vars.interested_call_duration_threshold_seconds}}` seconds** or more.
* **Contacted**: Call duration is between **`{{vars.contacted_call_duration_lower_threshold_seconds}}` seconds** and **`{{vars.contacted_call_duration_upper_threshold_minutes}}` minutes**.
* These statuses are system-assigned, but the agent can change the status from the UI. Additionally, if the status is changed from "Valid" to "Interested," it cannot be reverted to "Valid" by either the user or the system.

### Call Transfer Flow ➡️

* Click on the transfer icon. After that, we will ask for the transfer type and sub-product type, and then the panel will be displayed. However, the panel should patch to the first available agent rather than the previous one.

### Lead Treatment 🩹

* First, reject the initial lead with the disposition **"Interested in Other LOB"** and create a new lead with the lead source from the initial lead.
* **Assignment**: The new lead should be assigned to the first available agent, with selection available accordingly.

## Dialer Logics 🤖

---

### Rejection Logic ❌

| Subproduct ID | Status (New/Valid) | Status (Contacted) | Status (Interested) | Subproduct Name          |
| :------------ | :----------------- | :----------------- | :------------------ | :----------------------- |
| `{{vars.rejection_logic_subproduct_id_marine}}` | At `{{vars.rejection_logic_marine_new_valid_attempts}}` attempts | At `{{vars.rejection_logic_marine_contacted_attempts}}` attempts | After `{{vars.rejection_logic_marine_interested_attempts}}` attempts | Marine Insurance         |
| `{{vars.rejection_logic_subproduct_id_wc}}` | At `{{vars.rejection_logic_wc_new_valid_attempts}}` attempts | At `{{vars.rejection_logic_wc_contacted_attempts}}` attempts | After `{{vars.rejection_logic_wc_interested_attempts}}` attempts | Workmen compensation     |
| `{{vars.rejection_logic_subproduct_id_fire_burglary}}` | At `{{vars.rejection_logic_fire_burglary_new_valid_attempts}}` attempts | At `{{vars.rejection_logic_fire_burglary_contacted_attempts}}` attempts | At `{{vars.rejection_logic_fire_burglary_interested_attempts}}` attempts | Fire and Burglary        |
| `{{vars.rejection_logic_subproduct_id_shop_owner}}` | At `{{vars.rejection_logic_shop_owner_new_valid_attempts}}` attempts | At `{{vars.rejection_logic_shop_owner_contacted_attempts}}` attempts | At `{{vars.rejection_logic_shop_owner_interested_attempts}}` attempts | Shop owner Insurance     |
| `{{vars.rejection_logic_subproduct_id_office_package}}` | At `{{vars.rejection_logic_office_package_new_valid_attempts}}` attempts | At `{{vars.rejection_logic_office_package_contacted_attempts}}` attempts | At `{{vars.rejection_logic_office_package_interested_attempts}}` attempts | Office package Policy    |
| `{{vars.rejection_logic_subproduct_id_construction_risk}}` | At `{{vars.rejection_logic_construction_risk_new_valid_attempts}}` attempts | At `{{vars.rejection_logic_construction_risk_contacted_attempts}}` attempts | At `{{vars.rejection_logic_construction_risk_interested_attempts}}` attempts | Construction all Risk    |
| `{{vars.rejection_logic_subproduct_id_erection_risk}}` | At `{{vars.rejection_logic_erection_risk_new_valid_attempts}}` attempts | At `{{vars.rejection_logic_erection_risk_contacted_attempts}}` attempts | At `{{vars.rejection_logic_erection_risk_interested_attempts}}` attempts | Erection All risk        |
| `{{vars.rejection_logic_subproduct_id_plant_machinery_1}}` | At `{{vars.rejection_logic_plant_machinery_1_new_valid_attempts}}` attempts | At `{{vars.rejection_logic_plant_machinery_1_contacted_attempts}}` attempts | At `{{vars.rejection_logic_plant_machinery_1_interested_attempts}}` attempts | Plant and Machinery      |
| `{{vars.rejection_logic_subproduct_id_general_liability}}` | At `{{vars.rejection_logic_general_liability_new_valid_attempts}}` attempts | At `{{vars.rejection_logic_general_liability_contacted_attempts_1}}` attempts | At `{{vars.rejection_logic_general_liability_contacted_attempts_2}}` attempts | General Liability        |
| `{{vars.rejection_logic_subproduct_id_do}}` | At `{{vars.rejection_logic_do_new_valid_attempts}}` attempts | At `{{vars.rejection_logic_do_contacted_attempts_1}}` attempts | At `{{vars.rejection_logic_do_contacted_attempts_2}}` attempts | D&O                      |
| `{{vars.rejection_logic_subproduct_id_eo}}` | At `{{vars.rejection_logic_eo_new_valid_attempts}}` attempts | At `{{vars.rejection_logic_eo_contacted_attempts_1}}` attempts | At `{{vars.rejection_logic_eo_contacted_attempts_2}}` attempts | E&O                      |
| `{{vars.rejection_logic_subproduct_id_ghi}}` | At `{{vars.rejection_logic_ghi_new_valid_attempts}}` attempts | At `{{vars.rejection_logic_ghi_contacted_attempts_1}}` attempts | At `{{vars.rejection_logic_ghi_contacted_attempts_2}}` attempts | GHI                      |
| `{{vars.rejection_logic_subproduct_id_gpa}}` | At `{{vars.rejection_logic_gpa_new_valid_attempts}}` attempts | At `{{vars.rejection_logic_gpa_contacted_attempts_1}}` attempts | At `{{vars.rejection_logic_gpa_contacted_attempts_2}}` attempts | GPA                      |
| `{{vars.rejection_logic_subproduct_id_opd_care}}` | At `{{vars.rejection_logic_opd_care_new_valid_attempts}}` attempts | At `{{vars.rejection_logic_opd_care_contacted_attempts_1}}` attempts | At `{{vars.rejection_logic_opd_care_contacted_attempts_2}}` attempts | OPD care 360             |
| `{{vars.rejection_logic_subproduct_id_pi}}` | At `{{vars.rejection_logic_pi_new_valid_attempts}}` attempts | At `{{vars.rejection_logic_pi_contacted_attempts_1}}` attempts | At `{{vars.rejection_logic_pi_contacted_attempts_2}}` attempts | PI                       |
| `{{vars.rejection_logic_subproduct_id_public_liability}}` | At `{{vars.rejection_logic_public_liability_new_valid_attempts}}` attempts | At `{{vars.rejection_logic_public_liability_contacted_attempts_1}}` attempts | At `{{vars.rejection_logic_public_liability_contacted_attempts_2}}` attempts | Public Liability         |
| `{{vars.rejection_logic_subproduct_id_cyber_risk}}` | At `{{vars.rejection_logic_cyber_risk_new_valid_attempts}}` attempts | At `{{vars.rejection_logic_cyber_risk_contacted_attempts_1}}` attempts | At `{{vars.rejection_logic_cyber_risk_contacted_attempts_2}}` attempts | Cyber Risk Insurance     |
| `{{vars.rejection_logic_subproduct_id_plant_machinery_2}}` | At `{{vars.rejection_logic_plant_machinery_2_new_valid_attempts}}` attempts | At `{{vars.rejection_logic_plant_machinery_2_contacted_attempts_1}}` attempts | At `{{vars.rejection_logic_plant_machinery_2_contacted_attempts_2}}` attempts | Plant and Machinery      |

### New Lead Calling Flow 📞

* All leads can be dialed max **`{{vars.new_lead_calling_flow_max_calls_per_week}}` times** in a week.

### Calculation of Active Days 🗓️

* **Active Days Count**: Only the days when the agent is actively working will be considered. If the agent is not active on a particular day (e.g., on leave or off), that day will not be counted in the scheduling logic.

### Call Schedule for Unconnected Leads 📆

If a lead has not been contacted yet, the following call schedule will be followed:

* **Day 1**:
    * **`{{vars.unconnected_leads_day1_calls}}` Calls**: The lead should receive a total of **`{{vars.unconnected_leads_day1_calls}}` calls** on the first day.
    * **`{{vars.unconnected_leads_day1_shift_calls}}` Calls** in one shift (e.g., morning shift).
    * **`{{vars.unconnected_leads_day1_shift_calls}}` Calls** in another shift (e.g., evening shift).
* **Day 2**:
    * **`{{vars.unconnected_leads_day2_calls}}` Calls**: The lead should receive **`{{vars.unconnected_leads_day2_calls}}` calls**, scheduled in shifts different from those on Day 1.
* **Day 3**:
    * **`{{vars.unconnected_leads_day3_calls}}` Call**: The lead should receive **`{{vars.unconnected_leads_day3_calls}}` call** on this day.
* **Day 5**:
    * **`{{vars.unconnected_leads_day5_calls}}` Call**: Another **`{{vars.unconnected_leads_day5_calls}}` call** should be made on this day.
* **Day 7**:
    * **`{{vars.unconnected_leads_day7_calls}}` Call**: The final call in this sequence should be made on this day.

### Important Notes 📝

* **Application of Call Flow**: This call schedule is applicable only if none of the calls have been connected with the lead.
* **Connected Calls**: If a call is connected, the scheduling and prioritization of further calls will follow a different set of rules.

### Nullify First Attempt 🚫

* **Condition**: The last attempt will be nullified if the customer revisits (via Revisit, Inbound, or Email) between the first and second attempt.

### Revisit Criteria 🔙

* **Time Difference**: A revisit will only be considered if the time between the last visit and the current visit is greater than **`{{vars.revisit_criteria_time_difference_minutes}}` minutes**.
* **During Call**: A revisit during a call will be considered a revisit.
* **Website Revisit**: If the customer revisits the PB website within **`{{vars.revisit_criteria_website_revisit_minutes}}` minutes**, it will be treated as if the revisit did not occur.

### Active Callback 🟢

* **Time Frame**: All scheduled callbacks within **CB-`{{vars.active_callback_time_frame_minutes}}` minutes** to **CB+`{{vars.active_callback_time_frame_minutes}}` minutes** fall under this category.
* **Sorting**: Internal sorting will be based on the difference between the current time and the callback time. The nearest callbacks will have higher priority.
* **Handling**: If not attempted, the lead will be moved to the ‘Passive Callback’ bucket.

### Scenarios 📊

#### Scenario 1a: Picked (1st Attempt) ✅

* **Actions**: The agent can either:
    * Book the lead or set up a callback.
    * If neither action is taken, the lead will move to the **Rest/Answered Bucket**.

#### Scenario 1b: Not Attempted/Not Answered/Not Connected (1st Attempt) 🔴

* **Handling**: The lead will be moved out of the queue for **`{{vars.scenario_1b_queue_hold_minutes}}` minutes** and will reappear after **`{{vars.scenario_1b_queue_reappear_minutes}}` minutes** according to the prioritization logic.

#### Scenario 1c: Picked (2nd Attempt) Where 1st Attempt Was Unanswered ✅

* **Actions**: The agent can either:
    * Book the lead or set up a callback.
    * If neither action is taken, the lead will move to the **Rest/Answered Bucket**.

#### Scenario 1d: Not Attempted/Not Answered/Not Connected (2nd Attempt) ❌

* **Handling**: The lead will be moved to the **Rest/Answered Bucket**.

## Inbound Workflow ☎️

---

### IVR Revamp for SME Hotline: `{{vars.sme_hotline_number}}`

#### Previous Flow

* **Main IVR**:
    * 1: GHI/GTL (1. GHI, 2. GPA, 3. GTL)
    * 2: Fire, WC, Marine, Liability & Engineering Insurance (1. Fire Insurance, 2. Workmen Compensation, 3. Marine Insurance, 4. Liability Insurance, 5. Engineering Insurance)
    * 3: If you have not received a policy copy
    * 4: Is it renewal related?
    * 5-9: Unassigned
    * 0: Unassigned

#### Current Flow

* **Main IVR**:
    * 1: Group Health Insurance, Group Personal Accident Insurance, Group Term Life
        * **Sub-IVR**: "For Group Health Insurance, press 1. For Group Personal Accident Insurance, press 2. For Group Term Life Insurance, press 3."
    * 2: Workmen Compensation
        * **Queue**: `{{vars.ivr_wc_queue_name}}`
        * **Message**: "For Workmen's Compensation Insurance, please press 2."
    * 3: Fire Insurance
        * **Queue**: `{{vars.ivr_fire_queue_name}}`
        * **Message**: "For Fire Insurance for your business, please press 3."
    * 4: Marine Insurance
        * **Queue**: `{{vars.ivr_marine_queue_name}}`
        * **Message**: "For Marine Insurance to secure your transit, please press 4."
    * 5: Doctor's Indemnity
        * **Queue**: `{{vars.ivr_doctors_indemnity_queue_name}}`
        * **Message**: "For Doctor's Indemnity Insurance, please press 5."
    * 6: Liability Insurance
        * **Queue**: `{{vars.ivr_liability_queue_name}}`
        * **Message**: "For any kind of business Liability Insurance, please press 6."
        * **Sub-IVR**: "For General Liability Insurance, press 1." "For Directors & Officers Insurance, press 2." "For Cyber Risk Insurance, press 3." "For any other professional indemnity (other than doctor), press 4." (Will land in the `{{vars.ivr_other_indemnity_queue_name}}` queue.)
    * 7: Engineering Insurance
        * **Queue**: `{{vars.ivr_engineering_queue_name}}`
        * **Message**: "For Construction Insurance, please press 7."
    * 8: Policy Renewal Related
    * 9: If you have not received a policy copy or have service-related issues
        * **Queue**: `{{vars.ivr_bms_general_queries_queue_name}}`
        * **Message**: "For any other service-related inquiries or to receive a policy copy, please press 9."

### Additional Information ℹ️

* **Lead Creation**: A lead will be created without a sub-product only when a call is received on the sales IVR.
* **Central IVR Flow**: The central IVR will play the message and direct to the SME hotline for the same user experience.
* **Message**: “For any type of business insurance, please press `{{vars.central_ivr_sme_hotline_option}}`.”

## Lead Creation Logic ✨

---

### Renewal  renewals 🔄

* **For CC**: Before **`{{vars.renewal_cc_days_before_expiry}}` days** of the expiry date.
* **For FOS**: Before **`{{vars.renewal_fos_days_before_expiry}}` days** of the expiry date.

### Winback 🏆

* **Expired**:
    * WC, CAR, EAR & CPM: Before **`{{vars.winback_expired_wccarearpm_days_from_doe}}` days** from the Date of Expiry (DOE).
    * LYLR: Last year's lost renewal: **`{{vars.winback_lylr_days_before_expiry}}` days** before the expiry.
    * LYLIR: Last year's lost interested rejected: **`{{vars.winback_lylir_days_before_expiry}}` days** before the expiry.
    * LYLCR: Last year's lost contacted rejected: **`{{vars.winback_lylcr_days_before_expiry}}` days** before the expiry.
* **Core rejected**: **`{{vars.winback_core_rejected_days_after_rejection}}` days** after the rejection date.
* **Own Rejected Winback (WB)**: **`{{vars.winback_own_rejected_days_after_rejection}}` days** after the rejection date.

## Calling Logics 🗣️

---

### Manual Attempts rules 🖐️

* If historical talk time (TT) < **`{{vars.manual_attempts_rule_tt_threshold_1_minutes}}` min** and same day TT = **`{{vars.manual_attempts_rule_same_day_tt_threshold_1_minutes}}`** and there are **`{{vars.manual_attempts_rule_unanswered_attempts}}`** unanswered attempts (UA), the advisor cannot release the call and dial manually.
* Maximum **`{{vars.manual_attempts_rule_max_daily_attempts_1}}` manual attempts** allowed in a day if same day talk time < **`{{vars.manual_attempts_rule_same_day_tt_threshold_2_minutes}}` minutes**.
* Maximum **`{{vars.manual_attempts_rule_max_daily_attempts_2}}` manual attempts** allowed in a day if same day talk time > **`{{vars.manual_attempts_rule_same_day_tt_threshold_3_minutes}}` minutes**.
* If total talk time on Leadid is less than **`{{vars.manual_attempts_rule_total_tt_threshold_minutes}}` minute**, manual attempts are not allowed and the system will dial according to its priority.

### Burst Calling rule 💥

* At customer level, if more than **`{{vars.burst_calling_unanswered_attempts_threshold}}` unanswered attempts** occur in **`{{vars.burst_calling_time_frame_minutes}}` minutes**, no calls are allowed to that customer for the next **`{{vars.burst_calling_cool_off_hours}}` hours**.
* **Exceptions** include: Paymentcallback, Callback (set before Burst calling), CTC, IB and Revisit allowed.
* If same day talk time > **`{{vars.burst_calling_same_day_tt_threshold_minutes}}` minutes**, manual calls are allowed.

## AI<>Calling - Status Stamping 🤖📝

---

* If we receive any negative sentiment from the customer (Cx), we apply a cool-off period of **`{{vars.ai_calling_cool_off_period_1_days}}` day**.
* On the second negative sentiment, the cool-off period extends to **`{{vars.ai_calling_cool_off_period_2_days}}` days**.
* On the third negative sentiment, the Cx is unsubscribed for **`{{vars.ai_calling_unsubscribed_period_days}}` days**.
* If, during this period, the Cx revisits our journey and opts to resubscribe, they will be subscribed again.
* If they do not take any action, they will be automatically resubscribed after **`{{vars.ai_calling_auto_resubscribe_period_days}}` days**.
* On rejection, we pass an identifier in the sub-status.

## Virtual Numbers 📞🌐

---

* After **`{{vars.virtual_numbers_attempts_threshold}}` attempts**, the agent can dial using virtual numbers, which have strong connectivity.
* We have enabled approximately **`{{vars.virtual_numbers_count}}` virtual numbers** across various Lines of Business (LoBs).

## Communication Process 📧💬

---

### System Communication Channels 📲

#### WhatsApp 🟢

* **Generic Communication**:
    * On lead rejection (manual or system-driven), a generic message is sent for all sub-products.
    * If the customer (Cx) clicks the provided button, the system reopens the lead and assigns it to the last assigned agent.
* **Unanswered Attempts**:
    * For selected products like D&O, PI, an Unanswered Attempts message is sent.
    * For other products, this feature is in queue for implementation.
* **PRB Communication (Potential Repeat Buyer - PRB SOP)**:
    * **First Communication**: Before scheduling a callback, the system provides an option to schedule calls earlier. This includes educational videos highlighting the risks of lack of insurance. This initiative is applied across all products, starting with PI.
    * **Video Link**: `{{vars.prb_communication_video_link}}`

#### Email Communication 📧

* CJ has an email campaign plan, but there is no current drop campaign for emails.

### Manual Communication Channels ✍️

#### WhatsApp 💬

* **Advisor Channel**:
    * Advisors have access to free text messaging for communication.
    * Currently live for WC and Marine products.
* **Main Channel**:
    * Only template-based communication is allowed.
    * Live for all non-EB products, except Cyber Retail and Property products.
    * Calendar blocking templates are enabled for these exceptions.
    * **Sales journey includes**: Greeting, Quote requirement questions, Proposal form sharing, Payment link sharing, Thank-you message.

#### Email Templates 📄

* **Generic Templates**: CJ Link, PB Meet Link, Payment Link, Blank Template.

#### PB Meet 🤝

* PB Meet functionality is currently available for GHI.
* No non-EB product is using this feature yet.
* PB Meet is a recorded video call (VC) system. The agent can send a link and request the customer to connect over PB Meet.

## Outreach Process 📢

---

* **Calling of purchase database**
* **Calling Mode**: SIM panel calling

## HOC Process 🏥

---

* Implemented for Health, Motor, and Commercial products.
* For Term and Investment, it is currently in queue.

## Lead Sourcing 💡

---

* Sales
* Service
* Employee Referrals