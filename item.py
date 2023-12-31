import cv2
import numpy as np
import pytesseract
from PIL import Image
import global_var

class Item:
    def __init__(self):


        # OCR preprocessing steps
        self.preprocessed_name = self.preprocess_image_txt(global_var.name_img_name)
        self.preprocessed_quantity = self.preprocess_image_nbr(global_var.quantity_img_name)
        self.preprocessed_prices_1 = self.preprocess_image_nbr(global_var.prices_1_img_name)
        self.preprocessed_prices_10 = self.preprocess_image_nbr(global_var.prices_10_img_name)
        self.preprocessed_prices_100 = self.preprocess_image_nbr(global_var.prices_100_img_name)

        # Custom config for numeric OCR
        custom_config_nbr = r'--psm 10 outputbase digits'

        # OCR to extract data
        self.name = pytesseract.image_to_string(self.preprocessed_name)
        self.quantity = int(pytesseract.image_to_string(self.preprocessed_quantity, config=custom_config_nbr))
        self.prices_1 = int(pytesseract.image_to_string(self.preprocessed_prices_1, config=custom_config_nbr))
        self.prices_10 = int(pytesseract.image_to_string(self.preprocessed_prices_10, config=custom_config_nbr))
        self.prices_100 = int(pytesseract.image_to_string(self.preprocessed_prices_100, config=custom_config_nbr))

    def preprocess_image_nbr(self, img_path):
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        kernel = np.ones((1, 1), np.uint8)
        eroded = cv2.erode(thresh, kernel, iterations=1)
        resized = cv2.resize(eroded, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
        return resized

    def preprocess_image_txt(self, img_path):
        img = cv2.imread(img_path)
        return img