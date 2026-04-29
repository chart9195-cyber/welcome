import platform
import sys

def check_env():
    arch = platform.machine()
    print(f"[*] Detecting System Architecture: {arch}")
    
    supported = ["aarch64", "x86_64", "armv8l"]
    if arch not in supported:
        print(f"[!] Warning: Architecture {arch} might face comfortability issues.")
        return False
        
    print("[+] Environment verified. Moving to execution.")
    return True

if __name__ == "__main__":
    check_env()
