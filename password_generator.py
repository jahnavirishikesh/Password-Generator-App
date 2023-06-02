from tkinter import *
import pyperclip
import random

from jinja2.compiler import generate

root = Tk()
# making the application window
root.geometry("400x400")

# declaring a variable of string type - will store the generated password, a variable of int type will store password length
pwd_str = StringVar()
pwd_len = IntVar()
pwd_len.set(0)

def generate_pwd():
    #storing keys in a list to generate password
    pass1 = s1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    password = ""
    for x in range(pwd_len.get()):
        password = password + random.choice(pass1)

    pwd_str.set(password)


def copy_to_clipboard():
    random_pwd = pwd_str.get()
    pyperclip.copy(random_pwd)

Label(root, text="Password Generator Application", font="calibri 20 bold").pack()
Label(root, text="Enter password length").pack(pady=3)

Entry(root, textvariable=pwd_len).pack(pady=3)

Button(root, text="Generate Password", command=generate_pwd).pack(pady=7)

Entry(root, textvariable=pwd_str).pack(pady=3)

Button(root, text="copy to clipboard", activebackground='Red', command=copy_to_clipboard).pack()

root.mainloop()

