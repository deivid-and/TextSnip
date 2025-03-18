import platform
import sys
import subprocess


def capture_screenshot():
    if platform.system() == "Darwin": 
        subprocess.run(["screencapture", "-i", "src/cropped.png"])  
    elif platform.system() == "Windows":
        subprocess.run(["SnippingTool.exe"])  
    else:
        print("❌ Unsupported OS")

    subprocess.run([sys.executable, "src/ocr.py"])

if __name__ == "__main__":
    capture_screenshot()
