# Canvas Widgets in python.

from tkinter import *

root = Tk()
canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Notepad v10.5.8")
canvas_widget = Canvas(root, width=canvas_width, height=canvas_height)
canvas_widget.pack()

# The line goes from  x1,y1 to x2,y2.
# canvas_widget.create_line(0, 0, 800, 200)
canvas_widget.create_line(0, 0, 800, 400, fill="blue")
canvas_widget.create_line(0, 400, 800, 0, fill="red")

# te create a rectangle, coordinates are  given by -
# coordinate syntax - Top-Left coordinate, Bottom-Right coordinate.
canvas_widget.create_rectangle(3, 5, 700, 300, fill="green")

# coordinate to make text are given as -
# coordinate given is - centre coordinate hoga uss text ka jo text mai rakh rha hu gui window mai.
canvas_widget.create_text(200, 200, text="PYTHON")

# coordinate given to create oval.
# coordinates of rectangle is given (top-left coord. & bottom-right coord.)
# reason - oval is made inside rectangle. refer to oval.png
canvas_widget.create_oval(100, 100, 350, 350)

# to make a circle we will give the coordinates of a square.
canvas_widget.create_oval(500, 100, 650, 250)

root.mainloop()