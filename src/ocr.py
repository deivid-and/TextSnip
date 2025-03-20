import pytesseract
import cv2
import subprocess
import sys
import os

LOCAL_TESSERACT = os.path.join(os.getcwd(), "Tesseract-OCR", "tesseract.exe")

if os.path.exists(LOCAL_TESSERACT):
    pytesseract.pytesseract.tesseract_cmd = LOCAL_TESSERACT
else:
    print("ERROR: Tesseract not found in the project folder!")
    sys.exit(1)

def extract_text(image_path="src/cropped.png"):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    text = pytesseract.image_to_string(gray, config="--psm 6 --oem 3")
    return text.strip()

if __name__ == "__main__":
    extracted_text = extract_text()

    if extracted_text:
        print(f"Extracted Text:\n{extracted_text}")
        subprocess.run([sys.executable, "src/clipboard.py", extracted_text])
    else:
        print("ERROR: No text detected.")
