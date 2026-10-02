# Frames in tkinter.

from tkinter import *
root = Tk()
root.geometry("555x455")

f1 = Frame(root, bg="grey", borderwidth=4, relief=SUNKEN)   # mai iss frame ko root kai andar pack (daalna) karna chahta hu.
f1.pack(side=LEFT, fill=Y)

f2 = Frame(root, borderwidth=8, relief=SUNKEN, bg="grey")
f2.pack(side=TOP, fill=X)

l = Label(f1, text="Pycharm Projects Tkinter GUI")   # mai iss label ko f1 frame kai andar daalna (pack karna) chahata hu.
l.pack(pady=142)

l2 = Label(f2, text="Welcome to Pycharm Community Edition 2025", font="Helvetica 11 bold", fg="blue", pady=8)
l2.pack(pady=8)

root.mainloop()