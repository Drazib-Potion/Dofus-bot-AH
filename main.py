
import os
import random
import time
import keyboard
import pyautogui

from OCR import OCRClass
from Logger import LoggerClass

if not os.path.exists("logs"): os.makedirs("logs")
if not os.path.exists("img"): os.makedirs("img")

Logger = LoggerClass()
Logger.init_logs()

while(True):
    if keyboard.is_pressed('f8'):
        print("Stopping script.")
        break

    #first item in bag
    pyautogui.moveTo(1278, 206)
    pyautogui.click()
    time.sleep(random.uniform(0.5, 1.5))
    
    Ocr  = OCRClass()
    Ocr.process_name()
    Ocr.process_quantity()

    clean_name = Ocr.name.strip().replace('\n', ' ')
    Logger.name_logs(clean_name)
    Logger.quantity_logs(Ocr.quantity)

    match Ocr.quantity:
        case 1:
            Ocr.process_price_1()
            if (Ocr.price_1 == 1):
                pyautogui.write(str(1))
                Logger.price_1_logs(1)
            else:
                pyautogui.write(str(Ocr.price_1 - 1))
                Logger.price_1_logs(Ocr.price_1 - 1)
        case 10:
            Ocr.process_price_10()
            pyautogui.write(str(Ocr.price_10 - 1))
            Logger.price_10_logs(Ocr.price_10 - 1)
        case 100:
            Ocr.process_price_100()
            pyautogui.write(str(Ocr.price_100 - 1))
            Logger.price_100_logs(Ocr.price_100 - 1)


    # sell button
    pyautogui.moveTo(498, 445)
    pyautogui.click()

    # popup attention priux trop bas
    pyautogui.moveTo(863, 689)
    pyautogui.click()
    
    Logger.delimiter()