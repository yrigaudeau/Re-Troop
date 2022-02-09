from lib2to3.pgen2.token import RIGHTSHIFT
import re
from turtle import width


try:
    from Tkinter import *
except ImportError:
    from tkinter import *


class PlayerInterface:
    def __init__(self, interface):
        self.interface = interface
        self.visible = False

    def create(self):
        self.window = Toplevel()
        self.window.title("Create Player")
        # self.window.geometry("800x800")
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

        self.playerNameText = Text(texts, height=1, width=10, wrap=None)
        self.playerInstText = Text(texts, height=1, width=10, wrap=None)
        self.playerNameText.pack(padx=5, pady=5)
        self.playerInstText.pack(padx=5, pady=5)

        Button(self.window, text="Create Player", command=self.createPlayer).pack(padx=5, pady=5, side=BOTTOM)

        self.visible = True
        self.window.grab_set()
        self.window.mainloop()

    def createPlayer(self):
        playerName = self.playerNameText.get('1.0', 'end-1c')
        playerInst = self.playerInstText.get('1.0', 'end-1c')
        if playerName != "" and playerInst != "":
            self.interface.playerBuilder.addPlayer(playerName, playerInst)
            self.destroy()

    def destroy(self):
        self.window.destroy()
        self.visible = False

    def lift(self):
        self.window.lift()
