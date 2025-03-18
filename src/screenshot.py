import time
import subprocess
import pyautogui
from PIL import ImageGrab
import sys
import os

SAVE_PATH = "src/cropped.png"

def capture_screenshot():
    print("Activating Windows Snip Mode... Select a region!")

    initial_clipboard = ImageGrab.grabclipboard()

    pyautogui.hotkey("win", "shift", "s")
    print("Waiting for a new screenshot...")

    # Wait up to 5 seconds for clipboard to change
    timeout = time.time() + 5
    image = None
    while time.time() < timeout:
        image = ImageGrab.grabclipboard()
        
        # Process only if clipboard content has changed
        if image and image != initial_clipboard:
            break  
        time.sleep(0.5)  

    if image:
        image.save(SAVE_PATH)
        print(f"Screenshot saved")

        # Run OCR
        subprocess.run([sys.executable, "src/ocr.py"]) 

        os.remove(SAVE_PATH)
        print("Removed processed screenshot")

    else:
        print("⚠️ No new screenshot found. Try again.")

if __name__ == "__main__":
    capture_screenshot()
