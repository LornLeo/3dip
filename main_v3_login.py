# main.py
import subprocess
from tkinter import *
from PIL import ImageTk, Image
from csv import writer
from tkinter import messagebox
import csv
def login():
    if Username_ent.get() and Password_ent.get():
        create_account=True
        with open("user_database.csv", 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                print(row)
                if row!=[]:
                    if row[1]==Username_ent.get():
                        create_account=False
                        if row[2]==Password_ent.get():
                            create_account=None
                            window.destroy()
                            subprocess.run(['python', 'main_v3.py'])
                    
            if create_account==True:
                result=messagebox.askyesno("Create account", "Invalid username\nYou can use these details to create an account")
                if result==True:
                    User_ID=0
                    with open("user_database.csv", 'r') as file:
                        csvreader = csv.reader(file)
                        for row in csvreader:
                            User_ID=User_ID+1
                    List=[User_ID,Username_ent.get(),Password_ent.get()]
                    with open('user_database.csv', 'a',newline='') as f_object:
                        writer_object = writer(f_object)
                        writer_object.writerow(List)
                        f_object.close()
                    create_account=False
                else:
                    pass
            elif create_account==False:
                messagebox.showerror("showerror", "Wrong password")
    else:
        if Username_ent.get():
            messagebox.showerror("Error", "Please enter the password")
        else:
            messagebox.showerror("Error", "Please enter the Username")
            
window = Tk()
window.geometry('850x550')
window.title("Login")
window.resizable(0, 0)
window.configure(bg="white")

Entry_frame = Frame(window,width=400,bg="white")
Entry_frame.place(x=180,y=300)

image_path = "logo.png"
food_image = Image.open(image_path)
resized_image = food_image.resize((200, 200), Image.ANTIALIAS)
image = ImageTk.PhotoImage(resized_image)
Logo = Label(window, image=image, bg="white")
Logo.place(x=325, y=30)


Name_lbl=Label(window,text="Food Shop",bg="white",font=('Rockwell 22'),fg="#fcc302",width=10)
Name_lbl.place(x=343,y=240)
Username_lbl=Label(Entry_frame,text="Username: ",bg="white",font=('Arial 17'))
Username_lbl.grid(row=1,column=0,sticky=W)
Username_ent= Entry(Entry_frame,bd=3,width=25,font=('Arial 19'))
Username_ent.grid(row=1, column=1,sticky=W)
Password_lbl=Label(Entry_frame,text="Password: ",bg="white",font=('Arial 17'))
Password_lbl.grid(row=2,column=0,sticky=W,pady=(23,0))
Password_ent= Entry(Entry_frame,show="*",bd=3,width=25,font=('Arial 19'))
Password_ent.grid(row=2, column=1,sticky=W,pady=(23,0))
'''Create_button = Button(Entry_frame, text="Create account", command=login,width=20,font=('serif 9'),anchor=E,activebackground="white",activeforeground="red",fg="black",bg="white",bd=0, highlightthickness=0)
Create_button.grid(row=3,column=1,sticky=NE)'''
Login_button = Button(Entry_frame, text="Login", command=login,width=20,font=('serif 13'),fg="white",bg="black")
Login_button.grid(row=4,column=1,sticky=E,pady=(15,0))


window.mainloop()