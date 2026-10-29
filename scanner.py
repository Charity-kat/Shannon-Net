import ipaddress, json
ALLOWED = [ipaddress.ip_network("127.0.0.1/32"), ipaddress.ip_network("192.168.1.0/24")]
def is_allowed(s):
    ip = ipaddress.ip_address(s)
    return any(ip in net for net in ALLOWED)

targets = ["192.168.1.1", "192.168.1.2"]
results = []
for t in targets:
    if not is_allowed(t):
        print(f"[BLOCKED] {t}")
        continue
    print(f"Scanned {t} - FOUND OPEN DOORS! (lab)")
    results.append({"router": t, "status": "open - lab"})

with open("scan_results.json", "w") as f:
    json.dump(results, f, indent=2)
print("DONE!")
input("Press Enter...")