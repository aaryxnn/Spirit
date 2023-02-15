from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


global mycursor


def connect():
    global mycursor, con

    try:
        con = pymysql.connect(host='localhost', user='sqluser', password='password')
        mycursor = con.cursor()
    except:
        messagebox.showerror('Error', 'Invalid Details')
    try:
        query = 'create database studentmanagement'
        mycursor.execute(query)
        query = 'use studentmanagement'
        mycursor.execute(query)
        query = 'create table student(id int not null primary key, name varchar(40), dateOfBirth varchar(30), ' \
                'dateOfJoining varchar(30), mobile varchar(10), branch varchar(20),' \
                'beltRank varchar(20), proof varchar(20), address varchar(100)  )'
        mycursor.execute(query)
    except:
        query = 'use studentmanagement'
        mycursor.execute(query)
    messagebox.showinfo('Success', 'Data Connection is successful')
    addStudentBtn.config(state=NORMAL)
    searchStudentBtn.config(state=NORMAL)
    editStudentBtn.config(state=NORMAL)
    showStudentBtn.config(state=NORMAL)
    deleteStudentBtn.config(state=NORMAL)

def showStudent():
    query = 'select *from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)


def updateStudent():

    def updateData():
        query = '''update student set name=%s , dateOfBirth=%s ,dateOfJoining=%s , mobile=%s ,
                 branch=%s , proof=%s , address=%s where id=%s '''
        mycursor.execute(query, (name_Entry.get(), dob_Entry.get(), doj_Entry.get(), mobile_Entry.get(),
                         branch_Entry.get(), proof_Entry.get(), address_Entry.get(), id_Entry.get()))
        con.commit()
        messagebox.showinfo('Success', 'Student updated successfully')
        query = 'select *from student'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('', END, values=data)


    updatewindow = Toplevel()
    updatewindow.title('Search')
    backgroundLabel = Label(updatewindow, bg='LightBlue')
    backgroundLabel.place(x=0, y=0, relheight=1, relwidth=1)

    id_Label = Label(updatewindow, text="ID: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    id_Label.grid(row=1, column=0, pady=20, sticky=W)
    id_Entry = Entry(updatewindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    id_Entry.grid(row=1, column=1, padx=20)

    name_Label = Label(updatewindow, text="Name: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    name_Label.grid(row=2, column=0, pady=20, sticky=W)
    name_Entry = Entry(updatewindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    name_Entry.grid(row=2, column=1, padx=20)

    dob_Label = Label(updatewindow, text="Date of Birth: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    dob_Label.grid(row=3, column=0, pady=20, sticky=W)
    dob_Entry = Entry(updatewindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    dob_Entry.grid(row=3, column=1, padx=20)

    doj_Label = Label(updatewindow, text="Date of Joining: ", font=('helvetica', 18, 'bold'), fg='black',
                  bg='LightBlue')
    doj_Label.grid(row=4, column=0, pady=20, sticky=W)
    doj_Entry = Entry(updatewindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    doj_Entry.grid(row=4, column=1, padx=20)

    mobile_Label = Label(updatewindow, text="Mobile: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    mobile_Label.grid(row=5, column=0, pady=20, sticky=W)
    mobile_Entry = Entry(updatewindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    mobile_Entry.grid(row=5, column=1, padx=20)

    branch_Label = Label(updatewindow, text="Branch: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    branch_Label.grid(row=6, column=0, pady=20, sticky=W)
    branch_Entry = Entry(updatewindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    branch_Entry.grid(row=6, column=1, padx=20)

    proof_Label = Label(updatewindow, text="Proof: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    proof_Label.grid(row=7, column=0, pady=20, sticky=W)
    proof_Entry = Entry(updatewindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    proof_Entry.grid(row=7, column=1, padx=20)

    address_Label = Label(updatewindow, text="Address: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    address_Label.grid(row=8, column=0, pady=20, sticky=W)
    address_Entry = Entry(updatewindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    address_Entry.grid(row=8, column=1, padx=20)

    updatebtn = Button(updatewindow, text='Update Student', font=('helvetica', 18), width=10,
                       fg='DarkOrange3', activeforeground='DarkOrange3',
                       cursor='hand1', command=updateData)
    updatebtn.grid(row=9, columnspan=2, pady=20)

    indexing = studentTable.focus()
    content = studentTable.item(indexing)
    listdata = content['values']
    id_Entry.insert(0, listdata[0])
    name_Entry.insert(0, listdata[1])
    dob_Entry.insert(0, listdata[2])
    doj_Entry.insert(0, listdata[3])
    mobile_Entry.insert(0, listdata[4])
    branch_Entry.insert(0, listdata[5])
    proof_Entry.insert(0, listdata[6])
    address_Entry.insert(0, listdata[7])



def searchStudent():
    def searchData():
        query = 'select *from student where id=%s or name=%s or dateOfBirth=%s or dateOfJoining=%s or mobile=%s or ' \
                'branch=%s or proof=%s or address=%s'
        mycursor.execute(query, (id_Entry.get(), name_Entry.get(), dob_Entry.get(), doj_Entry.get(), mobile_Entry.get(),
                         branch_Entry.get(), proof_Entry.get(), address_Entry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data = mycursor.fetchall()
        if len(fetched_data) == 0:
            messagebox.showerror('Error', 'The searched value is not present')
        else:
            for data in fetched_data:
                studentTable.insert('', END, values=data)

    searchwindow = Toplevel()
    searchwindow.title('Search')
    backgroundLabel = Label(searchwindow, bg='LightBlue')
    backgroundLabel.place(x=0, y=0, relheight=1, relwidth=1)

    id_Label = Label(searchwindow, text="ID: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    id_Label.grid(row=1, column=0, pady=20, sticky=W)
    id_Entry = Entry(searchwindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    id_Entry.grid(row=1, column=1, padx=20)

    name_Label = Label(searchwindow, text="Name: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    name_Label.grid(row=2, column=0, pady=20, sticky=W)
    name_Entry = Entry(searchwindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    name_Entry.grid(row=2, column=1, padx=20)

    dob_Label = Label(searchwindow, text="Date of Birth: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    dob_Label.grid(row=3, column=0, pady=20, sticky=W)
    dob_Entry = Entry(searchwindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    dob_Entry.grid(row=3, column=1, padx=20)

    doj_Label = Label(searchwindow, text="Date of Joining: ", font=('helvetica', 18, 'bold'), fg='black',
                      bg='LightBlue')
    doj_Label.grid(row=4, column=0, pady=20, sticky=W)
    doj_Entry = Entry(searchwindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    doj_Entry.grid(row=4, column=1, padx=20)

    mobile_Label = Label(searchwindow, text="Mobile: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    mobile_Label.grid(row=5, column=0, pady=20, sticky=W)
    mobile_Entry = Entry(searchwindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    mobile_Entry.grid(row=5, column=1, padx=20)

    branch_Label = Label(searchwindow, text="Branch: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    branch_Label.grid(row=6, column=0, pady=20, sticky=W)
    branch_Entry = Entry(searchwindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    branch_Entry.grid(row=6, column=1, padx=20)

    proof_Label = Label(searchwindow, text="Proof: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    proof_Label.grid(row=7, column=0, pady=20, sticky=W)
    proof_Entry = Entry(searchwindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    proof_Entry.grid(row=7, column=1, padx=20)

    address_Label = Label(searchwindow, text="Address: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    address_Label.grid(row=8, column=0, pady=20, sticky=W)
    address_Entry = Entry(searchwindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    address_Entry.grid(row=8, column=1, padx=20)

    searchbtn = Button(searchwindow, text='Search Student', font=('helvetica', 18), width=10,
                       fg='DarkOrange3', activeforeground='DarkOrange3',
                       cursor='hand1', command=searchData)
    searchbtn.grid(row=9, columnspan=2, pady=20)


def deleteStudent():
    indexing = studentTable.focus()
    content = studentTable.item(indexing)
    contentId= content['values'][0]
    query = 'delete from student where id=%s'
    mycursor.execute(query, contentId)
    con.commit()
    query = 'select *from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)

def addStudent():
    def addData():
        if idEntry.get()=='' or nameEntry.get() == '' or dobEntry.get() == '' or dojEntry.get() == '' or \
                proofEntry.get() == '' or addressEntry.get() == '' or branchEntry.get() == '' or \
                mobileEntry.get() == '' \
                or beltEntry.get() == '':
            messagebox.showerror('Error', 'Fields cannot be empty')
        else:
            try:
                query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query, (idEntry.get(), nameEntry.get(), dobEntry.get(), dojEntry.get(),
                                         mobileEntry.get(), branchEntry.get(),beltEntry.get()
                                         ,proofEntry.get(), addressEntry.get()))
                con.commit()
                rs = messagebox.askyesno('Confirmation', 'Student added successfully. Do you want to clean the form?')
                if rs:
                    idEntry.delete(0,END)
                    nameEntry.delete(0, END)
                    dobEntry.delete(0, END)
                    dojEntry.delete(0, END)
                    mobileEntry.delete(0, END)
                    branchEntry.delete(0, END)
                    beltEntry.delete(0, END)
                    proofEntry.delete(0, END)
                    addressEntry.delete(0, END)
                else:
                    pass
            except:
                messagebox.showerror('Error', 'ID cannot be repeated again')
                return

        query=('select *from student')
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            datalist=list(data)
            studentTable.insert('', END, values=datalist, )

    updatewindow = Toplevel()
    updatewindow.title('Search')
    backgroundLabel = Label(updatewindow, bg='LightBlue')
    backgroundLabel.place(x=0, y=0, relheight=1, relwidth=1)

    id_Label = Label(updatewindow, text="ID: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    id_Label.grid(row=1, column=0, pady=20, sticky=W)
    idEntry = Entry(updatewindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    idEntry.grid(row=1, column=1, padx=20)

    name_Label = Label(updatewindow, text="Name: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    name_Label.grid(row=2, column=0, pady=20, sticky=W)
    nameEntry = Entry(updatewindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    nameEntry.grid(row=2, column=1, padx=20)

    dob_Label = Label(updatewindow, text="Date of Birth: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    dob_Label.grid(row=3, column=0, pady=20, sticky=W)
    dobEntry = Entry(updatewindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    dobEntry.grid(row=3, column=1, padx=20)

    doj_Label = Label(updatewindow, text="Date of Joining: ", font=('helvetica', 18, 'bold'), fg='black',
                      bg='LightBlue')
    doj_Label.grid(row=4, column=0, pady=20, sticky=W)
    dojEntry = Entry(updatewindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    dojEntry.grid(row=4, column=1, padx=20)

    mobile_Label = Label(updatewindow, text="Mobile: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    mobile_Label.grid(row=5, column=0, pady=20, sticky=W)
    mobileEntry = Entry(updatewindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    mobileEntry.grid(row=5, column=1, padx=20)

    branch_Label = Label(updatewindow, text="Branch: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    branch_Label.grid(row=6, column=0, pady=20, sticky=W)
    branchEntry = Entry(updatewindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    branchEntry.grid(row=6, column=1, padx=20)

    belt_Label = Label(updatewindow, text="Belt: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    belt_Label.grid(row=7, column=0, pady=20, sticky=W)
    beltEntry = Entry(updatewindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    beltEntry.grid(row=7, column=1, padx=20)

    proof_Label = Label(updatewindow, text="Proof: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    proof_Label.grid(row=8, column=0, pady=20, sticky=W)
    proofEntry = Entry(updatewindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    proofEntry.grid(row=8, column=1, padx=20)

    address_Label = Label(updatewindow, text="Address: ", font=('helvetica', 18, 'bold'), fg='black', bg='LightBlue')
    address_Label.grid(row=9, column=0, pady=20, sticky=W)
    addressEntry = Entry(updatewindow, font=('helvetica', 18), bd=3, fg='orange', width=18)
    addressEntry.grid(row=9, column=1, padx=20)

    addbtn = Button(updatewindow, text='Add Student', font=('helvetica', 18), width=10,
                    fg='DarkOrange3', activeforeground='DarkOrange3',
                    cursor='hand1', height=2, command=addData)
    addbtn.grid(row=10, columnspan=2, pady=20)



def exit():
    window.destroy()
    import menu

def exit_func():
    window.destroy()
    import equipmentOrder

window = Tk()
window.geometry('1440x840+0+0')
window.title('Student Page')

backgroundLabel = Label(window, bg='LightBlue')
backgroundLabel.place(x=0, y=0, relheight=1, relwidth=1)

studentLabel = Label(window, text='Student Management', font=('Helvetica', 30, 'bold'), bg='LightBlue', fg='black')
studentLabel.grid(row=0, column=0, padx=570, pady=40)

connectButton = Button(window, text='Connect Database', font=('helvetica', 18), width=15, height=1,
                       fg='DarkOrange3', activeforeground='DarkOrange3',
                       cursor='hand1', command=connect)
connectButton.place(x=1170, y=40)

leftFrame = Frame(window, bg="LightBlue")
leftFrame.place(x=50, y=90, width=350, height=700)

logo_image = PhotoImage(file='Logo.png')
logoLabel = Label(leftFrame, image=logo_image)
logoLabel.grid(row=0, column=0)

addStudentBtn = Button(leftFrame, text='Add Student', font=('helvetica', 18), width=17,height=2,
                       fg='DarkOrange3', activeforeground='DarkOrange3',
                       cursor='hand1', state=DISABLED, command=addStudent)
addStudentBtn.grid(row=1, column=0, pady=27)

searchStudentBtn = Button(leftFrame, text='Search Student', font=('helvetica', 18), width=17,height=2,
                          fg='DarkOrange3', activeforeground='DarkOrange3',
                          cursor='hand1',state=DISABLED, command=searchStudent)
searchStudentBtn.grid(row=2, column=0, pady=27)

deleteStudentBtn = Button(leftFrame, text='Delete Student', font=('helvetica', 18), width=17,height=2,
                          fg='DarkOrange3', activeforeground='DarkOrange3',
                          cursor='hand1', state=DISABLED, command=deleteStudent)
deleteStudentBtn.grid(row=3, column=0, pady=27)

editStudentBtn = Button(leftFrame, text='Edit Student', font=('helvetica', 18), width=17,height=2,
                        fg='DarkOrange3', activeforeground='DarkOrange3',
                        cursor='hand1', state=DISABLED, command=updateStudent)
editStudentBtn.grid(row=4, column=0, pady=27)

showStudentBtn = Button(leftFrame, text='Show Students', font=('helvetica', 18), width=17,height=2,
                        fg='DarkOrange3', activeforeground='DarkOrange3',
                        cursor='hand1', state=DISABLED, command=showStudent)
showStudentBtn.grid(row=5, column=0, pady=27)

exitStudentBtn = Button(window, text='Equipment Order', font=('helvetica', 18), width=11,
                        fg='DarkOrange3', activeforeground='DarkOrange3',
                        cursor='hand1', command=exit_func)
exitStudentBtn.place(x=10, y=750)

exitStudentBtn = Button(window, text='Exit', font=('helvetica', 18), width=7,
                        fg='DarkOrange3', activeforeground='DarkOrange3',
                        cursor='hand1', command=exit)
exitStudentBtn.place(x=220, y=750)

rightFrame = Frame(window, bg="LightBlue")
rightFrame.place(x=350, y=90, width=1050, height=700)

scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

studentTable = ttk.Treeview(rightFrame, columns=('ID', 'Name', 'Date of Birth', 'Date of Joining', 'Mobile Number',
                                                 'Branch','Belt' ,'ID Proof', 'Address')
                            , xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

studentTable.place(width=1035, height=685)

studentTable.heading('ID', text='Sr No.')
studentTable.heading('Name', text='Name')
studentTable.heading('Date of Birth', text='Date of Birth')
studentTable.heading('Date of Joining', text='Date of Joining')
studentTable.heading('Mobile Number', text='Mobile No.')
studentTable.heading('Branch', text='Branch')
studentTable.heading('Belt', text='Belt')
studentTable.heading('ID Proof', text='ID Proof')
studentTable.heading('Address', text='Address')

studentTable.config(show='headings')

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)

window.mainloop()
