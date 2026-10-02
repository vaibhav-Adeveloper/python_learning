# Handling Events in tkinter.

from tkinter import *

def vaibhav(eventObj):
    print(f"You clicked on the button, and your cursor was at {eventObj.x}, {eventObj.y}")


root = Tk()
root.title("Events in tk")
root.geometry("500x300")

btn = Button(root, text="Click me Please")
btn.pack()

# Events
btn.bind('<Button-1>', vaibhav)
# we have bind the button with event and it's event handling function.
# matlb jab bhi yeh event perform ho ('<Button-1>') iss button par (Click me Please), toh iss function ko call laga doo (vaibhav) to
# handle the event.

# handling double click event on the button.
# its event handling function is a quit function which will quit the user from GUI window.
btn.bind('<Double-1>', quit)

root.mainloop()
