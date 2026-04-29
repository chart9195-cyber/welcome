import sys
import os
from core.sandbox.engine_fetcher import EngineFetcher
from core.sandbox.patcher import BinaryPatcher
from core.sandbox.signer import ProfessionalSigner

class UltraCloner:
    def __init__(self):
        # 1. Fetch Engine Core for CI stability
        self.fetcher = EngineFetcher()
        self.fetcher.pull_engine()
        
        self.patcher = BinaryPatcher()
        self.signer = ProfessionalSigner()

    def run_primary_op(self, apk_name):
        print("🚀 --- [ULTRA-CLONER: VIRTUAL ENGINE INITIALIZED] ---")
        
        # Execution Flow
        if self.patcher.virtualize_apk(apk_name):
            # The engine produces an unsigned file; we sign it
            unsigned_path = f"data/output/{apk_name}"
            final_apk = self.signer.sign_binary(unsigned_apk=unsigned_path)
            print(f"🏁 --- [PRIMARY COMPLETE: {final_apk}] ---")

if __name__ == "__main__":
    # Test with a dummy name for CI validation
    target = sys.argv[1] if len(sys.argv) > 1 else "sample.apk"
    engine = UltraCloner()
    engine.run_primary_op(target)
