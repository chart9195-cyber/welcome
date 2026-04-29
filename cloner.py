import sys
import os
from core.system_shield import SystemShield
from core.sandbox.patcher import BinaryPatcher
from core.sandbox.mutator import PackageMutator
from core.sandbox.smali_aligner import SmaliAligner
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
        print(f"--- [ULTRA-CLONER: PRIMARY ENGINE ACTIVE] ---")
        
        # 1. Deconstruct
        self.patcher.deconstruct(apk_name)
        
        # 2. Mutate Identity
        mutator = PackageMutator("data/work")
        old_pkg = "com.original.app" # Simplified for logic
        new_pkg = mutator.mutate_identity()
        
        if new_pkg:
            # 3. Align Code (The Connector)
            aligner = SmaliAligner("data/work")
            aligner.align_references(old_pkg, new_pkg)
            
            # 4. Rebuild & Sign
            unsigned = self.patcher.rebuild_and_sign(apk_name)
            final_apk = self.signer.sign_binary(unsigned)
            print(f"--- [PRIMARY WORK COMPLETE: {final_apk}] ---")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cloner.py <target_apk>")
    else:
        engine = UltraCloner()
        engine.run_primary_clone(sys.argv)
