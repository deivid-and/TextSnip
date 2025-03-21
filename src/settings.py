import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, 
    QCheckBox, QComboBox
)
from PyQt5.QtGui import QFont, QIcon

CONFIG_FILE = "config.json"
HOTKEY_OPTIONS = [
    "Ctrl+Shift", "Ctrl+Alt", "Alt+Shift", "Cmd+Shift", "Cmd+Alt",
    "Ctrl+Shift+X", "Alt+Shift+S", "Cmd+Shift+T", "Ctrl+Alt+Space",
    "Ctrl+Shift+V", "Alt+Shift+C", "Cmd+Alt+Shift", "Win+Shift+S",
    "Ctrl+Alt+T"
]

ICON_PATH = os.path.join(os.getcwd(), "assets", "icon.png")

class SettingsUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TextSnip Settings")
        self.setGeometry(100, 100, 280, 160)
        self.setStyleSheet("background-color: #f0f0f0; padding: 10px;")

        if os.path.exists(ICON_PATH):
            self.setWindowIcon(QIcon(ICON_PATH))

        layout = QVBoxLayout()
        self.hotkey_label = QLabel("Select Hotkey:")
        self.hotkey_label.setFont(QFont("Arial", 10))
        self.hotkey_dropdown = QComboBox()
        self.hotkey_dropdown.addItems(HOTKEY_OPTIONS)
        layout.addWidget(self.hotkey_label)
        layout.addWidget(self.hotkey_dropdown)

        self.startup_checkbox = QCheckBox("Run on Startup")
        layout.addWidget(self.startup_checkbox)

        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_settings)
        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.close_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.load_settings()

    def save_settings(self):
        config = {
            "hotkey": self.hotkey_dropdown.currentText(),
            "startup": self.startup_checkbox.isChecked()
        }
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f)

        self.enable_startup() if config["startup"] else self.disable_startup()
        self.close()

    def load_settings(self):
        try:
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
                self.hotkey_dropdown.setCurrentText(config.get("hotkey", HOTKEY_OPTIONS[0]))
                self.startup_checkbox.setChecked(config.get("startup", False))
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def enable_startup(self):
        if sys.platform == "win32":
            startup_path = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup", "TextSnip.lnk")
            with open(startup_path, "w") as f:
                f.write(f'pythonw "{os.path.abspath(__file__)}"')

    def disable_startup(self):
        if sys.platform == "win32":
            startup_path = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup", "TextSnip.lnk")
            if os.path.exists(startup_path):
                os.remove(startup_path)

def main():
    app = QApplication(sys.argv)
    settings_window = SettingsUI()
    settings_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
