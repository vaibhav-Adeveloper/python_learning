# Sliders in tkinter using scale() widget.

from tkinter import *
import tkinter.messagebox as tmsg

def getdollar():
    print(f"We have credited {slider2.get()} dollar to your bank account 142XXX1004")
    tmsg.showinfo("Money Credited to Account", f"We have credited {slider2.get()} dollars to your bank account 142XXX1004")


root = Tk()
root.geometry("500x300")
root.title("Sliders in tkinter")

# making slider
# slider = Scale(root, from_=0, to=120)
# slider.pack()

# making horizontal slider.
# slider2 = Scale(root, from_=0, to=120 ,orient=HORIZONTAL)
# slider2.pack()

# getting value of slider
# you can get the value of slider using get() function.
# Label(root, text="How much dollar so you want").pack()
# # slider2 = Scale(root, from_=30, to=120, orient=HORIZONTAL)
# slider2 = Scale(root, from_=0, to=120, orient=HORIZONTAL)
# # to set the initial value of slider, without affecting value of from_ --> we have to use set() function.
# slider2.set(40)
# slider2.pack()
# Button(root, text="Get Dollar!", command=getdollar, padx=8, pady=4).pack(pady=8)


# tickinterval - ek particular multiple mai value lainai kai liyai in slider use hota hai.
Label(root, text="How much dollar so you want").pack()
slider2 = Scale(root, from_=0, to=120, orient=HORIZONTAL, tickinterval=40)
slider2.set(40)
slider2.pack()
Button(root, text="Get Dollar!", command=getdollar, padx=8, pady=4).pack(pady=8)

root.mainloop()


# Task - will ask to customer to rate their experience of the food they ordered.    (0 to 10)
# and write the value of slider (customer experience value) in the file.
# display message.
