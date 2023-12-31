import cv2
import numpy as np
from pytesseract import pytesseract

# Set the path to the tesseract executable
pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def preprocess_image(img_path):
    # Read the image
    img = cv2.imread(img_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply a binary threshold
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Erode to separate characters
    kernel = np.ones((1, 1), np.uint8)
    eroded = cv2.erode(thresh, kernel, iterations=1)

    # Resize the image to make the text more prominent
    resized = cv2.resize(eroded, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    return resized

# Path to your image
img_path = "prices.png"

# Preprocess the image
processed_img = preprocess_image(img_path)

# Perform OCR on the pre-processed image using psm 10 for a single character
custom_config = r'--psm 10'
word = pytesseract.image_to_string(processed_img, config=custom_config)

# Print the OCR result
print(word.strip())
