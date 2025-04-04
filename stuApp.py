import tkinter as tk
from tkinter import messagebox
import db
from db import  Database
db = Database("studentDB.db")

class studentApp:
    def __init__(self, app):
        self.app = app
        self.app.title("Student Management App")
        self.app.geometry("750x750")
        self.addwidgets()

    def addwidgets(self):
        nametxt = tk.StringVar()
        nameLabel  =  tk.Label(self.app, text="Name", pady=20, padx=10, font=("Bold", 14))
        nameLabel.grid(column=0, row=0)
        name_Entry= tk.Entry(self.app, textvariable=nametxt)
        name_Entry.grid(column=1, row=0)

        surnametxt = tk.StringVar()
        surnameLabel = tk.Label(self.app, text="Surname", pady=20, padx=10, font=("Bold", 14))
        surnameLabel.grid(column=0, row=1)
        surname_Entry = tk.Entry(self.app, textvariable=surnametxt)
        surname_Entry.grid(column=1, row=1)

        Prognametxt = tk.StringVar()
        PrognameLabel = tk.Label(self.app, text="Program", pady=20, padx=10, font=("Bold", 14))
        PrognameLabel.grid(column=0, row=2)
        Progname_Entry = tk.Entry(self.app, textvariable=Prognametxt)
        Progname_Entry.grid(column=1, row=2)

        gendertxt = tk.StringVar()
        genderLabel = tk.Label(self.app, text="Gender", pady=20, padx=10, font=("Bold", 14))
        genderLabel.grid(column=2, row=0)
        gender_Entry = tk.Entry(self.app, textvariable=gendertxt)
        gender_Entry.grid(column=3, row=0)

        phonetxt = tk.StringVar()
        phoneLabel = tk.Label(self.app, text="Phone", pady=20, padx=10, font=("Bold", 14))
        phoneLabel.grid(column=2, row=1)
        phone_Entry = tk.Entry(self.app, textvariable=phonetxt)
        phone_Entry.grid(column=3, row=1)

        insertBtn = tk.Button(self.app, text="Insert", width=15)
        insertBtn.grid(column=5, row=0)

        Updatebtn = tk.Button(self.app, text="Update", width=15)
        Updatebtn.grid(column=5, row=1)

        deletebtn = tk.Button(self.app, text="Delete", width=15)
        deletebtn.grid(column=8, row=0)

        Searchbtn = tk.Button(self.app, text="Search", width=15)
        Searchbtn.grid(column=8, row=1)

        listview = tk.Listbox(self.app,height=30, width=80, border=5 )
        listview.grid(column=1, columnspan= 8, row=4 )






app = tk.Tk()
studentApp(app)
app.mainloop()
