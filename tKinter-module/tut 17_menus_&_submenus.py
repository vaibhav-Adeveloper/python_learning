# Menu and Sub-menu.

from tkinter import *

def myfunc():
    print("Learning a Menu widget in depth")


root = Tk()
root.geometry("500x300")
root.title("Pycharm Projects")

# Creating Menu widget - use below to create a non-dropdown menu.
mymenu = Menu(root)
# adding command to menu
mymenu.add_command(label="File", command=myfunc)
mymenu.add_command(label="Exit", command=quit)
# placing menu in GUI window
# root.config(menu=mymenu)

# Creating a Drop-down menu.
mainmenu = Menu(root)    # creating menu inside root (created a menu bar) - created a horizontal bar.
m1 = Menu(mainmenu, tearoff=0)      # creating menu inside yourmenubar.
m1.add_command(label="New Project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()      # will make a horizontal line.
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)

mainmenu.add_cascade(label="File", menu=m1)
# add_cascade - mainmenu mai (yani jo horizontal bar hai) uskai andar daal doo m1 menu ko.

# configuring
root.config(menu=mainmenu)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Delete", command=myfunc)
mainmenu.add_cascade(label="Edit", menu=m2)
root.config(menu=mainmenu)

mainmenu.add_command(label="Exit", command=quit)
root.config(menu=mainmenu)

root.mainloop()