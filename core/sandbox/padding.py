import os
import random

class BinaryPadder:
    def inject_junk(self, work_dir):
        """Adds a unique amount of junk data to change the file size."""
        print("[*] PADDING: Adjusting binary weight for uniqueness...")
        
        junk_path = os.path.join(work_dir, "assets", "integrity_blob.dat")
        os.makedirs(os.path.dirname(junk_path), exist_ok=True)
        
        # Injects between 10KB and 50KB of random data
        junk_size = random.randint(10240, 51200)
        with open(junk_path, "wb") as f:
            f.write(os.urandom(junk_size))
            
        print(f"[+] PADDING: Injected {junk_size} bytes of unique junk data.")
