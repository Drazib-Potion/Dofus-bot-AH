import global_var
import preprocess_img
from pytesseract import pytesseract
from PIL import ImageGrab

class OCRClass:
    def __init__(self):
            self.custom_config_nbr = r'--psm 10 outputbase digits'

            self.screenshot_frame(global_var.name_pos, global_var.name_img_name)
            self.screenshot_frame(global_var.quantity_pos, global_var.quantity_img_name)
            self.screenshot_frame(global_var.price_1_pos, global_var.price_1_img_name)
            self.screenshot_frame(global_var.price_10_pos, global_var.price_10_img_name)
            self.screenshot_frame(global_var.price_100_pos, global_var.price_100_img_name)
            self.preprocessed_name_img = preprocess_img.preprocess_image_txt(global_var.name_img_name)
            self.preprocessed_quantity_img = preprocess_img.preprocess_image_nbr(global_var.quantity_img_name)
            self.preprocessed_price_1_img = preprocess_img.preprocess_image_nbr(global_var.price_1_img_name)
            self.preprocessed_price_10_img = preprocess_img.preprocess_image_nbr(global_var.price_10_img_name)
            self.preprocessed_price_100_img = preprocess_img.preprocess_image_nbr(global_var.price_100_img_name)

    def screenshot_frame(self, frame, file_name):
        screenshot = ImageGrab.grab(bbox=(frame['x'], frame['y'], frame['x'] + frame['width'], frame['y'] + frame['height']))
        screenshot.save(file_name)
    
    def process_name(self):
        self.name = pytesseract.image_to_string(self.preprocessed_name_img)

    def process_quantity(self):
        self.quantity = int(pytesseract.image_to_string(self.preprocessed_quantity_img, config=self.custom_config_nbr))

    def process_price(self, price, img):
        price = int(pytesseract.image_to_string(img, config=self.custom_config_nbr))

    def process_price_1(self):
        self.price_1 = int(pytesseract.image_to_string(self.preprocessed_price_1_img, config=self.custom_config_nbr))

    def process_price_10(self):
        self.price_10 = int(pytesseract.image_to_string(self.preprocessed_price_10_img, config=self.custom_config_nbr))

    def process_price_100(self):
        self.price_100 = int(pytesseract.image_to_string(self.preprocessed_price_100_img, config=self.custom_config_nbr))
