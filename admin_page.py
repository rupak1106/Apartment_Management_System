import tkinter
from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
from atexit import register
from doctest import master
from PIL import ImageTk
import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
username="root",
passwd="ram9486",
database="apart"
)
if mydb.is_connected():
 print("connection established")
mycursor=mydb.cursor()



def exit():
    result=messagebox.askyesno('CONFIRM','DO YOU WANT TO LOG-OUT')
    if result:
        root.destroy()
        import admin_login
    else:
        pass

def clock():
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000,clock)

def addapp():
    def add_data():
        global mycursor,mydb
        if floorEntry.get()=='' or priceEntry.get()=='' or BlockEntry.get()=='':
            messagebox.showerror('Error','All fields are required',parent=addwin)
       # else if(Number.isdigit(idEntry.get()) and floorEntry.isdigit() and priceEntry.isdigit() and BlockEntry.isdigit()):
        else:

            query='insert into apartment(Apartment_id,floor_number,price,block_id) values(%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(),floorEntry.get(),priceEntry.get(),BlockEntry.get()))
            result=messagebox.askyesno('Confirm','Data added successfully.Do you want to make any change?',parent=addwin)
            if result:
                idEntry.delete(0,END)
                floorEntry.delete(0,END)
                priceEntry.delete(0,END)
                BlockEntry.delete(0,END)
            else:
                pass
                mydb.commit()

            #for x,user,y,s in enumerate(mycursor.execute()):


    addwin=Toplevel()
    addwin.grab_set()
    addwin.resizable(False,False)
    idLabel=Label(addwin,text='Appartment_id',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,stick=W)
    idEntry=Entry(addwin,font=('times new roman', 20, 'bold'), bd=5, fg='dark orange',width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    floorLabel = Label(addwin, text='Floor no', font=('times new roman', 20, 'bold'))
    floorLabel.grid(row=2, column=0, padx=30, pady=15,stick=W)
    floorEntry = Entry(addwin, font=('times new roman', 20, 'bold'), bd=5, fg='dark orange',width=24)
    floorEntry.grid(row=2, column=1, pady=15, padx=10)

    priceLabel = Label(addwin, text='Price', font=('times new roman', 20, 'bold'))
    priceLabel.grid(row=4, column=0, padx=30, pady=15,stick=W)
    priceEntry = Entry(addwin,font=('times new roman', 20, 'bold'), bd=5, fg='dark orange',width=24)
    priceEntry.grid(row=4, column=1, pady=15, padx=10)

    BlockLabel = Label(addwin, text='Block_id', font=('times new roman', 20, 'bold'))
    BlockLabel.grid(row=6, column=0, padx=30, pady=15,stick=W)
    BlockEntry = Entry(addwin, font=('times new roman', 20, 'bold'), bd=5, fg='dark orange',width=24)
    BlockEntry.grid(row=6, column=1, pady=15, padx=10)

    addbutton=ttk.Button(addwin,text='SUBMIT',command=add_data)
    addbutton.grid(row=7,columnspan=2,pady=15)

def addres():
    def add_rdata():
        global mycursor,mydb
        apid = apidEntry.get()
        query=f"select Apartment_id from apartment where Apartment_id='{apid}'"
        mycursor.execute(query)
        row = mycursor.fetchone()
        if row is None:
                messagebox.showerror('Error','Apartment not Avilable ')
                addresidwin.destroy()

        if ridEntry.get()=='' or nameEntry.get()=='' or apidEntry.get()=='' or ageEntry.get()=='' or phoneEntry.get()=='':
            messagebox.showerror('Error','All fields are required',parent=addresidwin)
       # else if(Number.isdigit(idEntry.get()) and floorEntry.isdigit() and priceEntry.isdigit() and BlockEntry.isdigit()):
        try:

            query='insert into residents(Resident_id,name,Apartment_id,age,phone) values(%s,%s,%s,%s,%s)'
            mycursor.execute(query,(ridEntry.get(),nameEntry.get(),apidEntry.get(),ageEntry.get(),phoneEntry.get()))
            result=messagebox.askyesno('Confirm','Data added successfully.Do you want to make any change?',parent=addresidwin)
            if result:
                ridEntry.delete(0,END)
                nameEntry.delete(0,END)
                ageEntry.delete(0,END)
                apidEntry.delete(0,END)
                phoneEntry.delete(0,END)
            else:
                pass
                mydb.commit()
        except:
            messagebox.showerror('Error','Id cannot be repeted',parent=addresidwin)
            return

        query='select * from residents'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        resTable.delete(*resTable.get_children())

        for data in fetched_data:
                datalist=list(data)
                resTable.insert('',END,values=datalist)

            #for x,user,y,s in enumerate(mycursor.execute()):



    addresidwin=Toplevel()
    addresidwin.grab_set()
    addresidwin.resizable(False,False)
    ridLabel=Label(addresidwin,text='Resident_id',font=('times new roman',20,'bold'))
    ridLabel.grid(row=0,column=0,padx=30,pady=15,stick=W)
    ridEntry=Entry(addresidwin,font=('times new roman', 20, 'bold'), bd=5, fg='dark orange',width=24)
    ridEntry.grid(row=0,column=1,pady=15,padx=10)

    nameLabel = Label(addresidwin, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=2, column=0, padx=30, pady=15,stick=W)
    nameEntry = Entry(addresidwin, font=('times new roman', 20, 'bold'), bd=5, fg='dark orange',width=24)
    nameEntry.grid(row=2, column=1, pady=15, padx=10)

    ageLabel = Label(addresidwin, text='Age', font=('times new roman', 20, 'bold'))
    ageLabel.grid(row=4, column=0, padx=30, pady=15,stick=W)
    ageEntry = Entry(addresidwin,font=('times new roman', 20, 'bold'), bd=5, fg='dark orange',width=24)
    ageEntry.grid(row=4, column=1, pady=15, padx=10)

    phoneLabel = Label(addresidwin, text='Phone_no', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=6, column=0, padx=30, pady=15,stick=W)
    phoneEntry = Entry(addresidwin, font=('times new roman', 20, 'bold'), bd=5, fg='dark orange',width=24)
    phoneEntry.grid(row=6, column=1, pady=15, padx=10)

    apidLabel = Label(addresidwin, text='Apartment_id', font=('times new roman', 20, 'bold'))
    apidLabel.grid(row=8, column=0, padx=30, pady=15, stick=W)
    apidEntry = Entry(addresidwin, font=('times new roman', 20, 'bold'), bd=5, fg='dark orange', width=24)
    apidEntry.grid(row=8, column=1, pady=15, padx=10)

    addbutton=ttk.Button(addresidwin,text='SUBMIT',command=add_rdata)
    addbutton.grid(row=9,columnspan=2,pady=15)

count=0
text=''

    #def update_entry_state(mode):
     #   if mode == "Yes":
     #       p_date_entry.config(state=tkinter.NORMAL)
     #       mode_entry.config(state=tkinter.NORMAL)
     #       ref_id_entry.config(state=tkinter.NORMAL)
     #   else:
      #      p_date_entry.delete(0,tkinter.END)
       #     p_date_entry.config(state=tkinter.DISABLED)
     #       mode_entry.delete(0, tkinter.END)
      #      mode_entry.config(state=tkinter.DISABLED)
      #      ref_id_entry.delete(0, tkinter.END)
       #     ref_id_entry.config(state=tkinter.DISABLED)'''
def editpay():

        def submit():
            apartment_id = apartment_id_entry.get()
            a_id = int(apartment_id)
            a_date = a_date_entry.get()
            cost = total_cost_entry.get()
            query = 'INSERT INTO payment (bill_arrived_date, total_cost, Apartment_id) VALUES (%s, %s, %s)'
            values = (a_date, cost, a_id)

            try:

                mycursor.execute(query, values)
                mydb.commit()
                messagebox.showinfo("Success", "Subscription added successfully")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", str(e))
            finally:
                if mycursor:
                    mycursor.close()


        edpaywin = Toplevel()
        edpaywin.grab_set()
        edpaywin.resizable(False, False)
        apartment_id_label = Label(edpaywin, text="Enter the apartment id:",font=('times new roman',20,'bold'))
        apartment_id_label.grid(row=0,column=0,padx=30,pady=15,stick=W)
        apartment_id_entry = Entry(edpaywin,font=('times new roman', 20, 'bold'), bd=5, fg='dark orange',width=24)
        apartment_id_entry.grid(row=0,column=1,pady=15,padx=10)

        a_date_label = Label(edpaywin, text="Enter the Bill Arrived Date:",font=('times new roman',20,'bold'))
        a_date_label.grid(row=2,column=0,padx=30,pady=15,stick=W)
        a_date_entry = Entry(edpaywin,font=('times new roman', 20, 'bold'), bd=5, fg='dark orange',width=24)
        a_date_entry.grid(row=2,column=1,pady=15,padx=10)

        total_cost_label = Label(edpaywin, text="Enter the total cost:",font=('times new roman',20,'bold'))
        total_cost_label.grid(row=4,column=0,padx=30,pady=15,stick=W)
        total_cost_entry = Entry(edpaywin,font=('times new roman', 20, 'bold'), bd=5, fg='dark orange',width=24)
        total_cost_entry.grid(row=4,column=1,pady=15,padx=10)

        submit_button=ttk.Button(edpaywin,text="Submit",command=submit)
        submit_button.grid(row=6,columnspan=2,pady=15)


def parking():
    global mycursor, mydb
    def topparkin():
        pkwin = Toplevel()
        pkwin.title('Unpayed bills')
        pkwin.grab_set()
        pkwin.resizable(False, False)
        # upiwin = Frame(root, bg='white')
        # upiwin.place(x=350, y=80, width=1100, height=650)
        scrollbarx = Scrollbar(pkwin, orient=HORIZONTAL)
        scrollbary = Scrollbar(pkwin, orient=VERTICAL)
        parktreeTable = ttk.Treeview(pkwin, columns=('Parking_lot_id', 'Parking_status','Apartment_id'),
                                  xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        scrollbarx.config(command=parktreeTable.xview)
        scrollbary.config(command=parktreeTable.yview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=RIGHT, fill=Y)
        parktreeTable.pack(fill=BOTH, expand=1)

        parktreeTable.heading('Parking_lot_id', text='Parking_lot_id')
        parktreeTable.heading('Parking_status', text='Parking_status')
        parktreeTable.heading('Apartment_id', text='Apartment_id')

        parktreeTable.column('Parking_lot_id', width=50, anchor=CENTER)
        parktreeTable.column('Apartment_id', width=200, anchor=CENTER)
        parktreeTable.column('Parking_status', width=200, anchor=CENTER)

        style = ttk.Style()
        style.configure('Treeview', rowheight=40, font=('arial', 12, 'bold'), foreground='black', background='white'
                        , fieldbackground='white')
        style.configure('Treeview.Heading', font=('arial', 14, 'bold'))
        parktreeTable.config(show='headings')

        query = 'select * from parking_lot'
        mycursor.execute(query)

        parktreeTable.delete(*parktreeTable.get_children())
        fetchdata = mycursor.fetchall()
        for data in fetchdata:
            parktreeTable.insert('', END, values=data)



    def submit():
        choice = parking_status_var.get()
        a_id = apartment_id_entry.get()
        query = "INSERT INTO Parking_lot (parking_status, Apartment_id) VALUES (%s, %s)"
        mycursor.execute(query, (choice, a_id))

        mydb.commit()
        messagebox.showinfo("Success", "Parking entry added successfully.")
        topparkin()

    parkwin = Toplevel()
    parkwin.grab_set()
    parkwin.resizable(False, False)

    apartment_id_label = Label(parkwin, text="Enter the apartment id:", font=('times new roman', 20, 'bold'))
    apartment_id_label.grid(row=0, column=0, padx=30, pady=15, stick=W)
    apartment_id_entry = Entry(parkwin, font=('times new roman', 20, 'bold'), bd=5, fg='dark orange', width=24)
    apartment_id_entry.grid(row=0, column=1, pady=15, padx=10)

    parking_status_label = Label(parkwin, text="Parking Status (1 for available, 0 for occupied):")
    parking_status_label.grid(row=2, column=0, padx=30, pady=15, stick=W)
    parking_status_var = IntVar()
    park_status_radio1 = ttk.Radiobutton(parkwin, text="Yes", variable=parking_status_var , value=1)
    park_status_radio1.grid(row=2, column=1, pady=15, padx=2)
    park_status_radio2 = ttk.Radiobutton(parkwin, text="No", variable=parking_status_var , value=0)
    park_status_radio2.grid(row=2, column=2, pady=15, padx=2)

    submit_button = ttk.Button(parkwin, text="Submit", command=submit)
    submit_button.grid(row=3, columnspan=2, pady=15)

def searchres():
    def search_rdata():
        global mycursor, mydb
        query='select * from residents where Resident_id=%s or name=%s or Apartment_id=%s or age=%s or phone=%s '
        mycursor.execute(query,(ridEntry.get(),nameEntry.get(),apidEntry.get(),ageEntry.get(),phoneEntry.get()))
        resTable.delete(*resTable.get_children())
        fetchdata=mycursor.fetchall()
        for data in fetchdata:
            resTable.insert('',END,values=data)


    searchwin = Toplevel()
    searchwin.title('Search resident')
    searchwin.grab_set()
    searchwin.resizable(False, False)
    ridLabel = Label(searchwin, text='Resident_id', font=('times new roman', 20, 'bold'))
    ridLabel.grid(row=0, column=0, padx=30, pady=15, stick=W)
    ridEntry = Entry(searchwin, font=('times new roman', 20, 'bold'), bd=5, fg='dark orange', width=24)
    ridEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(searchwin, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=2, column=0, padx=30, pady=15, stick=W)
    nameEntry = Entry(searchwin, font=('times new roman', 20, 'bold'), bd=5, fg='dark orange', width=24)
    nameEntry.grid(row=2, column=1, pady=15, padx=10)

    ageLabel = Label(searchwin, text='Age', font=('times new roman', 20, 'bold'))
    ageLabel.grid(row=4, column=0, padx=30, pady=15, stick=W)
    ageEntry = Entry(searchwin, font=('times new roman', 20, 'bold'), bd=5, fg='dark orange', width=24)
    ageEntry.grid(row=4, column=1, pady=15, padx=10)

    phoneLabel = Label(searchwin, text='Phone_no', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=6, column=0, padx=30, pady=15, stick=W)
    phoneEntry = Entry(searchwin, font=('times new roman', 20, 'bold'), bd=5, fg='dark orange', width=24)
    phoneEntry.grid(row=6, column=1, pady=15, padx=10)

    apidLabel = Label(searchwin, text='Apartment_id', font=('times new roman', 20, 'bold'))
    apidLabel.grid(row=8, column=0, padx=30, pady=15, stick=W)
    apidEntry = Entry(searchwin, font=('times new roman', 20, 'bold'), bd=5, fg='dark orange', width=24)
    apidEntry.grid(row=8, column=1, pady=15, padx=10)

    addbutton = ttk.Button(searchwin, text='SEARCH', command=search_rdata)
    addbutton.grid(row=9, columnspan=2, pady=15)

def deleteres():

    selitem=resTable.selection()[0]
    rid=resTable.item(selitem)['values'][0]
    query='delete from residents where Resident_id= %s '
    seldata=(rid,)
    mycursor.execute(query,seldata)
    mydb.commit()
    messagebox.showinfo('Deleted',f'resident {rid} is deleted ')
    query1='select * from residents'
    mycursor.execute(query1)
    fetchdata=mycursor.fetchall()
    resTable.delete(*resTable.get_children())
    for data in fetchdata:
        resTable.insert('',END,values=data)

def viewall():

    query1 = 'select * from residents'
    mycursor.execute(query1)
    fetchdata = mycursor.fetchall()
    resTable.delete(*resTable.get_children())
    for data in fetchdata:
        resTable.insert('', END, values=data)

def unpaybill():
    upiwin = Toplevel()
    upiwin.title('Unpayed bills')
    upiwin.grab_set()
    upiwin.resizable(False, False)
    #upiwin = Frame(root, bg='white')
    #upiwin.place(x=350, y=80, width=1100, height=650)
    scrollbarx = Scrollbar(upiwin, orient=HORIZONTAL)
    scrollbary = Scrollbar(upiwin, orient=VERTICAL)

    unpayTable = ttk.Treeview(upiwin, columns=('Pay_id', 'Apartment_id','Arrived_date','Total_cost'),
                            xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
    scrollbarx.config(command=unpayTable.xview)
    scrollbary.config(command=unpayTable.yview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    scrollbary.pack(side=RIGHT, fill=Y)
    unpayTable.pack(fill=BOTH, expand=1)

    unpayTable.heading('Pay_id', text='Pay_id')
    unpayTable.heading('Apartment_id', text='Apartment_id')
    unpayTable.heading('Arrived_date', text='Arrived_date')
    unpayTable.heading('Total_cost', text='Total_cost')

    unpayTable.column('Pay_id', width=50, anchor=CENTER)
    unpayTable.column('Apartment_id', width=200, anchor=CENTER)
    unpayTable.column('Arrived_date', width=200, anchor=CENTER)
    unpayTable.column('Total_cost', width=100, anchor=CENTER)

    style = ttk.Style()
    style.configure('Treeview', rowheight=40, font=('arial', 12, 'bold'), foreground='black', background='white'
                    , fieldbackground='white')
    style.configure('Treeview.Heading', font=('arial', 14, 'bold'))
    unpayTable.config(show='headings')

    query = 'select pay_id,Apartment_id,bill_arrived_date,total_cost from payment where bill_paid_date is null and pay_id is not null'
    mycursor.execute(query)

    unpayTable.delete(*unpayTable.get_children())
    fetchdata = mycursor.fetchall()
    for data in fetchdata:
        unpayTable.insert('', END, values=data)



def slider():
    global text,count
    if count==len(a):
        count=0
        text=''
    text=text+a[count]#a
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(300,slider)


root=ttkthemes.ThemedTk()

root.get_themes()
root.set_theme('radiance')

root.geometry('1474x750+0+0')
root.resizable(0,0)
root.title('Apartment Management System')

datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()

a='Apartment Management System'
sliderLabel=Label(root,text=a,font=('arial',28,'italic bold'),width=50)
sliderLabel.place(x=200,y=0)
slider()

connectButton=ttk.Button(root,text='LOG OUT',command=exit)
connectButton.place(x=1300,y=0)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logoimage=PhotoImage(file='resident.png')
logoLabel=Label(leftFrame,image=logoimage)
logoLabel.grid(row=0,column=0)

addflatbutton=ttk.Button(leftFrame,text='Add Appartment',cursor='hand2',width=20,command=addapp)
addflatbutton.grid(row=1,column=0,pady=10)
adresibutton=ttk.Button(leftFrame,text='Add new resident',cursor='hand2',width=20,command=addres)
adresibutton.grid(row=2,column=0,pady=10)
adpaybutton=ttk.Button(leftFrame,text='Add Pay cost',cursor='hand2',width=20,command=editpay)
adpaybutton.grid(row=3,column=0,pady=10)
parkbutton=ttk.Button(leftFrame,text='Edit Parking',cursor='hand2',width=20,command=parking)
parkbutton.grid(row=4,column=0,pady=10)
vunpaybutton=ttk.Button(leftFrame,text='View Unpaid bills',cursor='hand2',width=20,command=unpaybill)
vunpaybutton.grid(row=5,column=0,pady=10)
vallresbutton=ttk.Button(leftFrame,text='View All Residents',cursor='hand2',width=20,command=viewall)
vallresbutton.grid(row=6,column=0,pady=10)
searchbutton=ttk.Button(leftFrame,text='Search Resident',cursor='hand2',width=20,command=searchres)
searchbutton.grid(row=7,column=0,pady=10)
deleresbutton=ttk.Button(leftFrame,text='Delete Resident',cursor='hand2',width=20,command=deleteres)
deleresbutton.grid(row=8,column=0,pady=10)


rightFrame = Frame(root, bg='white')
rightFrame.place(x=350, y=80, width=1100, height=650)
scrollbarx = Scrollbar(rightFrame,orient=HORIZONTAL)
scrollbary = Scrollbar(rightFrame,orient=VERTICAL)

resTable=ttk.Treeview(rightFrame,columns=('Resident_id','Name','Apartment_id','Age','Contact.no'),
                      xscrollcommand=scrollbarx.set,yscrollcommand=scrollbary.set)
scrollbarx.config(command=resTable.xview)
scrollbary.config(command=resTable.yview)
scrollbarx.pack(side=BOTTOM,fill=X)
scrollbary.pack(side=RIGHT,fill=Y)
resTable.pack(fill=BOTH,expand=1)

resTable.heading('Resident_id',text='Resident_id')
resTable.heading('Name',text='Name')
resTable.heading('Apartment_id',text='Apartment_id')
resTable.heading('Age',text='Age')
resTable.heading('Contact.no',text='Contact.no')

resTable.column('Resident_id',width=50,anchor=CENTER)
resTable.column('Name',width=300,anchor=CENTER)
resTable.column('Apartment_id',width=200,anchor=CENTER)
resTable.column('Age',width=100,anchor=CENTER)
resTable.column('Contact.no',width=200,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=40,font=('arial',12,'bold'),foreground='black',background='white'
                ,fieldbackground='white')
style.configure('Treeview.Heading',font=('arial',14,'bold'))
resTable.config(show='headings')
root.mainloop()