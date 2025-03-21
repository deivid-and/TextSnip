TextSnip
Take a screenshot and get the text immediately in your clipboard, ready for Ctrl+V.

TextSnip runs in the background, listens for your set shortcut, lets you take a screenshot, extracts text using OCR, and pastes it into your clipboard. Fast, simple, and efficient.

Installation
Clone the project

bash
Copy
Edit
git clone https://github.com/your-repo/TextSnip.git
cd TextSnip
Create and activate a virtual environment

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
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
Quick Start for End Users
Run the TextSnip.exe
The app will minimize to the system tray
Click the tray icon to open settings
Use the hotkey, take a screenshot, and paste text anywhere
Important Notes
Windows Snipping Tool must be bound to Win + Shift + S
If you use a different shortcut, update it in src/screenshot.py
This project is open-source and built for productivity. Feel free to contribute, improve, or customize it for your workflow.
