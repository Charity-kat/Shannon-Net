logo.jpg

# 🔥 Shannon-Net
### ISP Router Vulnerability Scanner |
Your ISP said the router is secure? Shannon-Net said **"let's check."**

### 😭 The Tea
Thousands of SA routers still have port 23 (Telnet) and 80 (HTTP) WIDE OPEN. Default password `admin/admin` and they wonder why WiFi gets hacked.

### 😎 What Shannon-Net Does
- Scans routers for open management ports
- Flags them: `🔴 HIGH RISK | 🟡 MEDIUM | 🟢 SAFE`
- Drops results into `scan_results.json`
- Shows a live, sexy dashboard — no boring terminal

### 📸 Live Proof
Dashboard live on `localhost:8000` — 2 HIGH RISK routers caught on camera.

### 🚀 Run It Like This
```bash
git clone https://github.com/Charity-kat/Shannon-Net.git
cd Shannon-Net
python scanner.py
python -m http.server 8000
