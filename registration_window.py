from tkinter import *
from tkinter.messagebox import showerror,showinfo,showwarning
import pymysql as pq
conn = pq.connect(
    host = "localhost",
    user = "root",
    password ="",
    database = "train_management"
)
cursor = conn.cursor()

class registration_window_class:
    def __init__(self):
        query = '''create table if not exists  user_data(
        user_id int auto_increment primary key ,
        user_name varchar(50),
        password varchar(30),
        current_date_time timestamp)'''
        cursor.execute(query)

    def insert_data(self):

        self.user_name = self.user_name.get()

        self.user_password = self.user_password.get()

        self.user_data = [self.user_name,self.user_password]
        if self.user_data != "" and self.user_password != "":
            query = '''insert into user_data(user_name,password)
            values(%s,%s)'''
            cursor.execute(query,self.user_data)
            conn.commit()
            showinfo(title="data inserted",message=f"you are successfully registered "
                                                   f"your user name is {self.user_name} and your password is {self.user_password}")

        else:
            showerror(title="insufficient data",message="please fill all mandatory fields")







    def registration_window(self):
        reg_w = Toplevel()
        reg_w.title("REGISTRATION WINDOW")
        reg_w.geometry("400x222")
        reg_w.resizable(False,False)
        reg_w.iconbitmap("registration_window.ico")

        # LABELS

        bg_img = PhotoImage(file="rg_bgimage.png")
        l1 = Label(reg_w,image=bg_img)
        l1.place(x=0,y=0,width=400,height=222)
        user_label = Label(reg_w,text="USER NAME* :",bg="#9B9F9D",cursor="no",font="calibri 10 bold ")
        user_label.place(x=19,y=49,width=98,height=19)
        user_label = Label(reg_w,text="PASSWORD* :",bg="#9B9F9D",cursor="no",font="calibri 10 bold ")
        user_label.place(x=19,y=118,width=98,height=19)
        # ENTRY BOXES

        self.user_name = Entry(reg_w,bg="#9B9F9D",font="calibri 15 bold")
        self.user_name.place(x=180,y=32,width=173,height=45)

        self.user_password = Entry(reg_w,bg="#9B9F9D",font="calibri 15 bold")
        self.user_password.place(x=180,y=102,width=173,height=45)

        # Button

        self.submit_button = Button(reg_w,text="Submit",font="calibri 10 bold",bg="#9B9F9D",cursor="hand2",command=self.insert_data)
        self.submit_button.place(x=252,y=178,width=111,height=31)

        reg_w.mainloop()