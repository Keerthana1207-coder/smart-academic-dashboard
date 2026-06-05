from tkinter import *
import dashboard_gui

def login():

    if username.get() == "admin" and password.get() == "1234":

        login_window.destroy()

        dashboard_gui.open_dashboard()

    else:

        result.config(
            text="Invalid Username or Password",
            fg="red"
        )

login_window = Tk()

login_window.title("Login")
login_window.geometry("350x250")

Label(
    login_window,
    text="Study Planner Login",
    font=("Arial",16,"bold")
).pack(pady=20)

username = Entry(login_window)
username.pack(pady=10)

password = Entry(login_window, show="*")
password.pack(pady=10)

Button(
    login_window,
    text="Login",
    command=login
).pack(pady=10)

result = Label(login_window, text="")
result.pack()

login_window.mainloop()
