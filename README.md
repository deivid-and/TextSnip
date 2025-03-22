# **TextSnip**

Take a screenshot and get the text **instantly** copied to your clipboard.  

TextSnip runs in the background, listens for your set **hotkey**, lets you take a screenshot, extracts text using **OCR**, and **copies** it to your clipboard—ready for **Ctrl+V**. **Fast, simple, and efficient.**  

Currently only Windows version is available. MacOS in progress...

---

## **Installation & Setup**

### **1. Clone the Project**
```bash
https://github.com/deivid-and/TextSnip.git
cd TextSnip
```
### **2. Create and Activate a Virtual Environment**
```bash
python -m venv venv
venv\Scripts\activate
```
### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```
### **4. Run the App**
```bash
python src/main.py
```

## **Usage**

### **1. Take a Screenshot & Extract Text**
Press the hotkey (default: Alt+Shift).
Select a screenshot region.
TextSnip extracts the text and copies it to your clipboard.
Paste it anywhere using Ctrl+V.

### **2. Accessing the Settings**
Right-click the TextSnip icon in the system tray.
Click Settings to change the hotkey.

## **Important Notes**
Windows Snipping Tool must be set to Win + Shift + S for screenshots.
If you use a different screenshot shortcut, update it in src/screenshot.py.

## **Open Source & Contributions
This project is open-source and built to improve productivity. Feel free to contribute, suggest improvements, or customize it to fit your needs.
