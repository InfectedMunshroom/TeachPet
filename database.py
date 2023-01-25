import tkinter as tk
import pyautogui as pg
import mysql.connector as mysql
import home as h

class scenes():

    def __init__ (self,window):
        self.root = window
        self.root.attributes('-fullscreen',True)
        self.mainloop = self.root.mainloop

        self.Width,self.Height = pg.size()

    def scene1(self):

    

        frame1 = tk.Frame(self.root,bg='#5534A5',height=self.Height,width=self.Width)
        label1 = tk.Label(frame1,text='Student Records Database',font=('Times New Roman',45),fg='white',bg='#5534A5')

        def get():
            frame1.destroy()
            self.scene_get_record()
        def gohome():
            frame1.destroy()
            h.home(self.root).scene1()
        def insert():
            frame1.destroy()
            self.scene_insert_record()
        def update():
            frame1.destroy()
            self.scene_update_record()
        
        

        button1 = tk.Button(frame1,text='Get Record',font=('Times New Roman',25),fg='white',bg='#2E0249',command=get)
        button2 = tk.Button(frame1,text='Insert Record',font=('Times New Roman',25),fg='white',bg='#2E0249',command=insert)
        button3 = tk.Button(frame1, text='Update Record',font=('Times New Roman',25),fg='white',bg='#2E0249',command=update)
        button4 = tk.Button(frame1,text='Home',font=('Times New Roman',25),fg='white',command=gohome,bg='#2E0249')



        frame1.place(x=0,y=0)
        label1.place(x=720,y=80,anchor='center')
        button1.place(x=720,y=300,anchor='center')
        button2.place(x=720,y=400,anchor='center')
        button3.place(x=720,y=500,anchor='center')
        button4.place(x=720,y=600,anchor='center')
        

        self.mainloop()

#-------------------------------------------- Insert starts here-------------------------------------------------------------------------------------------

    def scene_insert_record(self): #Choose which database to insert in
        menu = tk.StringVar()
        menu.set("Database")
        frame1 = tk.Frame(self.root,bg='#5534A5',height=self.Height,width=self.Width)
        label1 = tk.Label(frame1,bg='#5534A5',fg='white',text='Select Database: ',font=('Times New Roman',25))
        options = tk.OptionMenu(frame1,menu,'fees','marks','attendance')
        options.configure(font=('Times New Roman',25))

        def back():
            frame1.destroy()
            self.scene1()

        
        def database():
            ak = menu.get()
            if ak == 'fees':
                frame1.destroy()
                self.sql_insert_fees()
            elif ak == 'marks':
                frame1.destroy()
                self.sql_insert_marks()
            elif ak == 'attendance':
                frame1.destroy()
                self.sql_insert_attendance()

        button1 = tk.Button(frame1,bg='#6FDFDF',fg='white',text='Go',font=('Times New Roman','25'),command=database)
        button2 = tk.Button(frame1,bg='#E15FED',fg='white',text='Back',font=('Times New Roman',25),command=back)

        frame1.place(x=0,y=0) #Place them
        label1.place(x=500,y=450,anchor='center')
        options.place(x=850,y=450,anchor='center')
        button1.place(x=720,y=550,anchor='center')
        button2.place(x=50,y=850,anchor='w')



        self.mainloop()

    def sql_insert_attendance(self): #Sql frame + insert

        obj = mysql.connect(host='localhost',user='tester',passwd='1234',database='students')
        cusor = obj.cursor()
        sch_no = tk.StringVar()
        attendance = tk.StringVar()
        total_days = tk.StringVar()

        frame1 = tk.Frame(self.root,bg='#5534A5',height=self.Height,width=self.Width)

        label1 = tk.Label(frame1,text='Scholar Number',font=('Times New Roman',25),bg='#5534A5',fg='white')
        label2 = tk.Label(frame1,text='Attendance',font=('Times New Roman',25),bg='#5534A5',fg='white')
        label3 = tk.Label(frame1,text='Total Days',font=('Times New Roman',25),bg='#5534A5',fg='white')
        entry1 = tk.Entry(frame1,font=('Times New Roman',25),textvariable=sch_no)
        entry2 = tk.Entry(frame1,font=('Times New Roman',25),textvariable=attendance)
        entry3 = tk.Entry(frame1,font=('Times New Roman',25),textvariable=total_days)

        def get_insert_commit():
            alpha = entry1.get()
            beta = entry2.get()
            theta = entry3.get()
            #Try except block used
            try:
                cusor.execute('insert into student_attendance values({},{},{})'.format(alpha,beta,theta))
                obj.commit()
            except:
                frame1.destroy()
                frame2 = tk.Frame(self.root,bg='#5534A5',height=self.Height,width=self.Width)
                label1 = tk.Label(frame2,bg='#5534A5',fg='red',font=('Times New Roman',25),text='Error: Please recheck the entered details')
                button1 = tk.Button(frame2,text='Back',bg='#6FDFDF',font=('Times New Roman',25),fg='white',command=self.sql_insert_attendance)
                frame2.place(x=0,y=0)
                label1.place(x=720,y=450,anchor='center')
                button1.place(x=50,y=600,anchor='w')

        def back():
            frame1.destroy()
            self.scene_insert_record()
        button1 = tk.Button(frame1,font=('Times New Roman',25),text='Enter',command=get_insert_commit)
        button2 = tk.Button(frame1,font=('Times New Roman',25),text='Back',command=back)

        frame1.place(x=0,y=0)
        label1.place(x=220,y=75,anchor='center')
        label2.place(x=220,y=175,anchor='center')
        label3.place(x=220,y=275,anchor='center')
        entry1.place(x=820,y=75,anchor='center')
        entry2.place(x=820,y=175,anchor='center')
        entry3.place(x=820,y=275,anchor='center')
        button1.place(x=720,y=400,anchor='center')
        button2.place(x=50,y=850,anchor='w')

    def sql_insert_marks(self):
        obj = mysql.connect(host='localhost',user='tester',passwd='1234',database='students')
        cusor = obj.cursor()
        sch_no = tk.StringVar()
        marks_obtained = tk.StringVar()
        total_marks = tk.StringVar()
        grade = tk.StringVar()

        frame1 = tk.Frame(self.root,bg='#5534A5',height=self.Height,width=self.Width)
        label1 = tk.Label(frame1,text='Scholar Number',font=('Times New Roman',25),bg='#5534A5',fg='white')
        label2 = tk.Label(frame1,text='Marks Obtained',font=('Times New Roman',25),bg='#5534A5',fg='white')
        label3 = tk.Label(frame1,text='Total Marks',font=('Times New Roman',25),bg='#5534A5',fg='white')
        label4 = tk.Label(frame1,text='Grade',font=('Times New Roman',25),bg='#5534A5',fg='white')

        entry1 = tk.Entry(frame1,font=('Times New Roman',25),textvariable=sch_no)
        entry2 = tk.Entry(frame1,font=('Times New Roman',25),textvariable=marks_obtained)
        entry3 = tk.Entry(frame1,font=('Times New Roman',25),textvariable=total_marks)
        entry4 = tk.Entry(frame1,font=('Times New Roman',25),textvariable=grade)

        def get_insert_commit():
            alpha=entry1.get()
            beta=entry2.get()
            theta=entry3.get()
            gamma=entry4.get()
            try:
                cusor.execute('insert into student_marks values({},{},{},\'{}\')'.format(alpha,beta,theta,gamma))
                obj.commit()
                frame1.destroy()
                frame2 = tk.Frame(self.root,bg='#5534A5',width=self.Width,height=self.Height)
                label1 = tk.Label(frame2,bg='#5534A5',fg='red',font=('Times New Roman',25),text='Record Inserted')
                button1 = tk.Button(frame2,text='Back',bg='#6FDFDF',font=('Times New Roman',25),fg='white',command=self.sql_insert_marks)

                frame2.place(x=0,y=0)
                label1.place(x=720,y=450,anchor='center')
                button1.place(x=50,y=600,anchor='w')
            except:
                frame1.destroy()
                frame2 = tk.Frame(self.root,bg='#5534A5',width=self.Width,height=self.Height)
                label1 = tk.Label(frame2,bg='#5534A5',fg='red',font=('Times New Roman',25),text='Error: Please recheck the entered details')
                button1 = tk.Button(frame2,text='Back',bg='#6FDFDF',font=('Times New Roman',25),fg='white',command=self.sql_insert_marks)

                frame2.place(x=0,y=0)
                label1.place(x=720,y=450,anchor='center')
                button1.place(x=50,y=600,anchor='w')
        def back():
            frame1.destroy()
            self.scene_insert_record()

        button1 = tk.Button(frame1,font=('Times New Roman',25),text='Enter',command=get_insert_commit)
        button2 = tk.Button(frame1,font=('Times New Roman',25),text='Back',command=back)

        frame1.place(x=0,y=0)
        label1.place(x=220,y=75,anchor='center')
        label2.place(x=220,y=175,anchor='center')
        label3.place(x=220,y=275,anchor='center')
        label4.place(x=220,y=375,anchor='center')
        entry1.place(x=820,y=75,anchor='center')
        entry2.place(x=820,y=175,anchor='center')
        entry3.place(x=820,y=275,anchor='center')
        entry4.place(x=820,y=375,anchor='center')
        button1.place(x=720,y=775,anchor='center')
        button2.place(x=50,y=850,anchor='w')



    def sql_insert_fees(self):
        obj = mysql.connect(host='localhost',user='tester',passwd='1234',database='students')
        cusor = obj.cursor()
        sch_no = tk.StringVar()
        amount = tk.StringVar()
        status = tk.StringVar()
        due = tk.StringVar()

        fram1 = tk.Frame(self.root,bg='#5534A5',width = self.Width,height=self.Height)
        label1 = tk.Label(fram1,bg='#5534A5',text='Scholar Number',font=('Times New Roman',25))
        label2 = tk.Label(fram1,bg='#5534A5',text='Amount',font=('Times New Roman',25))
        label3 = tk.Label(fram1,bg='#5534A5',text='Status',font=('Times New Roman',25))
        label4 = tk.Label(fram1,bg='#5534A5',text='Due',font=('Times New Roman',25))
        entry1 = tk.Entry(fram1,textvariable = sch_no,font=('Times New Roman',25))
        entry2 = tk.Entry(fram1,textvariable = amount,font=('Times New Roman',25))
        entry3 = tk.Entry(fram1,textvariable = status,font=('Times New Roman',25))
        entry4 = tk.Entry(fram1,textvariable = due,font=('Times New Roman',25))

        def get_insert_commit():
            alpha = entry1.get()
            beta = entry2.get()
            theta = entry3.get()
            gamma = entry4.get()
            try:
                cusor.execute('insert into student_fees values({},{},\'{}\',{})'.format(alpha,beta,theta,gamma))
                obj.commit()
            except:
                fram1.destroy()
                frame2 = tk.Frame(self.root,bg='#5534A5',width = self.Width,height=self.Height)
                label1 = tk.Label(frame2,bg='#5534A5',fg='red',font=('Times New Roman',25),text='Error: Please recheck the entered details')
                button1 = tk.Button(frame2,text='Back',bg='#6FDFDF',font=('Times New Roman',25),fg='white',command=self.sql_insert_fees)


                frame2.place(x=0,y=0)
                label1.place(x=720,y=450,anchor='center')
                button1.place(x=50,y=600,anchor='w')
        def back():
            fram1.destroy()
            self.scene_insert_record()

        button1 = tk.Button(fram1,text='Enter Record',bg='#6FDFDF',font=('Times New Roman',25),fg='white',command=get_insert_commit)
        button2 = tk.Button(fram1,text='Back',bg='#E15FED',font=('Times New Roman',25),fg='white',command=back)

        fram1.place(x=0,y=0)
        label1.place(x=220,y=75,anchor='center')
        label2.place(x=220,y=275,anchor='center')
        label3.place(x=220,y=475,anchor='center')
        label4.place(x=220,y=675,anchor='center')
        entry1.place(x=820,y=75,anchor='center')
        entry2.place(x=820,y=275,anchor='center')
        entry3.place(x=820,y=475,anchor='center')
        entry4.place(x=820,y=675,anchor='center')
        button1.place(x=720,y=775,anchor='center')
        button2.place(x=50,y=850,anchor='w')



#---------------------------------------------- Insert Record Ends Here------------------------------------------------------------------------------------

        
#---------------------------------------------- Get Record Starts Here-------------------------------------------------------------------------------------

    def scene_get_record(self):
        menu = tk.StringVar()
        menu.set("Database")
        frame1 = tk.Frame(self.root,bg='#5534A5',height=self.Height,width=self.Width)
        schno = tk.StringVar()

        def back():
            frame1.destroy()
            self.scene1()

        label1 = tk.Label(frame1,text='Student Scholar Number',font=("Times New Roman",25),fg='white',bg='#5534A5')
        entry1 = tk.Entry(frame1,font=("Times New Roman",25),textvariable=schno)

        def database():
            ak = menu.get()
            if ak == 'Fees':
                bk = entry1.get()
                frame1.destroy()
                self.sql_get_fees(bk)
            elif ak == 'Marks':
                bk = entry1.get()
                frame1.destroy()
                self.sql_get_marks(bk)
            elif ak=='Attendance':
                bk = entry1.get()
                frame1.destroy()
                self.sql_get_attendance(bk)

        button1 = tk.Button(frame1,font=("Times New Roman",25),text="Search",bg='#6FDFDF',fg='white',command=database)
        button2 = tk.Button(frame1,font=("Times New Roman",25),text="Back",command=back,bg='#E15FED',fg='white')
        options = tk.OptionMenu(frame1,menu,"Fees","Marks","Attendance")
        options.config(font=('Times New Roman',25))




        frame1.place(x=0,y=0)
        label1.place(x=470,y=200,anchor='center')
        entry1.place(x=970,y=200,anchor='center')
        options.place(x=720,y=300,anchor='center')
        button1.place(x=720,y=400,anchor='center')
        button2.place(x=15,y=850,anchor='w')

    def sql_get_attendance(self,num):
        
        obj = mysql.connect(host='localhost',user='tester',passwd='1234',database='students')
        cursor = obj.cursor()
        cursor.execute('select * from student_attendance where sch_no = {}'.format(num))
        a = cursor.fetchall()
        checker = True

        def goback():
            frame1.destroy()
            self.scene_get_record()

        try:
            b,c,d = a[0]
        except:
            checker = False
            frame1 = tk.Frame(self.root,bg='#5534A5',height=self.Height,width=self.Width)
            label1 = tk.Label(frame1,text='Record Not Found',font=('Times New Roman',25))
            button1 = tk.Button(frame1,text='Back',font=('Times New Roman',25),command=goback)

            frame1.place(x=0,y=0)
            label1.place(x=720,y=450,anchor='center')
            button1.place(x=2,y=600,anchor='w')

        if checker:
            frame1 = tk.Frame(self.root,bg='grey',height=self.Height,width=self.Width)
            label1 = tk.Label(frame1,text='Scholar Number: {}'.format(b),font=('Times New Roman',25))
            label2 = tk.Label(frame1,text='Attendance: {}'.format(c),font=('Times New Roman',25))
            label3 = tk.Label(frame1,text='Total Days: {}'.format(d),font=('Times New Roman',25))
            button1 = tk.Button(frame1,text='Back',font=('Times New Roman',25),command=goback)


            frame1.place(x=0,y=0)
            label1.place(x=720,y=50,anchor='center')
            label2.place(x=720,y=150,anchor='center')
            label3.place(x=720,y=250,anchor='center')
            button1.place(x=50,y=800,anchor='w')





    def sql_get_marks(self,num):
        obj = mysql.connect(host='localhost',user='tester',passwd='1234',database='students')
        cursor = obj.cursor()
        cursor.execute('select * from student_marks where sch_no = {}'.format(num))
        a = cursor.fetchall()
        checker = True
        def goback():
            frame1.destroy()
            self.scene_get_record()

        try:
            b,c,d,e = a[0]

        except:
            checker = False
            frame1 = tk.Frame(self.root,bg='grey',height=self.Height,width=self.Width)
            label1 = tk.Label(frame1,text='Record Not Found',font=('Times New Roman',25))
            button1 = tk.Button(frame1,text='Back',font=('Times New Roman',25),command=goback)


            frame1.place(x=0,y=0)
            label1.place(x=720,y=450,anchor='center')
            button1.place(x=2,y=600,anchor='w')
        if checker:

            frame1 = tk.Frame(self.root,bg='grey',height=self.Height,width=self.Width)
            label1 = tk.Label(frame1,text='Scholar Number: {}'.format(b),font=('Times New Roman',25))
            label2 = tk.Label(frame1,text='Marks Obtained: {}'.format(c),font=('Times New Roman',25))
            label3 = tk.Label(frame1,text='Total Marks: {}'.format(d),font=('Times New Roman',25))
            label4 = tk.Label(frame1,text='Grade: {}'.format(e),font=('Times New Roman',25))
            button1 = tk.Button(frame1,text='Back',font=('Times New Roman',25),command=goback)



            frame1.place(x=0,y=0)
            label1.place(x=720,y=50,anchor='center')
            label2.place(x=720,y=150,anchor='center')
            label3.place(x=720,y=250,anchor='center')
            label4.place(x=720,y=350,anchor='center')
            button1.place(x=50,y=800,anchor='w')


    def sql_get_fees(self,num):
        obj = mysql.connect(host='localhost',user='tester',passwd='1234',database='students')
        cursor = obj.cursor()
        cursor.execute('select * from student_fees where sch_no = {};'.format(num))
        a = cursor.fetchall()
        checker = True
        def goback():
            frame1.destroy()
            self.scene_get_record()
        try:
            
            b,c,d,e = a[0]
            
        except:
            checker = False
            frame1 = tk.Frame(self.root,bg='grey',height=self.Height,width=self.Width)
            label1 = tk.Label(frame1,text='Record Not Found',font=('Times New Roman',25))
            button1 = tk.Button(frame1,text='Back',font=('Times New Roman',25),command=goback)

            frame1.place(x=0,y=0)
            label1.place(x=720,y=450,anchor='center')
            button1.place(x=2,y=600,anchor='w')
            


        if checker:
            frame1 = tk.Frame(self.root,height=self.Height,width=self.Width,bg='#5534A5')
            label1 = tk.Label(frame1,text='Scholar Number: {}'.format(b),font=('Times New Roman',25),bg='#5534A5',fg='white')
            label2 = tk.Label(frame1,text='Amount: {}'.format(c),font=('Times New Roman',25),bg='#5534A5',fg='white')
            label3 = tk.Label(frame1,text='Status: {}'.format(d.upper()),font=('Times New Roman',25),bg='#5534A5',fg='white')
            label4 = tk.Label(frame1,text='Amount Due: {}'.format(e),font=('Times New Roman',25),bg='#5534A5',fg='white')
            button1 = tk.Button(frame1,text='Back',font=('Times New Roman',25),command=goback)

            frame1.place(x=0,y=0)
            label1.place(x=2,y=50,anchor='w')
            label2.place(x=2,y=150,anchor='w')
            label3.place(x=2,y=250,anchor='w')
            label4.place(x=2,y=350,anchor='w')
            button1.place(x=2,y=450,anchor='w')


#---------------------------------------Get Record ends here-----------------------------------------------------------------------------------------------
#---------------------------------------Update Record Starts Here------------------------------------------------------------------------------------------

    def scene_update_record(self):
        frame1 = tk.Frame(self.root,bg='#5534A5',height=self.Height,width=self.Width)
        def delete():
            frame1.destroy()
            self.sql_delete_record()
        def update():
            frame1.destroy()
            self.sql_update_record()
        def back():
            frame1.destroy()
            self.scene1()
        button1 = tk.Button(frame1,text='Delete Record',font=('Times New Roman',25),command=delete)
        button2 = tk.Button(frame1,text='Update Record',font=('Times New Roman',25),command=update)
        button3 = tk.Button(frame1,text='Back',font=('Times New Roman',25),command=back)

        frame1.place(x=0,y=0)
        button1.place(x=720,y=350,anchor='center')
        button2.place(x=720,y=450,anchor='center')
        button3.place(x=50,y=850,anchor='w')


    def sql_delete_record(self):
        obj= mysql.connect(host='localhost',user='tester',passwd='1234',database='students')
        cursor = obj.cursor()

        


        frame1 = tk.Frame(self.root,bg='#5534A5',height=self.Height,width=self.Width)
        menu = tk.StringVar()
        sch_no = tk.StringVar()
        menu.set("Database")
        optionsmenu = tk.OptionMenu(frame1,menu,'Fees','Marks','Attendance')
        optionsmenu.configure(font=('Times New Roman',25))
        entry1 = tk.Entry(frame1,font=('Times New Roman',25),textvariable=sch_no) 

        def delete():
            bk = menu.get()
            ak = entry1.get()
            if bk == 'Fees':
                try:
                    cursor.execute('delete from student_fees where sch_no = {}'.format(ak))
                    obj.commit()
                    frame1.destroy()
                    frame2 = tk.Frame(self.root,bg='#5534A5',width = self.Width,height=self.Height)
                    label1 = tk.Label(frame2,bg='#5534A5',fg='white',font=('Times New Roman',25),text='Success: Record Deleted Successfully')
                    button1 = tk.Button(frame2,text='Back',bg='#6FDFDF',font=('Times New Roman',25),fg='white',command=self.sql_delete_record)
                    frame2.place(x=0,y=0)
                    label1.place(x=720,y=450,anchor='center')
                    button1.place(x=50,y=600,anchor='w')
                except: 
                    frame1.destroy()
                    frame2 = tk.Frame(self.root,bg='#5534A5',width = self.Width,height=self.Height)
                    label1 = tk.Label(frame2,bg='#5534A5',fg='red',font=('Times New Roman',25),text='Error: Please recheck the entered details')
                    button1 = tk.Button(frame2,text='Back',bg='#6FDFDF',font=('Times New Roman',25),fg='white',command=self.sql_delete_record)


                    frame2.place(x=0,y=0)
                    label1.place(x=720,y=450,anchor='center')
                    button1.place(x=50,y=600,anchor='w')

            elif bk == 'Marks':
                try:
                    cursor.execute('delete from student_marks where sch_no = {}'.format(ak))
                    obj.commit()
                    frame1.destroy()
                    frame2 = tk.Frame(self.root,bg='#5534A5',width = self.Width,height=self.Height)
                    label1 = tk.Label(frame2,bg='#5534A5',fg='white',font=('Times New Roman',25),text='Success: Record Deleted Successfully')
                    button1 = tk.Button(frame2,text='Back',bg='#6FDFDF',font=('Times New Roman',25),fg='white',command=self.sql_delete_record)
                    frame2.place(x=0,y=0)
                    label1.place(x=720,y=450,anchor='center')
                    button1.place(x=50,y=600,anchor='w')
                except: 
                    frame1.destroy()
                    frame2 = tk.Frame(self.root,bg='#5534A5',width = self.Width,height=self.Height)
                    label1 = tk.Label(frame2,bg='#5534A5',fg='red',font=('Times New Roman',25),text='Error: Please recheck the entered details')
                    button1 = tk.Button(frame2,text='Back',bg='#6FDFDF',font=('Times New Roman',25),fg='white',command=self.sql_delete_record)


                    frame2.place(x=0,y=0)
                    label1.place(x=720,y=450,anchor='center')
                    button1.place(x=50,y=600,anchor='w')

            elif bk == 'Attendance':
                try:
                    cursor.execute('delete from student_attendance where sch_no = {}'.format(ak))
                    obj.commit()
                    frame1.destroy()
                    frame2 = tk.Frame(self.root,bg='#5534A5',width = self.Width,height=self.Height)
                    label1 = tk.Label(frame2,bg='#5534A5',fg='white',font=('Times New Roman',25),text='Success: Record Deleted Successfully')
                    button1 = tk.Button(frame2,text='Back',bg='#6FDFDF',font=('Times New Roman',25),fg='white',command=self.sql_delete_record)
                    frame2.place(x=0,y=0)
                    label1.place(x=720,y=450,anchor='center')
                    button1.place(x=50,y=600,anchor='w')

                except: 
                    frame1.destroy()
                    frame2 = tk.Frame(self.root,bg='#5534A5',width = self.Width,height=self.Height)
                    label1 = tk.Label(frame2,bg='#5534A5',fg='red',font=('Times New Roman',25),text='Error: Please recheck the entered details')
                    button1 = tk.Button(frame2,text='Back',bg='#6FDFDF',font=('Times New Roman',25),fg='white',command=self.sql_delete_record)


                    frame2.place(x=0,y=0)
                    label1.place(x=720,y=450,anchor='center')
                    button1.place(x=50,y=600,anchor='w')

        button1 = tk.Button(self.root,text='Delete',command=delete,font=('Times New Roman',25))
        button2 = tk.Button(self.root,text='Back',font=('Times New Roman',25),command=self.scene_update_record)

        frame1.place(x=0,y=0)
        entry1.place(x=720,y=350,anchor='center')
        optionsmenu.place(x=720,y=450,anchor='center')
        button1.place(x=720,y=550,anchor='center')
        button2.place(x=50,y=600,anchor='w')

    def sql_update_record(self):    
        frame1 = tk.Frame(self.root,bg='#5534A5',height=self.Height,width=self.Width)
        menu = tk.StringVar()
        menu.set("Database")
        optionsmenu = tk.OptionMenu(frame1,menu,'Fees','Marks','Attendance')
        optionsmenu.configure(font=('Times New Roman',25))

        def optionWindow():
            bk = menu.get()
            if bk=='Fees':
                frame1.destroy()
                sql_update_fees()
            elif bk=='Attendance':
                frame1.destroy()
                sql_update_attendance()
            elif bk=='Marks':
                frame1.destroy()
                sql_update_marks()
        label1 = tk.Label(frame1,text='Update Record',font=('Times New Roman',25),bg='#5534A5',fg='white')
        button1 = tk.Button(frame1,text='Go',font=('Times New Roman',25),command=optionWindow)


        frame1.place(x=0,y=0)
        label1.place(x=720,y=10,anchor='center')
        optionsmenu.place(x=220,y=450)
        button1.place(x=320,y=450)





    def sql_update_attendance(self):
        obj= mysql.connect(host='localhost',user='tester',passwd='1234',database='students')
        cursor = obj.cursor()
        frame1 = tk.Frame(self.root,bg='#5534A5',height=self.Height,width=self.Width)
        sch_no = tk.StringVar()
        attend = tk.StringVar()

        label1 = tk.Label(frame1,text='Scholar Number',font=('Times New Roman',25),bg='#5534A5')
        label2 = tk.Label(frame1,text='Attendance',font=('Times New Roman',25),bg='#5534A5')
        entry1 = tk.Entry(frame1,textvariable=sch_no,font=('Times New Roman',25))
        entry2 = tk.Entry(frame1,textvariable=attend,font=('Times New Roman',25))
        def change():
            alpha = entry1.get()
            beta = entry2.get()

            try:
                cursor.execute('update student_attendance set attendance={} where sch_no = {}'.format(beta,alpha))
                if beta == 'A':
                    cursor.execute('update student_attendance set total_days=total_days-1 where sch_no = {}'.format(alpha))
                elif beta == 'P': 
                    cursour.execute('update student_attendance set total_days=total_days+1 where sch_no = {}'.format(alpha))
                obj.commit()
            except:
                frame1.destroy()
                frame2 = tk.Frame(self.root,bg='#5534A5',height=self.Height,width=self.Width)
                def goback():
                    frame2.destroy()
                    self.sql_update_attendance()
                label1 = tk.Label(frame2,bg='#5534A5',font=('Times New Roman',25),text='Error: Please Checked Entered Details')
                button1 = tk.Button(frame2,text='Back',command=goback)
        
        def goback():
            frame1.destroy()
            self.scene_update_record()
        
        button1 = tk.Button(frame1,text='Enter',font=('Times New Roman'),command=change)
        button2 = tk.Button(frame1,text='back',command=goback)

        frame1.place(x=0,y=0)
        label3.place(x=720,y=30)
        label1.place(x=220,y=175)
        label2.place(x=220,y=275)
        entry1.place()

        # Lmao why did you do this
    
    '''
    def sql_update_attendance(self):
        obj= mysql.connect(host='localhost',user='tester',passwd='1234',database='students')
        cursor = obj.cursor()
        frame1 = tk.Frame(self.root,bg='#5534A5',height=self.Height,width=self.Width)
        sch_no = tk.StringVar()
        field = tk.StringVar()
        field.set('Field')
        optionsmenu = tk.OptionMenu(frame1, field, "Attendance","Total Days")
        entry1 = tk.Entry(frame1,font=('Times New Roman',25),textvariable=sch_no)

        def go():
            ak = optionsmenu.get()
            bk = entry1.get()
            if ak == 'Attendance':
                frame1.destroy()
                self.sql_update_attendance_attendance(bk)
            elif ak == 'Total Days':
                frame1.destroy()
                self.sql_update_attendance_total_days(bk)

        def goback():
            frame1.destroy()
            self.scene_update_record()
        label1 = tk.Label(frame1,text='Scholar No',font=('Times New Roman',25),bg='#5534A5',fg='white')
        button1 = tk.Button(frame1,font=('Times New Roman',25),command=go)
        button2 = tk.Buttno(frame1,font=("Times New Roman",25),command=goback)


        frame1.place(x=0,y=0)
        label1.place(x=470,y=200)
        entry1.place(x=970,y=200)
        optionsmenu.place(x=720,y=300)
        button1.place(x=720,y=400,anchor='center')
        button2.place(x=15,y=850,anchor='w')


    def sql_update_attendance_attendance(self,schno):
        frame1 = tk.Frame(self.root,bg='#5534A5',height=self.Height,width=self.Width)
    
    def sql_update_attendance_total_days(self,schno):
        frame1 = tk.Frame(self.root,bg='#5534A5',height=self.Height,width=self.Width)
'''
      
        
        

         
  

        






