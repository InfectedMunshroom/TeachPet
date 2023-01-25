import pyautogui as pg
import tkinter as tk
import database as db
import gamer as gg

class home():
    def __init__(self,window):
        self.root = window
        self.rootWidth,self.rootHeight = pg.size()

    def scene1(self):
        frame1 = tk.Frame(self.root,bg='#5534A5',width=self.rootWidth,height=self.rootHeight)
        frame2 = tk.Frame(frame1,bg='grey',width=200,height=self.rootHeight)
        def openbase():
            frame1.destroy()
            db.scenes(self.root).scene1()
        def opengame():
            frame1.destroy()
            gg.scenes(self.root).scene1()
        button1 = tk.Button(frame1,bg='#6FDFDF',width=25,height=10,text='Database',command=openbase)
        button2 = tk.Button(frame1,bg='#6FDFDF',width=25,height=10,text='Games',command=opengame)


        frame1.place(x=0,y=0)
        button1.place(x=15,y=90,anchor='w')
        button2.place(x=250,y=90,anchor='w')



