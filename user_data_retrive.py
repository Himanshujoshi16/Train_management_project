import tkinter as tk
from tkinter import ttk
import mysql.connector

class fetching_data_class:
    def __init__(self):
        pass

    def fetch_data(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="train_management"
        )

        cursor = connection.cursor()


        query = "SELECT * FROM user_data"
        cursor.execute(query)
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)

        connection.close()

    def showing_window(self):
        root = tk.Tk()
        root.title("ALL REGISTERED USERS")


        self.tree = ttk.Treeview(root, columns=("user_id", "user_name", "user_password"))
        self.tree.heading("user_id", text="ID")
        self.tree.heading("user_name", text="USER NAME")
        self.tree.heading("user_password", text="USER PASSWORD")


        fetch_button = tk.Button(root, text="Fetch Data", command=self.fetch_data)


        self.tree.pack(pady=10)
        fetch_button.pack(pady=10)


        root.mainloop()