
from datetime import datetime
import logging
import random
import time
import cv2
import keyboard
import numpy as np
import pyautogui
from pytesseract import pytesseract
from item import Item
import screenshots

current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") 
log_filename = f'logs/log_solding_dofus_{current_time}.log' 

logging.basicConfig(filename=log_filename, filemode='w', level=logging.INFO, format='%(message)s')
logging.info("----- Starting new session -----")

while(True):
    if keyboard.is_pressed('f8'):
        print("Stopping script.")
        break


    pyautogui.moveTo(1278, 206)
    pyautogui.click()
    time.sleep(2)

    screenshots.name()
    screenshots.quantity()
    screenshots.prices_1()
    screenshots.prices_10()
    screenshots.prices_100()

    my_item = Item()

    clean_name = my_item.name.strip().replace('\n', ' ')
    logging.info(f"name : {clean_name}")
    print(f"name : {clean_name}")
    logging.info(f"quantity : {my_item.quantity}")
    print(f"quantity : {my_item.quantity}")


    if (my_item.quantity == 1):
        pyautogui.write(str(my_item.prices_1 - 1))
        logging.info(f"1 solding for {my_item.prices_1 - 1} Kamas")
        print(f"1 solding for {my_item.prices_1 - 1} Kamas")


    elif (my_item.quantity == 10):
        pyautogui.write(str(my_item.prices_10 - 1))
        logging.info(f"10 solding for {my_item.prices_10 - 1} Kamas")
        print(f"10 solding for {my_item.prices_10 - 1} Kamas")


    elif (my_item.quantity == 100):
        pyautogui.write(str(my_item.prices_100 - 1))
        logging.info(f"100 solding for {my_item.prices_100 - 1} Kamas")
        print(f"100 solding for {my_item.prices_100 - 1} Kamas")


    pyautogui.moveTo(498, 445)
    pyautogui.click()
    # time.sleep(random.uniform(0, 2))
    print("--------------------------")
    logging.info("-----")