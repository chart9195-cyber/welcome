from core.sandbox.mutator import PackageMutator
from core.sandbox.smali_aligner import SmaliAligner
from core.sandbox.key_manager import KeyManager
import os

def run_test():
    print("🚀 --- STARTING PRIMARY ENGINE TEST ---")
    work_dir = "data/work"
    
    # 1. Test Mutation
    mutator = PackageMutator(work_dir)
    new_pkg = mutator.mutate_identity("test_clone")
    
    if "test_clone" in new_pkg:
        print("✅ Package Mutation: SUCCESS")
        
        # 2. Test Smali Alignment
        aligner = SmaliAligner(work_dir)
        aligner.align_references("com.original.app", new_pkg)
        
        with open("data/work/smali/com/original/app/MainActivity.smali", 'r') as f:
            content = f.read()
            if "test_clone" in content:
                print("✅ Smali Alignment: SUCCESS")
            else:
                print("❌ Smali Alignment: FAILED")
                
    # 3. Test Key Generation
    km = KeyManager()
    if km.generate_keystore():
        print("✅ Key Generation: SUCCESS")

    print("🏁 --- TEST COMPLETE ---")

if __name__ == "__main__":
    run_test()
