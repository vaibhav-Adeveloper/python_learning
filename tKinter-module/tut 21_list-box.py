# ListBox in tkinter.

# ListBox ek aise widget hai jo display karti hai alternatives ki list (list of alternatives).
# maan lijia app ko cheezai aise display karani hai, unka jo color hai, font hai wo same rhai or wo bilkul ek hi group mai dekhai
# aur ek list ho.

from tkinter import *

i = 1
def additem():
    global i
    lbx.insert(ACTIVE, f"{i}th Item of List Box")
    # ACTIVE - means jo menu maine select kar rakha uskai pehlai add ho jaiga.
    i += 1 

root = Tk()
root.geometry("500x300")
root.title("List Box in tkinter")

lbx = Listbox(root)     # will create a empty list box.
lbx.pack()

# inserting element in listbox.
lbx.insert(END, "First item of List Box")

Button(root, text="Add Item", command=additem).pack()

root.mainloop()