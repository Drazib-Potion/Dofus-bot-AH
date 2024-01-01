import global_var as gvar
from pytesseract import pytesseract
from PIL import ImageGrab
import cv2
import numpy as np

class OCRClass:
    def __init__(self):
            self.custom_config_nbr = r'--psm 10 outputbase digits'
            self.quantity = None
            self.price_1 = None
            self.price_10 = None
            self.price_100 = None

            self.preporcessed_quantity_img = None
            self.preporcessed_price_1_img = None
            self.preporcessed_price_10_img = None
            self.preporcessed_price_100_img = None

    def screenshoting(self):
        self.screenshot(gvar.name_pos, gvar.name_img_name)
        self.screenshot(gvar.quantity_pos, gvar.quantity_img_name)
        self.screenshot(gvar.price_1_pos, gvar.price_1_img_name)
        self.screenshot(gvar.price_10_pos, gvar.price_10_img_name)
        self.screenshot(gvar.price_100_pos, gvar.price_100_img_name)

    def preprocessing(self):
        self.preprocessed_name_img = self.preprocess_txt_img(gvar.name_img_name)
        self.preprocessed_quantity_img = self.preprocess_nbr_img(gvar.quantity_img_name)
        self.preprocessed_price_1_img = self.preprocess_nbr_img(gvar.price_1_img_name)
        self.preprocessed_price_10_img = self.preprocess_nbr_img(gvar.price_10_img_name)
        self.preprocessed_price_100_img = self.preprocess_nbr_img(gvar.price_100_img_name)

    def screenshot(self, frame, file_name):
        screenshot = ImageGrab.grab(bbox=(frame['x'], frame['y'], frame['x'] + frame['width'], frame['y'] + frame['height']))
        screenshot.save(file_name)
    

    def preprocess_nbr_img(self, img_path):
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        kernel = np.ones((1, 1), np.uint8)
        eroded = cv2.erode(thresh, kernel, iterations=1)
        resized = cv2.resize(eroded, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
        return resized

    def preprocess_txt_img(self, img_path):
        img = cv2.imread(img_path)
        return img
    
    def process_nbr_img(self, img):
        return int(pytesseract.image_to_string(img, config=self.custom_config_nbr))

    def process_txt_img(self, img):
        return pytesseract.image_to_string(img)