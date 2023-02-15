from tkinter import *
from tkinter import ttk
import random, os
from tkinter import messagebox




window=Tk()
window.geometry('1440x840+0+0')
window.title('Student Page')

#=======Variables======
c_name=StringVar()
c_phone=StringVar()
z = random.randint(1000, 99999)
bill_no=StringVar()
bill_no.set(str(z))
c_email=StringVar()
search_bill = StringVar()
brand = StringVar()
prices = IntVar()
qty = IntVar()
total = StringVar()

def clearBill():
    billText.delete(1.0, END)
    c_name.set("")
    c_phone.set("")
    c_email.set("")
    z = random.randint(1000, 9999)
    bill_no.set(str(z))
    brand.set("")
    prices.set(0)
    qty.set(0)
    total.set("")
    welcome()

def Categories(event=""):
    if categoryCombo.get() == 'Uniforms':
        typeCombo.config(values=UniformType)
        typeCombo.current(0)

    if categoryCombo.get() == 'Equipments':
        typeCombo.config(values=equipmentType)
        typeCombo.current(0)

def Type(event=""):
    if typeCombo.get() == 'Poomsae':
        BrandCombo.config(values=Poomsae)
        BrandCombo.current(0)

    if typeCombo.get() == 'Sparring':
        BrandCombo.config(values=Sparring)
        BrandCombo.current(0)

    if typeCombo.get() == 'Guards':
        BrandCombo.config(values=Guards)
        BrandCombo.current(0)

    if typeCombo.get() == 'Chest Guard':
        BrandCombo.config(values=Cguard)
        BrandCombo.current(0)

    if typeCombo.get() == 'Mittpads':
        BrandCombo.config(values=Mittpads)
        BrandCombo.current(0)

def price(event=""):
    if BrandCombo.get() == 'Daedo(Poomsae)':
        priceCombo.config(values=DaedoPrice)
        priceCombo.current(0)
        qty.set(1)

    if BrandCombo.get() == 'Mooto(Poomsae)':
        priceCombo.config(values=MootoPrice)
        priceCombo.current(0)
        qty.set(1)

    if BrandCombo.get() == 'JC(Poomsae)':
        priceCombo.config(values=JcPrice)
        priceCombo.current(0)
        qty.set(1)

    if BrandCombo.get() == 'Normal(White)':
        priceCombo.config(values=price_normal)
        priceCombo.current(0)
        qty.set(1)

    if BrandCombo.get() == 'Daedo(Sparring)':
        priceCombo.config(values=price_daedo)
        priceCombo.current(0)
        qty.set(1)

    if BrandCombo.get() == 'Mooto(Feather)':
        priceCombo.config(values=price_mooto)
        priceCombo.current(0)
        qty.set(1)

    if BrandCombo.get() == 'Daedo':
        priceCombo.config(values=daedoPrice)
        priceCombo.current(0)
        qty.set(1)

    if BrandCombo.get() == 'Mooto':
        priceCombo.config(values=mootoPrice)
        priceCombo.current(0)
        qty.set(1)

    if BrandCombo.get() == 'Shivgan(Chest Guard)':
        priceCombo.config(values=Shivgan_price)
        priceCombo.current(0)
        qty.set(1)

    if BrandCombo.get() == 'Daedo(Chest Guard)':
        priceCombo.config(values=Daedo_Price)
        priceCombo.current(0)
        qty.set(1)

    if BrandCombo.get() == 'Normal':
        priceCombo.config(values=normalPrice)
        priceCombo.current(0)
        qty.set(1)

    if BrandCombo.get() == 'Shivgan(Mittpad)':
        priceCombo.config(values=shivganPrice)
        priceCombo.current(0)
        qty.set(1)

def welcome():
    billText.delete(1.0,END)
    billText.insert(END, "\tWELCOME TO SPIRIT TAEKWONDO FITNESS ACADEMY")
    billText.insert(END, f"\nBill Number: {bill_no.get()}")
    billText.insert(END, f"\nCustomer Name: {c_name.get()}")
    billText.insert(END, f"\nMobile Number: {c_phone.get()}")
    billText.insert(END, f"\nEmail: {c_email.get()}")
    billText.insert(END, "\n=======================================================")
    billText.insert(END, f"\n Products\t\t\tQTY\tPrice")
    billText.insert(END, "\n=======================================================")

l = []

def addToCart():
    n = prices.get()
    m = qty.get()*n
    l.append(m)
    tt = sum(l)
    if brand.get() == "":
        messagebox.showerror('Error', 'Add Items to generate bill')
    else:
        billText.insert(END, f"\n{brand.get()}\t\t\t{qty.get()}\t{m}")
        total.set(str('Rs.%.2f' % tt))

def genBill():
    if brand.get() == "":
        messagebox.showerror('Error', 'Please select an Item')
    else:
        #welcome()
        text = billText.get(9.0, (9.0+float(len(l))))
        welcome()
        billText.insert(END, text)
        billText.insert(END, "\n=======================================================")
        billText.insert(END, f"\n Total Amount:\t\t\t{total.get()}")
        billText.insert(END, "\n=======================================================")


def saveBill():
    if billText.get(9.0, END) == '':
        messagebox.showerror('Error', 'Generate the bill first')
    else:
        r = messagebox.askyesno("Save Bill", 'Do you want to save the bill')
        if r>0:
            bill_data = billText.get(1.0, END)
            f1 = open('bills/'+str(bill_no.get())+".txt", "w")
            messagebox.showinfo("Success", f"Bill No:{bill_no.get()} saved successfully")
            f1.write(bill_data)
            f1.close()

def searchBill():
    flag = False
    files = []
    for i in os.listdir('bills/'):
        files.append(i)

    files.pop(0)

    for i in files:

        if i.split('.')[0] == search_bill.get():
            f1 = open(f'bills/{i}', 'r')
            billText.delete(1.0, END)
            for d in f1:
                billText.insert(END, d)
            f1.close()
            flag = True
            messagebox.showinfo("Success", "Bill found")
            break
        elif flag:
            messagebox.showerror("Error", "Invalid Bill No.")
            break


def exitFunc():
    window.destroy()
    import menu

#Categories
CategoryList = ['Select Option', 'Uniforms', 'Equipments']

# Type Uniform
UniformType = ['Poomsae', 'Sparring']
Poomsae = ['Daedo(Poomsae)', 'Mooto(Poomsae)', 'JC(Poomsae)']
DaedoPrice = 3500
MootoPrice = 4500
JcPrice = 4000

Sparring = ['Normal(White)', 'Daedo(Sparring)', 'Mooto(Feather)']
price_normal = 1200
price_daedo = 2300
price_mooto = 4000

# Type Equipments
equipmentType = ['Guards', 'Chest Guard', 'Mittpads']
Guards = ['Daedo', 'Mooto']
daedoPrice = 2100
mootoPrice = 3100

Cguard = ['Shivgan(Chest Guard)', 'Daedo(Chest Guard)']
Shivgan_price = 1900
Daedo_Price = 2300

Mittpads = ['Normal', 'Shivgan(Mittpad)']
normalPrice = 700
shivganPrice = 1000


backgroundLabel = Label(window, bg='LightBlue')
backgroundLabel.place(x=0, y=0, relheight=1, relwidth=1)

orderLabel = Label(window, text='Equipment Order', font=('Helvetica', 30, 'bold'), bg='LightBlue', fg='black')
orderLabel.grid(row=0, column=0, padx=570, pady=40)

mainFrame = Frame(window, bd=5, relief=GROOVE, bg='LightBlue')
mainFrame.place(x=5, y=90,width=1430, height=690)

custFrame = LabelFrame(mainFrame, text='Customer Details',
                       font=('Helvetica', 18, 'bold'), bg='LightBlue', fg='black')
custFrame.place(x=5, y=10, width=310, height=210)

nameLabel = Label(custFrame, text="Name: ", font=('helvetica', 15, 'bold'), fg='black', bg='LightBlue')
nameLabel.grid(row=0, column=0, pady=20, sticky=W)
nameEntry = Entry(custFrame, font=('helvetica', 15), fg='orange', width=22, bd=1, textvariable=c_name)
nameEntry.grid(row=0, column=1, padx=6)

mobLabel = Label(custFrame, text="Mobile No: ", font=('helvetica', 15, 'bold'), fg='black', bg='LightBlue')
mobLabel.grid(row=1, column=0, pady=20, sticky=W)
mobEntry = Entry(custFrame, font=('helvetica', 15), fg='orange', width=22, bd=1, textvariable=c_phone)
mobEntry.grid(row=1, column=1, padx=6)

emailLabel = Label(custFrame, text="Email: ", font=('helvetica', 15, 'bold'), fg='black', bg='LightBlue')
emailLabel.grid(row=2, column=0, pady=20, sticky=W)
emailEntry = Entry(custFrame, font=('helvetica', 15), fg='orange', width=22,bd=1, textvariable=c_email)
emailEntry.grid(row=2, column=1, padx=6)

# Product Frame
productFrame = LabelFrame(mainFrame, text='Products',
                         font=('Helvetica', 18, 'bold'), bg='LightBlue', fg='black')
productFrame.place(x=340, y=10, width=650, height=210)

categoryLabel = Label(productFrame, text="Category: ", font=('helvetica', 15, 'bold'), fg='black', bg='LightBlue')
categoryLabel.grid(row=0, column=0, pady=20, sticky=W)
categoryCombo = ttk.Combobox(productFrame, font=('helvetica', 15), width=20, state='readonly', values=CategoryList)
categoryCombo.current(0)
categoryCombo.grid(row=0, column=1, padx=6)
categoryCombo.bind("<<ComboboxSelected>>", Categories)

typeLabel = Label(productFrame, text="Type: ", font=('helvetica', 15, 'bold'), fg='black', bg='LightBlue')
typeLabel.grid(row=1, column=0, pady=20, sticky=W)
typeCombo = ttk.Combobox(productFrame, font=('helvetica', 15), width=20, state='readonly')
typeCombo.grid(row=1, column=1, padx=6)
typeCombo.bind("<<ComboboxSelected>>", Type)

BrandLabel = Label(productFrame, text="Brand: ", font=('helvetica', 15, 'bold'), fg='black', bg='LightBlue')
BrandLabel.grid(row=2, column=0, pady=20, sticky=W)
BrandCombo = ttk.Combobox(productFrame, font=('helvetica', 15), width=20, state='readonly', textvariable=brand)
BrandCombo.grid(row=2, column=1, padx=6)
BrandCombo.bind('<<ComboboxSelected>>', price)

priceLabel = Label(productFrame, text="Price: ", font=('helvetica', 15, 'bold'), fg='black', bg='LightBlue')
priceLabel.grid(row=0, column=2, pady=20, padx=25)
priceCombo = ttk.Combobox(productFrame, font=('helvetica', 15), width=20, state='readonly', textvariable=prices)
priceCombo.grid(row=0, column=3, padx=1)

QtyLabel = Label(productFrame, text="Quantity: ", font=('helvetica', 15, 'bold'), fg='black', bg='LightBlue')
QtyLabel.grid(row=1, column=2, pady=20, padx=25)
QtyEntry = Entry(productFrame, font=('helvetica', 15),fg='orange', width=22, bd=1, textvariable=qty)
QtyEntry.grid(row=1, column=3, padx=1)

searchFrame = Frame(mainFrame, bg='LightBlue')
searchFrame.place(x=1000,y=10, width=420, height=40)

searchLabel = Label(searchFrame, text="Bill Search: ", font=('helvetica', 15, 'bold'), fg='black', bg='LightBlue')
searchLabel.grid(row=0, column=0, sticky=W)
searchEntry = Entry(searchFrame, font=('helvetica', 15), fg='orange', width=22, bd=1, textvariable=search_bill)
searchEntry.grid(row=0, column=1)

searchButton = Button(searchFrame, text='Search',font=('helvetica', 15), fg='DarkOrange3',
                      activeforeground='DarkOrange3', cursor='hand1', command = searchBill)
searchButton.grid(row=0, column=2, padx=4)


billFrame = LabelFrame(mainFrame,text='Bill',
                       font=('Helvetica', 18, 'bold'), bg='LightBlue', fg='black')
billFrame.place(x=1000, y=45, width=400, height=510)

scroll_y = Scrollbar(billFrame, orient=VERTICAL, bg='LightBlue')
billText = Text(billFrame, yscrollcommand=scroll_y.set, bg='white',fg='blue', font=('Helvetica', 12, 'bold'))
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=billText.yview)
billText.pack(fill=BOTH, expand=1)

bottomFrame = LabelFrame(mainFrame, text='Bill Counter',
                       font=('Helvetica', 18, 'bold'), bg='LightBlue', fg='black')
bottomFrame.place(x=0, y=550, width=1420, height=130)

middleFrame = LabelFrame(mainFrame, bg='LightBlue')
middleFrame.place(x=0, y=220, width=1000, height=330)

logo_image = PhotoImage(file='bg-2.png')
logoLabel = Label(middleFrame, image=logo_image)
logoLabel.grid(row=0, column=0)


addButton = Button(bottomFrame, text='Add to Cart', font=('helvetica', 18), width=17,height=2,
                    fg='DarkOrange3', activeforeground='DarkOrange3',
                    cursor='hand1', command=addToCart)
addButton.grid(row=0, column=0, pady=23, padx=28)

generateBillButton = Button(bottomFrame, text='Generate Bill', font=('helvetica', 18), width=17,height=2,
                    fg='DarkOrange3', activeforeground='DarkOrange3',
                    cursor='hand1', command=genBill)
generateBillButton.grid(row=0, column=1, pady=23, padx=28)

saveButton = Button(bottomFrame, text='Save Bill', font=('helvetica', 18), width=17,height=2,
                    fg='DarkOrange3', activeforeground='DarkOrange3',
                    cursor='hand1', command=saveBill)
saveButton.grid(row=0, column=2, pady=23, padx=28)

clearButton = Button(bottomFrame, text='Clear', font=('helvetica', 18), width=17,height=2,
                    fg='DarkOrange3', activeforeground='DarkOrange3',
                    cursor='hand1', command = clearBill)
clearButton.grid(row=0, column=3, pady=23, padx=28)

exitButton = Button(bottomFrame, text='Exit', font=('helvetica', 18), width=17,height=2,
                    fg='DarkOrange3', activeforeground='DarkOrange3',
                    cursor='hand1', command=exitFunc)
exitButton.grid(row=0, column=4, pady=23, padx=28)

welcome()

window.mainloop()
