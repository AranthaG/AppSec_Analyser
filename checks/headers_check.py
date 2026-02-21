import requests
import urllib3

# Disable SSL warnings when verify=False is used
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]

def check_headers(url):
    findings = []

    try:
        response = requests.get(url, timeout=5, verify=False)

        for header in SECURITY_HEADERS:
            if header not in response.headers:
                findings.append({
                    "issue": f"Missing {header}",
                    "severity": "Medium",
                    "remediation": f"Configure the {header} HTTP response header"
                })

    except requests.exceptions.SSLError as e:
        findings.append({
            "issue": "SSL certificate validation failed",
            "severity": "Medium",
            "details": str(e),
            "remediation": "Ensure the server presents a valid certificate chain trusted by clients"
        })

    except requests.exceptions.RequestException as e:
        findings.append({
            "issue": "HTTP request failed",
            "severity": "Low",
            "details": str(e),
            "remediation": "Verify the target URL is reachable and responding correctly"
        })

    return findings
