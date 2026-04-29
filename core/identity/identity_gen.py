import hashlib
import random
import uuid

class DeviceGenerator:
    def __init__(self):
        self.models = ["iPhone 14 Pro", "iPhone 15 Pro Max", "iPad Pro M2"]
        self.ios_versions = ["16.6", "17.1", "17.4"]

    def generate_dna(self):
        """Generates a unique hardware signature to bypass fingerprinting."""
        model = random.choice(self.models)
        version = random.choice(self.ios_versions)
        
        # Creating unique hardware hashes
        canvas_id = hashlib.sha256(str(random.random()).encode()).hexdigest()[:16]
        hw_id = "".join(random.choices("0123456789ABCDEF", k=16))
        
        dna = {
            "model": model,
            "os_version": f"iOS {version}",
            "hw_id": hw_id,
            "canvas_hash": canvas_id,
            "user_agent": f"Mozilla/5.0 (iPhone; CPU iPhone OS {version.replace('.', '_')} like Mac OS X)",
            "proxy_ready": False
        }
        print(f"[DNA] Forged Identity: {model} | HWID: {hw_id}")
        return dna
