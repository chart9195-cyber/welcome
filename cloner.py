from core.identity.identity_gen import DeviceGenerator
from core.identity.validator import StealthValidator
from core.identity.persistence import PersistenceEngine
from core.network.rotator import NetworkManager
from core.sandbox.patcher import BinaryPatcher
from core.sandbox.signer import ProfessionalSigner
from core.sandbox.forensics import ForensicScrubber
import sys

class UltraCloner:
    def __init__(self):
        self.id_gen = DeviceGenerator()
        self.vault = PersistenceEngine()
        self.net_man = NetworkManager()
        self.patcher = BinaryPatcher()
        self.signer = ProfessionalSigner()

    def execute_rigorous_op(self, app_name):
        print(f"--- [ULTRA-CLONER: PERSISTENT EXECUTION] ---")
        
        # 1. Persistence Check (Look in the Vault first)
        dna = self.vault.load_identity(app_name)
        if not dna:
            print("[*] No existing DNA found. Generating new profile...")
            dna = self.id_gen.generate_dna()
            self.vault.save_identity(app_name, dna)
        
        # 2. Network & Validation
        self.net_man.get_rotation()
        validator = StealthValidator(dna)
        validator.audit_fingerprint()
        
        # 3. Patching & Scrubbing
        self.patcher.deconstruct(f"{app_name}.apk")
        scrubber = ForensicScrubber(dna)
        scrubber.scrub_directory("data/work/assets")
        
        # 4. Finalization
        unsigned = self.patcher.rebuild_and_sign(app_name)
        final_apk = self.signer.sign_binary(unsigned)
        
        print(f"--- [SUCCESS: {app_name} IS LOCKED AND DEPLOYED] ---")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cloner.py <app_name>")
    else:
        engine = UltraCloner()
        engine.execute_rigorous_op(sys.argv[1])
