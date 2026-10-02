# Entry Widget & Grid Layout.

from tkinter import *

def getvals():
    print(f"Value of user name is: {uservalue.get()}")
    print(f"Value of password is: {passvalue.get()}")
#     get() function inn StringVar kai andar input ki gyi value lakar daita hai.

root = Tk()
root.geometry("555x455")

# Grid Layout

user = Label(root, text="Username")
password = Label(root, text="Password")
user.grid()     # row=0, column=0 is a default value.
password.grid(row=1)

# Entry Widgets - ek aise widget hai tk mai jismai app values input kar saktai ho.
# but before making the EW, we have to make the string variables.

# Variable classes in tkinter.
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getvals).grid()

root.mainloop()


# Task - make a form for a dance class and print details in console.
# and also values inputted will be get stored in a file.
