from tkinter import *
# import tkinter.messagebox as tmsg
from tkinter import messagebox as tsmg
from tkinter import ttk
import json

class LibraryApp(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x650")
        self.minsize(1200,650)
        self.maxsize(1200,650)
        self.title("Online Library Management System")
        self.main_frame = Frame(self, bg="white")
        self.main_frame.pack(fill=BOTH, expand=True)
        self.create_starting_interface()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def create_starting_interface(self):
        f1 = Frame(self.main_frame, bg="lightblue", height=250)
        f1.pack(side=TOP, fill=X)
        f1.pack_propagate(False)
        Label(f1, text="Welcome to NIT Srinagar Library", fg="black", font="Comicsans 30 bold").pack(pady=100)
        f2 = Frame(self.main_frame, bg="yellow", height=400)
        f2.pack(side=BOTTOM, fill=X)
        f2.pack_propagate(False)

        # register button
        regbtn = Canvas(f2, width=600, height=400, highlightthickness=1, highlightbackground="green")
        regbtn.pack(side=LEFT)
        regbtn.create_rectangle(0,0,600,400, fill="lightblue")
        reg_oval_id = regbtn.create_oval(150, 50, 450, 350, fill="black")
        reg_text_id = regbtn.create_text(300, 200, text="REGISTER", fill="white", font="Helvetica 20 bold")
        def regbutton(event):
            self.clear_frame()
            RegistrationForm(self.main_frame, app)
            # self.quit()
            # self.after(100,self.destroy)
        regbtn.tag_bind(reg_oval_id, '<Button-1>', regbutton)
        regbtn.tag_bind(reg_text_id, '<Button-1>', regbutton)

        # login button
        logbtn = Canvas(f2, width=600, height=400, highlightthickness=1, highlightbackground="green")
        logbtn.pack(side=RIGHT)
        logbtn.create_rectangle(0, 0, 600, 400, fill="lightblue")
        log_oval_id = logbtn.create_oval(150, 50, 450, 350, fill="black")
        log_text_id = logbtn.create_text(300, 200, text="LOGIN", fill="white", font="Helvetica 20 bold")
        def logbutton(event):
            self.clear_frame()
            LoginForm(self.main_frame, app)
            # self.quit()
            # self.after(100, self.destroy)
        logbtn.tag_bind(log_oval_id, '<Button-1>', logbutton)
        logbtn.tag_bind(log_text_id, '<Button-1>', logbutton)

class RegistrationForm:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        parent.config(bg="lightgrey")
        # registration form is not coming at the centre so to centre it -
        # we will create a new frame inside a parent frame(main_frame) as will place this form frame at centre og the window using place,
        # geometry manager, and will put the whole content inside it.
        form_frame = Frame(parent, bg="lightgrey")
        # form_frame.place(relx=0.5, rely=0.5, anchor="s")
        form_frame.pack()
        # Label(form_frame, text="Registration", font="Helvetica 30 bold").grid(row=0, column=2, pady=30)
        Label(form_frame, text="Registration", font="Helvetica 32 bold").grid(row=0, column=0, pady=30, padx=10)
        Label(form_frame, text="Enrollment No:", font="Helvetica 18 italic").grid(row=1, column=0)
        Label(form_frame, text="Email Id:", font="Helvetica 18 italic").grid(row=2, column=0)
        Label(form_frame, text="Password:", font="Helvetica 18 italic").grid(row=3, column=0)
        # Label(form_frame, text="Student Image:", font="Helvetica 18 italic").grid(row=4, column=0)
        enroll = StringVar()
        email = StringVar()
        password = StringVar()

        Entry(form_frame, textvariable=enroll, font="Helvetica 15").grid(row=1, column=1, ipady=4, pady=10)
        Entry(form_frame, textvariable=email, font="Helvetica 15").grid(row=2, column=1, ipady=4, pady=10)
        Entry(form_frame, textvariable=password, font="Helvetica 15").grid(row=3, column=1, ipady=4, pady=10)
        # Entry(form_frame, textvariable=password, font="Helvetica 15").grid(row=3, column=1, ipady=4, pady=10)
        button = Button(form_frame, text="Sumbit", font="Helvetica 15", padx=20, pady=10)
        button.grid(row=5, column=0, columnspan=2, pady=20, sticky="ew")

        def submit(event):
            info = {"Enrollment": f"{enroll.get().upper()}", "email_id": f"{email.get()}", "password": f"{password.get()}"}
            with open("library_registration_details.txt", "a") as f:
                f.write(f"{info}\n")
            self.app.clear_frame()
            MainInterface(self.parent, self.app)
        button.bind('<Button-1>', submit)


class LoginForm:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        parent.config(bg="lightgrey")
        form_frame = Frame(parent, bg="lightgrey")
        form_frame.pack()
        btn_frame = Frame(parent, bg="lightgrey")
        btn_frame.pack()
        Label(form_frame, text="Login", font="Helvetica 32 bold").grid(row=0, column=0, pady=30, padx=10)
        Label(form_frame, text="Email Id:", font="Helvetica 18 italic").grid(row=2, column=0)
        Label(form_frame, text="Password:", font="Helvetica 18 italic").grid(row=3, column=0)
        email = StringVar()
        password = StringVar()
        Entry(form_frame, textvariable=email, font="Helvetica 15").grid(row=2, column=1, ipady=4, pady=10)
        Entry(form_frame, textvariable=password, font="Helvetica 15").grid(row=3, column=1, ipady=4, pady=10)
        button = Button(btn_frame, text="Sumbit", font="Helvetica 15", padx=20, pady=10)
        button.pack(pady=30)

        def submit(event):
            self.app.clear_frame()
            MainInterface(self.parent, self.app)
        button.bind('<Button-1>', submit)

class MainInterface:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        info_frame = Frame(parent, width=1200, height=250,  bg="green")
        info_frame.pack()
        info_frame.pack_propagate(False)
        # Label(info_frame, text="Search").grid(row=0, column=0)
        search_query = StringVar()
        ew = ttk.Entry(info_frame, textvariable=search_query)
        # ew.grid(row=0, column=1)

        display_frame = Frame(parent, width=1200, height=400)
        display_frame.pack(side=BOTTOM)
        display_frame.pack_propagate(False)
        borrow_canvas = Canvas(display_frame, width=400, height=400, bg="white")
        borrow_canvas.pack(side=LEFT)
        b_oval_id = borrow_canvas.create_oval(50, 50, 350, 350, fill="black")
        b_text_id = borrow_canvas.create_text(200, 200, text="BORROW", fill="white", font="Helvetica 18 bold")
        return_canvas = Canvas(display_frame, width=400, height=400, bg="white")
        return_canvas.pack(side=LEFT)
        r_oval_id = return_canvas.create_oval(50, 50, 350, 350, fill="black")
        r_text_id = return_canvas.create_text(200, 200, text="RETURN", fill="white", font="Helvetica 18 bold")
        enquiry_canvas = Canvas(display_frame, width=400, height=400, bg="white")
        enquiry_canvas.pack(side=LEFT)
        e_oval_id = enquiry_canvas.create_oval(50, 50, 350, 350, fill="black")
        e_text_id = enquiry_canvas.create_text(200, 200, text="ENQUIRY", fill="white", font="Helvetica 18 bold")

        def borrow_Click(event):
            self.app.clear_frame()
            Borrow(self.parent, self.app)
        def return_Click(event):
            self.app.clear_frame()
            Return(self.parent, self.app)
        def enquiry_Click(event):
            self.app.clear_frame()
            Enquiry(self.parent, self.app)

        borrow_canvas.tag_bind(b_oval_id, '<Button-1>', borrow_Click)
        borrow_canvas.tag_bind(b_text_id, '<Button-1>', borrow_Click)
        return_canvas.tag_bind(r_oval_id, '<Button-1>', return_Click)
        return_canvas.tag_bind(r_text_id, '<Button-1>', return_Click)
        enquiry_canvas.tag_bind(e_oval_id, '<Button-1>', enquiry_Click)
        enquiry_canvas.tag_bind(e_text_id, '<Button-1>', enquiry_Click)

class Borrow:
    def __init__(self, parent, app):
        search_frame = Frame(parent, width=1200, height=80, bg="grey")
        search_frame.pack()
        search_frame.pack_propagate(False)
        search_query = StringVar()
        search_widget = Entry(search_frame, textvariable=search_query, width=80, font="Helvetica 16 bold")
        search_widget.pack(ipady=8, side=LEFT, padx=40, pady=15)
        search_btn = Button(search_frame, text="Search", font="Helvetica 16 bold")
        search_btn.pack(side=LEFT)

        self.dropdown_frame = Frame(parent, width=1200 , height=50, bg="red")
        self.dropdown_frame.pack()
        self.dropdown_frame.pack_propagate(False)

        self.ece_frame = Frame(parent, width=1200, height=420, bg="green")
        self.ece_frame.pack()
        self.ece_frame.pack_propagate(False)
        Label(self.ece_frame, text="ECE Department Books", bg="yellow", font="Helvetica 18 bold").pack(pady=18)

        FormTreeviewTable(self.ece_frame, "ECE")

class Return:
    def __init__(self, parent, app):
        pass
class Enquiry:
    def __init__(self, parent, app):
        pass

class FormTreeviewTable:
    def __init__(self, department_frame, department_name):
        self.frame = department_frame
        self.department_name = department_name

        # creating a new frame to align scrollbar and table together
        self.tree_frame = Frame(self.frame)
        self.tree_frame.pack()

        # setting font style to Treeview widget
        style = ttk.Style()
        style.configure("Treeview.Heading", font="Aerial 15 bold")
        style.configure("Treeview", font="Calibri 12 italic")   # cells font

        # creating Treeview table
        self.tree = ttk.Treeview(self.tree_frame, columns=('S_NO', 'REF_ID', 'AUTHOR_NAME', 'BOOK_NAME', 'CHECKBOX'), show="headings", height=14)

        # formatting Columns - setting the size of columns
        self.tree.column('S_NO', anchor=CENTER, width=70)
        self.tree.column('REF_ID', anchor=CENTER, width=190)
        self.tree.column('AUTHOR_NAME', anchor=CENTER, width=230)
        self.tree.column('BOOK_NAME', anchor=CENTER, width=320)
        self.tree.column('CHECKBOX', anchor=CENTER, width=120)
        # setting headings of table
        self.tree.heading('S_NO', text='S_NO')
        self.tree.heading('REF_ID', text='REFERENCE_ID')
        self.tree.heading('AUTHOR_NAME', text='AUTHOR_NAME')
        self.tree.heading('BOOK_NAME', text='BOOK_NAME')
        self.tree.heading('CHECKBOX', text='CHECKBOX')

        #  making scroll bar in table.
        self.scrollbar = Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # loading data in the form of table / inserting data into rows and columns
        try:
            with open("Library_BOOKS.json", "r") as file:
                data = json.load(file)
                book_list = data.get(self.department_name, [])
                # print(type(data))  # -- > <class 'dict'>
                # print(type(book_list))
                # book_list is a list containing dictionaries as its elements.
        except FileNotFoundError:
            print("Library_BOOKS.json file not found")

        # print(book_list)
        for s_no, book_data in enumerate(book_list, start=1):
            # book_data is the dictionary
            self.tree.insert("", "end", values=(s_no, book_data["ref_id"], book_data["auth_name"], book_data["book"], "c"))

        self.tree.pack()

if __name__ == '__main__':
    app = LibraryApp()
    app.mainloop()