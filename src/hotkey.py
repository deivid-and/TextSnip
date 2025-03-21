import json
import keyboard
import subprocess
import sys

CONFIG_FILE = "config.json"

def load_hotkey():
    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            return config.get("hotkey", "alt+shit")
    except FileNotFoundError:
        return "alt+shit"

def trigger_screenshot():
    print("\nHotkey detected! Capturing screen...")
    subprocess.run([sys.executable, "src/screenshot.py"])

def start_hotkey_listener():
    hotkey = load_hotkey()
    keyboard.add_hotkey(hotkey, trigger_screenshot)
    print(f"Listening for hotkey: {hotkey}... (Press ESC to exit)")

    keyboard.wait("esc") 
