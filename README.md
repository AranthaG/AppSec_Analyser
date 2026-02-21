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
- **Protocol Validation:** Performs a real TLS handshake with the server  
- **Legacy Detection:** Identifies deprecated TLS versions (TLS 1.0 and TLS 1.1)  
- **Security Flagging:** Flags insecure or misconfigured TLS setups  

### 🧱 HTTP Security Headers
Checks for the presence and basic configuration of critical security headers:

- **Content-Security-Policy (CSP):** Prevents XSS and injection attacks  
- **Strict-Transport-Security (HSTS):** Enforces HTTPS connections  
- **X-Frame-Options:** Protects against Clickjacking  
- **X-Content-Type-Options:** Prevents MIME-sniffing  
- **Referrer-Policy:** Controls referrer information leakage  
- **Permissions-Policy:** Restricts browser features (camera, geolocation, etc.)

> **IMPORTANT**  
> Missing headers are reported as **medium-severity security posture issues**.

### 🌐 CORS (Cross-Origin Resource Sharing)
- Simulates requests from an **untrusted origin**  
- Detects **overly permissive** CORS policies  
- Flags risky configurations such as **wildcard origins (`*`)** and credential exposure  

---

## 🧠 Severity Model

| Severity | Indicator | Description |
|--------|----------|-------------|
| **High** | 🔴 | Direct security risk or critical misconfiguration |
| **Medium** | 🟠 | Weak security posture or missing protection |
| **Low** | 🟢 | Informational or connectivity-related issue |

---

## 📁 Project Structure

```text
AppSec_Analyser/
│
├── analyzer.py            # Main CLI entry point
├── requirements.txt       # Project dependencies
├── checks/                # Security logic modules
│   ├── __init__.py
│   ├── tls_check.py       # SSL/TLS handshake logic
│   ├── headers_check.py   # HTTP response header analysis
│   └── cors_check.py      # CORS simulation logic
└── README.md
```

## ▶️ How to Run

### 1️⃣ Install Dependencies
Ensure you have **Python 3.x** installed.

### 2️⃣ Run the Analyzer
```bash
pip install -r requirements.txt
python analyzer.py https://example.com
```
---

## 🚧 Project Status & Roadmap

**🚀 Status:** Actively under development

### Planned Improvements
- [ ] Advanced validation of security header values  
  (e.g., detecting `unsafe-inline` or `unsafe-eval` in CSP)
- [ ] Improved severity scoring with an overall **Security Grade (A–F)**
- [ ] Export findings to **JSON** and **HTML** reports
- [ ] CI/CD automation support using **GitHub Actions**
- [ ] Support for scanning multiple URLs in a single run

---

## ⚠️ Scope & Limitations

- **Posture Analysis Only**  
  This tool focuses on configuration and security posture, not exploitation.

- **Public Targets**  
  Designed for publicly accessible web applications only.

- **Non-Invasive**  
  No authentication testing, fuzzing, brute-force attacks, or deep crawling.

- **Environment Dependent**  
  TLS and certificate validation may vary based on local CA trust stores.

---

## 🎯 Learning Outcomes

Through building this tool, I am practicing:

- **Python for Cybersecurity**  
  Writing protocol-aware scripts that interact with TLS and HTTP layers.

- **Application Security Automation**  
  Converting manual AppSec checks into repeatable, automated workflows.

- **Defensive Security Thinking**  
  Understanding *why* security headers, TLS versions, and CORS policies matter.

- **DevSecOps Mindset**  
  Designing tools that can fit into CI/CD and security pipelines.

---

## 📌 Disclaimer

This project is intended for **educational purposes only**.

Only scan applications that you:
- Own, or
- Have **explicit written permission** to test.

The author is not responsible for misuse of this tool.

---

## 🤝 Author

**Arantha Shreya**  
Cybersecurity enthusiast exploring **application security** and **security automation** through hands-on projects.
