import tkinter as tk
from languages import STP_ABOUT, STP_BTN_INFO, STP_BTN_SEARCH, LANG
import search_page as sp
import info_page as ip


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_rowconfigure(2)
        self.grid_columnconfigure(3)
        label = tk.Label(self, text=STP_ABOUT[LANG])
        label.grid(row=1, column=2, columnspan=2, sticky='wens', padx=5, pady=5)
        search_button = tk.Button(self, text=STP_BTN_SEARCH[LANG], command=lambda: controller.show_frame(sp.SearchPage))
        search_button.grid(row=2, column=3)
        info_button = tk.Button(self, text=STP_BTN_INFO[LANG], command=lambda: controller.show_frame(ip.InfoPage))
        info_button.grid(row=2, column=2)
