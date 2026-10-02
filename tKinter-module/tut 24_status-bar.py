# Status bar in tkinter.

from tkinter import *

# def upload():
#     statusvar.set("Uploading...")
#     import time
#     time.sleep(3)
#     statusvar.set("Ready Now")
# tkinter time ko save karnai kai liyai and resources ko optimise karnai kai liyai, yeh karta hai
# jab app button par click karaigai toh aap ko Uploading... nhi dekhai daigaa, sirf 3 second baad ready ka ready now ho jaigaa, matlb
# function kai andar jo hai ussai tk ignore karigaa and last mai set function ko execute kar daigaa 3 second baad.

def upload():
    # agar app chahtai ki function kai andar app ki widget update ho jaai , iskai liyai aap ko use karna padega update().
    statusvar.set("Uploading...")
    statusbar.update()
    # yeh string variable (statusvar) merai jis bhi widget sai attached hoga wo widget mai update kar dunga agar toh yeh widget (statusbar) nayi value laiga
    # statusvar string variable ki.
    import time
    time.sleep(3)
    statusvar.set("Ready Now")



root = Tk()
root.geometry("500x300")
root.title("Status Bar in tkinter")

# status bar is not a widget.
# by using the label and border we will make a status bar.

statusvar = StringVar()
statusvar.set("Ready")
statusbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
statusbar.pack(side=BOTTOM, fill=X)

# updating the status bar.
Button(root, text="Upload", command=upload).pack()
root.mainloop()