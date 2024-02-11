from tkinter import *
import pymysql as pq
mydb = pq.connect(host="localhost",user="root",password="")
mycursor = mydb.cursor()

mycursor.execute("create database if not exists Train_management")
# importing whole panels

from admin_panel import *
from registration_window import *
from user_login_panel import *
from all_trains_details import *

def admin_panel_info():
    admin_panel_class().admin_panel()

def registraion_window_info():
    registration_window_class().registration_window()

def user_login_panel():
    user_panel_class().user_panel_login_window()

def train_data_fetching():
    all_train_details_class().showing_window()



win1 = Tk()
win1.geometry("850x550")
win1.title("JOSHI E-RESERVATION ")
win1.iconbitmap("main_windowicon.ico")
win1.resizable(False,False)

img1=PhotoImage(file="main_windowbg.png")
Label(win1,image=img1).place(x=0,y=0,width=850,height=550)
# ALL MAIN WINDOW BUTTONS

# 1st Button
user_login_Button = Button(text="USER LOGIN",bg="#6F88AC",font="calibri 10 bold",cursor="hand2",command=user_login_panel)
user_login_Button.place(x=70,y=82,width=265,height=61)

# 2nd Button
train_search_button = Button(text="SEARCH TRAINS BETWEEN STATIONS",bg="#6F88AC",font="calibri 10 bold",cursor="hand2")
train_search_button.place(x=466,y=82,width=265,height=61)

# 3rd Button
admin_button = Button(text="ADMIN PANEL",bg="#6F88AC",font="calibri 10 bold",cursor="hand2",command=admin_panel_info)
admin_button.place(x=70,y=244,width=265,height=61)

# 4th Button
all_available_trains = Button(text="SHOW ALL AVAILABLE TRAINS",bg="#6F88AC",font="Calibri 10 bold",cursor="hand2",command=train_data_fetching)
all_available_trains.place(x=466,y=244,width=265,height=61)

# Label

l1 = Label(text="IF NOT REGISTERED PLEASE CLICK HERE",bg="#6F88AC",font="Calibri 15 bold",cursor="no")
l1.place(x=33,y=422,width=375,height=27)
l2 = Label(text="PHONE NO:123456",bg="#6F88AC",font="Calibri 10 bold",cursor="no")
l2.place(x=0,y=0,width=180,height=26)
l3 = Label(text="MAIL ID: JOSHI@GMAIL.COM",bg="#6F88AC",font="Calibri 10 bold",cursor="no")
l3.place(x=530,y=0,width=250,height=26)

# 5th Button
register_button = Button(text="CLICK HERE",bg="#6F88AC",font="Calibri 15 bold",cursor="hand2",command=registraion_window_info)
register_button.place(x=153,y=467,width=101,height=20)

# 6th Button
exit_button = Button(text="<-EXIT->",bg="#6F88AC",font="Calibri 15 bold",cursor="hand2",command=lambda:win1.destroy())
exit_button.place(x=586,y=449,width=129,height=61)



win1.mainloop()