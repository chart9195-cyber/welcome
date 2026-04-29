import sys
from core.downloader import DependencyDownloader
from core.sandbox.patcher import BinaryPatcher
from core.sandbox.mutator import PackageMutator
from core.sandbox.smali_aligner import SmaliAligner
from core.sandbox.signer import ProfessionalSigner
from core.sandbox.key_manager import KeyManager

class UltraCloner:
    def __init__(self):
        # Initialize Primary Hands
        self.downloader = DependencyDownloader()
        self.downloader.fetch_tools()
        
        self.key_man = KeyManager()
        self.key_man.generate_keystore()
        
        self.patcher = BinaryPatcher()
        self.signer = ProfessionalSigner()

    def run_primary_operation(self, apk_path):
        print("🚀 --- STARTING PRIMARY CLONE SEQUENCE ---")
        
        # 1. Deconstruct
        self.patcher.deconstruct(apk_path)
        
        # 2. Mutate Identity
        mutator = PackageMutator("data/work")
        new_pkg = mutator.mutate_identity()
        
        if new_pkg:
            # 3. Align Code
            aligner = SmaliAligner("data/work")
            aligner.align_references("com.original.app", new_pkg)
            
            # 4. Rebuild
            unsigned_apk = self.patcher.rebuild_and_sign("target_app")
            
            # 5. Sign (Final Product)
            final_apk = self.signer.sign_binary(unsigned_apk)
            print(f"🏁 --- PRIMARY COMPLETE: {final_apk} ---")

if __name__ == "__main__":
    engine = UltraCloner()
    engine.run_primary_operation("target.apk")
