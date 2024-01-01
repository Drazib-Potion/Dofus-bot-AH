import global_var
import screenshots
import preprocess_img
from pytesseract import pytesseract

class OCRClass:
    def __init__(self):
            self.custom_config_nbr = r'--psm 10 outputbase digits'

            screenshots.name()
            screenshots.quantity()
            screenshots.price_1()
            screenshots.price_10()
            screenshots.price_100()
            self.preprocessed_name_img = preprocess_img.preprocess_image_txt(global_var.name_img_name)
            self.preprocessed_quantity_img = preprocess_img.preprocess_image_nbr(global_var.quantity_img_name)
            self.preprocessed_price_1_img = preprocess_img.preprocess_image_nbr(global_var.price_1_img_name)
            self.preprocessed_price_10_img = preprocess_img.preprocess_image_nbr(global_var.price_10_img_name)
            self.preprocessed_price_100_img = preprocess_img.preprocess_image_nbr(global_var.price_100_img_name)

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
