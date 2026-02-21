import sys
from checks.tls_check import check_tls
from checks.headers_check import check_headers
from checks.cors_check import check_cors

def analyze(url):
    results = {
        "target": url,
        "findings": []
    }

    # TLS check (single result)
    tls_result = check_tls(url)
    if isinstance(tls_result, dict) and "issue" in tls_result:
        results["findings"].append(tls_result)

    # Header checks
    try:
        results["findings"].extend(check_headers(url))
    except Exception as e:
        results["findings"].append({
            "issue": "Header analysis failed",
            "severity": "Low",
            "details": str(e)
        })

    # CORS checks
    try:
        results["findings"].extend(check_cors(url))
    except Exception as e:
        results["findings"].append({
            "issue": "CORS analysis failed",
            "severity": "Low",
            "details": str(e)
        })

    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyzer.py https://example.com")
        sys.exit(1)

    target_url = sys.argv[1]
    report = analyze(target_url)

    print(report)

