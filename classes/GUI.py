import os
import sys
import tkinter as tk
from tkinter import PhotoImage, scrolledtext
import global_var as gvar

class GUIClass:
    def __init__(self):
        self.log_feed = None
        self.master = tk.Tk()
        self.is_running = True
        self.item_img = None
        self.image_refs = {}

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def init(self, start_bot_func):
        self.master.title("AH Bot Control Panel")


        # Determine if we're running in a bundle or a normal Python environment
        if getattr(sys, 'frozen', False):
            # If the application is run as a bundle, the pyInstaller bootloader
            # extends the sys module by a flag frozen=True and sets the app 
            # path into variable _MEIPASS'.
            application_path = sys._MEIPASS
        else:
            application_path = os.path.dirname(os.path.abspath(__file__))

        # Use os.path.join to construct the absolute path to the resource
        icon_path = os.path.join(application_path, 'icon.png')
        self.master.iconphoto(False, PhotoImage(file=icon_path))



        self.start_button = tk.Button(self.master, text="Start", command=start_bot_func)
        self.start_button.pack()

        self.log_feed = scrolledtext.ScrolledText(self.master, wrap=tk.WORD)
        self.log_feed.pack(expand=True, fill='both')
        self.log_feed.config(state='disabled')

    def log_txt(self, log):
        if self.is_running:
            self.log_feed.config(state='normal')
            self.log_feed.insert(tk.END, "\n" + log )
            self.log_feed.config(state='disabled')
            self.log_feed.see(tk.END)

    def log_icon(self, uuid):
        if self.is_running:
            if os.path.exists(gvar.icon_item_img_name):
                if uuid not in self.image_refs:
                    img = tk.PhotoImage(file=gvar.icon_item_img_name)
                    self.image_refs[uuid] = img
                else:
                    img = self.image_refs[uuid]

                self.log_feed.config(state='normal')
                self.log_feed.insert(tk.END, "\n")

                self.log_feed.image_create(tk.END, image=img)
                self.log_feed.config(state='disabled')
                self.log_feed.see(tk.END)

    def start(self):
        self.master.mainloop()
        self.is_running = False

    def on_closing(self):
        self.is_running = False
        self.master.destroy()
