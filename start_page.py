import tkinter as tk
from search_page import SearchPage
from info_page import InfoPage


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_rowconfigure(3)
        self.grid_columnconfigure(3)
        label = tk.Label(self, text="Hi, my name Oleg Zhovnuvatiy aka mr_oz\n" +
                                    "I am fourth year student of KPI\n" +
                                    "group PB-41\n" +
                                    "teacher Katruk Orest Viktorovuch\n" +
                                    "program created for easy choose measuring instruments")
        label.grid(row=1, column=0, columnspan=3, sticky='wens', padx=5, pady=5)
        search_button = tk.Button(self, text="Search",
                           command=lambda: controller.show_frame(SearchPage))
        search_button.grid(row=2, column=2)
        info_button = tk.Button(self, text="Info", command=lambda: controller.show_frame(InfoPage))
        info_button.grid(row=2, column=1)
