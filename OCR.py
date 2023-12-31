import cv2
import numpy as np


def preprocess_image(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((1, 1), np.uint8)
    eroded = cv2.erode(thresh, kernel, iterations=1)
    resized = cv2.resize(eroded, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    return resized