import os
import sys
import tkinter as tk
from tkinter import PhotoImage, scrolledtext, messagebox
import global_var as gvar

class GUIClass:
    def __init__(self):
        self.log_feed = None
        self.master = tk.Tk()
        self.is_running = True
        self.item_img = None
        self.image_refs = {}

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def init(self, selling, repricing):
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



        self.selling_button = tk.Button(self.master, text="Start selling", command=lambda: self.popup_msg("Warning", "Make sure the items in your bags are sorted by name, Click OK to proceed or Cancel to wait.", selling))
        self.repricing_button = tk.Button(self.master, text="Start repricing", command=lambda: self.popup_msg("Warning", "Make sure the items in your AH feed are sorted by time (lower time at the top), Click OK to proceed or Cancel to wait.", repricing))

        self.selling_button.pack()
        self.repricing_button.pack()

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

    def popup_msg(self, type_msg, msg, func=None):
        resp = messagebox.askokcancel(type_msg, msg)
        if resp and func: func()
