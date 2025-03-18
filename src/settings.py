import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, 
    QCheckBox, QComboBox
)
from PyQt5.QtGui import QFont

CONFIG_FILE = "config.json"

# Extended hotkey options (non-conflicting global shortcuts)
HOTKEY_OPTIONS = [
    "Ctrl+Shift",
    "Ctrl+Alt",
    "Alt+Shift",
    "Cmd+Shift",
    "Cmd+Alt",
    "Ctrl+Shift+X",
    "Alt+Shift+S",
    "Cmd+Shift+T",
    "Ctrl+Alt+Space",
    "Ctrl+Shift+V",
    "Alt+Shift+C",
    "Cmd+Alt+Shift",
    "Win+Shift+S",   # Windows Snip Tool Shortcut
    "Ctrl+Alt+T"
]

class SettingsUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TextSnip Settings")
        self.setGeometry(100, 100, 280, 160)  # Compact window size
        self.setStyleSheet("background-color: #f0f0f0; padding: 10px;")

        layout = QVBoxLayout()

        # Hotkey Selection
        self.hotkey_label = QLabel("Select Hotkey:", self)
        self.hotkey_label.setFont(QFont("Arial", 10))
        self.hotkey_dropdown = QComboBox(self)
        self.hotkey_dropdown.addItems(HOTKEY_OPTIONS)
        layout.addWidget(self.hotkey_label)
        layout.addWidget(self.hotkey_dropdown)

        # Startup Checkbox
        self.startup_checkbox = QCheckBox("Run on Startup", self)
        layout.addWidget(self.startup_checkbox)

        # Buttons: Save & Close (Separated)
        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_settings)

        self.close_button = QPushButton("Close", self)
        self.close_button.clicked.connect(self.close)

        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.close_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.load_settings()

    def save_settings(self):
        """Save user settings to config.json and apply startup settings."""
        selected_hotkey = self.hotkey_dropdown.currentText()
        run_on_startup = self.startup_checkbox.isChecked()
        config = {"hotkey": selected_hotkey, "startup": run_on_startup}

        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f)

        if run_on_startup:
            self.enable_startup()
        else:
            self.disable_startup()

        print(f"✅ Settings saved! Hotkey: {selected_hotkey}, Run on Startup: {run_on_startup}")

    def load_settings(self):
        """Load user settings from config.json."""
        try:
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
                hotkey = config.get("hotkey", HOTKEY_OPTIONS[0])  # Default first option
                self.hotkey_dropdown.setCurrentText(hotkey)
                self.startup_checkbox.setChecked(config.get("startup", False))
        except (FileNotFoundError, json.JSONDecodeError):
            print("⚠️ No valid config file found. Using defaults.")

    def enable_startup(self):
        """Enable startup on Windows."""
        if sys.platform == "win32":
            startup_path = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup", "TextSnip.lnk")
            with open(startup_path, "w") as f:
                f.write(f'pythonw "{os.path.abspath(__file__)}"')
            print("✅ Startup enabled!")

    def disable_startup(self):
        """Disable startup on Windows."""
        if sys.platform == "win32":
            startup_path = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup", "TextSnip.lnk")
            if os.path.exists(startup_path):
                os.remove(startup_path)
            print("❌ Startup disabled!")

def main():
    app = QApplication(sys.argv)
    settings_window = SettingsUI()
    settings_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, 
    QCheckBox, QComboBox
)
from PyQt5.QtGui import QFont

CONFIG_FILE = "config.json"

# Extended hotkey options (non-conflicting global shortcuts)
HOTKEY_OPTIONS = [
    "Ctrl+Shift",
    "Ctrl+Alt",
    "Alt+Shift",
    "Cmd+Shift",
    "Cmd+Alt",
    "Ctrl+Shift+X",
    "Alt+Shift+S",
    "Cmd+Shift+T",
    "Ctrl+Alt+Space",
    "Ctrl+Shift+V",
    "Alt+Shift+C",
    "Cmd+Alt+Shift",
    "Win+Shift+S",  
    "Ctrl+Alt+T"
]

class SettingsUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TextSnip Settings")
        self.setGeometry(100, 100, 280, 160)
        self.setStyleSheet("background-color: #f0f0f0; padding: 10px;")

        layout = QVBoxLayout()

        # Hotkey Selection
        self.hotkey_label = QLabel("Select Hotkey:", self)
        self.hotkey_label.setFont(QFont("Arial", 10))
        self.hotkey_dropdown = QComboBox(self)
        self.hotkey_dropdown.addItems(HOTKEY_OPTIONS)
        layout.addWidget(self.hotkey_label)
        layout.addWidget(self.hotkey_dropdown)

        # Startup Checkbox
        self.startup_checkbox = QCheckBox("Run on Startup", self)
        layout.addWidget(self.startup_checkbox)

        # Buttons: Save & Close
        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_settings)

        self.close_button = QPushButton("Close", self)
        self.close_button.clicked.connect(self.close)

        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.close_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.load_settings()

    def save_settings(self):
        selected_hotkey = self.hotkey_dropdown.currentText()
        run_on_startup = self.startup_checkbox.isChecked()
        config = {"hotkey": selected_hotkey, "startup": run_on_startup}

        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f)

        if run_on_startup:
            self.enable_startup()
        else:
            self.disable_startup()

        print(f"✅ Settings saved! Hotkey: {selected_hotkey}, Run on Startup: {run_on_startup}")
        self.close()

    def load_settings(self):
        try:
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
                hotkey = config.get("hotkey", HOTKEY_OPTIONS[0]) 
                self.hotkey_dropdown.setCurrentText(hotkey)
                self.startup_checkbox.setChecked(config.get("startup", False))
        except (FileNotFoundError, json.JSONDecodeError):
            print("⚠️ No valid config file found. Using defaults.")

    def enable_startup(self):
        if sys.platform == "win32":
            startup_path = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup", "TextSnip.lnk")
            with open(startup_path, "w") as f:
                f.write(f'pythonw "{os.path.abspath(__file__)}"')
            print("✅ Startup enabled!")

    def disable_startup(self):
        if sys.platform == "win32":
            startup_path = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup", "TextSnip.lnk")
            if os.path.exists(startup_path):
                os.remove(startup_path)
            print("❌ Startup disabled!")

def main():
    app = QApplication(sys.argv)
    settings_window = SettingsUI()
    settings_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
