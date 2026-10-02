# Travel form using Check-Buttons and Entry Widgets.

from tkinter import *

def getvals():
    print("Its Work")

root = Tk()
root.geometry("555x455")

# Heading Label
Label(root, text="Welcome to Satya Sai Travellers", font="Comicsansms 13 bold", pady=20).grid(row=0, column=3)

# Text for our Form
name = Label(root, text="Name")
phone = Label(root, text="Phone No")
sex = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact")
payment = Label(root, text="Payment Mode")

# Pack Text for our Form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
sex.grid(row=3, column=2)
emergency.grid(row=4, column=2)
payment.grid(row=5, column=2)

# Tkinter variables for storing entries.
namevalue = StringVar()
phonevalue = StringVar()
sexvalue = StringVar()
emergencyvalue = StringVar()
paymentvalue = StringVar()
foodservicevalue = IntVar()

# Entries for a form.
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
sexentry = Entry(root, textvariable=sexvalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymententry = Entry(root, textvariable=paymentvalue)

# Packing the Entries.
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
sexentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymententry.grid(row=5, column=3)

# Checkbox * Packing it.
foodservice = Checkbutton(text="Want to preorder your meal?", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

# Buttons, Packing it & Assigning it a command.
Button(text="Submit to SatyaSai Travels", command=getvals).grid(row=7, column=3)

root.mainloop()