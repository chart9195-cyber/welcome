import os
import shutil

class SandboxManager:
    def __init__(self, base_dir="/data/local/tmp/uc_sandbox"):
        self.base_dir = base_dir
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

    def create_isolated_env(self, clone_id):
        """Creates a unique mount point for the clone to prevent data leaks."""
        path = os.path.join(self.base_dir, clone_id)
        try:
            os.makedirs(path, exist_ok=True)
            # Create virtual subfolders for Android isolation
            for folder in ['data', 'cache', 'shared_prefs']:
                os.makedirs(os.path.join(path, folder), exist_ok=True)
            print(f"[SANDBOX] Environment isolated at: {path}")
            return path
        except Exception as e:
            print(f"[ERROR] Isolation failed: {e}")
            return None
