import pytesseract
import cv2

def extract_text(image_path="cropped.png"):
    """Extract text from an image file using Tesseract OCR."""
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    text = pytesseract.image_to_string(gray)
    return text.strip()

if __name__ == "__main__":
    extracted_text = extract_text()
    print(f"📝 Extracted Text:\n{extracted_text}")
