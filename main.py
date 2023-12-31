
import cv2
import numpy as np
from pytesseract import pytesseract
import os

import screenshots
import global_var
import OCR

# if os.path.exists(global_var.quantity_img_name): os.remove(global_var.quantity_img_name)
# if os.path.exists(global_var.prices_1_img_name):os.remove(global_var.prices_1_img_name)
# if os.path.exists(global_var.prices_10_img_name):os.remove(global_var.prices_10_img_name)
# if os.path.exists(global_var.prices_100_img_name):os.remove(global_var.prices_100_img_name)

screenshots.quantity()
screenshots.prices_1()
screenshots.prices_10()
screenshots.prices_100()

preprocessed_quantity = OCR.preprocess_image(global_var.quantity_img_name)
preprocessed_prices_1 = OCR.preprocess_image(global_var.prices_1_img_name)
preprocessed_prices_10 = OCR.preprocess_image(global_var.prices_10_img_name)
preprocessed_prices_100 = OCR.preprocess_image(global_var.prices_100_img_name)


custom_config = r'--psm 10 outputbase digits'

word = pytesseract.image_to_string(preprocessed_quantity, config=custom_config)
print(word.strip())

word = pytesseract.image_to_string(preprocessed_prices_1, config=custom_config)
print(word.strip())
word = pytesseract.image_to_string(preprocessed_prices_10, config=custom_config)
print(word.strip())
word = pytesseract.image_to_string(preprocessed_prices_100, config=custom_config)
print(word.strip())