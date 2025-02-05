from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl, xlrd 
from openpyxl import Workbook
import pathlib 


background = "#1B1E2B"

root = Tk()
root.title("Student Registration System")
root.geometry("1250x700+210+100")
root.config(bg=background)

file = pathlib.Path("student_data.xlsx")
if file.exists():
    pass
else: 
    workbook = Workbook()  # Yeni bir çalışma kitabı oluştur
    sheet = workbook.active  
    sheet["A1"] = "Registration No"
    sheet["B1"] = "Name"
    sheet["C1"] = "surname"
    sheet["D1"] = "Gender"
    sheet["E1"] = "Date of Birth"
    sheet["F1"] = "Email"
    sheet["G1"] = "Phone Number"
    sheet["H1"] = "University"
    sheet["I1"] = "Student No"
    sheet["J1"] = "Class"
    sheet["K1"] = "Skill"

    workbook.save("student_data.xlsx")

#exit
def Exit():
    root.destroy()

def showimage():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select image file", filetype=(("JPG File","*.jpg"), ("PNG File","*.png"),
                                                                               ("ALL Files","*.txt")))

#gender
def selection():
    value=radio.get()
    if value == 1:
        gender = "Male"
    else :
        gender = "Female"

# top frames
Label(
   root,
    text="Student Registration System",
    bg="#292D3E",  # Daha koyu bir arka plan
    fg="white",
    font=("Arial", 20, "bold"),  # Daha büyük ve modern font
    pady=15,  # Padding yüksekliği
).pack(side=TOP, fill=X)



# search box
Search = StringVar()
Entry(root, textvariable= Search, width=10, bd=2, bg="#f8f8f6", font="arial 19 ").place(x =910, y =80)
imageicon3 =PhotoImage(file ="images/search.png")
Srch= Button(root, text="Search student ",bg="#f8f8f6", fg= "#1B1E2B",compound=LEFT ,image = imageicon3, 
             width =130, height= 28)
Srch.place(x= 1070, y =80)

imageicon4 =PhotoImage(file ="images/reload.png")
update_button = Button(root, image = imageicon4, width =55, height= 30, bg="#292D3E")
update_button.place(x= 100, y =18)


# registration  and date
Label(
   root,
    text="Registration No: ",
    bg="#1B1E2B",  # Daha koyu bir arka plan
    fg="#f8f8f6",
    font=("Arial", 13 ),  # Daha büyük ve modern font
).place(x= 30, y=130)

Label(
   root,
    text="Date: ",
    bg="#1B1E2B",  # Daha koyu bir arka plan
    fg="#f8f8f6",
    font=("Arial", 13 ),  # Daha büyük ve modern font
).place(x= 480, y=130)

Registration= StringVar()
Date = StringVar()

reg_entry = Entry(root, textvariable= Registration, width=15, font=("Arial", 10), bg="#f8f8f6")
reg_entry.place(x= 160, y=130)

#registration_no 
today = date.today()
d1=today.strftime("%d/%m/%Y")
date_entry = Entry(root, textvariable= Date, width=15, font=("Arial 10"),bg="#f8f8f6")
date_entry.place(x=550, y=130)

Date.set(d1)

#students_details
obj = LabelFrame(root, text="Student's Details", 
                 font=("Arial 16"), bd=2, 
                 bg="#292D3E",
                 fg="#f8f8f6",
                 width=850,
                height=230, relief= GROOVE)
obj.place(x=30, y=200)

Label( obj,text="Name: ",bg="#292D3E", fg="#f8f8f6",font=("Arial", 13 ),  ).place(x= 30, y=50)
Label( obj,text="Surname: ",bg="#292D3E", fg="#f8f8f6",font=("Arial", 13 ),  ).place(x= 30, y=100)
Label( obj,text="Gender: ",bg="#292D3E", fg="#f8f8f6",font=("Arial", 13 ),  ).place(x= 30, y=150)

Label( obj,text="Date of Birth: ",bg="#292D3E", fg="#f8f8f6",font=("Arial", 13 ),  ).place(x=400, y=50)
Label( obj,text="Email: ",bg="#292D3E", fg="#f8f8f6",font=("Arial", 13 ),  ).place(x=400, y=100)
Label( obj,text="Phone Number: ",bg="#292D3E", fg="#f8f8f6",font=("Arial", 13 ),  ).place(x= 400, y=150)

Name = StringVar()
name_entry= Entry(obj, textvariable= Name, width= 20, font=("Arial", 10),bg="#f8f8f6")
name_entry.place(x=100, y=50)

Surname = StringVar()
surname_entry= Entry(obj, textvariable= Surname, width= 20, font=("Arial", 10),bg="#f8f8f6")
surname_entry.place(x=120, y=100)

radio= IntVar()
radio1 = Radiobutton(obj, text="Male", variable=radio, bg="#f8f8f6",value=1, command=selection) 
radio1.place(x=120, y=150)

radio2 = Radiobutton(obj, text="Female", bg="#f8f8f6", variable=radio, value=2, command=selection)
radio2.place(x=180, y=150)

DOB = StringVar()
dob_entry= Entry(obj, textvariable= DOB ,width= 20,bg="#f8f8f6", font=("Arial", 10))
dob_entry.place(x=515, y=50)

Email = StringVar()
email_entry= Entry(obj, textvariable= Email, bg="#f8f8f6",width= 20, font=("Arial", 10))
email_entry.place(x=460, y=100)

Phone = StringVar()
phone_entry= Entry(obj, textvariable= Phone, bg="#f8f8f6",width= 20, font=("Arial", 10))
phone_entry.place(x=530, y=150)

#school_details
obj2 = LabelFrame(root, text="University's Details", 
                 font=("Arial 16"), bd=2, 
                 bg="#292D3E",
                 fg="#f8f8f6",
                 width=850,
                height=200, relief= GROOVE)
obj2.place(x=30, y=450)

Label( obj2,text="University Name: ",bg="#292D3E", fg="#f8f8f6",font=("Arial", 13 ),  ).place(x= 30, y=40)
Label( obj2,text="Student No: ",bg="#292D3E", fg="#f8f8f6",font=("Arial", 13 ),  ).place(x= 30, y=100)

Label( obj2,text="Class: ",bg="#292D3E", fg="#f8f8f6",font=("Arial", 13 ),  ).place(x= 400, y=40)
Label( obj2,text="Skill: ",bg="#292D3E", fg="#f8f8f6",font=("Arial", 13 ),  ).place(x= 400, y=100)

UniName = StringVar()
uniName_entry= Entry(obj2, textvariable= UniName, width= 20, font=("Arial", 10),bg="#f8f8f6" )
uniName_entry.place(x=170, y=40)

StudentNo = StringVar()
student_no_entry= Entry(obj2, textvariable= StudentNo, width= 20, font=("Arial", 10),bg="#f8f8f6")
student_no_entry.place(x=130, y=100)

Class = Combobox(obj2, values=["1","2","3","4"], font=("Arial",10), width =17, state = "r"  )
Class.place(x=460, y=40)
Class.set("Select Class")

Skill = StringVar()
skill_entry= Entry(obj2, textvariable= StudentNo, width= 20, font=("Arial", 10),bg="#f8f8f6")
skill_entry.place(x=450, y=100)


#image

f =Frame(root, bd=3, bg="black", width=200, height=200, relief=GROOVE) 
f.place(x=980, y=150)

img = PhotoImage(file="images/add-user.png")
lbl = Label(f, bg="black",image= img)
lbl.place(x=0, y=0)


#button

Button(root, text="Upload", width=19, height=2, font="Arial 12 bold",bg="#88CE65", command=showimage).place(x=980, y=370)
SaveButton=Button(root, text="Save", width=19, height=2, font="Arial 12 bold", bg="#17ACE8")
SaveButton.place(x=980, y=450)
Button(root, text="Reset", width=19, height=2, font="Arial 12 bold",bg="#FFBB17").place(x=980, y=530)
Button(root, text="Exit", width=19, height=2, font="Arial 12 bold",bg="#F44336", command=Exit).place(x=980, y=610)

root.mainloop()

