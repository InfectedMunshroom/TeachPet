import tkinter as tk
import pyautogui as pg
import csv
import login as lg

class signup():
    def __init__(self,window):
        self.root = window
        self.rootHeight,self.rootWidth = pg.size()
        self.mainloop = self.root.mainloop

    def scene1(self):
        username = tk.StringVar()
        password = tk.StringVar()

        def enterpas():
            self.enterpass(entry1.get(),entry2.get())
            frame1.destroy()
            obj = lg.login(self.root)
            obj.scene1()

        def goback():
            frame1.destroy()
            lg.login(self.root).scene1()


        frame1 = tk.Frame(self.root,height=self.rootWidth,width=self.rootHeight,bg='#5534A5')
        label1 = tk.Label(frame1,text='Sign Up',bg='#5534A5',font=('Times New Roman',75))
        label2 = tk.Label(frame1,text='Username',bg='#5534A5',font=('Times New Roman',25))
        label3 = tk.Label(frame1,text='Password',bg='#5534A5',font=('Times New Roman',25))
        entry1 = tk.Entry(frame1,bg='white',textvariable=username,font=('Times New Roman',25))
        entry2 = tk.Entry(frame1,bg='white',textvariable=password, font=('Times New Roman',25))
        button1 = tk.Button(frame1,text='Sign Up',font=('Times New Roman',25),bg='#6FDFDF',command=enterpas)
        button2 = tk.Button(frame1,text='Return',font=('Times New Roman',25),bg='#6FDFDF',command=goback)
        

        frame1.place(x=0,y=1)
        label1.place(x=700,y=50,anchor='center')
        label2.place(x=400,y=250)
        label3.place(x=400,y=350)
        entry1.place(x=700,y=250)
        entry2.place(x=700,y=350)
        button1.place(x=600,y=500)
        button2.place(x=25,y=800)


    def enterpass(self,uname,upass):
        file = open(r'password.csv','a')
        obj = csv.writer(file)
        ls = [uname,upass]
        obj.writerow(ls)
        file.close()
