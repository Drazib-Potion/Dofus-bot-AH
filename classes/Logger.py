from datetime import datetime
import logging
import uuid

class LoggerClass:
    def __init__(self, gui):
        current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") 
        self.log_filename = f'logs/log_solding_dofus_{current_time}.log'
        self.Gui = gui

    def init_logs(self):
        logging.basicConfig(filename=self.log_filename, filemode='w', level=logging.INFO, format='%(message)s')
        logging.info("----- Starting new session -----")
        print("----- Starting new session -----")
        self.Gui.log_txt("----- Starting new session -----")

    def log(self, string, is_icon):
        logging.info(string)
        print(string)
        if is_icon: self.Gui.log_icon(uuid.uuid4())
        self.Gui.log_txt(string)

    def delimiter(self):
        logging.info("-------------------------------------")
        print("-------------------------------------")
        self.Gui.log_txt("-------------------------------------")

