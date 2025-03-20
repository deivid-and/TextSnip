from paddleocr import PaddleOCR
import cv2
import sys
import subprocess

OCR_ENGINE = PaddleOCR(
    use_angle_cls=True, 
    lang="en",  
    rec_algorithm="SVTR_LCNet",  
    det_db_box_thresh=0.5,  
    show_log=False
)

def extract_text(image_path="src/cropped.png"):
    """Directly extracts text from the image using PaddleOCR."""
    results = OCR_ENGINE.ocr(image_path, cls=True)

    if not results or not results[0]:
        return ""

    return "\n".join(line[1][0] for line in results[0]).strip()

if __name__ == "__main__":
    extracted_text = extract_text()

    if extracted_text:
        print(f"Extracted Text:\n{extracted_text}")
        subprocess.run([sys.executable, "src/clipboard.py", extracted_text])
    else:
        print("⚠️ No text detected.")
