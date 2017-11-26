import tkinter as tk
from constants import WINDOW_HEIGHT
from start_page import StartPage
from tkinter import messagebox
from tkinter import scrolledtext as tkst


class ResultPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.records = []
        self.database = None
        self.listbox = tk.Listbox(self, height=WINDOW_HEIGHT - 200)
        self.listbox.bind('<<ListboxSelect>>', self.select_item)
        self.listbox.pack(side="left")
        self.instrument_info = tkst.ScrolledText(self, wrap=tk.WORD)
        self.instrument_info.pack(side="right")
        button = tk.Button(self, text="StartPage",
                           command=lambda: controller.show_frame(StartPage))
        button.pack()

    def update_data(self, records):
        self.records = records
        self.listbox.delete(0, tk.END)
        for item in records:
            self.listbox.insert(tk.END, item['type'])
            print(self.listbox.focus)

    @staticmethod
    def prettify(**kwargs):
        result_str = ''
        if kwargs is None:
            return result_str
        for param in kwargs:
            result_str = result_str + param + ' : ' + kwargs[param] + '\n'
        return result_str

    def choose_instrument(self, ins_type):
        for item in self.records:
            if item['type'] == ins_type:
                return item
        return None

    def select_item(self):
        current_selection = self.listbox.curselection()
        instrument = self.choose_instrument(current_selection)
        self.instrument_info.insert(tk.INSERT, self.prettify(instrument))
        print(current_selection)