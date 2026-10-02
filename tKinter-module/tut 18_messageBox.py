# Message box in tkinter.
# Dialogue Boxes.

from tkinter import *
import tkinter.messagebox as tmsg

def myfunc():
    print("Learning a Menu widget in depth")

def help():
    print("I will help you")
    # Syntax for showinfo is (title, message).
    tmsg.showinfo("Help", "vaibhav will help with your problem using this GUI")
#     return value of showinfo
#     a = tmsg.showinfo("Help", "vaibhav will help with your problem using this GUI")
#     print(a)

def rate():
    # syntax - (title, message, options)
    # tmsg.askquestion("Experience Rating", "Was your Experience Good with this GUI ?")
#     return value of askquestion
    value = tmsg.askquestion("Experience Rating", "Was your Experience Good with this GUI ?")
    print(value)    # this return value OF askquestion iS of 'USE' for us. (output - yes, no)
    if value == "yes":
        msg = "Great. Rate us on appstore please"
    else:
        msg = "Tell us what went wrong, We will fix it"
    tmsg.showinfo("Experience", msg)

def nishita():
    ans = tmsg.askretrycancel("Nishita sai dosti kar lo", "Sorry Nishita nhi baniagii app ki dost")
#     askretrycancel returns either True or False.
    if ans:
        print("Retry karnai par bhi kuch nhi hoga")
    else:
        print("Bahut badiya bhai cancel kar diya warna pittee ")


root = Tk()
root.geometry("500x300")
root.title("Pycharm Projects")

# Creating a Drop-down menu.
mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New Project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()      # will make a horizontal line.
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)


m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Delete", command=myfunc)
mainmenu.add_cascade(label="Edit", menu=m2)
root.config(menu=mainmenu)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate Us", command=rate)
m3.add_command(label="Be Friend Nishita", command=nishita)
mainmenu.add_cascade(label="Help", menu=m3)
root.config(menu=mainmenu)

m4 = Menu(mainmenu, tearoff=0)
m4.add_command(label="Exit GUI", command=quit)
mainmenu.add_cascade(label="Exit", menu=m4)
root.config(menu=mainmenu)

root.mainloop()