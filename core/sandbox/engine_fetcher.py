import os
import requests

class EngineFetcher:
    def __init__(self):
        self.bin_dir = "bin"
        # Official stable LSPatch release
        self.url = "https://github.com"
        self.target = os.path.join(self.bin_dir, "lspatch.jar")

    def pull_engine(self):
        """Fetches the virtualization core if missing."""
        if not os.path.exists(self.bin_dir):
            os.makedirs(self.bin_dir)
            
        if not os.path.exists(self.target):
            print(f"[*] CI: Fetching Virtual Engine Core...")
            try:
                response = requests.get(self.url, stream=True, timeout=30)
                with open(self.target, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print("[+] CI: Virtual Engine Integrated.")
            except Exception as e:
                print(f"[ERROR] Engine fetch failed: {e}")
                return False
        return True
