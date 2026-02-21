import ssl
import socket
from urllib.parse import urlparse

def check_tls(url):
    hostname = urlparse(url).hostname
    context = ssl.create_default_context()

    try:
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                protocol = ssock.version()

                if protocol in ["TLSv1", "TLSv1.1"]:
                    return {
                        "issue": "Weak TLS version enabled",
                        "severity": "High",
                        "remediation": "Disable TLS 1.0 and 1.1. Enforce TLS 1.2 or higher"
                    }

                return {
                    "status": "Secure TLS configuration",
                    "protocol": protocol
                }

    except Exception as e:
        return {
            "issue": "TLS misconfiguration",
            "severity": "High",
            "details": str(e),
            "remediation": "Ensure HTTPS is correctly configured with a valid certificate"
        }
