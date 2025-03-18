import pyperclip

def copy_to_clipboard(text):
    """Copy text to clipboard."""
    pyperclip.copy(text)
    print(f"✅ Text copied to clipboard: {text[:50]}...") 

if __name__ == "__main__":
    test_text = "Hello, this is a test!"
    copy_to_clipboard(test_text)
