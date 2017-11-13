import tkinter as tk
# from tkinter import ttk
#from numpy import genfromtxt
from constants import WINDOW_HEIGHT, WINDOW_WIDTH
from search_page import SearchPage


class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        self.frames = {}
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        for F in (ResultPage, StartPage, SearchPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def show_result(self, **kwargs):
        frame = self.frames[ResultPage]
        frame.tkraise()
        frame.find_result(**kwargs)





win = MainApp()
win.title('Measuring instrument')
win.geometry(str(WINDOW_HEIGHT)+'x'+str(WINDOW_WIDTH))
win.resizable(False, False)

win.mainloop()
