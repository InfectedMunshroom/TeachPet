import tkinter as tk

import pyautogui as pg
import ttt as t

class scenes():
    def __init__(self,window):
        self.root = window
        self.width,self.height=pg.size()
        self.mainloop = window.mainloop


    def scene1(self):
        t.ttt(self.root).scene1()
