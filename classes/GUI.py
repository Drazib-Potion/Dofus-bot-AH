import tkinter as tk
from tkinter import scrolledtext

class GUIClass:
    def __init__(self):
        self.log_feed = None
        self.master = tk.Tk()

        self.is_running = True
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def init(self, start_bot_func):
        self.master.title("AH Bot Control Panel")

        self.start_button = tk.Button(self.master, text="Start", command=start_bot_func)
        self.start_button.pack()

        self.log_feed = scrolledtext.ScrolledText(self.master, wrap=tk.WORD)
        self.log_feed.pack(expand=True, fill='both')
        self.log_feed.config(state='disabled')

    def log(self, log):
        if self.is_running:
            self.log_feed.config(state='normal')
            self.log_feed.insert(tk.END, log + "\n")
            self.log_feed.config(state='disabled')
            self.log_feed.see(tk.END)
        
    def start(self):
        self.master.mainloop()
        self.is_running = False
        
    def on_closing(self):
        self.is_running = False
        self.master.destroy()
