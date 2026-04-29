import os

class SmaliAligner:
    def __init__(self, work_dir):
        self.work_dir = work_dir

    def align_references(self, old_package, new_package):
        """Swaps old package paths for new ones in Smali code."""
        print(f"[*] PRIMARY: Aligning Smali references...")
        
        # Convert dots to slashes (com.app -> com/app)
        old_path = old_package.replace('.', '/')
        new_path = new_package.replace('.', '/')
        
        smali_folders = [d for d in os.listdir(self.work_dir) if d.startswith('smali')]
        
        for folder in smali_folders:
            target_root = os.path.join(self.work_dir, folder)
            for root, dirs, files in os.walk(target_root):
                for file in files:
                    if file.endswith(".smali"):
                        file_path = os.path.join(root, file)
                        with open(file_path, 'r') as f:
                            content = f.read()
                        
                        if old_path in content:
                            new_content = content.replace(old_path, new_path)
                            with open(file_path, 'w') as f:
                                f.write(new_content)
        
        print("[+] PRIMARY: Smali code synchronized with new identity.")
        return True
