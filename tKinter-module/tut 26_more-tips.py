# More on tkinter.

from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("MORE on tkinter")

# how to change GUI icon.
# let say we have .ico file.
# root.wm_iconbitmap("notepad-512.ico")
root.wm_iconbitmap("Windows_Notepad_icon.ico")


# about root.config() function.
# kabhi bhi GUI kai andar koi changes lanai padtai hai, toh hum root.config function ka use kartai hai.
root.config(background="grey")


# hum jis screen mai hai uski width and height chaiyai hai agar.
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
# merai laptop ki screen ki width x height aa jaigi - 1536x864.
print(f"{width}x{height}")

# root.destroy function GUI window ko destroy karnai kai kaam aata hai.
Button(text="Close", command=root.destroy).pack()

root.mainloop()