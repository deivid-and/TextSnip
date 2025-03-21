# TextSnip

Take a screenshot and get the text immediately in your clipboard, ready for Ctrl+V.

TextSnip runs in the background, listens for your set shortcut, lets you take a screenshot, extracts text using OCR, and pastes it into your clipboard. Fast, simple, and efficient.

Installation
Clone the project
git clone https://github.com/your-repo/TextSnip.git
cd TextSnip

Create a virtual environment
python -m venv venv

Activate the virtual environment

CMD: venv\Scripts\activate
PowerShell: venv\Scripts\Activate.ps1
Install dependencies
pip install -r requirements.txt

Run the app
python src/main.py

The app will now run in the system tray and listen for your hotkey shortcut.

Usage
By default, the hotkey is Alt+Shift
Press the shortcut, select a screenshot region
The app extracts text from the image and copies it to your clipboard
Just paste anywhere with Ctrl+V
Settings
Right-click the TextSnip icon in the system tray to access settings
Change the shortcut
Enable/disable startup launch
Important Notes
Windows Snipping Tool must be bound to Win + Shift + S
If you use a different shortcut, update it in src/screenshot.py
TextSnip is designed to be lightweight and automatic, making it seamless to extract text from screenshots with minimal effort.