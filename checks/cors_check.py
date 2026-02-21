import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_cors(url):
    findings = []
    headers = {
        "Origin": "https://evil.com"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=5,
            verify=False
        )

        if response.headers.get("Access-Control-Allow-Origin") == "*":
            findings.append({
                "issue": "Overly permissive CORS policy",
                "severity": "High",
                "remediation": "Restrict Access-Control-Allow-Origin to trusted domains"
            })

        if response.headers.get("Access-Control-Allow-Credentials") == "true":
            findings.append({
                "issue": "CORS allows credentials",
                "severity": "High",
                "remediation": "Avoid allowing credentials unless strictly required"
            })

    except requests.exceptions.SSLError as e:
        findings.append({
            "issue": "SSL certificate validation failed during CORS check",
            "severity": "Medium",
            "details": str(e),
            "remediation": "Ensure valid TLS certificate chain is configured"
        })

    except requests.exceptions.RequestException as e:
        findings.append({
            "issue": "CORS check request failed",
            "severity": "Low",
            "details": str(e),
            "remediation": "Verify the application is reachable"
        })

    return findings
