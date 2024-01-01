import global_var
import preprocess_img
from pytesseract import pytesseract
from PIL import ImageGrab

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
        self.screenshot(global_var.name_pos, global_var.name_img_name)
        self.screenshot(global_var.quantity_pos, global_var.quantity_img_name)
        self.screenshot(global_var.price_1_pos, global_var.price_1_img_name)
        self.screenshot(global_var.price_10_pos, global_var.price_10_img_name)
        self.screenshot(global_var.price_100_pos, global_var.price_100_img_name)

    def preprocessing(self):
        self.preprocessed_name_img = preprocess_img.preprocess_image_txt(global_var.name_img_name)
        self.preprocessed_quantity_img = preprocess_img.preprocess_image_nbr(global_var.quantity_img_name)
        self.preprocessed_price_1_img = preprocess_img.preprocess_image_nbr(global_var.price_1_img_name)
        self.preprocessed_price_10_img = preprocess_img.preprocess_image_nbr(global_var.price_10_img_name)
        self.preprocessed_price_100_img = preprocess_img.preprocess_image_nbr(global_var.price_100_img_name)

    def screenshot(self, frame, file_name):
        screenshot = ImageGrab.grab(bbox=(frame['x'], frame['y'], frame['x'] + frame['width'], frame['y'] + frame['height']))
        screenshot.save(file_name)
    
    def process_txt_img(self, img):
        return pytesseract.image_to_string(img)

    def process_nbr_img(self, img):
        return int(pytesseract.image_to_string(img, config=self.custom_config_nbr))
