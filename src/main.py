import threading
from hotkey import start_hotkey_listener
from tray import run_tray

if __name__ == "__main__":
    hotkey_thread = threading.Thread(target=start_hotkey_listener, daemon=True)
    hotkey_thread.start()

    run_tray()
