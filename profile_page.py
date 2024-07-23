from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox
import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
username="root",
passwd="ram9486",
database="apart"
)
if mydb.is_connected():
  print("connection established")
mycursor = mydb.cursor()

# functions

def profile():
    rightFrame = Frame(root, bg='white')
    rightFrame.place(x=350, y=80, width=1200, height=1000)
    query = "SELECT * FROM residents WHERE resident_id = %s"
    myda=(res_id,)
    mycursor.execute(query,myda)
    data = mycursor.fetchone()

    namelabel = Label(rightFrame, text="Name            : " + data[1], font=('arial', 18), bg='white')
    namelabel.place(x=200, y=50)
    idlabel = Label(rightFrame, text="Resident id    : " + str(data[0]), font=('arial', 18), bg='white')
    idlabel.place(x=200, y=100)
    agelabel = Label(rightFrame, text="Age               : " + str(data[3]), font=('arial', 18), bg='white')
    agelabel.place(x=200, y=150)
    apalabel = Label(rightFrame, text="Apartment id : " + str(data[2]), font=('arial', 18), bg='white')
    apalabel.place(x=200, y=200)
    pholabel = Label(rightFrame, text="Phone          : " + str(data[4]), font=('arial', 18), bg='white')
    pholabel.place(x=200, y=250)


def pay():
    def setpay():
        query="update payment set bill_paid_date=current_date where Apartment_id=%s"
        mycursor.execute(query,(data[5],))
        mydb.commit
        messagebox.showinfo('Success','Paid successful')
        pay()

    rightFrame = Frame(root, bg='white')
    rightFrame.place(x=350, y=80, width=1200, height=1000)
    mycursor.execute("select pay_id,bill_arrived_date,bill_paid_date,total_cost,mode_of_payment,payment.Apartment_id from residents,payment where residents.Apartment_id=payment.Apartment_id and Resident_id= %s",
        (res_id,))
    data = mycursor.fetchone()

    if len(data) == 0:
        messagebox.showinfo("No Bills", "Sorry!! You don't have any bills arrived yet!")
        return

    totlabel = Label(rightFrame, text="Bill id          : " + str(data[0]), font=('arial', 18), bg='white')
    totlabel.place(x=200, y=100)
    pidlabel = Label(rightFrame, text="Bill Arrive Date            : " + str(data[1]), font=('arial', 18), bg='white')
    pidlabel.place(x=200, y=150)
    aparlabel = Label(rightFrame, text="Bill Paid Date          : " + str(data[2]), font=('arial', 18), bg='white')
    aparlabel.place(x=200, y=200)
    tcostlabel = Label(rightFrame, text="Total Cost           : " + str(data[3]), font=('arial', 18), bg='white')
    tcostlabel.place(x=200, y=250)
    modelabel = Label(rightFrame, text="Payment Mode            : " + str(data[4]), font=('arial', 18), bg='white')
    modelabel.place(x=200, y=300)
    aplabel = Label(rightFrame, text="Apartment_Id             : " + str(data[5]), font=('arial', 18), bg='white')
    aplabel.place(x=200, y=350)


    if(data[2] is None):
        paycost_button = ttk.Button(rightFrame, text="PAY", command=setpay)
        paycost_button.place(x=300,y=500)



def park():
    rightFrame = Frame(root, bg='white')
    rightFrame.place(x=350, y=80, width=1200, height=1000)
    query='select * from parking_lot where Apartment_id in(select parking_lot.Apartment_id from residents inner join parking_lot on residents.Apartment_id=parking_lot.Apartment_id and Resident_id=%s)'
    mycursor.execute(query,(res_id,))
    data=mycursor.fetchone()

    if len(data) == 0:
        messagebox.showinfo("No Lifts", "Sorry!! Lifts not available!")
        return
    if data[1]==1:
        co='Vehicle Parked'
    else:
        co='Vehicle Not Parked'
    pidlabel = Label(rightFrame, text="Working Condition          : " +co, font=('arial', 18), bg='white')
    pidlabel.place(x=200, y=150)
    aparlabel = Label(rightFrame, text="Parking Id         : " + str(data[0]), font=('arial', 18), bg='white')
    aparlabel.place(x=200, y=200)
    tcostlabel = Label(rightFrame, text="Apartment id           : " + str(data[2]), font=('arial', 18), bg='white')
    tcostlabel.place(x=200, y=250)


def lift():
    rightFrame = Frame(root, bg='white')
    rightFrame.place(x=350, y=80, width=1200, height=1000)
    query='select * from lifts where Block_id in(select Block_id from residents inner join apartment on residents.Apartment_id=apartment.Apartment_id and Resident_id=%s)'
    mycursor.execute(query,(res_id,))
    data = mycursor.fetchone()

    if len(data) == 0:
        messagebox.showinfo("No Lifts", "Sorry!! Lifts not available!")
        return

    totlabel = Label(rightFrame, text="Lift id          : " + str(data[0]), font=('arial', 18), bg='white')
    totlabel.place(x=200, y=100)
    if data[1]==1:
        b='Good'
    else:
        b='Under repair'
    pidlabel = Label(rightFrame, text="Working Condition          : " + b, font=('arial', 18), bg='white')
    pidlabel.place(x=200, y=150)
    aparlabel = Label(rightFrame, text="Position          : " + str(data[2]), font=('arial', 18), bg='white')
    aparlabel.place(x=200, y=200)
    tcostlabel = Label(rightFrame, text="Block id           : " + str(data[3]), font=('arial', 18), bg='white')
    tcostlabel.place(x=200, y=250)


def exit():
    result = messagebox.askyesno('CONFIRM', 'DO YOU WANT TO LOG-OUT')
    if result:
        root.destroy()
        import login_page
    else:
        pass


def clock():
    date = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000, clock)

def idd():
    def submit():
        global res_id
        res_id = res_id_entry.get()
        idwin.destroy()
    idwin = Toplevel()
    idwin.grab_set()
    idwin.resizable(False, False)
    res_id_label = Label(idwin, text="Enter the Resident id:", font=('times new roman', 20, 'bold'))
    res_id_label.grid(row=0, column=0, padx=30, pady=15, stick=W)
    res_id_entry = Entry(idwin, font=('times new roman', 20, 'bold'), bd=5, fg='dark orange', width=24)
    res_id_entry.grid(row=0, column=1, pady=15, padx=10)
    submit_button = ttk.Button(idwin, text="Submit", command=submit)
    submit_button.grid(row=6, columnspan=2, pady=15)


count = 0
text = ''


def slider():
    global text, count
    if count == len(a):
        count = 0
        text = ''
    text = text + a[count]  # a
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(300, slider)

# GUI
root = ttkthemes.ThemedTk()

root.get_themes()
root.set_theme('radiance')

root.geometry('1474x750+0+0')
root.resizable(0, 0)
root.title('Apartment Management System')

datetimeLabel = Label(root, font=('times new roman', 18, 'bold'))
datetimeLabel.place(x=5, y=5)
clock()

a = 'Apartment Management System'
sliderLabel = Label(root, text=a, font=('arial', 28, 'italic bold'), width=50)
sliderLabel.place(x=200, y=0)
slider()

connectButton = ttk.Button(root, text='LOG OUT', command=exit)
connectButton.place(x=1300, y=0)

leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

logoimage = PhotoImage(file='resident.png')
logoLabel = Label(leftFrame, image=logoimage)
logoLabel.grid(row=0, column=0)

profilebutton = ttk.Button(leftFrame, text='PROFILE', cursor='hand2', width=20,command=profile)
profilebutton.grid(row=1, column=0, pady=20)
paybutton = ttk.Button(leftFrame, text='PAYMENT', cursor='hand2', width=20, command=pay)
paybutton.grid(row=3, column=0, pady=20)
parkbutton = ttk.Button(leftFrame, text='PARKING', cursor='hand2', width=20, command=park)
parkbutton.grid(row=5, column=0, pady=20)
liftbutton = ttk.Button(leftFrame, text='LIFT', cursor='hand2', width=20, command=lift)
liftbutton.grid(row=7, column=0, pady=20)
iddbutton = ttk.Button(leftFrame, text='CONNECT ID', cursor='hand2', width=20, command=idd)
iddbutton.grid(row=8, column=0, pady=20)

rightFrame = Frame(root, bg='white')
rightFrame.place(x=350, y=80, width=1200, height=1000)
tlabel = Label(rightFrame, text="WELCOME TO RESIDENT PAGE", font=('times new roman', 25, 'bold'), bg='white',
               fg='dark orange')
tlabel.place(x=300, y=250)
root.mainloop()