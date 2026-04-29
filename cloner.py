import sys
import os
from core.system_shield import SystemShield
from core.sandbox.patcher import BinaryPatcher
from core.sandbox.mutator import PackageMutator
from core.sandbox.signer import ProfessionalSigner

class UltraCloner:
    def __init__(self):
        self.shield = SystemShield()
        if not self.shield.verify_environment(): sys.exit(1)
        
        self.patcher = BinaryPatcher()
        self.signer = ProfessionalSigner()

    def run_primary_clone(self, apk_name):
        print(f"--- [ULTRA-CLONER: PRIMARY MUTATION] ---")
        
        # 1. Deconstruct
        self.patcher.deconstruct(apk_name)
        
        # 2. Mutate (The Smart Move)
        mutator = PackageMutator("data/work")
        new_id = mutator.mutate_identity()
        
        if new_id:
            # 3. Rebuild & Sign
            unsigned = self.patcher.rebuild_and_sign(apk_name)
            final_apk = self.signer.sign_binary(unsigned)
            print(f"--- [SUCCESS: {final_apk} CREATED] ---")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cloner.py <target_apk>")
    else:
        engine = UltraCloner()
        engine.run_primary_clone(sys.argv[1])
