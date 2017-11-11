import tkinter as tk
#from numpy import genfromtxt

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
SEARCH_VARIANT = [
    "thread",
    "diameter",
    "main sizes",
    "angle"
]


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


class ResultPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        listbox = tk.Listbox(self, height=WINDOW_HEIGHT - 200)
        listbox.pack(side="left")
        for elem in ["test", "sdgdgdf", "asfsfsdf"]:
            listbox.insert(tk.END, elem)

        button = tk.Button(self, text="StartPage",
                           command=lambda: controller.show_frame(StartPage))
        button.pack()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start page")
        label.pack()
        button = tk.Button(self, text="Result",
                           command=lambda: controller.show_frame(SearchPage))
        button.pack()


class SearchPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.param_frame = {}
        self.grid_rowconfigure(3)
        label = tk.Label(self, text="Search page")
        label.grid(row=1, ipadx=WINDOW_WIDTH / 2 - 50, ipady=30)
        self.param = tk.StringVar(self)
        self.param.set(SEARCH_VARIANT[0])
        choose_box = tk.OptionMenu(self, self.param, *SEARCH_VARIANT)
        choose_box.grid(row=2)
        self.param.trace('w', self.change_param)
        #thread instrument
        self.param_frame[SEARCH_VARIANT[0]] = tk.Frame(self)

    def change_param(self, *args):
        print(self.param.get())

    def change_param_frame(self, param):



win = MainApp()
win.title('Measuring instrument')
win.geometry(str(WINDOW_HEIGHT)+'x'+str(WINDOW_WIDTH))
win.resizable(False, False)

win.mainloop()
