# Using Classes and Objects to create GUIs.

from tkinter import *

# Inhereting GUI class from Tk class.
class GUI(Tk):

    # jo hum pehlai root sai likha kartai thai wo ab self (OBJECT of the CLASS) sai replace ho gya.
    # jab hum root = Tk() likha kartai thai (jo ki hum hamesha likha kartai thai) toh Tk class ka constructor call ho jata tha.
    # kyunki hum hamesha root=Tk() likhtai hai, matlb Tk() class ka constructor hamesha call hota hai, isliyai ab bhi humai Tk() class
    # ka constructor call karna padega.
    # root = Tk() - means we have created the object of the class Tk(), we named the objecct of this Tk class as root.

    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.title("OOPs concept in tkinter")

# class kai andar root --> self hai

    def statusBar(self):
        self.var = StringVar()
        self.var.set("Ready")
#       we have created  instance variables of our object (root==window)
        self.statusbar = Label(self, textvariable=self.var, relief=SUNKEN, anchor="w")
        self.statusbar.pack(side=BOTTOM, fill=BOTH)

    def click(self):
        print("Button is clicked")

    def createbutton(self, inptext):
        Button(text=inptext, command=self.click).pack()

# Creating a main function.
if __name__ == '__main__':
    # ab mera object mera root hai.
    window = GUI()
    window.statusBar()
    window.createbutton("Click Me")
    window.mainloop()

# Encapsulation ho jata hai using classes in our program - implementation details GUI class kai andar hided hai.
# apka main program ekdam clean hai, bas 4 line of code and GUI build.
