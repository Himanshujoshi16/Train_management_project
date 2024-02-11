from tkinter import *
from tkinter.messagebox import showerror,showinfo,showwarning
from user_data_retrive import *
from all_trains_details import *
def user_data_fetching():
    fetching_data_class().showing_window()

def train_data_fetching():
    all_train_details_class().showing_window()

class admin_panel_menu_window_class:
    def __init__(self):
        pass

    def admin_menus(self):

        admin_menu_window = Toplevel()
        admin_menu_window.geometry("528x320")
        admin_menu_window.title("MENU WINDOW")
        admin_menu_window.iconbitmap("admin_panel ico.ico")
        admin_menu_window.resizable(False,False)
        bg_img = PhotoImage(file="admin_menu_window.png")
        l1 = Label(admin_menu_window,image=bg_img,cursor="no")
        l1.place(x=0,y=0,width=528,height=320)

        #Buttons

        b1 = Button(admin_menu_window,text="SHOW ALL BOOKINGS",bg="#988080",cursor="hand2")
        b1.place(x=38,y=46,width=188,height=79)
        b2 = Button(admin_menu_window,text="SHOW ALL TRAINS",bg="#988080",cursor="hand2",command=train_data_fetching)
        b2.place(x=296,y=46,width=188,height=79)
        b3 = Button(admin_menu_window,text="SHOW ALL REGISTERED USERS",bg="#988080",cursor="hand2",command=user_data_fetching)
        b3.place(x=38,y=190,width=188,height=79)
        b4 = Button(admin_menu_window,text="ADD A TRAIN",bg="#988080",cursor="hand2")
        b4.place(x=296,y=190,width=188,height=79)


        admin_menu_window.mainloop()

