# Displaying Images using Label.

# image bhi ek aise widget hai jiskai saath user interact nhi karta hai, matlb yeh hai ek Label.

from tkinter import *
from PIL import Image, ImageTk  # PIL - pillow module.

root = Tk()

# argument - "Width x Height"
root.geometry("800x740")

# argument - Width, Height
root.minsize(250,100)

# argument - Width, Height
root.maxsize(1200,820)

# firstText = Label(text="This is my first GUI window created.")
# firstText.pack()

# in tk we have a PhotoImage class, for displaying image.
# photo = PhotoImage(file="diamond problem.png")
# photo = PhotoImage(file="tablet.jpg")   # error
# Now have to create a Label.
# image_label = Label(image=photo)
# image_label.pack()

# now install pillow module - it is a python imaging library(PIL).

# tk directly not support the jpg format of the images.
# ImageTk - is a method that supports to take a jpg file in the tkinter.

# for jpg images.
jpg_image = Image.open("tablet.jpg")
photo = ImageTk.PhotoImage(jpg_image)
img_label = Label(image=photo)
img_label.pack()

# NOTE: pehlai jo humnai PhotoImage class use ki thi wo tkinter module ki thi. PhotoImage(file="..")
# abhi jo humnai PhotoImage class use ki hai wo ImageTk module ki, kii hai.  PhotoImage(image)

root.mainloop()


# Task - Exercise using OS module.
