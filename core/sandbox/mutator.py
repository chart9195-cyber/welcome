import os
import re

class PackageMutator:
    def __init__(self, work_dir):
        self.work_dir = work_dir
        self.manifest_path = os.path.join(work_dir, "AndroidManifest.xml")

    def mutate_identity(self, new_suffix="ultra_clone"):
        """Changes the internal package name to allow parallel installation."""
        print("[*] MUTATOR: Altering app package identity...")
        
        if not os.path.exists(self.manifest_path):
            print("[!] ERROR: AndroidManifest.xml not found!")
            return False

        with open(self.manifest_path, 'r') as f:
            content = f.read()

        # Find the original package name (e.g., package="com.target.app")
        match = re.search(r'package="([^"]+)"', content)
        if match:
            old_package = match.group(1)
            new_package = f"{old_package}.{new_suffix}"
            
            # Replace in Manifest
            new_content = content.replace(f'package="{old_package}"', f'package="{new_package}"')
            
            with open(self.manifest_path, 'w') as f:
                f.write(new_content)
                
            print(f"[+] MUTATOR: {old_package} -> {new_package}")
            return new_package
        return None
