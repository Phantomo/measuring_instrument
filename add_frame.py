import json
from constants import DATABASE
import tkinter as tk
from languages import ADD_TITLE, LANG, ADD_TYPE, ADD_MODEL, ADD_ACCURACY, ADD_BRAND, ADD_PANEL, ADD_WEIGHT, ADD_BTN, \
    ADD_MEASURE, ADD_PANEL_TYPE, SP_BACK, ADD_MEASURE_TYPE
import start_page as sp
from instrument import Instrument

class AddInstrument(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_rowconfigure(10)
        self.grid_columnconfigure(4)
        label_title = tk.Label(self, text=ADD_TITLE[LANG])
        label_title.grid(row=0, column=0, columnspan=4, sticky='news', padx=200, pady=20)

        label_measure_type = tk.Label(self, text=ADD_MEASURE_TYPE[LANG])
        label_measure_type.grid(row=1, column=0,columnspan=3)

        self.check_measure_types = {}
        count = 2
        for key, value in ADD_MEASURE[LANG].items():
            self.check_measure_types[value] = tk.IntVar()
            tk.Checkbutton(self, text=key, variable=self.check_measure_types[value], anchor=tk.W).grid(row=count, column=0, columnspan=2, sticky='e')
            count += 1

        count = 1
        self.param_entry = {}
        for name in (ADD_TYPE, ADD_MODEL, ADD_ACCURACY, ADD_BRAND, ADD_WEIGHT):
            tk.Label(self, text=name[LANG]).grid(row=count, column=3)
            self.param_entry[name['en']] = tk.Entry(self)
            self.param_entry[name['en']].grid(row=count, column=4)
            count += 1
        tk.Label(self, text=ADD_PANEL[LANG]).grid(row=7, column=3)
        self.panel = tk.IntVar(self, 1)
        tk.Radiobutton(self, text=list(ADD_PANEL_TYPE[LANG].keys())[0], value=1, variable=self.panel).grid(row=7, column=4, sticky='w')
        tk.Radiobutton(self, text=list(ADD_PANEL_TYPE[LANG].keys())[1], value=0, variable=self.panel).grid(row=8, column=4, sticky='w')
        tk.Button(self, text=SP_BACK[LANG], command=lambda: controller.show_frame(sp.StartPage)).grid(row=9, column=2)
        tk.Button(self, text=ADD_BTN[LANG], command=lambda: self.add_instrument()).grid(row=9, column=3)

    def add_instrument(self):
        new = Instrument()