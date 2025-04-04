import tkinter as tk
from tkinter import messagebox

import db
from db import  Database
db = Database("studentDB.db")
class Login():
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management Application")
        self.root.geometry("350x250")
        self.create_widgets()

    def verify(self):
        username = self.usernameTxt.get()
        password = self.password.get()

        if db.validate( username ,password):
            messagebox.showinfo("info", "Successfully Logged in")
            self.root.destroy()
        else:
            messagebox.showerror("error", "The user does not exists")

    def registering(self):
        username = self.usernameTxt.get()
        password = self.password.get()
        if db.register(username, password):
            messagebox.showinfo("Success", "User registered successfully!")
        else:
            messagebox.showerror("Error", "Username already exists!")

    def create_widgets(self):
        self.usernameTxt = tk.StringVar()
        self.usernameLbl = tk.Label(
            self.root, text="Username", pady=20, padx=10, font=("bold", 14))
        self.usernameLbl.grid(column=0, row=0, sticky="ew")
        self.username_Entry = tk.Entry(self.root, textvariable=self.usernameTxt)
        self.username_Entry.grid(column=2, row=0)

        self.password = tk.StringVar()
        self.passwordLbl = tk.Label(
            self.root, text="Password", padx=10, pady=10 ,font=("bold", 14))
        self.passwordLbl.grid(column=0, row=1, sticky="ew")
        self.password_Entry = tk.Entry(self.root, textvariable=self.password)
        self.password_Entry.grid(column=2, row=1)

        self.loginBtn = tk.Button(self.root, text="Log in", width=15, padx=10, command=self.verify)
        self.loginBtn.grid(column=2, row=3)

        self.SignInBtn = tk.Button(self.root, text="Sign Up", width=15, padx=10, command=self.registering)
        self.SignInBtn.grid(column=2, row=4)


if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
