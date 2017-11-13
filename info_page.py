import tkinter as tk
from start_page import StartPage


class InfoPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label_info = tk.Label(self, text="Info")
        label_info.pack()
        back_btn = tk.Button(self, text="<-Back", command=lambda: controller.show_frame(StartPage))
        back_btn.pack(side="bottom")