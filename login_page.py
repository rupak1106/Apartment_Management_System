
from tkinter import *

from tkinter import messagebox
from PIL import ImageTk
import mysql.connector


mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    passwd="ram9486",
    database="apart"
)

if mydb.is_connected():
 print("login connection established")
mycursor=mydb.cursor()

def login():
    username = unEntry.get()
    password = pwEntry.get()
    query = f"SELECT * FROM residents WHERE name = '{username}' AND resident_id = '{password}'"
    mycursor.execute(query)
    row = mycursor.fetchone()
    if row is not None:
        messagebox.showinfo("Login", "Login successful!")
        window.destroy()
        import profile_page
        def uss():
            return (username)

        def pss():
            return (password)
        uss(username)
        pss(password)

    else:
        messagebox.showerror("Login", "Invalid username or password.")

window=Tk()
window.geometry('1525x760+0+0')
window.title('Login System of Apartment Management System')
window.resizable(0,0)
backImage=ImageTk.PhotoImage(file='lpg.webp')
label1=Label(window,image=backImage)
label1.pack()
loginFrame=Frame(window,bg='white')
loginFrame.place(x=400,y=150)
logoImage=PhotoImage(file='alogo.png')
label2=Label(loginFrame,image=logoImage)
label2.grid(row=0,column=1,columnspan=2,pady=10)

unImage=PhotoImage(file='user.png')
unLabel=Label(loginFrame,image=unImage,text='Username',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
unLabel.grid(row=1,column=1,pady=10,padx=20)
unEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
unEntry.grid(row=1,column=2,pady=10,padx=20)


pwImage = PhotoImage(file='pass.png')
pwLabel = Label(loginFrame, image=pwImage, text='Password', compound=LEFT, font=('times new roman', 20, 'bold'),
                   bg='white')
pwLabel.grid(row=2, column=1, pady=10, padx=20)
pwEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='royalblue')
pwEntry.grid(row=2, column=2, pady=10, padx=20)


loginButton=Button(loginFrame,text='Login',font=('times new roman', 14, 'bold'),width=15,fg='white'
                      ,bg='cornflowerblue',activebackground='cornflowerblue',activeforeground='white',cursor='hand2'
                      ,command=login)
loginButton.grid(row=3,column=2,pady=10)
window.mainloop()