import subprocess
import json
import keyboard
import sys

CONFIG_FILE = "config.json"

def load_hotkey():
    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            return config.get("hotkey", "shift+tab") 
    except FileNotFoundError:
        return "shift+tab" 

def trigger_screenshot():
    print("\n Hotkey detected! Capturing screen...")
    subprocess.run([sys.executable, "src/screenshot.py"])

def start_hotkey_listener():
    hotkey = load_hotkey()
    keyboard.add_hotkey(hotkey, trigger_screenshot)
    print(f"Listening for hotkey: {hotkey}... (Press ESC to exit)")

    keyboard.wait("esc")  

if __name__ == "__main__":
    start_hotkey_listener()
