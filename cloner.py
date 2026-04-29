import sys
import os
from core.system_shield import SystemShield
from core.sandbox.patcher import BinaryPatcher
from core.sandbox.mutator import PackageMutator
from core.sandbox.signer import ProfessionalSigner
from core.sandbox.key_manager import KeyManager

class UltraCloner:
    def __init__(self):
        self.shield = SystemShield()
        if not self.shield.verify_environment(): sys.exit(1)
        
        self.key_man = KeyManager()
        self.key_man.generate_keystore()
        
        self.patcher = BinaryPatcher()
        self.signer = ProfessionalSigner()

    def run_primary_clone(self, apk_name):
        print(f"--- [ULTRA-CLONER: PRIMARY SIGNING] ---")
        
        self.patcher.deconstruct(apk_name)
        
        mutator = PackageMutator("data/work")
        if mutator.mutate_identity():
            unsigned = self.patcher.rebuild_and_sign(apk_name)
            final_apk = self.signer.sign_binary(unsigned)
            print(f"--- [PRIMARY WORK COMPLETE: {final_apk}] ---")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cloner.py <target_apk>")
    else:
        engine = UltraCloner()
        engine.run_primary_clone(sys.argv)
