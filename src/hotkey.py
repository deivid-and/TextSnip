import keyboard
import subprocess

def trigger_screenshot():
    print("\n📸 Hotkey detected! Capturing screen...")
    subprocess.run(["python", "src/screenshot.py"]) 

def start_hotkey_listener():
    hotkey = "shift+tab"
    keyboard.add_hotkey(hotkey, trigger_screenshot)
    print(f"🎧 Listening for hotkey: {hotkey}... (Press ESC to exit)")

    keyboard.wait("esc")

if __name__ == "__main__":
    start_hotkey_listener()
