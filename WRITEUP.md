Brute Force Detection with Automated Response (Splunk)
🧩 Project Overview

This project demonstrates how raw authentication logs can be transformed into actionable security intelligence using:

✔ Detection Engineering
✔ Alerting
✔ Automation
✔ Dashboard Visibility

The goal was simple:

Detect brute force attempts → Trigger alert → Auto-respond → Visualize attacker

📥 Step 1 — Log Ingestion

Authentication logs were uploaded into Splunk using CSV format.

Once ingested, the logs were structured into tabular format inside Splunk for analysis.

📸 [Screenshot 1 – CSV uploaded]
📸 [Screenshot 2 – Parsed into table view]

This step ensured fields like:

time

user

src_ip

action

result

were properly extracted.

🔎 Step 2 — Suspicious Activity Identification

From the structured logs, failed login patterns were analyzed.

Using SPL, we extracted repeated failed attempts from a single IP within a short time window.

This represents a classic brute-force behavior.

📸 [Screenshot 3 – Detection Query Output]

This stage is called:

👉 Behavioral Pattern Extraction

🚨 Step 3 — Alert Creation

A detection rule was created to identify:

Multiple failed login attempts within 1 minute

Once this threshold was met:

Splunk generated an alert automatically.

📸 [Screenshot 4 – Alert Created]

This moved detection from passive monitoring to active response readiness.

🤖 Step 4 — Automated Response via Script

Instead of stopping at alerting, an automated containment action was added.

A Python script was integrated with the alert action.

The script:

✔ Extracts attacker IP
✔ Writes it into a blocklist file

📸 [Screenshot 5 – Script Integration]

🛡️ Step 5 — Simulated Firewall Blocking

Since no real firewall was available in this lab setup,

A simulated response mechanism was implemented.

When alert triggered:

The attacker IP was automatically added to:

firewall_blocklist.txt

📸 [Screenshot 6 – Blocklist Updated]

This represents:

👉 Automated incident containment

📊 Step 6 — Dashboard Visibility

To improve visibility, a detection dashboard was created.

Panel:

Top Suspicious IPs

Now, whenever an attacker triggers detection:

Their IP appears in the dashboard.

📸 [Screenshot 7 – Dashboard View]

This enables quick prioritization and monitoring.

🔁 Detection Pipeline Achieved
Capability	Status
Log ingestion	✅
Field extraction	✅
Attack detection	✅
Alerting	✅
Automated response	✅
Dashboard visualization	✅
🧠 What This Demonstrates

This project shows:

✔ How logs become intelligence
✔ How alerts become actions
✔ How automation reduces response time

Even without real infrastructure, detection-to-response logic was successfully simulated.

🚀 Future Scope

Real firewall integration

Slow brute force detection

Risk scoring

Geo anomaly detection