import pymysql as pq
import tkinter as tk
from tkinter import ttk
train_db = pq.connect(
    host="localhost",
    user="root",
    password="",
    database="train_management"
)

cu = train_db.cursor()

class all_train_details_class:
    def __init__(self):
        query = ('''CREATE TABLE if not exists Train_Details
        (train_id int,
        train_name varchar(50),
        source_station varchar(50),
        destination varchar(50),
        seats_available int,
        remaining_seats int)
        ''')
        cu.execute(query)
        train_db.commit()

    def fetch_data(self):
        connection = pq.connect(
            host="localhost",
            user="root",
            password="",
            database="train_management"
        )

        cursor = connection.cursor()


        query = "SELECT * FROM train_details"
        cursor.execute(query)
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)

        connection.close()

    def showing_window(self):
        root = tk.Tk()
        root.title("ALL REGISTERED USERS")


        self.tree = ttk.Treeview(root, columns=("train_id", "train_name", "source_station","destination","seats_available","remaining_seats"))
        self.tree.heading("train_id", text="TRAIN ID")
        self.tree.heading("train_name", text="TRAIN NAME")
        self.tree.heading("source_station", text="SOURCE STATION")
        self.tree.heading("destination", text="DESTINATION")
        self.tree.heading("seats_available", text="AVAILABLE SEATS")
        self.tree.heading("remaining_seats", text="REMAINING SEATS")


        fetch_button = tk.Button(root, text="Fetch Data", command=self.fetch_data)


        self.tree.pack(pady=10)
        fetch_button.pack(pady=10)


        root.mainloop()




