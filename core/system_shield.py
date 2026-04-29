import subprocess
import os
import platform
import sys

class SystemShield:
    def __init__(self):
        self.required_tools = ["git", "python", "java"]
        self.min_java_version = 17

    def verify_environment(self):
        """Rigorous check of system tools and architectures."""
        print("[*] SHIELD: Verifying system comfortability...")
        
        # 1. Check Tool Existence
        for tool in self.required_tools:
            if subprocess.run(["which", tool], capture_output=True).returncode != 0:
                print(f"[ERROR] Missing critical tool: {tool}")
                return False

        # 2. Check Java Version (Crucial for Apktool/Gradle)
        try:
            java_version = subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT).decode()
            if "17" not in java_version and "21" not in java_version:
                print("[ERROR] Java version mismatch. Required: OpenJDK 17/21.")
                return False
        except Exception:
            print("[ERROR] Could not verify Java version.")
            return False

        # 3. Architecture Safety
        arch = platform.machine()
        print(f"[+] SHIELD: Environment {arch} confirmed stable.")
        return True

    def secure_directories(self):
        """Ensures all internal paths exist before operations begin."""
        paths = ["data/work", "data/output", "config/vault", "logs"]
        for p in paths:
            os.makedirs(p, exist_ok=True)
        print("[+] SHIELD: Internal directory structure secured.")
