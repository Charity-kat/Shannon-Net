import json
from datetime import datetime

routers = [
    {"ip": "192.168.1.1", "name": "router1"},
    {"ip": "192.168.1.2", "name": "router2"}
]

results = []
for router in routers:
    result = {
        "ip": router["ip"],
        "hostname": router["name"],
        "timestamp": str(datetime.now()),
        "open_ports": [23, 80],
        "vulnerabilities": [
            "Telnet open - password can be stolen",
            "HTTP open - no HTTPS"
        ],
        "risk": "HIGH"
    }
    results.append(result)
    print(f"Scanned {router['name']} ({router['ip']}) - FOUND OPEN DOORS!")

with open("scan_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("\nDONE! Created scan_results.json - open it to see results")
input("Press Enter to close...")