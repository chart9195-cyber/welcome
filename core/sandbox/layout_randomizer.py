import os
import random
import re

class LayoutRandomizer:
    def __init__(self, work_dir):
        self.work_dir = work_dir

    def shuffle_resources(self):
        """Subtly modifies XML values to change the APK's binary signature."""
        print("[*] LAYOUT: Shuffling resource signatures for uniqueness...")
        
        layout_path = os.path.join(self.work_dir, "res", "layout")
        if not os.path.exists(layout_path):
            return

        for root, dirs, files in os.walk(layout_path):
            for file in files:
                if file.endswith(".xml"):
                    self._obfuscate_xml(os.path.join(root, file))

    def _obfuscate_xml(self, file_path):
        """Randomizes margins and colors by negligible amounts."""
        with open(file_path, 'r') as f:
            content = f.read()

        # Change padding/margins by 1dp to alter file hash
        new_content = re.sub(r'(\d+)dp', lambda m: f"{int(m.group(1)) + random.choice([-1, 0, 1])}dp", content)
        
        with open(file_path, 'w') as f:
            f.write(new_content)
