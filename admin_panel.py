from tkinter import *
from tkinter.messagebox import showerror,showinfo,showwarning
import pymysql as pq
import random
from admin_panel_menu_window import *
mydb=pq.connect(
    host="localhost",
    user="root",
    database="Train_management",
    password=""

)
cursor = mydb.cursor()

class admin_panel_class:
    def __init__(self):
        pass




    def admin_panel(self):
        admin_main = Toplevel()
        admin_main.title("VERIFY CREDENTIALS")
        admin_main.iconbitmap("admin_panel ico.ico")
        admin_main.geometry("522x284")
        admin_main.resizable(False,False)

        bg_img = PhotoImage(file=r"C:\Users\Dell\Downloads\review.png")
        Label(admin_main,image=bg_img).place(x=0,y=0,width=522,height=284)
        y = StringVar(value="")
        # verify credentials
        def verify():
            if E1.get() == "Himanshu" and E2.get() == "12345" and E3.get() == y.get():
                showinfo(title="login successful",message="you can continue")
                admin_panel_menu_window_class().admin_menus()

            else:
                showerror(title="something wrong",message="please enter correct credentials")

        #LABELS
        l1 = Label(admin_main,text="USER NAME :",bg="#EDDBDB",font="calibri 20 bold",cursor="no")
        l1.place(x=69,y=44,width=151,height=21)
        l2 = Label(admin_main,text="PASSWORD :",bg="#EDDBDB",font="calibri 20 bold",cursor="no")
        l2.place(x=69,y=90,width=151,height=21)
        l3 = Label(admin_main,textvariable=y,bg="#EDDBDB",cursor="no")
        l3.place(x=314,y=126,width=128,height=23)
        l4 = Label(admin_main,text="captcha",bg="#EDDBDB")
        l4.place(x=220,y=130,width=59,height=19)
        # For captcha

        captcha_generation = ["123@iu", "89bty","yu8900","er679","uio86","ab4&*"]
        y.set(random.choice(captcha_generation))

        # Entry Widgets

        E1 = Entry(admin_main,bg="#D9D9D9",font="calibri 10 bold")
        E1.place(x=285,y=40,width=187,height=29)
        E2 = Entry(admin_main,bg="#D9D9D9",font="calibri 10 bold")
        E2.place(x=285,y=86,width=187,height=29)
        E3 = Entry(admin_main,bg="#D9D9D9",font="calibri 10 bold")
        E3.place(x=306,y=160,width=146,height=26)

        # Button

        admin_Button = Button(admin_main,text="VERIFY",bg="#EDDBDB",cursor="hand2"
                              ,font="calibri 20 bold",command=verify)
        admin_Button.place(x=372,y=231,width=125,height=28)






        admin_main.mainloop()






