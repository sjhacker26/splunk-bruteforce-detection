# Splunk Bruteforce Detection & Automated Action Using Splunk

_This project detects brute-force login attempts from logs and automatically performs a response action using Splunk alerts and a Python script._

---

## Table of Contents
- <a href="#objectives">Objectives</a>
- <a href="#overview">Overview</a>
- <a href="#tools--technologies">Tools & Technologies</a>
- <a href="#methodology">Methodology</a>
- <a href="#future-improvements">Future improvements</a>
- <a href="#final-recommendation">Final Recommendation</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#author-contact">Author & Contact</a>

---

<h2><a class="anchor" id="objectives"></a>Objectives</h2>

- Detect brute-force login attemps using log analysis
- Create automated alerts for suspicious activity
- Simulate basic automatic response by blocking attacker IP
- Visualize suspicious behavior using dashboard


---

<h2><a class="anchor" id="overview"></a>Overview</h2>

Security teams rely on logs to identify suspicious activity. One common attack pattern is repeated failed login attempts from the same IP. 

In this project, authentication logs were ingested into Splunk , analyzed to detect brute-force behaviour, and an automated response was triggered when suspicious activiy was identified.

---

<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>

- Splunk Enterprise
- SPL (Splunk Processing Language)
- Python Automation Script
- CSV log Files
- GitHub

---

<h2><a class="anchor" id="methodology"></a>Methodology</h2>

The following steps were performed:
1. Logs ere uploaded into Splunk.
2. A detection query was created to identify multiple failed logins.
3. An alert was configured based on detection threshold.
4. A python script was triggered automalically.
5. Suspicious IP was added to simulated blocklist.
6. Dashboard was created to visualize suspicious activity.

---

<h2><a class="anchor" id="future-improvements"></a>Future improvements</h2>

- Real firewall integration
- Real-time log ingestion
- SOAR-based response automation

---

<h2><a class="anchor" id="final-recommendation"></a>Final Recommendation</h2>

Organizations should implement automated detection and response mechanisms to quickly identify brute-force attacks from login logs.

Even basic log analysis combined with alert automation can significantly improve security visibility and response time.

---

<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

```
splunk-bruteforce-detection/
├── README.md
├── WRITEUP.md
├── data/                      
│   ├── logs.csv  
│   └── spl_query.txt                 
├── scripts/                       # Automation scripts
│   └──autoscript.py
├── images/                        # imgs, screenshots
├── output/
│   └── firewall_blocklist.txt
├── .gitignore                

```
<h2><a class="anchor" id="author-contact"></a>Author & Contact</h2>

**Sonu Kumar**
- Email: sjhacker@gmail.com
- [LinkedIN](https:www.linkedin.com/in/sonu-kumar-00a707a8/)

