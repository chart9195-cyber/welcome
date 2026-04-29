from core.engine_linker import EngineLinker
from core.sandbox.abi_manager import ABIManager
from core.identity.identity_gen import DeviceGenerator
from core.sandbox.patcher import BinaryPatcher
from core.sandbox.signer import ProfessionalSigner
import sys

class UltraCloner:
    def __init__(self):
        self.linker = EngineLinker()
        self.abi = ABIManager()
        self.id_gen = DeviceGenerator()
        self.patcher = BinaryPatcher()
        self.signer = ProfessionalSigner()

    def run_stable_clone(self, target_apk):
        print("--- [ULTRA-CLONER: STABLE BUILD MODE] ---")
        
        # 1. Verification
        if not self.linker.verify_stability():
            return

        # 2. Preparation
        self.patcher.deconstruct(target_apk)
        self.abi.align_architecture("data/work")
        
        # 3. Customization
        dna = self.id_gen.generate_dna()
        
        # 4. Finalization
        unsigned = self.patcher.rebuild_and_sign(target_apk)
        final_apk = self.signer.sign_binary(unsigned)
        
        print(f"--- [STABLE CLONE COMPLETE: {final_apk}] ---")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cloner.py <target_apk>")
    else:
        engine = UltraCloner()
        engine.run_stable_clone(sys.argv[1])
