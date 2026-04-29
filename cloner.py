from core.identity.identity_gen import DeviceGenerator
from core.identity.persistence import PersistenceEngine
from core.sandbox.patcher import BinaryPatcher
from core.sandbox.signer import ProfessionalSigner
from core.sandbox.layout_randomizer import LayoutRandomizer
from core.sandbox.manifest_doctor import ManifestDoctor
import sys

class UltraCloner:
    def __init__(self):
        self.id_gen = DeviceGenerator()
        self.vault = PersistenceEngine()
        self.patcher = BinaryPatcher()
        self.signer = ProfessionalSigner()

    def execute_rigorous_op(self, app_name):
        print(f"--- [ULTRA-CLONER: CHAMELEON MODE] ---")
        
        # 1. Identity & Deconstruct
        dna = self.id_gen.generate_dna()
        self.patcher.deconstruct(f"{app_name}.apk")
        
        # 2. Smart Layout Randomization (The Smart Move)
        randomizer = LayoutRandomizer("data/work")
        randomizer.shuffle_resources()
        
        # 3. Manifest Hardening
        doctor = ManifestDoctor("data/work/AndroidManifest.xml")
        doctor.optimize_for_stealth()
        
        # 4. Finalize
        unsigned = self.patcher.rebuild_and_sign(app_name)
        final_apk = self.signer.sign_binary(unsigned)
        
        print(f"--- [SUCCESS: {app_name} IS UNIQUE AND COMFORTABLE] ---")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cloner.py <app_name>")
    else:
        engine = UltraCloner()
        engine.execute_rigorous_op(sys.argv[1])
