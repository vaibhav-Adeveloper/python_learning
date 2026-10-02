# Creating radio buttons in tkinter.

from tkinter import *
import tkinter.messagebox as tmsg

def order():
    tmsg.showinfo("Order Received!", f"We have received your {var.get()} order. It will get deliverd in 2 minutes")

root = Tk()
root.geometry("500x300")
root.title("Radio buttons in tkinter")

# var = IntVar()

Label(root, text="What would you like to eat ?", font="lucida 15 bold", padx=14, justify=LEFT).pack()
# radio = Radiobutton(root, text="Dosa", padx=11, variable=var, value=1).pack(anchor="nw")
# radio = Radiobutton(root, text="Idly", padx=11, variable=var, value=2).pack(anchor="nw")
# radio = Radiobutton(root, text="Aloo Paratha", padx=11, variable=var, value=3).pack(anchor="nw")
# radio = Radiobutton(root, text="Samosa", padx=11, variable=var, value=4).pack(anchor="nw")

# we can make these radio button in one liner using for loop, if we have a list of food.

var = StringVar()
var.set("Radio")    # initial value set.
radio = Radiobutton(root, text="Dosa", padx=11, variable=var, value="Dosa").pack(anchor="nw")
radio = Radiobutton(root, text="Idly", padx=11, variable=var, value="Idly").pack(anchor="nw")
radio = Radiobutton(root, text="Aloo Paratha", padx=11, variable=var, value="Aloo Paratha").pack(anchor="nw")
radio = Radiobutton(root, text="Samosa", padx=11, variable=var, value="Samosa").pack(anchor="nw")

# retrieving value of radio button
Button(root, text="Order Now", command=order).pack()
root.mainloop()
