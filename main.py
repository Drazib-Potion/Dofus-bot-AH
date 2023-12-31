
from datetime import datetime
import logging
import os
import random
import time
import cv2
import keyboard
import numpy as np
import pyautogui
from pytesseract import pytesseract
import preprocess_img
import screenshots
import global_var


if not os.path.exists("logs"): os.makedirs("logs")
if not os.path.exists("img"): os.makedirs("img")

current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") 
log_filename = f'logs/log_solding_dofus_{current_time}.log' 

logging.basicConfig(filename=log_filename, filemode='w', level=logging.INFO, format='%(message)s')
logging.info("----- Starting new session -----")

while(True):
    if keyboard.is_pressed('f8'):
        print("Stopping script.")
        os.remove(global_var.name_img_name)
        os.remove(global_var.quantity_img_name)
        os.remove(global_var.prices_1_img_name)
        os.remove(global_var.prices_10_img_name)
        os.remove(global_var.prices_100_img_name)

        break

    #first item in bag
    pyautogui.moveTo(1278, 206)
    pyautogui.click()
    time.sleep(1)
    time.sleep(random.uniform(0.5, 1.5))
    
    screenshots.name()
    screenshots.quantity()
    screenshots.prices_1()
    screenshots.prices_10()
    screenshots.prices_100()

    preprocessed_name = preprocess_img.preprocess_image_txt(global_var.name_img_name)
    preprocessed_quantity = preprocess_img.preprocess_image_nbr(global_var.quantity_img_name)
    preprocessed_prices_1 = preprocess_img.preprocess_image_nbr(global_var.prices_1_img_name)
    preprocessed_prices_10 = preprocess_img.preprocess_image_nbr(global_var.prices_10_img_name)
    preprocessed_prices_100 = preprocess_img.preprocess_image_nbr(global_var.prices_100_img_name)

    custom_config_nbr = r'--psm 10 outputbase digits'

    name = pytesseract.image_to_string(preprocessed_name)
    quantity = int(pytesseract.image_to_string(preprocessed_quantity, config=custom_config_nbr))

    clean_name = name.strip().replace('\n', ' ')
    logging.info(f"name : {clean_name}")
    print(f"name : {clean_name}")
    logging.info(f"quantity : {quantity}")
    print(f"quantity : {quantity}")



    if (quantity == 1):
        prices_1 = int(pytesseract.image_to_string(preprocessed_prices_1, config=custom_config_nbr))
        if (prices_1 > 1):
            pyautogui.write(str(prices_1 - 1))
            logging.info(f"1 solding for {prices_1 - 1} Kamas")
            print(f"1 solding for {prices_1 - 1} Kamas")
        else:
            pyautogui.write(str(1))
            logging.info(f"1 solding for {1} Kamas")
            print(f"1 solding for {1} Kamas")
    elif (quantity == 10):
        prices_10 = int(pytesseract.image_to_string(preprocessed_prices_10, config=custom_config_nbr))
        pyautogui.write(str(prices_10 - 1))
        logging.info(f"10 solding for {prices_10 - 1} Kamas")
        print(f"10 solding for {prices_10 - 1} Kamas")
    elif (quantity == 100):
        prices_100 = int(pytesseract.image_to_string(preprocessed_prices_100, config=custom_config_nbr))
        pyautogui.write(str(prices_100 - 1))
        logging.info(f"100 solding for {prices_100 - 1} Kamas")
        print(f"100 solding for {prices_100 - 1} Kamas")


    # sell button
    pyautogui.moveTo(498, 445)
    pyautogui.click()

    # popup attention priux trop bas
    pyautogui.moveTo(863, 689)
    pyautogui.click()
    
    print("--------------------------")
    logging.info("-----")