import time
import subprocess
import pyautogui
from PIL import ImageGrab
import sys

SAVE_PATH = "src/cropped.png"

def capture_screenshot():
    print("Activating Windows Snip Mode... Select a region!")

    pyautogui.hotkey("win", "shift", "s")

    print("Waiting for screenshot to appear in clipboard...")

    # Wait up to 5 seconds for clipboard to contain a new image
    image = None
    timeout = time.time() + 5 
    while time.time() < timeout:
        image = ImageGrab.grabclipboard()
        if image:
            break  
        time.sleep(0.5) 

    if image:
        image.save(SAVE_PATH)
        print(f"Screenshot saved as {SAVE_PATH}")
        subprocess.run([sys.executable, "src/ocr.py"]) 
    else:
        print("⚠️ No image found in clipboard. Try again.")

if __name__ == "__main__":
    capture_screenshot()
