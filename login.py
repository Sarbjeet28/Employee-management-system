from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        #
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Sarbjeet\PycharmProjects\EMS\Ems images\back.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\Sarbjeet\PycharmProjects\EMS\Ems images\2h.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)
        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 25, "bold"), fg="dark violet",
                             bg="white")
        register_lbl.place(x=20, y=20)

        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)
        fname_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lname.place(x=370, y=100)
        self.txt_lname = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        #row2

        contact = Label(frame, text="Contact", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50,y=170)
        self.txt_contact = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370,y=170)
        self.txt_email = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        #row3
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman", 15, "bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q = ttk.Combobox(frame, font=("times new roman", 15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Favorite Flower","Your Favorite Fruit")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame, text=" Security Answers", font=("times new roman", 15, "bold"), bg="white",
                           fg="black")
        security_A.place(x=370, y=240)
        self.txt_security = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        #row4
        pswd= Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)
        self.txt_pswd = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)
        self.txt_confirm_pswd = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        #check button
        checkbtn=Checkbutton(frame,text="I Agree The Terms And Conditions",font=("times new roman", 12, "bold"),onvalue=1,offvalue=0)

        checkbtn.place(x=50, y=380)

        #button
        img=Image.open(r"C:\Users\Sarbjeet\PycharmProjects\EMS\Ems images\6h.jpg")
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimage= ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)

        img1 = Image.open(r"C:\Users\Sarbjeet\PycharmProjects\EMS\Ems images\login.png")
        img1 = img1.resize((200, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2")
        b1.place(x=320, y=400, width=200)

        #function declaration

















#
# if __name__ == "__main__":
#     root = Tk()


if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()

