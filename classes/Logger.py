from datetime import datetime
import logging

class LoggerClass:
    def __init__(self, gui):
        current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") 
        self.log_filename = f'logs/log_solding_dofus_{current_time}.log'
        self.Gui = gui

    def init_logs(self):
        logging.basicConfig(filename=self.log_filename, filemode='w', level=logging.INFO, format='%(message)s')
        logging.info("----- Starting new session -----")
        print("----- Starting new session -----")
        self.Gui.log("----- Starting new session -----")

    def log(self, string):
        logging.info(string)
        print(string)
        self.Gui.log(string)

    def delimiter(self):
        logging.info("-------------------------------------")
        print("-------------------------------------")
        self.Gui.log("-------------------------------------")

