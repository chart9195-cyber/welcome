import sys
from core.system_shield import SystemShield
from core.sandbox.patcher import BinaryPatcher
from core.sandbox.comfort_aligner import ComfortAligner
from core.sandbox.ssl_patcher import SSLPatcher
from core.identity.identity_gen import DeviceGenerator

class UltraCloner:
    def __init__(self):
        self.shield = SystemShield()
        if not self.shield.verify_environment(): sys.exit(1)
        
        self.patcher = BinaryPatcher()
        self.id_gen = DeviceGenerator()

    def run_professional_op(self, apk_name):
        print(f"--- [ULTRA-CLONER: UNIVERSAL COMFORT MODE] ---")
        
        # 1. Deconstruct
        self.patcher.deconstruct(apk_name)
        
        # 2. Comfort & Stability (The Smart Move)
        aligner = ComfortAligner("data/work")
        aligner.optimize_for_device()
        
        # 3. Security Bypass
        ssl = SSLPatcher("data/work")
        ssl.bypass_pinning()
        
        # 4. Identity & Finalize
        dna = self.id_gen.generate_dna()
        print(f"[+] SUCCESS: {apk_name} is now optimized and stealth-ready.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cloner.py <app_name>")
    else:
        engine = UltraCloner()
        engine.run_professional_op(sys.argv)
