# Lead Management & Communication SOP 🚀

This document details the strategies and processes for **lead allocation**, **dialing**, **inbound call handling**, **lead creation**, and various **communication channels** across different product lines.

---

## 1. Lead Allocation 🤝

### Core Leads
* **Below {{vars.core_lead_lives_threshold_low}} Lives**: Assigned to the **{{vars.group_high_ape}}**.
* **{{vars.core_lead_lives_threshold_high}} & Above {{vars.core_lead_lives_threshold_high}} Lives**: Assigned to the **{{vars.group_online_hybrid_high_lives}}**.
* **Note**: All leads from the core channel with **{{vars.core_lead_zero_lives}}** lives are now also assigned to the **{{vars.group_high_ape}}**.

### Non-Core Leads
* All non-core leads are assigned to the **{{vars.group_high_ape}}**.

### Mobile App Allocation 📱
* If the customer selects "**Company**" as input, the lead is assigned to the **{{vars.group_high_ape}}**.
* If the customer selects "**Individual**", the lead is assigned to the **{{vars.group_sme_hoc}}**.

### Winback Allocation 🔄
* **Strategy**: Leads are generally assigned to the agents who previously worked on those cases.
* **Winback Types**:
    * **{{vars.winback_type_lylr}}** (Last Year Lapsed Renewal)
    * **{{vars.winback_type_lylir}}** (Last Year Lapsed Intermediate Renewal)
    * **{{vars.winback_type_lylcr}}** (Last Year Lapsed Canceled Renewal)
* **{{vars.winback_type_lylr}} Specifics**: Most **{{vars.winback_type_lylr}}** allocations are now directed to fresh agents. However, a few leads are still assigned to renewal agents if they were the last agents to work on those cases prior to this allocation.

---

## 2. Assignment TAT ⏱️
* Leads are assigned within **{{vars.lead_assignment_tat_minutes}}** minutes of their creation.

---

## 3. Dialing Logics 📞

### Generic
* **Working Hours**: **{{vars.working_hours_start}}** to **{{vars.working_hours_end}}** (Last lead assignment time: **{{vars.last_lead_assignment_time}}**)
* **Non-Working Hours**: **{{vars.non_working_hours_start}}** to **{{vars.non_working_hours_end}}**
* **Lead Age**: If a lead has a status of "**New**" or "**Valid**" and no contact has been made within the next **{{vars.lead_rejection_days_no_contact}}** days, the system will automatically mark the lead as "**Rejected**."
* **Future Prospect**:
    * If the talk time on a particular lead is **{{vars.future_prospect_talk_time_threshold_minutes}}** minutes, the agent cannot mark the lead as a "**Future Prospect**."
    * If a lead in Sub-product A is rejected as a "**Future Prospect**" and the user (at the customer ID level) purchases any sub-product across SME before the specified date, no lead will be created on that specific date.
    * The minimum start date for a "**Future Prospect**" is D+**{{vars.future_prospect_min_start_date_days}}** days.

### Winback Logic 🔙
* **WC Expired Leads**: Created before **{{vars.wc_expired_lead_creation_days}}** days of policy expiry.
* **PI Last Year Lost Cases/Renewal**: Created before **{{vars.pi_lost_cases_renewal_creation_days}}** days of policy expiry.
* **Marine Winback**: For last year's lost renewals.
* **Liability Winback**: For last year's lost renewals.

### Lead (Call) Status 📊
These statuses are system-assigned, but the agent can change the status from the UI. Additionally, if the status is changed from "**Valid**" to "**Interested**," it cannot be reverted to "**Valid**" by either the user or the system.

* **New**: A new lead in the system. If a user creates a new child ID while having an existing parent lead with a status other than "**New**," the child ID will be marked as "**New**," but the call will always be initiated on the parent ID. After booking, the status of the call will be marked as "**Parent/Child Booked**."
* **Valid**: The customer didn’t pick up the call (i.e., there is a ring time available), or the number was switched off, or the call duration was less than **{{vars.status_valid_call_duration_seconds}}** seconds.
* **Interested**: Call duration is **{{vars.status_interested_call_duration_seconds}}** seconds or more.
* **Contacted**: Call duration is between **{{vars.status_contacted_call_duration_min_seconds}}** seconds and **{{vars.status_contacted_call_duration_max_minutes}}** minutes.

### Call Transfer Flow ➡️
* Click on the transfer icon. After that, we will ask for the transfer type and sub-product type, and then the panel will be displayed. However, the panel should patch to the first available agent rather than the previous one.

### Lead Treatment 🔄
* First, reject the initial lead with the disposition "**Interested in Other LOB**" and create a new lead with the lead source from the initial lead.
* **Assignment**: The new lead should be assigned to the first available agent, with selection available accordingly.

---

## 4. Dialer Logics 🤖

### Dialer Priority ⬆️
* Dialer with explanation.

### Rejection Logic ❌

| Subproduct ID | Subproduct Name | New / Valid | Contacted | Interested |
| :------------ | :-------------- | :---------- | :-------- | :--------- |
| **{{vars.prod_id_marine_insurance}}** | Marine Insurance | At **{{vars.marine_rej_attempts_new_valid}}** attempts | At **{{vars.marine_rej_attempts_contacted}}** attempts | After **{{vars.marine_rej_attempts_interested}}** attempts |
| **{{vars.prod_id_workmen_compensation}}** | Workmen compensation | At **{{vars.wc_rej_attempts_new_valid}}** attempts | At **{{vars.wc_rej_attempts_contacted}}** attempts | After **{{vars.wc_rej_attempts_interested}}** attempts |
| **{{vars.prod_id_fire_burglary}}** | Fire and Burglary | At **{{vars.fire_rej_attempts_new_valid}}** attempts | At **{{vars.fire_rej_attempts_contacted}}** attempts | At **{{vars.fire_rej_attempts_interested}}** attempts |
| **{{vars.prod_id_shop_owner_insurance}}** | Shop owner Insurance | At **{{vars.shop_rej_attempts_new_valid}}** attempts | At **{{vars.shop_rej_attempts_contacted}}** attempts | At **{{vars.shop_rej_attempts_interested}}** attempts |
| **{{vars.prod_id_office_package_policy}}** | Office package Policy | At **{{vars.office_rej_attempts_new_valid}}** attempts | At **{{vars.office_rej_attempts_contacted}}** attempts | At **{{vars.office_rej_attempts_interested}}** attempts |
| **{{vars.prod_id_construction_all_risk}}** | Construction all Risk | At **{{vars.construction_rej_attempts_new_valid}}** attempts | At **{{vars.construction_rej_attempts_contacted}}** attempts | At **{{vars.construction_rej_attempts_interested}}** attempts |
| **{{vars.prod_id_erection_all_risk}}** | Erection All risk | At **{{vars.erection_rej_attempts_new_valid}}** attempts | At **{{vars.erection_rej_attempts_contacted}}** attempts | At **{{vars.erection_rej_attempts_interested}}** attempts |
| **{{vars.prod_id_plant_machinery_1}}** | Plant and Machinery | At **{{vars.plant_machinery_1_rej_attempts_new_valid}}** attempts | At **{{vars.plant_machinery_1_rej_attempts_contacted}}** attempts | At **{{vars.plant_machinery_1_rej_attempts_interested}}** attempts |
| **{{vars.prod_id_general_liability}}** | General Liability | At **{{vars.general_liability_rej_attempts_new_valid}}** attempts | At **{{vars.general_liability_rej_attempts_contacted}}** attempts | At **{{vars.general_liability_rej_attempts_interested}}** attempts |
| **{{vars.prod_id_d_o}}** | D&O | At **{{vars.d_o_rej_attempts_new_valid}}** attempts | At **{{vars.d_o_rej_attempts_contacted}}** attempts | At **{{vars.d_o_rej_attempts_interested}}** attempts |
| **{{vars.prod_id_e_o}}** | E&O | At **{{vars.e_o_rej_attempts_new_valid}}** attempts | At **{{vars.e_o_rej_attempts_contacted}}** attempts | At **{{vars.e_o_rej_attempts_interested}}** attempts |
| **{{vars.prod_id_ghi}}** | GHI | At **{{vars.ghi_rej_attempts_new_valid}}** attempts | At **{{vars.ghi_rej_attempts_contacted}}** attempts | At **{{vars.ghi_rej_attempts_interested}}** attempts |
| **{{vars.prod_id_gpa}}** | GPA | At **{{vars.gpa_rej_attempts_new_valid}}** attempts | At **{{vars.gpa_rej_attempts_contacted}}** attempts | At **{{vars.gpa_rej_attempts_interested}}** attempts |
| **{{vars.prod_id_opd_care_360}}** | OPD care 360 | At **{{vars.opd_rej_attempts_new_valid}}** attempts | At **{{vars.opd_rej_attempts_contacted}}** attempts | At **{{vars.opd_rej_attempts_interested}}** attempts |
| **{{vars.prod_id_pi}}** | PI | At **{{vars.pi_rej_attempts_new_valid}}** attempts | At **{{vars.pi_rej_attempts_contacted}}** attempts | At **{{vars.pi_rej_attempts_interested}}** attempts |
| **{{vars.prod_id_public_liability}}** | Public Liability | At **{{vars.public_liability_rej_attempts_new_valid}}** attempts | At **{{vars.public_liability_rej_attempts_contacted}}** attempts | At **{{vars.public_liability_rej_attempts_interested}}** attempts |
| **{{vars.prod_id_cyber_risk_insurance}}** | Cyber Risk Insurance | At **{{vars.cyber_risk_rej_attempts_new_valid}}** attempts | At **{{vars.cyber_risk_rej_attempts_contacted}}** attempts | At **{{vars.cyber_risk_rej_attempts_interested}}** attempts |
| **{{vars.prod_id_plant_machinery_2}}** | Plant and Machinery | At **{{vars.plant_machinery_2_rej_attempts_new_valid}}** attempts | At **{{vars.plant_machinery_2_rej_attempts_contacted}}** attempts | At **{{vars.plant_machinery_2_rej_attempts_interested}}** attempts |

### Export to Sheets 📤

### New Lead Calling Flow 🆕
* All leads can get dialed max **{{vars.max_calls_per_week}}** times in a week.

### Calculation of Active Days 🗓️
* **Active Days Count**: Only the days when the agent is actively working will be considered. If the agent is not active on a particular day (e.g., on leave or off), that day will not be counted in the scheduling logic.

### Call Schedule for Unconnected Leads ⏳
If a lead has not been contacted yet, the following call schedule will be followed:

* **Day {{vars.unconnected_calls_day_1}}**: **{{vars.unconnected_calls_day_1_total}}** Calls: The lead should receive a total of 4 calls on the first day.
    * **{{vars.unconnected_calls_day_1_shift_1}}** Calls in one shift (e.g., morning shift).
    * **{{vars.unconnected_calls_day_1_shift_2}}** Calls in another shift (e.g., evening shift).
* **Day {{vars.unconnected_calls_day_2}}**: **{{vars.unconnected_calls_day_2_total}}** Calls: The lead should receive 2 calls, scheduled in shifts different from those on Day 1. For example, if calls on Day 1 were in the morning and evening, the calls on Day 2 might be scheduled in the afternoon and late evening.
* **Day {{vars.unconnected_calls_day_3}}**: **{{vars.unconnected_calls_day_3_total}}** Call: The lead should receive 1 call on this day.
* **Day {{vars.unconnected_calls_day_5}}**: **{{vars.unconnected_calls_day_5_total}}** Call: Another 1 call should be made on this day.
* **Day {{vars.unconnected_calls_day_7}}**: **{{vars.unconnected_calls_day_7_total}}** Call: The final call in this sequence should be made on this day.

**Important Notes**:

* **Application of Call Flow**: This call schedule is applicable only if none of the calls have been connected with the lead. In other words, if the lead has not answered any of the calls or if the calls went unanswered.
* **Connected Calls**: If a call is connected (i.e., the lead answers the call), the scheduling and prioritization of further calls will follow a different set of rules or logic, which should be specified in your system's guidelines.

This flow ensures systematic and regular attempts to contact the lead, adjusting for agent availability and prioritizing connected calls based on established rules.

### Nullify First Attempt 🚫
* **Condition**: The last attempt will be nullified if the customer revisits (via Revisit, Inbound, or Email) between the first and second attempt.

### Revisit Criteria 🔙
* **Time Difference**: A revisit will only be considered if the time between the last visit and the current visit is greater than **{{vars.revisit_time_difference_minutes}}** minutes.
* **During Call**: A revisit during a call will be considered a revisit.
* **Website Revisit**: If the customer revisits the PB website within **{{vars.pb_website_revisit_duration_minutes}}** minutes, it will be treated as if the revisit did not occur.

### Active Callback 🔄
* **Time Frame**: All scheduled callbacks within CB-**{{vars.active_callback_time_frame_minutes}}** minutes to CB+**{{vars.active_callback_time_frame_minutes}}** minutes fall under this category.
* **Sorting**: Internal sorting will be based on the difference between the current time and the callback time. The nearest callbacks will have higher priority.
* **Handling**: If not attempted, the lead will be moved to the ‘Passive Callback’ bucket.

### Scenarios 🧩
* **Scenario 1a: Picked (1st Attempt)**
    * **Actions**: The agent can either: Book the lead or set up a callback.
    * If neither action is taken, the lead will move to the Rest/Answered Bucket.
* **Scenario 1b: Not Attempted/Not Answered/Not Connected (1st Attempt)**
    * **Handling**: The lead will be moved out of the queue for **{{vars.scenario_1b_queue_out_duration_minutes}}** minutes and will reappear after **{{vars.scenario_1b_queue_out_duration_minutes}}** minutes according to the prioritization logic.
* **Scenario 1c: Picked (2nd Attempt) Where 1st Attempt Was Unanswered**
    * **Actions**: The agent can either: Book the lead or set up a callback.
    * If neither action is taken, the lead will move to the Rest/Answered Bucket.
* **Scenario 1d: Not Attempted/Not Answered/Not Connected (2nd Attempt)**
    * **Handling**: The lead will be moved to the Rest/Answered Bucket.

---

## 5. Inbound Workflow ☎️

### IVR Revamp for SME Hotline: **{{vars.sme_hotline_number}}**

### Current Flow
* **Main IVR**:
    * **1**: Group Health Insurance, Group Personal Accident Insurance, Group Term Life
        * **Sub-IVR**: "For Group Health Insurance, press **{{vars.sme_ivr_ghi_option}}**. For Group Personal Accident Insurance, press **{{vars.sme_ivr_gpa_option}}**. For Group Term Life Insurance, press **{{vars.sme_ivr_gtl_option}}**."
    * **2**: Workmen's Compensation
        * **Queue**: **{{vars.sme_wc_ivr_queue}}**
        * **Message**: "For Workmen's Compensation Insurance, please press **{{vars.sme_wc_ivr_option}}**."
    * **3**: Fire Insurance
        * **Queue**: **{{vars.sme_fire_ivr_queue}}**
        * **Message**: "For Fire Insurance for your business, please press **{{vars.sme_fire_ivr_option}}**."
    * **4**: Marine Insurance
        * **Queue**: **{{vars.sme_marine_ivr_queue}}**
        * **Message**: "For Marine Insurance to secure your transit, please press **{{vars.sme_marine_ivr_option}}**."
    * **5**: Doctor's Indemnity
        * **Queue**: **{{vars.sme_doctor_indemnity_ivr_queue}}**
        * **Message**: "For Doctor's Indemnity Insurance, please press **{{vars.sme_doctor_indemnity_ivr_option}}**."
    * **6**: Liability Insurance
        * **Queue**: **{{vars.sme_liability_ivr_queue}}**
        * **Message**: "For any kind of business Liability Insurance, please press **{{vars.sme_liability_ivr_option}}**."
        * **Sub-IVR**:
            * "For General Liability Insurance, press **{{vars.sme_liability_ivr_general_option}}**."
            * "For Directors & Officers Insurance, press **{{vars.sme_liability_ivr_d_o_option}}**."
            * "For Cyber Risk Insurance, press **{{vars.sme_liability_ivr_cyber_option}}**."
            * "For any other professional indemnity (other than doctor), press **{{vars.sme_liability_ivr_other_indemnity_option}}**." (Will land in the indemnity queue.)
    * **7**: Engineering Insurance
        * **Queue**: **{{vars.sme_engineering_ivr_queue}}**
        * **Message**: "For Construction Insurance, please press **{{vars.sme_engineering_ivr_option}}**."
    * **8**: Policy Renewal Related
    * **9**: If you have not received a policy copy or have service-related issues
        * **Queue**: **{{vars.sme_general_queries_ivr_queue}}**
        * **Message**: "For any other service-related inquiries or to receive a policy copy, please press **{{vars.sme_general_queries_ivr_option}}**."

### Additional Information:
* **Lead Creation**: A lead will be created without a sub-product only when a call is received on the sales IVR.
* **Central IVR Flow**: The central IVR will play the message and direct to the SME hotline for the same user experience.
    * **Message**: “For any type of business insurance, please press **{{vars.central_ivr_business_insurance_option}}**.”

---

## 6. Lead Creation Logic ✨

### Renewal  renewals
* **For CC**: Before **{{vars.renewal_lead_creation_cc_days}}** days of the expiry date.
* **For FOS**: Before **{{vars.renewal_lead_creation_fos_days}}** days of the expiry date.

### Winback
* **Expired**:
    * WC, CAR, EAR & CPM: Before **{{vars.winback_expired_wc_car_ear_cpm_days}}** days from the Date of Expiry (DOE).
    * LYLR: Last year's lost renewal: **{{vars.winback_lylr_days}}** days before the expiry.
    * LYLIR: Last year's lost interest rejected: **{{vars.winback_lylir_days}}** days before the expiry.
    * LYLCR: Last year's lost contacted rejected: **{{vars.winback_lylcr_days}}** days before the expiry.
* **Core Rejected**: **{{vars.winback_core_rejected_days}}** days after the rejection date.
* **Own Rejected Winback (WB)**: **{{vars.winback_own_rejected_days}}** days after the rejection date.

---

## 7. Calling Logics 🗣️

### Manual Attempts Rules 📝
* If historical talk time (TT) < **{{vars.manual_attempts_hist_tt_threshold_min}}** min and same day TT = **{{vars.manual_attempts_same_day_tt_threshold_min}}** and there are **{{vars.manual_attempts_unanswered_threshold}}** unanswered attempts (UA), the advisor cannot release the call and dial manually.
* Maximum **{{vars.manual_attempts_max_per_day_low_tt}}** manual attempts allowed in a day if same day talk time < **{{vars.manual_attempts_same_day_tt_low_threshold_min}}** minutes.
* Maximum **{{vars.manual_attempts_max_per_day_high_tt}}** manual attempts allowed in a day if same day talk time > **{{vars.manual_attempts_same_day_tt_high_threshold_min}}** minutes.
* If total talk time on Leadid is less than **{{vars.manual_attempts_total_tt_no_manual_min}}** minute, manual attempts are not allowed and the system will dial according to its priority.

### Burst Calling Rule 📈
* At customer level, if more than **{{vars.burst_calling_unanswered_attempts_threshold}}** unanswered attempts occur in **{{vars.burst_calling_time_frame_minutes}}** minutes, no calls are allowed to that customer for the next **{{vars.burst_calling_cool_off_hours}}** hours.
* Exceptions include: Paymentcallback, Callback (set before Burst calling), CTC, IB and Revisit allowed.
* If same-day talk time > **{{vars.burst_calling_same_day_tt_exception_minutes}}** minutes, manual calls are allowed.

### AI <> Calling - Status Stamping 🤖💬
* In Brief: If we receive any negative sentiment from the customer (Cx), we apply a cool-off period of **{{vars.ai_negative_sentiment_cool_off_days_1}}** day.
* On the second negative sentiment, the cool-off period extends to **{{vars.ai_negative_sentiment_cool_off_days_2}}** days.
* On the third negative sentiment, the Cx is unsubscribed for **{{vars.ai_negative_sentiment_unsubscribe_days}}** days.
* If, during this period, the Cx revisits our journey and opts to resubscribe, they will be subscribed again.
* If they do not take any action, they will be automatically resubscribed after **{{vars.ai_negative_sentiment_resubscribe_days}}** days.
* On rejection, we pass an identifier in the sub-status.

### Virtual Numbers 🌐
* After **{{vars.virtual_number_attempts_threshold}}** attempts, the agent can dial using virtual numbers, which have strong connectivity.
* We have enabled approximately **{{vars.total_virtual_numbers_enabled}}** virtual numbers across various Lines of Business (LoBs).

---

## 8. Communication Process ✉️

### Tracker
* Link: [Communication Tracker]

### System Communication Channels 📲

* **WhatsApp**
    * **Generic Communication**: On lead rejection (manual or system-driven), a generic message is sent for all sub-products.
    * If the customer (Cx) clicks the provided button, the system reopens the lead and assigns it to the last assigned agent.
    * **Unanswered Attempts**: For selected products like D&O, PI, an Unanswered Attempts message is sent.
    * For other products, this feature is in queue for implementation.
* **PRB Communication (Potential Repeat Buyer - PRB SOP)**
    * **First Communication**: Before scheduling a callback, the system provides an option to schedule calls earlier.
    * This includes educational videos highlighting the risks of lack of insurance.
    * This initiative is applied across all products, starting with PI.
    * Video Link: **{{vars.prb_communication_video_link}}**
* **Email Communication**: CJ has an email campaign plan, but there is no current drop campaign for emails.

### Manual Communication Channels ✍️

* **WhatsApp**
    * **Advisor Channel**: Advisors have access to free text messaging for communication.
    * Currently live for WC and Marine products.
    * **Main Channel**: Only template-based communication is allowed.
    * Live for all non-EB products, except Cyber Retail and Property products.
    * Calendar blocking templates are enabled for these exceptions.
    * **Sales journey includes**:
        * Greeting
        * Quote requirement questions
        * Proposal form sharing
        * Payment link sharing
        * Thank-you message
* **Email Templates**
    * **Generic Templates**:
        * CJ Link
        * PB Meet Link
        * Payment Link
        * Blank Template
* **PB Meet**
    * PB Meet functionality is currently available for GHI.
    * No non-EB product is using this feature yet.
    * PB Meet is a recorded video call (VC) system.
    * The agent can send a link and request the customer to connect over PB Meet.
* **Matrix GoSME flow**
* **Field Advisor flow**
* **Outreach Process**
    * Calling of purchase database
    * **Calling Mode**: SIM panel calling
* **HOC Process**
    * Implemented for Health, Motor, and Commercial products.
    * For Term and Investment, it is currently in queue.

### Lead Sourcing 💡
* Sales
* Service
* Employee Referrals