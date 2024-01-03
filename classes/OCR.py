import global_var as gvar
from pytesseract import pytesseract
from PIL import ImageGrab
import cv2
import numpy as np

class OCRClass:
    def __init__(self):
            self.custom_config_nbr = r'--psm 10 outputbase digits'

            self.item = {
                'name': '',
                'quantity': '',
                'quantity_in_feed': '',
                'price_1': '',
                'price_10': '',
                'price_100': ''
            }

            self.last_item = {
                'name': '',
                'quantity_in_feed': '',
                'quantity': '',
                'price_1': '',
                'price_10': '',
                'price_100': ''
            }

            self.preprocessed_quantity_img = None
            self.preprocessed_quantity_in_feed_img = None
            self.preprocessed_price_1_img = None
            self.preprocessed_price_10_img = None
            self.preprocessed_price_100_img = None

    def screenshoting(self):
        self.screenshot(gvar.icon_item_rect, gvar.icon_item_img_name)
        self.screenshot(gvar.name_rect, gvar.name_img_name)
        self.screenshot(gvar.quantity_rect, gvar.quantity_img_name)
        self.screenshot(gvar.quantity_repricing_rect, gvar.quantity_in_feed_img_name)
        self.screenshot(gvar.price_1_rect, gvar.price_1_img_name)
        self.screenshot(gvar.price_10_rect, gvar.price_10_img_name)
        self.screenshot(gvar.price_100_rect, gvar.price_100_img_name)

    def preprocessing(self):
        self.preprocessed_name_img = self.preprocess_txt_img(gvar.name_img_name)
        self.preprocessed_quantity_img = self.preprocess_nbr_img(gvar.quantity_img_name)
        self.preprocessed_quantity_in_feed_img = self.preprocess_nbr_img(gvar.quantity_in_feed_img_name)
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
        try:
            result_str = pytesseract.image_to_string(img, config=self.custom_config_nbr).strip().replace("\n", "").replace(".", "")
            result_int = int(result_str)
            return result_int
        except ValueError:
            print("process_nbr failed")
            exit(84)

    def process_txt_img(self, img):
        return pytesseract.image_to_string(img)
    
    def process_nbr_feed_img(self, image):
        # Configure Pytesseract to only recognize specific characters
        custom_config = r'--psm 10 outputbase digits tessedit_char_whitelist=10'
        
        try:
            result_str = pytesseract.image_to_string(self.preprocessed_quantity_in_feed_img, config=custom_config)
            result_int = int(result_str)
            return result_int
        except ValueError:
            print("process_nbr_feed failed")
            exit(84)
        