from tkinter import*
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management System")

text_input = StringVar()
operator = ""

tops = Frame(root,width =1600,height = 50,relief = SUNKEN)
tops.pack(side = TOP)

tops1 = Frame(root,width =800,height = 700,relief = SUNKEN)
tops1.pack(side = RIGHT)

tops2 = Frame(root,width =300,height = 700,relief = SUNKEN)
tops2.pack(side = LEFT)
#---------------------------------------------------------------------------------------------------------------
localtime = time.asctime(time.localtime(time.time()))

#-----------------------------------------------------------------------------------------------------------------------
lblinfo = Label(tops,font =("arial",50,"bold"), text = "Restaurant Management System",fg ="navy blue",bd = 10,anchor = "w")
lblinfo.grid(row=0,column =0)

lblinfo = Label(tops,font =("arial",20,"bold"), text = localtime,fg ="steel blue",bd = 10,anchor = "w")
lblinfo.grid(row=1,column =0)
#--------------------------------------------------------------------------------------------------------------------
def btnck(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btnClearDisplay():
    global operatora
    operator =""
    text_input.set("")

def btnEqualInput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator =""

def Ref():
    x = random.randint(10908,500876)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(fries.get())
    cod =float(drinks.get())
    coft = float(filet.get())
    cob =float(burger.get())
    cock =float(chicken.get())
    coch =float(cheese.get())

    costoffries = cof *250.00
    costofdrinks = cod*70.00
    costoffilet = coft *300.00
    costofchicken = cock*200.00
    costofburger = cob *160.00
    costofcheese = coch *400.00

    costofmeal = "₹",str("%.2f" % (costoffries + costofdrinks + costofchicken + costofburger + costofcheese))
    payTax = ((costoffries + costofdrinks + costofchicken + costofburger + costofcheese) *0.2)
    totalcost = (costoffries + costofdrinks + costofchicken + costofburger + costofcheese)
    ser_charge = ((costoffries + costofdrinks + costofchicken + costofburger + costofcheese)/99)
    service = "₹", str("%.2f" % ser_charge)

    overallcost = "₹", str("%.2f" % (payTax + totalcost + ser_charge))
    paidtax = "₹", str("%.2f" % payTax)
    service_charge.set(service)
    cost.set(costofmeal)
    tax.set(paidtax)
    subtotal.set(costofmeal)
    total.set(overallcost)

def qexit():
    root.destroy()

def reset():
    rand.set("")
    fries.set("")
    burger.set("")
    filet.set("")
    subtotal.set("")
    total.set("")
    service_charge.set("")
    drinks.set("")
    tax.set("")
    cost.set("")
    chicken.set("")
    cheese.set("")



txtdisplay = Entry(tops2,font=("arial",20,"bold"),textvariable =text_input,bd=30,insertwidth=4,
                   bg = "light yellow",justify ="right")
txtdisplay.grid(columnspan=4)
#-------------------------------------------------------------------------------------------------------------------------
btn7 =Button(tops2,padx = 16,pady =16,bd =8,fg ="black",font=("arial",20,"bold"),
             text="7",bg ="light yellow",command = lambda:btnck(7)).grid(row=2,column=0)

btn8 =Button(tops2,padx = 16,pady =16,bd =8,fg ="black",font=("arial",20,"bold"),
              text="8",bg ="light yellow",command = lambda:btnck(8)).grid(row=2,column=1)

btn9 =Button(tops2,padx = 16,pady =16,bd =8,fg ="black",font=("arial",20,"bold"),
               text="9",bg ="light yellow",command = lambda:btnck(9)).grid(row=2,column=2)

addition=Button(tops2,padx = 16,pady =16,bd =8,fg ="black",font=("arial",20,"bold"),
               text="+",bg ="light yellow",command = lambda:btnck("+")).grid(row=2,column=3)
#-------------------------------------------------------------------------------------------------------------------------
btn4 =Button(tops2,padx = 16,pady =16,bd =8,fg ="black",font=("arial",20,"bold"),
            text="4",bg ="light yellow",command = lambda:btnck(4)).grid(row=3,column=0)

btn5 =Button(tops2,padx = 16,pady =16,bd =8,fg ="black",font=("arial",20,"bold"),
             text="5",bg ="light yellow",command = lambda:btnck(5)).grid(row=3,column=1)

btn6 =Button(tops2,padx = 16,pady =16,bd =8,fg ="black",font=("arial",20,"bold"),
             text="6",bg ="light yellow",command = lambda:btnck(6)).grid(row=3,column=2)

subtraction=Button(tops2,padx = 16,pady =16,bd =8,fg ="black",font=("arial",20,"bold"),
             text="-",bg ="light yellow",command = lambda:btnck("-")).grid(row=3,column=3)
#---------------------------------------------------------------------------------------------------------------------------
btn1 =Button(tops2,padx = 16,pady =16,bd =8,fg ="black",font=("arial",20,"bold"),
             text="1",bg ="light yellow",command = lambda:btnck(1)).grid(row=4,column=0)

btn2 =Button(tops2,padx = 16,pady =16,bd =8,fg ="black",font=("arial",20,"bold"),
             text="2",bg ="light yellow",command = lambda:btnck(2)).grid(row=4,column=1)

btn3 =Button(tops2,padx = 16,pady =16,bd =8,fg ="black",font=("arial",20,"bold"),
           text="3",bg ="light yellow",command = lambda:btnck(3)).grid(row=4,column=2)

Multiplication=Button(tops2,padx = 16,pady =16,bd =8,fg ="black",font=("arial",20,"bold"),
           text="x",bg ="light yellow",command = lambda:btnck("*")).grid(row=4,column=3)
#-------------------------------------------------------------------------------------------------------------------------
btn0 =Button(tops2,padx = 16,pady =16,bd =8,fg ="black",font=("arial",20,"bold"),
           text="0",bg ="light yellow",command = lambda:btnck(0)).grid(row=5,column=0)

clear = Button(tops2,padx = 16,pady =16,bd =8,fg ="black",font=("arial",20,"bold"),
        text="C",bg ="light yellow",command =btnClearDisplay).grid(row=5,column=1)

divisn =Button(tops2,padx = 16,pady =16,bd =8,fg ="black",font=("arial",20,"bold"),
         text="/",bg ="light yellow",command = lambda:btnck("/")).grid(row=5,column=2)

equal=Button(tops2,padx = 16,pady =16,bd =8,fg ="black",font=("arial",20,"bold"),
         text="=",bg ="light yellow",command = btnEqualInput).grid(row=5,column=3)
#---------------------------------------------------------------------------------------------------------------------------
rand = StringVar()
fries = StringVar()
burger =StringVar()
filet = StringVar()
subtotal =StringVar()
total=StringVar()
service_charge = StringVar()
drinks = StringVar()
tax = StringVar()
cost = StringVar()
chicken = StringVar()
cheese= StringVar()
#--------------------------------------------------------------------------------------------------------------------------
lblref = Label(tops1,font=("arial",16,"bold"),text ="Reference",bd=16,anchor="w").grid(row=0,column=0)
textref=Entry(tops1,font=("arial",16,"bold"),textvariable =rand ,bd=10,insertwidth=4,
bg="light yellow",justify="right").grid(row=0,column=1)

lblfries = Label(tops1,font=("arial",16,"bold"),text =" Large fries",bd=16,anchor="w").grid(row=1,column=0)
textfries=Entry(tops1,font=("arial",16,"bold"),textvariable =fries ,bd=10,insertwidth=4,
bg="light yellow",justify="right").grid(row=1,column=1)

lblburger = Label(tops1,font=("arial",16,"bold"),text ="Burger Meal",bd=16,anchor="w").grid(row=2,column=0)
textburger=Entry(tops1,font=("arial",16,"bold"),textvariable =burger,bd=10,insertwidth=4,
bg="light yellow",justify="right").grid(row=2,column=1)

lblfilet = Label(tops1,font=("arial",16,"bold"),text ="Filet_o_Meal",bd=16,anchor="w").grid(row=3,column=0)
textfilet=Entry(tops1,font=("arial",16,"bold"),textvariable =filet ,bd=10,insertwidth=4,
bg="light yellow",justify="right").grid(row=3,column=1)

lblchicken = Label(tops1,font=("arial",16,"bold"),text ="Chicken Meal",bd=16,anchor="w").grid(row=4,column=0)
textchicken=Entry(tops1,font=("arial",16,"bold"),textvariable =chicken ,bd=10,insertwidth=4,
bg="light yellow",justify="right").grid(row=4,column=1)

lblcheese = Label(tops1,font=("arial",16,"bold"),text =" Cheese Meal",bd=16,anchor="w").grid(row=5,column=0)
textcheese=Entry(tops1,font=("arial",16,"bold"),textvariable =cheese ,bd=10,insertwidth=4,
bg="light yellow",justify="right").grid(row=5,column=1)
#----------------------------------------------------------------------------------------------------------------------------
lbldrinks = Label(tops1,font=("arial",16,"bold"),text="Drinks",bd=16,anchor="w").grid(row=0,column=4)
textdrinks=Entry(tops1,font=("arial",16,"bold"),textvariable =drinks ,bd=10,insertwidth=4,
bg="light yellow",justify="right").grid(row=0,column=5)

lblcost = Label(tops1,font=("arial",16,"bold"),text="Cost of Meal",bd=16,anchor="w").grid(row=1,column=4)
textcost=Entry(tops1,font=("arial",16,"bold"),textvariable =cost ,bd=10,insertwidth=4,
bg="light yellow",justify="right").grid(row=1,column=5)

lblsrvc = Label(tops1,font=("arial",16,"bold"),text="Service Charge",bd=16,anchor="w").grid(row=2,column=4)
textsrvc=Entry(tops1,font=("arial",16,"bold"),textvariable =service_charge ,bd=10,insertwidth=4,
bg="light yellow",justify="right").grid(row=2,column=5)


lblsub = Label(tops1,font=("arial",16,"bold"),text="Sub Total",bd=16,anchor="w").grid(row=4,column=4)
textsub=Entry(tops1,font=("arial",16,"bold"),textvariable =subtotal ,bd=10,insertwidth=4,
bg="light yellow",justify="right").grid(row=4,column=5)

lbltax = Label(tops1,font=("arial",16,"bold"),text="State Tax",bd=16,anchor="w").grid(row=3,column=4)
texttax=Entry(tops1,font=("arial",16,"bold"),textvariable =tax ,bd=10,insertwidth=4,
bg="light yellow",justify="right").grid(row=3,column=5)

lbltotal = Label(tops1,font=("arial",16,"bold"),text="Total Cost",bd=16,anchor="w").grid(row=5,column=4)
texttotal=Entry(tops1,font=("arial",16,"bold"),textvariable =total,bd=10,insertwidth=4,
bg="light yellow",justify="right").grid(row=5,column=5)
#-------------------------------------------------------------------------------------------------------------
btntotal =Button(tops1,padx=16,pady=8,bd =16,fg ="black",font=("arial",16,"bold"),width = 10,text="Total",
bg= "light yellow",command=Ref).grid(row=7,column =1)

btnreset =Button(tops1,padx=16,pady=8,bd =16,fg ="black",font=("arial",16,"bold"),width = 10,text="Reset",
bg= "light yellow",command=reset).grid(row=7,column =4)

btnexist =Button(tops1,padx=16,pady=8,bd =16,fg ="black",font=("arial",16,"bold"),width = 10,text="Exit",
bg= "light yellow",command=qexit).grid(row=7,column =5)
root.mainloop()
