import tkinter as tk
import start_page as sp
from languages import IP_BACK, IP_INFO, LANG

class InfoPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label_info = tk.Label(self, text=IP_INFO[LANG])
        label_info.pack()
        back_btn = tk.Button(self, text=IP_BACK[LANG], command=lambda: controller.show_frame(sp.StartPage))
        back_btn.pack(side="bottom")