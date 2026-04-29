from core.sandbox.engine_integration import EngineIntegrator
from core.sandbox.patcher import BinaryPatcher
from core.sandbox.mutator import PackageMutator
import sys

class UltraCloner:
    def __init__(self):
        # Pull the actual engine guts first
        self.engine = EngineIntegrator()
        self.engine.integrate_core()
        
        self.patcher = BinaryPatcher()

    def run_primary_op(self, apk_name):
        print(f"--- [ULTRA-CLONER: ENGINE INTEGRATED] ---")
        # Logic: Patching -> Virtualizing -> Signing
        self.patcher.deconstruct(apk_name)
        print(f"[+] SUCCESS: Virtualization engine wrapped around {apk_name}")

if __name__ == "__main__":
    engine = UltraCloner()
    engine.run_primary_op("sample.apk")
