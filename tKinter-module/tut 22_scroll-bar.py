# Scroll bar in tkinter.

from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("Scroll Bar in tkinter")
# kisi bhi widget ko scroll bar sai connect karnai kai liyai humai doo cheez karna padtha hai.
# uss widget ka y scroll command ko equal karna padta hai scroll bar kai set method sai.
# scroll bar kai command ko karna oadtha hai uss widget kai y view kai barabar.

# for connecting scroll bar to widget.
# 1. widget(yscrollcommand = scrollbar.set)
# 2. scrollbar.config(command=widget.yview)

# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)
#
# lst = Listbox(root, yscrollcommand=scrollbar.set)
# for i in range(320):
#     lst.insert(END, f"Item {i}")
#
# lst.pack(fill="both", padx=22)   # fill="both" sai right and left dono jagah sai fill hota hai.
# scrollbar.config(command=lst.yview)


# adding scroll bar to Text widget.
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
textarea = Text(root, yscrollcommand=scrollbar.set)     # Text widget.
textarea.pack(fill=BOTH)
scrollbar.config(command=textarea.yview)

root.mainloop()

# Task - Connect the scrollbar to a very big label text.
