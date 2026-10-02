# Packing buttons in tkinter.

from tkinter import *
root = Tk()
root.geometry("555x455")

def hello():
    print("Hello Tkinter Buttons.")

def name():
    print("Name is vaibhav.")

f1 = Frame(root, bg="grey", borderwidth=5, relief=SUNKEN)   # mai iss frame ko root kai andar pack (daalna) karna chahta hu.
f1.pack(side=LEFT, anchor="nw")

b1 = Button(f1, fg="red", text="Print Now", command=hello)
b1.pack(side=LEFT, padx=20)

b1 = Button(f1, fg="red", text="Tell me Name now", command=name)
b1.pack(side=LEFT, padx=20)

b1 = Button(f1, fg="red", text="Print Now")
b1.pack(side=LEFT, padx=20)

b1 = Button(f1, fg="red", text="Print Now")
b1.pack(side=LEFT, padx=20)

# l = Label(f1, text="Pycharm Projects Tkinter GUI")   # mai iss label ko f1 frame kai andar daalna (pack karna) chahata hu.
# l.pack(pady=142)

root.mainloop()