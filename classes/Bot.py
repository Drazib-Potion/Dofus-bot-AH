import keyboard
import pyautogui
import os
import random
import time
from classes.OCR import OCRClass
from classes.Logger import LoggerClass

class Bot:
    def __init__(self):
        self.Logger = LoggerClass()
        self.Ocr  = OCRClass()

    def init(self):
        if not os.path.exists("logs"): os.makedirs("logs")
        if not os.path.exists("img"): os.makedirs("img")
        self.Logger.init_logs()

    def run(self):
        while(True):
            if keyboard.is_pressed('f8'):
                print("Stopping script.")
                break

            #first item in bag
            pyautogui.moveTo(1278, 206)
            pyautogui.click()
            time.sleep(random.uniform(0.5, 1.5))
            
            Ocr  = OCRClass()
            Ocr.screenshoting()
            Ocr.preprocessing()

            Ocr.name = Ocr.process_txt_img(Ocr.preprocessed_quantity_img)
            Ocr.quantity = Ocr.process_nbr_img(Ocr.preprocessed_quantity_img)

            clean_name = Ocr.name.strip().replace('\n', ' ')
            self.Logger.name_logs(clean_name)
            self.Logger.quantity_logs(Ocr.quantity)

            match Ocr.quantity:
                case 1:
                    Ocr.price_1 = Ocr.process_nbr_img(Ocr.preprocessed_price_1_img)
                    if (Ocr.price_1 == 1):
                        pyautogui.write(str(1))
                        self.Logger.price_1_logs(1)
                    else:
                        pyautogui.write(str(Ocr.price_1 - 1))
                        self.Logger.price_1_logs(Ocr.price_1 - 1)
                case 10:
                    Ocr.price_10 = Ocr.process_nbr_img(Ocr.preprocessed_price_10_img)
                    pyautogui.write(str(Ocr.price_10 - 1))
                    self.Logger.price_10_logs(Ocr.price_10 - 1)
                case 100:
                    Ocr.price_100 = Ocr.process_nbr_img(Ocr.preprocessed_price_100_img)
                    pyautogui.write(str(Ocr.price_100 - 1))
                    self.Logger.price_100_logs(Ocr.price_100 - 1)


            # sell button
            pyautogui.moveTo(498, 445)
            pyautogui.click()

            # popup attention priux trop bas
            pyautogui.moveTo(863, 689)
            pyautogui.click()
            
            self.Logger.delimiter()

