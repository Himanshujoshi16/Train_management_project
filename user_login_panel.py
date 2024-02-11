import pymysql as pq
from tkinter import *
from tkinter.messagebox import showerror,showinfo,showwarning
conn = pq.connect(
    host="localhost",
    user="root",
    password="",
    database="train_management"
)
cursor = conn.cursor()

class user_panel_class:
    def __init__(self):
        pass

    def verify(self,name,password):
        if name=="" or password == "":
            showerror(text="invalid input",message="please fill all mandatory field")

        else:
            query = "select * from user_data where user_name=%s and password=%s"
            cursor.execute(query,(name,password))
            result = cursor.fetchall()
            print(result)
            if result:
             showinfo(title="login successful",message="you can continue")

            else:
                showerror(title="not exist", message="helo world")



    def login(self):
        name = self.user_name.get()
        password = self.user_password.get()
        self.verify(name,password)


    def user_panel_login_window(self):
        ul_window = Toplevel()
        ul_window.title("USER_LOGIN_WINDOW")
        ul_window.geometry("400x222")
        ul_window.resizable(False, False)
        ul_window.iconbitmap("user_login.ico")
        # LABELS
        bg_img = PhotoImage(file="user_login bg.png")
        l1 = Label(ul_window, image=bg_img)
        l1.place(x=0, y=0, width=400, height=222)
        user_label = Label(ul_window, text="USER NAME* :", bg="#9B9F9D", cursor="no", font="calibri 10 bold ")
        user_label.place(x=19, y=49, width=98, height=19)
        user_label = Label(ul_window, text="PASSWORD* :", bg="#9B9F9D", cursor="no", font="calibri 10 bold ")
        user_label.place(x=19, y=118, width=98, height=19)
        # ENTRY BOXES

        self.user_name = Entry(ul_window, bg="#9B9F9D", font="calibri 15 bold")
        self.user_name.place(x=180, y=32, width=173, height=45)


        self.user_password = Entry(ul_window, bg="#9B9F9D", font="calibri 15 bold")
        self.user_password.place(x=180, y=102, width=173, height=45)

        # Button
        self.submit_button = Button(ul_window, text="Submit", font="calibri 10 bold", bg="#9B9F9D", cursor="hand2",
                                    command=self.login)
        self.submit_button.place(x=252, y=178, width=111, height=31)

        ul_window.mainloop()

