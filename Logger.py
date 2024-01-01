from datetime import datetime
import logging

class LoggerClass:
    def __init__(self):
        current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") 
        self.log_filename = f'logs/log_solding_dofus_{current_time}.log'

    def init_logs(self):
        logging.basicConfig(filename=self.log_filename, filemode='w', level=logging.INFO, format='%(message)s')
        logging.info("----- Starting new session -----")
        print("----- Starting new session -----")

    def name_logs(self, name):
        logging.info(f"name : {name}")
        print(f"name : {name}")

    def quantity_logs(self, quantity):
        logging.info(f"quantity : {quantity}")
        print(f"quantity : {quantity}")

    def price_1_logs(self, price_1):
        logging.info(f"1 solding for {price_1 - 1} Kamas")
        print(f"1 solding for {price_1 - 1} Kamas")

    def price_10_logs(self, price_10):
        logging.info(f"10 solding for {price_10 - 1} Kamas")
        print(f"10 solding for {price_10 - 1} Kamas")

    def price_100_logs(self, price_100):
        logging.info(f"100 solding for {price_100 - 1} Kamas")
        print(f"100 solding for {price_100 - 1} Kamas")

    def delimiter(self):
        print("-------------------------------------")
        logging.info("-------------------------------------")

