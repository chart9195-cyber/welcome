import sys
import os
from core.system_shield import SystemShield
from core.sandbox.virtual_engine import UltraVirtualEngine
from core.sandbox.patcher import BinaryPatcher
from core.sandbox.signer import ProfessionalSigner

class UltraCloner:
    def __init__(self):
        self.shield = SystemShield()
        if not self.shield.verify_environment(): sys.exit(1)
        
        self.v_engine = UltraVirtualEngine()
        self.patcher = BinaryPatcher()
        self.signer = ProfessionalSigner()

    def run_primary_operation(self, apk_name):
        print("🚀 --- STARTING SUPREME VIRTUAL CLONE ---")
        
        # 1. Preparation
        self.patcher.deconstruct(apk_name)
        
        # 2. Integration (The Hardest Work)
        if self.v_engine.integrate_virtual_layer(apk_name):
            self.v_engine.optimize_performance()
            
            # 3. Finalization
            unsigned = "data/output/virtual_temp.apk"
            final_apk = self.signer.sign_binary(unsigned)
            print(f"🏁 --- PRIMARY WORK FINISHED: {final_apk} ---")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cloner.py <app_name>")
    else:
        engine = UltraCloner()
        engine.run_primary_operation(sys.argv)
