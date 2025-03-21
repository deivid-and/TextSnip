import os
import sys
import subprocess
from pystray import Icon, Menu, MenuItem
from PIL import Image

APP_NAME = "TextSnip"
ICON_PATH = os.path.join(os.getcwd(), "assets", "icon.png")

if not os.path.exists(ICON_PATH):
    ICON_PATH = None 

def open_settings(icon, item=None):
    subprocess.Popen([sys.executable, "src/settings.py"])

def exit_app(icon, item=None):
    icon.stop()
    os._exit(0)

menu = Menu(
    MenuItem("Settings", open_settings),
    MenuItem("Exit", exit_app)
)

def run_tray():
    tray_icon = Icon(APP_NAME, Image.open(ICON_PATH) if ICON_PATH else None, menu=menu)
    tray_icon.run(setup=lambda icon: setattr(icon, "visible", True))  
