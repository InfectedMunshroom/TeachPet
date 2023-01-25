import tkinter as tk
import pyautogui as pg
import csv
import home as h
import signup as s

class login():
    def __init__(self,window):
        self.root = window
        self.rootWidth,self.rootHeight = pg.size()

    def scene1(self):
        userName = tk.StringVar()
        passWord = tk.StringVar()
        def login():
            if (self.checkpass(username.get(),password.get())):
                frame1.destroy()
                #label1.destroy()
                label2.destroy()
                label3.destroy()
                label4.destroy()
                button1.destroy()
                button2.destroy()
                username.destroy()
                password.destroy()
                h.home(self.root).scene1()

        def signup():
            frame1.destroy()
            #label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            button1.destroy()
            button2.destroy()
            username.destroy()
            password.destroy()
            s.signup(self.root).scene1()
                

        




        frame1 = tk.Frame(self.root,bg='#5534A5',height=self.rootHeight,width=self.rootWidth)
        
        #label1 = tk.Label(self.root,bg='black',text='Shishyan Solutions',fg='white',font=('times new roman',25))
        label2 = tk.Label(self.root,bg='#5534A5',text='Teacher\'s Pet',fg='white',font=('times new roman',75))
        label3 = tk.Label(self.root,bg='#5534A5',text='Username',fg='white',font=('times new roman',25),width=9)
        label4 = tk.Label(self.root,bg='#5534A5',text='Password',fg='white',font=('times new roman',25),width = 9)

        button1 = tk.Button(self.root,bg='#6FDFDF',text='Login',fg='black',font=('times new roman',25),width=9,command=login)
        button2 = tk.Button(self.root,bg='#E15FED',text='Sign Up',fg='black',font=('times new roman',25),width=9,command=signup)

        username = tk.Entry(self.root,bg='white',textvariable = userName,font=('times new roman',22))
        password = tk.Entry(self.root,bg='white',textvariable = passWord,font=('times now roman',22))

        frame1.place(x=0,y=0)

       # label1.place(x=750,y=25,anchor='center')
        label2.place(x=720,y=175,anchor='center')
        label3.place(x=440,y=380)
        label4.place(x=440,y=450)
        username.place(x=680,y=380)
        password.place(x=680,y=450)
        button1.place(x=720,y=660,anchor='center')
        button2.place(x=720,y=750,anchor='center')


    def checkpass(self,username,password):
        file = open(r'password.csv','r')
        obj = csv.reader(file)

        for i in obj:
            if username == i[0]:
                if password == i[1]:
                    return True
        
