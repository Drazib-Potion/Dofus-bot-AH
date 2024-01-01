from pytesseract import pytesseract

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

name_img_name = 'img/name.png'
quantity_img_name = 'img/quantity.png'
price_1_img_name = 'img/price_1.png'
price_10_img_name = 'img/price_10.png'
price_100_img_name = 'img/price_100.png'

name_pos = {
    'x': 355,
    'y': 180,
    'width': 180,
    'height': 58
}

quantity_pos = {
    'x': 480,
    'y': 300,
    'width': 40,
    'height': 50
}

price_1_pos = {
    'x': 510,
    'y': 550,
    'width': 70,
    'height': 30
}

price_10_pos = {
    'x': 510,
    'y': 590,
    'width': 70,
    'height': 30
}

price_100_pos = {
    'x': 510,
    'y': 635,
    'width': 70,
    'height': 30
}

first_item_in_bags_pos = {
    'x': 1278,
    'y': 206,
}

sell_button_pos = {
    'x': 498,
    'y': 445,
}

popup_button_pos = {
    'x': 863,
    'y': 689,
}


