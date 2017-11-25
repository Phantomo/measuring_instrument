import tkinter as tk
# from tkinter import ttk
from constants import WINDOW_HEIGHT, WINDOW_WIDTH
from search_page import SearchPage
from languages import TITLE, LANG
from result_page import ResultPage
from start_page import StartPage
from info_page import InfoPage
from add_frame import AddInstrument


class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        self.frames = {}
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        for F in (ResultPage, StartPage, SearchPage, InfoPage, AddInstrument):
            frame = F(container, self)
            frame.grid(row=0, column=0, sticky='nsew')
            self.frames[F] = frame
        self.show_frame(AddInstrument)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def show_result(self, **kwargs):
        frame = self.frames[ResultPage]
        frame.tkraise()
        frame.find_result(**kwargs)


if __name__ == '__main__':
    win = MainApp()
    win.title(TITLE[LANG])
    win.geometry(str(WINDOW_WIDTH)+'x'+str(WINDOW_HEIGHT))
    win.iconbitmap('app_icon2.ico')
    win.resizable(False, False)

    win.mainloop()
