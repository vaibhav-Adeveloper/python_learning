# Calculator using Tkinter.

# To replicate full frame and buttons inside it.
# replicate it using For loop and list.
# OR
# make a function.
# make a class.


from tkinter import *

def click(eventObj):
    print("clicked")
    text = eventObj.widget.cget("text")
#   eventObj.widget -
#   cget() -


root = Tk()
root.geometry("644x700")
root.title("Calculator GUI TK()")
root.wm_iconbitmap("Windows_Notepad_icon.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="grey")
b = Button(f, text="9", font="lucida 28 bold", padx=20, pady=10)
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="8", font="lucida 28 bold", padx=20, pady=10)
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="7", font="lucida 28 bold", padx=20, pady=10)
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()