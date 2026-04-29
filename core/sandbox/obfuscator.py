import os
import uuid
import secrets

class ResourceObfuscator:
    def __init__(self, work_dir):
        self.work_dir = work_dir

    def randomize_assets(self):
        """Renames all image assets to random strings to break fuzzy hashing."""
        print("[*] OBFUSCATOR: Randomizing asset signatures...")
        
        asset_paths = [
            os.path.join(self.work_dir, "res", "drawable"),
            os.path.join(self.work_dir, "res", "mipmap-hdpi"),
            os.path.join(self.work_dir, "assets")
        ]

        for path in asset_paths:
            if os.path.exists(path):
                for filename in os.listdir(path):
                    if filename.endswith(('.png', '.jpg', '.jpeg', '.json')):
                        ext = os.path.splitext(filename)[1]
                        new_name = secrets.token_hex(8) + ext
                        
                        old_file = os.path.join(path, filename)
                        new_file = os.path.join(path, new_name)
                        
                        os.rename(old_file, new_file)
        
        print("[+] OBFUSCATOR: Resource map uniquely scrambled.")
