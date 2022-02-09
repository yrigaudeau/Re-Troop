from lib2to3.pgen2.token import RIGHTSHIFT
from turtle import width


try:
    from Tkinter import *
except ImportError:
    from tkinter import *


class PlayerInterface:
    def __init__(self):
        self.visible = False

    def create(self):
        self.window = Toplevel()
        self.window.title("Create Player")
        #self.window.geometry("800x800")
        self.window.resizable(0, 0)
        self.window.focus_force()
        self.window.protocol('WM_DELETE_WINDOW', self.destroy)
        
        top = Frame(self.window)
        top.pack(side=TOP, padx=30)
        labels = Frame(top)
        labels.pack(side=LEFT)
        texts = Frame(top)
        texts.pack(side=RIGHT)

        Label(labels, text="Player Name :").pack(padx=5, pady=5)
        Label(labels, text="Player Instrument: ").pack(padx=5, pady=5)
        
        Text(texts, height=1, width=10, wrap=None).pack(padx=5, pady=5)
        Text(texts, height=1, width=10, wrap=None).pack(padx=5, pady=5)

        Button(self.window, text="Create Player").pack(padx=5, pady=5, side=BOTTOM)


        self.visible = True
        self.window.mainloop()
        #self.window.grab_set()

    def destroy(self):
        self.window.destroy()
        self.visible = False

    def lift(self):
        self.window.lift()