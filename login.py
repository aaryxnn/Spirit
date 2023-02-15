from tkinter import *
from tkinter import messagebox

#login function


def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Field cannot be empty')
    elif usernameEntry.get() == 'Admin' and passwordEntry.get() == '1234':
        messagebox.showinfo('Success', 'Login Successful')
        window.destroy()
        import menu
    else:
        messagebox.showerror('Error', 'Enter valid credentials')

#Show pass word function


def show_password():
    if passwordEntry.cget('show') == '*':
        passwordEntry.config(show= '')
    else:
        passwordEntry.config(show='*')


window = Tk() #creating window
window.geometry('1365x820+0+0') #assigning geometrical values
window.title('Login Page') #title

backgroundLabel= Label(window, bg='LightBlue') #creating background
backgroundLabel.place(x=0, y=0, relwidth = 1, relheight = 1)


loginFrame = Frame(window, bg="LightBlue") #creating login frame
loginFrame.place(x=450, y=225)

logoImage = PhotoImage(file='Logo.png')  #Adding image
logoLabel = Label(loginFrame, image=logoImage)
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)  #placing

#Username labelling and adding entry fields
usernameLabel = Label(loginFrame, text="Username", font=('helvetica', 25, 'bold'), fg='black', bg='LightBlue')
usernameLabel.grid(row=1, column=0, pady=10, padx=10)

usernameEntry = Entry(loginFrame, font=('helvetica', 20), bd=5, fg='orange')
usernameEntry.grid(row=1, column=1, pady=10, padx=10)

#Password labelling and adding entry fields
passwordLabel = Label(loginFrame, text="Password",
                      font=('helvetica', 25, 'bold'), fg='black', bg='LightBlue')
passwordLabel.grid(row=2, column=0, pady=10, padx=10)

#Adding the show password button
showHideButton = Checkbutton(loginFrame, text='Show Password', command=show_password, bg= 'LightBlue', fg= 'black')
showHideButton.grid(row=2, column=2)

passwordEntry = Entry(loginFrame, font=('helvetica', 20), bd=5, fg='orange', show= '*')
passwordEntry.grid(row=2, column=1, pady=10, padx=10)

#Login button
loginButton = Button(loginFrame, text='Login', font=('helvetica', 15), width=10,
                     fg='DarkOrange3', bg='orange',  activeforeground='DarkOrange3',
                     cursor='hand1', command=login)
loginButton.grid(row=3, column=2, pady=10)

window.mainloop()
