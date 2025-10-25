## ⚡ Executive Summary

This project automates phishing triage using Python to extract and analyze domains safely, preventing analysts from opening malicious URLs. It demonstrates rapid evidence-based decision-making for SOC operations.

Core capabilities demonstrated:
- IOC extraction (domain and URL parsing)
- Safe automation (no browsing activity)
- Data visualization to support triage decisions
- Documentation for SOC workflows

---

# 🧠 Phishing Dissection Playbook

**Author:** D (DP-Ark)  
**Target Role:** SOC Analyst  
**Focus Areas:** Threat Triage, Security Automation, IOC Handling  

---

## 🎯 Objective
Automate phishing URL analysis to extract domain-based indicators and generate triage evidence efficiently.

---

## 🔍 Scope of Analysis
| Category | Details |
|---------|---------|
| Artifact Type | Phishing URLs |
| Count | 3 sample URLs |
| IOC Focus | Domain Structure |
| Output | CSV, Chart, Analyst Report |

---

## 🧪 Methodology
| Stage | Description |
|------|-------------|
| URL Parsing | Extract domain metadata via `tldextract` |
| Safe Inspection | Avoid direct access to malicious sites |
| Feature Engineering | Domain length metric |
| Visualization | Matplotlib chart |

---

## 📈 Visual Evidence
📎 File: `domain_length_chart.png`

Domain length often increases to impersonate well-known brands, especially in credential phishing campaigns.

---

## ✅ Key Triage Insights
1. Brand impersonation patterns observed  
2. Domain structures show suspicious elongation  
3. Fully safe automation removes infection risk  
4. Repeatable workflow scales to alert queues

---

## 🧠 Skills Demonstrated
| Skill | Evidence |
|------|----------|
| Automation | Python scripts generating CSV evidence |
| IOC Handling | URL → Domain transformation logic |
| Visualization | Triage enhancement through plots |
| Analyst Communication | Evidence-based reporting |

---

## 🗂️ Artifacts
