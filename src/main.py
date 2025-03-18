import subprocess
import sys

def trigger_screenshot():
    subprocess.run(["python3", "src/screenshot.py"])

if __name__ == "__main__":
    trigger_screenshot()
