import tkinter as tk
from numpy import genfromtext

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

class MainApp(object):

    def __init__(self, root, database_file):
        self.root = root
        try:
            self.database = genfromtext(database_file, delimiter=',')
        except Exception:
            print("Database file not valid or not exist. Check file and restart program")
            exit()

    def show_result(self, instrument_list):
        self.search_frame_deactivate()


    def search_instrument(self, size, precision):
        size = int(size)
        precision = int(precision)
        if not size:
            tk.Message(self.root, text="Parameter size mandatory. Please entry size!!!")
        elif size < 0:
            tk.Message(self.root, text="Size must be positive. Please entry correct size!!!")
        if not precision:
            precision = 0
        return self.database

    def search_element(self, frame):
        self.search_button = tk.Button(frame, text='Find', command=self.search_instrument())

        self.size_label = tk.Label(frame, text="Entry measure place size")
        self.size_var = tk.StringVar()
        self.search_size_entry = tk.Entry(frame, textvariable=self.size_var)
        self.size_label.place(x=100, y=90)
        self.search_size_entry.place(x=100, y=100)

        self.precision_label = tk.Label(frame, text="Entry precision")
        self.precision_var = tk.StringVar()
        self.search_precision = tk.Entry(frame, textvariablel=self.precision_var)
        self.precision_label.place(x=100, y=140)
        self.search_precision.place(x=100, y=150)

    def result_frame(self):
        self.result_frame = tk.Frame(self.root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)

    def result_element(self, frame):

    def search_frame(self):
        self.search_frame = tk.Frame(self.root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
        self.search_element(self.search_frame)

    def search_frame_activate(self):
        self.search_frame.pack()

    def search_frame_deactivate(self):
        self.search_frame.pack_forget()

win = tk.Tk()
win.title('Measuring instrument')
win.geometry(str(WINDOW_HEIGHT)+'x'+str(WINDOW_WIDTH))
win.resizable(False, False)

gui = MainApp(win, 'measuring_instrument.csv')

win.mainloop()
