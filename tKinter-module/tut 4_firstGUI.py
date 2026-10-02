# Label, Geometry, maxsize & minsize.

# Label - ek widget hota hai tkinter kai andar, jiskai saath user interact nhi karta hai.
# Label, Geometry, maxsize & minsize - these are the start of the GUI.

from tkinter import *

root = Tk()

# argument - "Width x Height"
root.geometry("600x500")

# argument - Width, Height
root.minsize(250,100)

# argument - Width, Height
root.maxsize(1200,650)

firstText = Label(text="This is my first GUI window created.")
firstText.pack()
# to display the label in GUI window, we have to pack the label.

root.mainloop()