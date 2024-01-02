from pytesseract import pytesseract

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

icon_item_img_name = 'img/icon_item.png'
name_img_name = 'img/name.png'
quantity_img_name = 'img/quantity.png'
quantity_in_feed_img_name = 'img/quantity_in_feed.png'

price_1_img_name = 'img/price_1.png'
price_10_img_name = 'img/price_10.png'
price_100_img_name = 'img/price_100.png'

icon_item_rect = {
    'x': 540,
    'y': 185,
    'width': 55,
    'height': 55
}

name_rect = {
    'x': 355,
    'y': 180,
    'width': 180,
    'height': 58
}

quantity_rect = {
    'x': 480,
    'y': 300,
    'width': 40,
    'height': 50
}

quantity_in_feed_rect = {
    'x': 535,
    'y': 325,
    'width': 35,
    'height': 40
}


price_1_rect = {
    'x': 510,
    'y': 550,
    'width': 70,
    'height': 30
}

price_10_rect = {
    'x': 510,
    'y': 590,
    'width': 70,
    'height': 30
}

price_100_rect = {
    'x': 510,
    'y': 635,
    'width': 70,
    'height': 30
}
#########################################################################
#########################################################################
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

repricing_button_pos = {
    'x': 520,
    'y': 445,
}

first_item_repricing_pos = {
    'x': 850,
    'y': 260,
}

