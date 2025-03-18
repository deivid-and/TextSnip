import keyboard

def trigger_screenshot():
    print("Hotkey pressed!") 

def start_hotkey_listener():
    hotkey = "shift+tab" 
    keyboard.add_hotkey(hotkey, trigger_screenshot)
    print(f"Listening for hotkey: {hotkey}... (Press ESC to exit)")
    # Keep the script running
    keyboard.wait("esc")

if __name__ == "__main__":
    start_hotkey_listener()
