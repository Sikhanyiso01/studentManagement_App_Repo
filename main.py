import tkinter as tk
from db import  Database
class Login():
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management Application")
        self.root.geometry("350x250")
        self.create_widgets()


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

        self.loginBtn = tk.Button(self.root, text="Log in", width=15, padx=10)
        self.loginBtn.grid(column=2, row=3)


if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
