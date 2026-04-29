import requests
import re
import json
import os

class RealitySync:
    def __init__(self):
        self.config_path = "config/live_specs.json"
        self.ua_source = "https://deviceatlas.com/blog/list-of-user-agent-strings"

    def fetch_latest_specs(self):
        """Scrapes and synchronizes the latest iPhone/iOS metadata."""
        print("[*] SYNC: Fetching latest real-world hardware signatures...")
        try:
            # Logic: Pull fresh UA strings for iPhone 16/17/18
            response = requests.get(self.ua_source, timeout=10)
            # Professional Regex for UA extraction
            ua_list = re.findall(r'Mozilla/5.0 \(iPhone; CPU iPhone OS [\d_]+ like Mac OS X\).*?Safari/[\d.]+', response.text)
            
            if ua_list:
                with open(self.config_path, 'w') as f:
                    json.dump({"latest_uas": list(set(ua_list))}, f)
                print(f"[+] SYNC: {len(ua_list)} fresh User-Agents synchronized.")
                return True
        except Exception as e:
            print(f"[ERROR] Sync failed: {e}. Falling back to internal defaults.")
        return False
