"""
Ollama + zephyr:7b on Colab - BEST FOR JSON
"""

import subprocess
import time
import sys
import os

print("Installing Python deps...")
subprocess.run(
    [sys.executable, "-m", "pip", "install", "-q", "ollama", "pandas", "tqdm"],
    timeout=120
)
print("✓")

print("\nGetting LATEST Ollama...")
result = subprocess.run(
    "curl -s https://api.github.com/repos/ollama/ollama/releases/latest | grep 'linux-amd64.tgz' | head -1 | cut -d'\"' -f4",
    shell=True,
    capture_output=True,
    text=True,
    timeout=30
)
latest_url = result.stdout.strip()

if not latest_url:
    latest_url = "https://github.com/ollama/ollama/releases/download/v0.5.0/ollama-linux-amd64.tgz"

print("Downloading...")
subprocess.run(
    f"wget -q '{latest_url}' -O /tmp/ollama.tgz",
    shell=True,
    timeout=180,
    check=True
)

print("Extracting...")
subprocess.run(
    "sudo tar -xzf /tmp/ollama.tgz -C /usr/local/",
    shell=True,
    check=True
)
print("✓ Ollama installed")

print("\nStarting service...")
os.system("nohup /usr/local/bin/ollama serve > /tmp/ollama.log 2>&1 &")
time.sleep(25)
print("✓")

print("\n" + "="*60)
print("Pulling zephyr:7b (5-10 minutes)")
print("="*60)

result = subprocess.run(
    "/usr/local/bin/ollama pull zephyr:7b",
    shell=True,
    timeout=1800
)

if result.returncode == 0:
    print("\n✓ zephyr:7b ready\n")
    print("="*60)
    print("READY! Run: %run distributed_processor.py")
    print("="*60)
else:
    print("\n✗ Pull failed")
    sys.exit(1)



