import pyautogui
from PIL import ImageGrab
import global_var

def name():
    x, y, width, height = 355, 180, 180, 58
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))

    screenshot.save(global_var.name_img_name)

def quantity():
    x, y, width, height = 480, 300, 40, 50
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))

    screenshot.save(global_var.quantity_img_name)

def prices_1():
    x, y, width, height = 510, 550, 70, 30
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))

    screenshot.save(global_var.prices_1_img_name)

def prices_10():
    x, y, width, height = 510, 590, 70, 30
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))

    screenshot.save(global_var.prices_10_img_name)

def prices_100():
    x, y, width, height = 510, 635, 70, 30
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))

    screenshot.save(global_var.prices_100_img_name)
