import random
import uuid

class DeviceGenerator:
    def create_iphone_profile(self):
        # Logic inspired by FingerprintJS and Faker
        models = ["iPhone 13 Pro", "iPhone 14", "iPhone 15 Pro Max"]
        profile = {
            "model": random.choice(models),
            "device_id": str(uuid.uuid4()),
            "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)",
            "canvas_hash": hex(random.getrandbits(64))
        }
        print(f"[ID] Spoofing as {profile['model']}")
        return profile
