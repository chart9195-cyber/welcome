from core.identity.identity_gen import DeviceGenerator
from core.sandbox.patcher import BinaryPatcher
from core.sandbox.signer import ProfessionalSigner
from core.sandbox.layout_randomizer import LayoutRandomizer
from core.sandbox.obfuscator import ResourceObfuscator
from core.sandbox.padding import BinaryPadder
import sys

class UltraCloner:
    def __init__(self):
        self.id_gen = DeviceGenerator()
        self.patcher = BinaryPatcher()
        self.signer = ProfessionalSigner()

    def execute_rigorous_op(self, app_name):
        print(f"--- [ULTRA-CLONER: PROFESSIONAL OBFUSCATION] ---")
        
        # 1. Deconstruct
        self.patcher.deconstruct(f"{app_name}.apk")
        
        # 2. Obfuscation & Randomization
        randomizer = LayoutRandomizer("data/work")
        randomizer.shuffle_resources()
        
        obfuscator = ResourceObfuscator("data/work")
        obfuscator.randomize_assets()
        
        # 3. Size Padding
        padder = BinaryPadder()
        padder.inject_junk("data/work")
        
        # 4. Finalize
        unsigned = self.patcher.rebuild_and_sign(app_name)
        final_apk = self.signer.sign_binary(unsigned)
        
        print(f"--- [SUCCESS: {final_apk} IS UNIQUE AT BINARY LEVEL] ---")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cloner.py <app_name>")
    else:
        engine = UltraCloner()
        engine.execute_rigorous_op(sys.argv)
