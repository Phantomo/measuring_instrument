import tkinter as tk
from constants import WINDOW_WIDTH, SEARCH_VARIANT
from tkinter import messagebox
from tkinter import scrolledtext as tkst
import result_page as rp
from languages import THREAD_RB_TYPE, LANG, SP_SEARCH, SP_L_ACCURACY, SP_L_DIAMETER, SP_L_STEP, SP_L_ADD_INFO, \
    SP_SEARCH_PAGE, SP_SIZE, SP_SEARCH_VARIANT


class SearchPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.param_frame = {}
        self.search_variant = {SEARCH_VARIANT[0]: ThreadSearch,
                               SEARCH_VARIANT[1]: DiameterSearch,
                               SEARCH_VARIANT[2]: MainSizesSearch,
                               SEARCH_VARIANT[3]: AngleSearch,
                               SEARCH_VARIANT[4]: RoughnessSearch,
                               SEARCH_VARIANT[5]: IndicatorSearch}
        self.grid_rowconfigure(4)
        label = tk.Label(self, text=SP_SEARCH_PAGE[LANG])
        label.grid(row=1, ipadx=WINDOW_WIDTH / 2 - 50, ipady=30)
        self.param = tk.StringVar(self)
        self.param.set(list(SP_SEARCH_VARIANT[LANG].keys())[0])
        choose_box = tk.OptionMenu(self, self.param, *list(SP_SEARCH_VARIANT[LANG].keys()))
        choose_box.grid(row=2)
        self.param.trace('w', self.change_param)
        container = tk.Frame(self)
        container.grid(row=3, sticky='nsew')
        for name, F in self.search_variant.items():
            frame = F(container, self)
            frame.grid(row=0, column=0, sticky='nsew')
            self.param_frame[F] = frame
        self.show_frame(SEARCH_VARIANT[0])

    def change_param(self, *args):
        self.show_frame(SP_SEARCH_VARIANT[LANG][self.param.get()])

    def show_frame(self, param):
        frame = self.param_frame[self.search_variant[param]]
        frame.tkraise()

    def start_search(self):
        pass
        # find_class = self.search_variant[self.param.get()]
        # error_msg = find_class.check_param()
        # if error_msg:
        #     messagebox.showerror(title="You fail bro", message=error_msg)
        # else:
        #     self.controller.show_frame(rp.ResultPage)


class ISearchParam(object):

    def check_param(self):
        raise NotImplementedError("Should have implemented this")


class DiameterSearch(ISearchParam, tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_rowconfigure(3)
        self.grid_columnconfigure(2)
        label_size = tk.Label(self, text=SP_L_DIAMETER[LANG])
        label_size.grid(row=1, column=1, padx=20, sticky='w')
        self.size = tk.Entry(self)
        self.size.grid(row=1, column=2)
        label_accuracy = tk.Label(self, text=SP_L_ACCURACY[LANG])
        label_accuracy.grid(row=2, column=1, padx=20, sticky='w')
        self.accuracy = tk.Entry(self)
        self.accuracy.grid(row=2, column=2)
        label_info = tk.Label(self, text=SP_L_ADD_INFO[LANG])
        label_info.grid(row=3, column=2, columnspan=2, pady=10)
        info_text = tkst.ScrolledText(self, wrap=tk.WORD)
        info_text.grid(row=4, column=2, columnspan=2)
        f = open('screw_thread_source.txt', 'r')
        if f:
            info_text.insert(tk.INSERT, f.read())
        f.close()
        search_btn = tk.Button(self, text=SP_SEARCH[LANG])
        search_btn.grid(row=5, column=2, columnspan=2, padx=100)

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


class ThreadSearch(ISearchParam, tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_rowconfigure(4)
        self.grid_columnconfigure(3)

        self.thread_choose = tk.StringVar()

        thread_variant = tk.StringVar()
        count = 1
        for key, value in THREAD_RB_TYPE[LANG].items():
            tk.Radiobutton(self, text=value, variable=thread_variant, value=key).grid(row=count, column=1, sticky='w', padx=40)
            count += 1
        label_step = tk.Label(self, text=SP_L_STEP[LANG])
        label_step.grid(row=1, column=2)

        self.step = tk.Entry(self)
        self.step.grid(row=2, column=2)
        search_btn = tk.Button(self, text=SP_SEARCH[LANG])
        search_btn.grid(row=5, column=2, columnspan=2, sticky='es')

    def get_step(self):
        return self.step

    def check_param(self):
        pass


class RoughnessSearch(ISearchParam, tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_rowconfigure(4)
        self.grid_columnconfigure(2)

    def check_param(self):
        pass


class MainSizesSearch(ISearchParam, tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label_size = tk.Label(self, text=SP_SIZE[LANG])
        label_size.grid(row=1, column=1)
        self.size = tk.Entry(self)
        self.size.grid(row=1, column=2)

    def get_size(self, parent, controller):
        return self.size

    def check_param(self):
        pass


class AngleSearch(ISearchParam, tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

    def check_param(self):
        pass


class IndicatorSearch(ISearchParam, tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

    def check_param(self):
        pass