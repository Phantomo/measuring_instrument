import tkinter as tk
from constants import WINDOW_WIDTH, SEARCH_VARIANT
from tkinter import messagebox
from tkinter import scrolledtext as tkst


class SearchPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.param_frame = {}
        self.grid_rowconfigure(4)
        label = tk.Label(self, text="Search page")
        label.grid(row=1, ipadx=WINDOW_WIDTH / 2 - 50, ipady=30)
        self.param = tk.StringVar(self)
        self.param.set(SEARCH_VARIANT[0])
        choose_box = tk.OptionMenu(self, self.param, *SEARCH_VARIANT)
        choose_box.grid(row=2)
        self.param.trace('w', self.change_param)
        container = tk.Frame(self)
        container.grid(row=3, sticky='nsew')

        search_button = tk.Button(self, text="Find", command=self.start_search())
        search_button.grid(4)

    def change_param(self, *args):
        print(self.param.get())

    def show_frame(self, param):
        frame = self.param_frame[param]
        frame.tkraise()

    def start_search(self):
        find_class = self.search_variant[self.param.get()]
        error_msg = find_class.check_param()
        if error_msg:
            messagebox.showerror(title="You fail bro", message=error_msg)
        else:
            self.controller.show_frame(ResultPage)


class ISearchParam(object):

    def check_param(self):
        raise NotImplementedError("Should have implemented this")


class DiameterSearch(ISearchParam, tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_rowconfigure(3)
        self.grid_columnconfigure(2)
        label_size = tk.Label(self, text="Measuring size")
        label_size.grid(row=1, column=1)
        self.size = tk.Entry(self)
        self.size.grid(row=1, column=1)
        label_accuracy = tk.Label(self, text="Accuracy")
        label_accuracy.grid(row=2, column=1)
        self.accuracy = tk.Entry(self)
        self.accuracy.grid(row=2, column=2)
        label_info = tk.Label(self, text="Additional information")
        label_info.grid(row=3, column=1)
        info_text = tkst.ScrolledText(self, wrap=tk.WORD)
        info_text.grid(row=3, column=2)
        f = open('screw_thread_source.txt', 'r')
        if f:
            info_text.insert(tk.INSERT, f.read())
        f.close()

    def get_size(self):
        return self.size

    def get_accuracy(self):
        return self.accuracy

    def check_param(self):
        size = self.size.get()
        accuracy = self.accuracy.get()
        if size.isnumeric() and accuracy.isnumeric():
            if size > 0 and accuracy > 0:
                return None
            else:
                return "Parameters must be positive"
        else:
            return "Parameter empty"





