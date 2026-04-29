#!/bin/bash
echo "[*] HARMONIZER: Aligning package versions for comfortability..."
pkg update && pkg upgrade -y
pkg install -y openjdk-17 python git binutils
pip install -r requirements.txt
echo "[+] HARMONIZER: System is now synchronized."
