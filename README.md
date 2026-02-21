# 🛡️ Application Security Posture Analyzer

A Python-based **Application Security Posture Analyzer** designed to identify common web security misconfigurations such as **insecure TLS settings, missing HTTP security headers, and weak CORS configurations**.

This project is being actively developed as part of a learning journey in **Python for cybersecurity and security automation**.

---

## 📌 Project Motivation

Most real-world security incidents occur due to **misconfigurations rather than complex exploits**.  
The goal of this project is to gain hands-on experience in **application security testing and automation**, similar to how real AppSec teams evaluate security posture early in the development lifecycle.

The tool is intentionally built as a **CLI-based application** to support automation and DevSecOps workflows.

---

## 🔍 Features

### 🔐 Transport Security (TLS)
* **Protocol Validation:** Performs a real TLS handshake with the server.
* **Legacy Detection:** Identifies deprecated TLS versions (TLS 1.0 and TLS 1.1).
* **Security Flagging:** Flags insecure or misconfigured TLS setups.

### 🧱 HTTP Security Headers
Checks for the presence and basic configuration of critical security headers:
* **Content-Security-Policy (CSP):** Prevents XSS and injection attacks.
* **Strict-Transport-Security (HSTS):** Enforces HTTPS connections.
* **X-Frame-Options:** Protects against Clickjacking.
* **X-Content-Type-Options:** Prevents MIME-sniffing.
* **Referrer-Policy:** Controls how much referrer information is shared.
* **Permissions-Policy:** Restricts browser features (Camera, Geolocation, etc.).

> [!IMPORTANT]  
> Missing headers are reported as **medium-severity security posture issues**.

### 🌐 CORS (Cross-Origin Resource Sharing)
* Simulates requests from an **untrusted origin**.
* Detects **overly permissive** CORS policies.
* Flags risky configurations such as **wildcard origins** (`*`) and credential exposure.

---

## 🧠 Severity Model

| Severity | Color | Description |
| :--- | :--- | :--- |
| **High** | 🔴 | Direct security risk or critical misconfiguration |
| **Medium** | 🟠 | Weak security posture or missing protection |
| **Low** | 🟢 | Informational or connectivity-related issue |

---

## 📁 Project Structure

```text
AppSec_Analyser/
│
├── analyzer.py            # Main CLI Entry Point
├── requirements.txt       # Project dependencies
├── checks/                # Security Logic Modules
│   ├── __init__.py
│   ├── tls_check.py       # SSL/TLS handshake logic
│   ├── headers_check.py   # HTTP Response header analysis
│   └── cors_check.py      # CORS simulation logic
└── README.md

---

## ▶️ How to Run

### 1️⃣ Install Dependencies
Ensure you have **Python 3.x** installed on your system.
```bash
pip install requests
### 2️⃣ Run the Analyzer
python analyzer.py [https://example.com](https://example.com)

**Try scanning common public sites for comparison:**

* [https://github.com](https://github.com)
* [https://www.wikipedia.org](https://www.wikipedia.org)

---
🚧 Project Status & Roadmap
🚀 Status: Actively under development.

Planned Improvements:

[ ] Advanced Validation: Check security header values (e.g., flagging 'unsafe-inline' in CSP).

[ ] Scoring System: Implement an improved severity scoring logic for a "Security Grade" (A-F).

[ ] Reporting: Support for exporting findings to JSON or HTML formats.

[ ] Automation: Add CI/CD integration support via GitHub Actions.

⚠️ Scope & Limitations
Posture Analysis: This tool focuses on configuration analysis, not active vulnerability exploitation.

Public Access: Designed specifically for publicly accessible web applications.

Non-Invasive: Does not perform authentication-based testing, fuzzing, or deep crawling.

Environment Dependent: SSL/TLS verification behavior may vary based on the local environment's CA certificates.

🎯 Learning Outcomes
Through the development of this tool, I am practicing:

Python for Cybersecurity: Building robust scripts that interact directly with web protocols.

AppSec Automation: Learning how to scale manual security checks into repeatable code.

Defensive Security: Gaining a deep understanding of the "why" behind TLS configurations and security headers.

📌 Disclaimer
This tool is intended for educational purposes only. Only scan applications you own or have explicit written permission to test. Use responsibly and ethically.

🤝 Author
Arantha Shreya Cybersecurity enthusiast exploring application security and automation through hands-on projects.
