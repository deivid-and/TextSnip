import pytesseract
import cv2
import subprocess

def extract_text(image_path="src/cropped.png"):
    """Extract text from an image file using Tesseract OCR."""
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    text = pytesseract.image_to_string(gray)
    return text.strip()

if __name__ == "__main__":
    extracted_text = extract_text()
    if extracted_text:
        print(f"📝 Extracted Text:\n{extracted_text}")
        subprocess.run(["python3", "src/clipboard.py", extracted_text])
    else:
        print("⚠️ No text detected.")
