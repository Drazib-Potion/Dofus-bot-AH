import subprocess
import threading
import keyboard
import pyautogui
import os
import random
import time
from classes.OCR import OCRClass
from classes.GUI import GUIClass
from classes.Logger import LoggerClass
import global_var as gvar
import shutil
import tkinter as tk
from tkinter import scrolledtext

class Bot:
    def __init__(self):
        self.Gui = GUIClass()
        self.Logger = LoggerClass(self.Gui)
        self.Ocr  = OCRClass()

    def init(self):
        if not os.path.exists("logs"): os.makedirs("logs")
        if not os.path.exists("img"): os.makedirs("img")
        subprocess.call(['attrib', '+H', "img"])

        self.Gui.init(self.selling_script_in_thread, self.repricing_script)
        self.Logger.init_logs()
        self.Gui.start()


    def click_pos(self, x, y):
        pyautogui.moveTo(x, y)
        pyautogui.click()

    def selling_script_in_thread(self):
        thread = threading.Thread(target=self.selling_script)
        thread.start()
    
    def repricing_script_in_thread(self):
        thread = threading.Thread(target=self.repricing_script)
        thread.start()

    def repricing_script(self):
        self.Ocr.last_item['name'] = ''
        self.Ocr.last_item['quantity'] = ''
        while(True):
            if keyboard.is_pressed('f8'):
                self.Logger.log("Stopping script.", False)
                # shutil.rmtree("img")
                break

            self.click_pos(gvar.first_item_repricing_pos['x'], gvar.first_item_repricing_pos['y'])
            time.sleep(random.uniform(0.5, 1.5))
            
            self.Ocr.screenshoting()
            self.Ocr.preprocessing()

            self.Ocr.item['name'] = self.Ocr.process_txt_img(self.Ocr.preprocessed_name_img)
            self.Ocr.item['quantity_in_feed'] = self.Ocr.process_nbr_img(self.Ocr.preprocessed_quantity_img)
            clean_name = self.Ocr.item['name'].strip().replace('\n', ' ')
            self.Logger.log(f"name : {clean_name}", True)
            self.Logger.log(f"quantity : {self.Ocr.item['quantity_in_feed']}", False)

            match self.Ocr.item['quantity_in_feed']:
                case 1:
                    self.Ocr.item['price_1'] = self.Ocr.process_nbr_img(self.Ocr.preprocessed_price_1_img)
                    price_to_write = 1 if self.Ocr.item['price_1'] == 1 else self.Ocr.item['price_1']
                    if price_to_write != 1:
                        price_to_write = price_to_write  if self.Ocr.last_item['name'] == self.Ocr.item['name'] and self.Ocr.last_item['quantity'] == self.Ocr.item['quantity_in_feed'] else price_to_write - 1
                    pyautogui.write(str(price_to_write))
                    self.Logger.log(f"1 repricing for {price_to_write} Kamas", False)
                case 10:
                    self.Ocr.item['price_10'] = self.Ocr.process_nbr_img(self.Ocr.preprocessed_price_10_img)
                    price_to_write = self.Ocr.item['price_10']
                    price_to_write = price_to_write  if self.Ocr.last_item['name'] == self.Ocr.item['name'] and self.Ocr.last_item['quantity'] == self.Ocr.item['quantity_in_feed'] else price_to_write - 1
                    pyautogui.write(str(price_to_write))
                    self.Logger.log(f"10 repricing for {price_to_write} Kamas", False)
                case 100:
                    self.Ocr.item['price_100'] = self.Ocr.process_nbr_img(self.Ocr.preprocessed_price_100_img)
                    price_to_write = self.Ocr.item['price_100']
                    price_to_write = price_to_write  if self.Ocr.last_item['name'] == self.Ocr.item['name'] and self.Ocr.last_item['quantity'] == self.Ocr.item['quantity_in_feed'] else price_to_write - 1
                    pyautogui.write(str(price_to_write))
                    self.Logger.log(f"100 repricing for {price_to_write} Kamas", False)

            self.Ocr.last_item['name'] = self.Ocr.item['name']
            self.Ocr.last_item['quantity'] = self.Ocr.item['quantity_in_feed']

            self.click_pos(gvar.repricing_button_pos['x'], gvar.repricing_button_pos['y'])
            self.click_pos(gvar.popup_button_pos['x'], gvar.popup_button_pos['y'])
            self.Logger.delimiter()

    def selling_script(self):
        self.Ocr.last_item['name'] = ''
        self.Ocr.last_item['quantity'] = ''
        while(True):
            if keyboard.is_pressed('f8'):
                self.Logger.log("Stopping script.", False)
                # shutil.rmtree("img")
                break

            self.click_pos(gvar.first_item_in_bags_pos['x'], gvar.first_item_in_bags_pos['y'])
            time.sleep(random.uniform(0.5, 1.5))
            
            self.Ocr.screenshoting()
            self.Ocr.preprocessing()

            self.Ocr.item['name'] = self.Ocr.process_txt_img(self.Ocr.preprocessed_name_img)
            self.Ocr.item['quantity'] = self.Ocr.process_nbr_img(self.Ocr.preprocessed_quantity_img)
            clean_name = self.Ocr.item['name'].strip().replace('\n', ' ')
            self.Logger.log(f"name : {clean_name}", True)
            self.Logger.log(f"quantity : {self.Ocr.item['quantity']}", False)

            match self.Ocr.item['quantity']:
                case 1:
                    self.Ocr.item['price_1'] = self.Ocr.process_nbr_img(self.Ocr.preprocessed_price_1_img)
                    price_to_write = 1 if self.Ocr.item['price_1'] == 1 else self.Ocr.item['price_1']
                    if price_to_write != 1:
                        price_to_write = price_to_write  if self.Ocr.last_item['name'] == self.Ocr.item['name'] and self.Ocr.last_item['quantity'] == self.Ocr.item['quantity'] else price_to_write - 1
                    pyautogui.write(str(price_to_write))
                    self.Logger.log(f"1 solding for {price_to_write} Kamas", False)
                case 10:
                    self.Ocr.item['price_10'] = self.Ocr.process_nbr_img(self.Ocr.preprocessed_price_10_img)
                    price_to_write = self.Ocr.item['price_10']
                    price_to_write = price_to_write  if self.Ocr.last_item['name'] == self.Ocr.item['name'] and self.Ocr.last_item['quantity'] == self.Ocr.item['quantity'] else price_to_write - 1
                    pyautogui.write(str(price_to_write))
                    self.Logger.log(f"10 solding for {price_to_write} Kamas", False)
                case 100:
                    self.Ocr.item['price_100'] = self.Ocr.process_nbr_img(self.Ocr.preprocessed_price_100_img)
                    price_to_write = self.Ocr.item['price_100']
                    price_to_write = price_to_write  if self.Ocr.last_item['name'] == self.Ocr.item['name'] and self.Ocr.last_item['quantity'] == self.Ocr.item['quantity'] else price_to_write - 1
                    pyautogui.write(str(price_to_write))
                    self.Logger.log(f"100 solding for {price_to_write} Kamas", False)

            self.Ocr.last_item['name'] = self.Ocr.item['name']
            self.Ocr.last_item['quantity'] = self.Ocr.item['quantity']

            self.click_pos(gvar.sell_button_pos['x'], gvar.sell_button_pos['y'])
            self.click_pos(gvar.popup_button_pos['x'], gvar.popup_button_pos['y'])
            self.Logger.delimiter()