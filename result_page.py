import tkinter as tk
from constants import WINDOW_HEIGHT
from start_page import StartPage
from tkinter import messagebox


class ResultPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.database = None
        # with open("database.json", 'r') as fp:
        #     json.dump(self.database, fp)
        # if self.database is None:
        #     messagebox.showerror("Database error!!", "Sorry but database not exist or invalid")
        self.listbox = tk.Listbox(self, height=WINDOW_HEIGHT - 200)
        self.listbox.pack(side="left")
        for elem in ["test", "sdgdgdf", "asfsfsdf"]:
            self.listbox.insert(tk.END, elem)

        button = tk.Button(self, text="StartPage",
                           command=lambda: controller.show_frame(StartPage))
        button.pack()

    #def find_result(self, **kwargs):