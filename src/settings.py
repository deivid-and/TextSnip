import sys
import json
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QCheckBox, QComboBox

CONFIG_FILE = "config.json"

HOTKEY_OPTIONS = [
    "Ctrl+Shift",
    "Ctrl+Alt",
    "Alt+Shift",
    "Cmd+Shift",
    "Cmd+Alt" 
]

class SettingsUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TextSnip Settings")
        self.setGeometry(100, 100, 400, 250)

        layout = QVBoxLayout()

        # Hotkey Selection Dropdown
        self.hotkey_label = QLabel("Select Hotkey:", self)
        self.hotkey_dropdown = QComboBox(self)
        self.hotkey_dropdown.addItems(HOTKEY_OPTIONS)
        layout.addWidget(self.hotkey_label)
        layout.addWidget(self.hotkey_dropdown)

        # Startup Checkbox
        self.startup_checkbox = QCheckBox("Run on Startup", self)
        layout.addWidget(self.startup_checkbox)

        # Save & Close Button
        self.save_button = QPushButton("Save & Close", self)
        self.save_button.clicked.connect(self.save_settings)
        layout.addWidget(self.save_button)

        self.setLayout(layout)
        self.load_settings()

    def save_settings(self):
        """Save user settings to a config file and apply startup setting."""
        selected_hotkey = self.hotkey_dropdown.currentText()
        run_on_startup = self.startup_checkbox.isChecked()
        config = {"hotkey": selected_hotkey, "startup": run_on_startup}

        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f)

        if run_on_startup:
            self.enable_startup()
        else:
            self.disable_startup()

        print(f"Settings saved! Hotkey: {selected_hotkey}, Run on Startup: {run_on_startup}")
        self.close()  

    def load_settings(self):
        """Load user settings from config file."""
        try:
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
                hotkey = config.get("hotkey", HOTKEY_OPTIONS[0]) 
                self.hotkey_dropdown.setCurrentText(hotkey)
                self.startup_checkbox.setChecked(config.get("startup", False))
        except (FileNotFoundError, json.JSONDecodeError):
            print("⚠️ No valid config file found. Using defaults.")

    def enable_startup(self):
        startup_command = f"python {os.path.abspath(__file__)}"
        if sys.platform == "win32":
            startup_path = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup", "TextSnip.lnk")
            with open(startup_path, "w") as f:
                f.write(startup_command)
        elif sys.platform == "darwin":  # macOS
            os.system(f"osascript -e 'tell application \"System Events\" to make login item at end with properties {{path:\"{startup_command}\", hidden:false}}'")
        print("Startup enabled!")

    def disable_startup(self):
        if sys.platform == "win32":
            startup_path = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup", "TextSnip.lnk")
            if os.path.exists(startup_path):
                os.remove(startup_path)
        elif sys.platform == "darwin":
            os.system(f"osascript -e 'tell application \"System Events\" to delete login item \"TextSnip\"'")
        print("Startup disabled!")

def main():
    app = QApplication(sys.argv)
    settings_window = SettingsUI()
    settings_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
