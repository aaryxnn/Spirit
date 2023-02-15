from tkinter import *  # from turtle import bg_color

def exit():
    window.destroy()


def student():
    window.destroy()
    import studentF


def equipmentOrder():
    window.destroy()
    import equipmentOrder

window = Tk()
window.geometry('1440x840+0+0')
window.title('Menu Page')

backgroundLabel = Label(window, bg='LightBlue')
backgroundLabel.place(x=0, y=0, relheight=1, relwidth=1)

menuLabel = Label(window, text='Menu Page', font=('Helvetica', 30, 'bold'), bg='LightBlue', fg='black')
menuLabel.grid(row=0, column=0, padx=650, pady=40)

menuFrame2 = Frame(window, bg="orange2")
menuFrame2.place(x=560, y=265)  # 310

students_btn = Button(menuFrame2, text='Students', font=('helvetica', 25), width=20, height=2,
                      fg='DarkOrange3', activeforeground='DarkOrange3',
                      cursor='hand1', command=student)
students_btn.grid(row=2, column=0)

menuFrame4 = Frame(window, bg="orange2")
menuFrame4.place(x=560, y=440)  # 600

Equipment_btn = Button(menuFrame4, text='Equipment Order', font=('helvetica', 25), width=20, height=2,
                       fg='DarkOrange3', bg='LightBlue', activeforeground='DarkOrange3',
                       cursor='hand1', command=equipmentOrder)
Equipment_btn.grid(row=4, column=0)

exitButton = Button(window, text="Exit", font=('helvetica', 25), width=10, command=exit)
exitButton.place(x=20, y=750)


window.mainloop()
