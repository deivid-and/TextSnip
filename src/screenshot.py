import numpy as np
import cv2
import pyautogui

# Take a full-screen screenshot
image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("screenshot.png", image)

drawing = False  
x1, y1, x2, y2 = -1, -1, -1, -1  

def draw_rectangle(event, x, y, flags, param):
    """Handles mouse events for drawing a selection rectangle."""
    global x1, y1, x2, y2, drawing, image

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x1, y1 = x, y

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        img_copy = image.copy()
        cv2.rectangle(img_copy, (x1, y1), (x, y), (0, 255, 0), 2)
        cv2.imshow("Select Region", img_copy)
        cv2.waitKey(1)  

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        x2, y2 = x, y

        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)

        crop_and_save()

def crop_and_save():
    """Crops the selected region and saves it."""
    global x1, y1, x2, y2, image

    if x1 < x2 and y1 < y2:
        cropped_img = image[y1:y2, x1:x2].copy()  
        cv2.imwrite("cropped.png", cropped_img)
        cv2.imshow("Cropped Image", cropped_img)
        print("Cropped image saved as cropped.png")

cv2.imshow("Select Region", image)
cv2.setMouseCallback("Select Region", draw_rectangle)

cv2.waitKey(0)
cv2.destroyAllWindows()
