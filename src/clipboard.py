import pyperclip
import sys

def copy_to_clipboard(text):
    pyperclip.copy(text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text_to_copy = " ".join(sys.argv[1:])
        copy_to_clipboard(text_to_copy)
    else:
        print("⚠️ No text received for copying.")
