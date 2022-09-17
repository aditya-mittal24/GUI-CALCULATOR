from tkinter import *

root = Tk()
root.title("Calculator")
root.resizable(False, False)
root.iconbitmap("/Users/aditya/Downloads/icon.ico")

e=Entry(root, width=35)
e.grid(row=0, column=0, columnspan=4)

ans=0


def button_click(number):
    current= e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    global ans
    global math
    e.delete(0, END)
    ans=0
    math=""
math=""
def button_plus():
    global ans
    first_number= e.get()
    global f_num
    global math
    f_num = int(first_number)
    if math=="subtraction":
        ans=ans-f_num
    elif math== "addition":
        ans=ans+f_num
    elif math=="multiplication":
        ans=ans*f_num
    elif math=="division":
        ans=ans/f_num
    elif math=="mod":
        ans=ans%f_num
    elif math=="":
        ans = ans + f_num
    math="addition"


    e.delete(0, END)

def button_sub():
    global ans
    first_number = e.get()
    global f_num
    global math
    f_num = int(first_number)
    if math == "subtraction":
        ans = ans - f_num
    elif math == "addition":
        ans = ans + f_num
    elif math == "multiplication":
        ans = ans * f_num
    elif math == "division":
        ans = ans / f_num
    elif math == "mod":
        ans = ans % f_num
    elif math=="":
        ans = f_num
    math = "subtraction"


    e.delete(0, END)

def button_equal():
    second_number= e.get()
    e.delete(0, END)
    if math=="addition":
        e.insert(0, ans +int(second_number))
    elif math=="subtraction":
        e.insert(0, ans -int(second_number))
    elif math=="multiplication":
        e.insert(0, ans *int(second_number))
    elif math=="division":
        e.insert(0, ans /int(second_number))
    elif math=="mod":
        e.insert(0, ans %int(second_number))

def button_multiply():
    global ans
    first_number = e.get()
    global f_num
    global math
    f_num = int(first_number)
    if math == "subtraction":
        ans = ans - f_num
    elif math == "addition":
        ans = ans + f_num
    elif math == "multiplication":
        ans = ans * f_num
    elif math == "division":
        ans = ans / f_num
    elif math == "mod":
        ans = ans % f_num
    elif math == "":
        ans = f_num
    math = "multiplication"


    e.delete(0, END)

def button_divide():
    global ans
    first_number = e.get()
    global f_num
    global math
    f_num = int(first_number)
    if math == "subtraction":
        ans = ans - f_num
    elif math == "addition":
        ans = ans + f_num
    elif math == "multiplication":
        ans = ans * f_num
    elif math == "division":
        ans = ans / f_num
    elif math == "mod":
        ans = ans % f_num
    elif math=="":
        ans = f_num
    math = "division"

    e.delete(0, END)

def button_mod():
    global ans
    first_number = e.get()
    global f_num
    global math
    f_num = int(first_number)
    if math == "subtraction":
        ans = ans - f_num
    elif math == "addition":
        ans = ans + f_num
    elif math == "multiplication":
        ans = ans * f_num
    elif math == "division":
        ans = ans / f_num
    elif math == "mod":
        ans = ans % f_num
    elif math=="":
        ans = f_num
    math = "mod"

    e.delete(0, END)


button_1=Button(root, text="1",padx=21, pady=20, command= lambda : button_click(1))
button_2=Button(root, text="2",padx=20, pady=20, command= lambda : button_click(2))
button_3=Button(root, text="3",padx=20, pady=20, command= lambda : button_click(3))
button_4=Button(root, text="4",padx=19, pady=20, command= lambda : button_click(4))
button_5=Button(root, text="5",padx=20, pady=20, command= lambda : button_click(5))
button_6=Button(root, text="6",padx=20, pady=20, command= lambda : button_click(6))
button_7=Button(root, text="7",padx=19, pady=20, command= lambda : button_click(7))
button_8=Button(root, text="8",padx=20, pady=20, command= lambda : button_click(8))
button_9=Button(root, text="9",padx=20, pady=20, command= lambda : button_click(9))
button_0=Button(root, text="0",padx=20, pady=20, command= lambda : button_click(0))

button_plus=Button(root, text="+",padx=20, pady=20,command=button_plus)
button_sub=Button(root, text="-",padx=20, pady=20,command=button_sub)
button_clear=Button(root, text="AC",padx=58, pady=20, command=button_clear)
button_equal=Button(root, text="=", padx=61, pady=20, command=button_equal)
button_multiply=Button(root, text="x",padx=20, pady=20,command=button_multiply)
button_divide=Button(root, text="÷",padx=20, pady=20,command=button_divide)
button_mod=Button(root, text="%",padx=19, pady=20,command=button_mod)



button_clear.grid(row=1, column=0, columnspan=2)
button_mod.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)


button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_plus.grid(row=4, column=3)


button_0.grid(row=5, column=1)
button_equal.grid(row=5, column=2, columnspan=2)

def switch():
    top= Toplevel()
    top.title("Calculators")
    button_length=Button(top, text="📏\nLength", command=length ,padx=20, pady=34)
    button_length.grid(row=0,column=0)
    button_area= Button(top, text="⧄\nArea",padx=23, pady=34, command=area)
    button_area.grid(row=0, column=1)
    button_volume= Button(top, text="❒\nVolume",padx=18, pady=34,command=volume)
    button_volume.grid(row=0, column=2)

    button_temp = Button(top, text="🌡️\nTemperature", padx=2, pady=34,command=temperature)
    button_temp.grid(row=1, column=0)
    button_speed = Button(top, text="🕛\nSpeed", padx=18, pady=34, command=speed)
    button_speed.grid(row=1, column=1)
    button_mass = Button(top, text="⚖️\nMass", padx=24, pady=34,command=mass)
    button_mass.grid(row=1, column=2)

    button_numsystem = Button(top, text="♳\nNumber\nsystem", padx=17, pady=26)
    button_numsystem.grid(row=2, column=0)
    button_bmi = Button(top, text="℁\nBMI", padx=26, pady=34)
    button_bmi.grid(row=2, column=1)
    button_currency = Button(top, text="💲️\nCurrency", padx=12, pady=34)
    button_currency.grid(row=2, column=2)

button_switch=Button(root, text="🔁",padx=15, pady=20, command=switch)
button_switch.grid(row=5,column=0)


def lbutton_click(number):
    global l
    current = l.get()
    l.delete(0, END)
    l.insert(0, str(current) + str(number))

def lbutton_equal():
    global unit1
    global unit2
    global l
    global l2
    global units
    initial=unit1.get()
    final=unit2.get()
    value1=l.get()
    if initial==units[0]:
        conv = int(value1) * 1000
    elif initial==units[1]:
        conv= int(value1)
    elif initial==units[2]:
        conv= int(value1)/100
    elif initial==units[3]:
        conv= int(value1)/1000
    elif initial==units[4]:
        conv= int(value1)*1609.344
    elif initial==units[5]:
        conv= int(value1)/3.28084
    elif initial==units[6]:
        conv= int(value1)/1.0936
    elif initial==units[7]:
        conv= int(value1)/39.37
    elif initial==units[8]:
        conv= int(value1)*1852



    if final==units[0]:
        ans= conv/1000
    elif final==units[1]:
        ans=conv
    elif final==units[2]:
        ans=conv*100
    elif final==units[3]:
        ans=conv*1000
    elif final==units[4]:
        ans=conv/1609.344
    elif final==units[5]:
        ans=conv*3.28084
    elif final==units[6]:
        ans=conv*1.0936
    elif final==units[7]:
        ans=conv*39.37
    elif final==units[8]:
        ans=conv/1852

    l2.delete(0, END)
    l2.insert(0, ans)

def buttoninterchange():
    global l
    global l2
    global unit1
    global unit2
    global units
    initial=unit1.get()
    final=unit2.get()
    for i in units:
        if i==initial:
            unit2.set(i)
            break
    for i in units:
        if i==final:
            unit1.set(i)
            break




def buttonreset():
    global l
    global l2
    global unit1
    global unit2
    global units
    l.delete(0,END)
    l2.delete(0,END)
    unit1.set(units[0])
    unit2.set(units[1])

def buttonc():
    global l
    global l2
    l.delete(0, END)
    l2.delete(0, END)


def length():
    global l
    global l2
    global unit1
    global unit2
    global units
    top2=Toplevel()
    top2.title('Length Converter')
    l = Entry(top2, width=25)
    l.grid(row=0, column=1, columnspan=3,pady=5)
    unit1=StringVar()
    unit2=StringVar()
    units=[
        "Kilometer km",
        "Meter m",
        "Centimeter cm",
        "Millimeter mm",
        "Mile mi",
        "Foot ft",
        "Yard yd",
        "Inch in",
        "Nautical Mile",
    ]
    unit1.set(units[0])
    unit2.set(units[1])

    drop=OptionMenu(top2,unit1, *units)
    drop.grid(row=0, column=0)

    l2 = Entry(top2, width=25)
    l2.grid(row=1, column=1, columnspan=3,pady=5)
    drop2 = OptionMenu(top2, unit2, *units)
    drop2.grid(row=1, column=0)

    button_1 = Button(top2, text="1", padx=33, pady=23, font=("Arial",22),command=lambda: lbutton_click(1))
    button_2 = Button(top2, text="2", padx=32, pady=22,font=("Arial",22), command=lambda: lbutton_click(2))
    button_3 = Button(top2, text="3", padx=32, pady=22,font=("Arial",22), command=lambda: lbutton_click(3))
    button_4 = Button(top2, text="4", padx=33, pady=21,font=("Arial",22), command=lambda: lbutton_click(4))
    button_5 = Button(top2, text="5", padx=32, pady=20,font=("Arial",22), command=lambda: lbutton_click(5))
    button_6 = Button(top2, text="6", padx=32, pady=22,font=("Arial",22), command=lambda: lbutton_click(6))
    button_7 = Button(top2, text="7", padx=33, pady=22,font=("Arial",22), command=lambda: lbutton_click(7))
    button_8 = Button(top2, text="8", padx=32, pady=22,font=("Arial",22), command=lambda: lbutton_click(8))
    button_9 = Button(top2, text="9", padx=32, pady=22,font=("Arial",22), command=lambda: lbutton_click(9))
    button_0 = Button(top2, text="0", padx=32, pady=16,font=("Arial",22), command=lambda: lbutton_click(0))
    button_equal = Button(top2, text="=", padx=32, pady=16, font=("Arial",22),command=lbutton_equal)
    button_quit=Button(top2, text="Exit",command=top2.destroy,font=("Arial",16),padx=26,pady=19)
    button_reset=Button(top2, text="Reset",command=buttonreset, font=("Arial",16),padx=18, pady=9)
    button_interchange=Button(top2,text="↑↓",command=buttoninterchange, font=("Arial",22),padx=28, pady=8)
    button_c=Button(top2, text="AC",command=buttonc, font=("Arial",16),padx=27, pady=9)


    button_reset.grid(row=2,column=2)
    button_interchange.grid(row=2,column=0)
    button_c.grid(row=2,column=1)

    button_7.grid(row=3, column=0)
    button_8.grid(row=3, column=1)
    button_9.grid(row=3, column=2)

    button_4.grid(row=4, column=0)
    button_5.grid(row=4, column=1)
    button_6.grid(row=4, column=2)

    button_1.grid(row=5, column=0)
    button_2.grid(row=5, column=1)
    button_3.grid(row=5, column=2)

    button_0.grid(row=6, column=1)
    button_equal.grid(row=6, column=2)
    button_quit.grid(row=6, column=0)



###Area#####--------------------------------------------------------------------------------

def abutton_click(number):
    global a
    current = a.get()
    a.delete(0, END)
    a.insert(0, str(current) + str(number))

def abutton_equal():
    global aunit1
    global aunit2
    global a
    global a2
    global aunits
    initial=aunit1.get()
    final=aunit2.get()
    value1=a.get()
    if initial==aunits[0]:
        conv= int(value1)*1000000
    elif initial==aunits[1]:
        conv= int(value1)*10000
    elif initial==aunits[2]:
        conv= int(value1)
    elif initial==aunits[3]:
        conv= int(value1)/10000
    elif initial==aunits[4]:
        conv= int(value1)/1000000
    elif initial==aunits[5]:
        conv= int(value1)*4046.856
    elif initial==aunits[6]:
        conv= int(value1)*2589988.11
    elif initial==aunits[7]:
        conv= int(value1)/10.7639104
    elif initial==aunits[8]:
        conv= int(value1)/1.19599005
    elif initial==aunits[9]:
        conv=int(value1)/1550



    if final==aunits[0]:
        ans= conv/1000000
    elif final==aunits[1]:
        ans=conv/10000
    elif final==aunits[2]:
        ans=conv
    elif final==aunits[3]:
        ans=conv*10000
    elif final==aunits[4]:
        ans=conv*1000000
    elif final==aunits[5]:
        ans=conv/4046.856
    elif final==aunits[6]:
        ans=conv/2589988.11
    elif final==aunits[7]:
        ans=conv*10.7639104
    elif final==aunits[8]:
        ans=conv*1.19599005
    elif final==aunits[9]:
        ans=conv*1550

    a2.delete(0, END)
    a2.insert(0, ans)

def abuttoninterchange():
    global a
    global a2
    global aunit1
    global aunit2
    global aunits
    initial=aunit1.get()
    final=aunit2.get()
    for i in aunits:
        if i==initial:
            aunit2.set(i)
            break
    for i in aunits:
        if i==final:
            aunit1.set(i)
            break




def abuttonreset():
    global a
    global a2
    global aunit1
    global aunit2
    global aunits
    a.delete(0,END)
    a2.delete(0,END)
    aunit1.set(aunits[0])
    aunit2.set(aunits[1])

def abuttonc():
    global a
    global a2
    a.delete(0, END)
    a2.delete(0, END)


def area():
    global a
    global a2
    global aunit1
    global aunit2
    global aunits
    top3=Toplevel()
    top3.title('Area Converter')
    a = Entry(top3, width=25)
    a.grid(row=0, column=1, columnspan=3,pady=5)
    aunit1=StringVar()
    aunit2=StringVar()
    aunits=[
        "Sq.Kilometer km²",
        "Hectare ha",
        "Sq.Meter m²",
        "Sq.Centimeter cm²",
        "Sq.Millimeter mm²",
        "Acre ac",
        "Sq.Mile mi²",
        "Sq.Foot ft²",
        "Sq.Yard yd²",
        "Sq.Inch in²",
    ]
    aunit1.set(aunits[0])
    aunit2.set(aunits[1])

    drop=OptionMenu(top3,aunit1, *aunits)
    drop.grid(row=0, column=0)

    a2 = Entry(top3, width=25)
    a2.grid(row=1, column=1, columnspan=3,pady=5)
    drop2 = OptionMenu(top3, aunit2, *aunits)
    drop2.grid(row=1, column=0)

    button_1 = Button(top3, text="1", padx=33, pady=23, font=("Arial",22),command=lambda: abutton_click(1))
    button_2 = Button(top3, text="2", padx=32, pady=22,font=("Arial",22), command=lambda: abutton_click(2))
    button_3 = Button(top3, text="3", padx=32, pady=22,font=("Arial",22), command=lambda: abutton_click(3))
    button_4 = Button(top3, text="4", padx=33, pady=21,font=("Arial",22), command=lambda: abutton_click(4))
    button_5 = Button(top3, text="5", padx=32, pady=20,font=("Arial",22), command=lambda: abutton_click(5))
    button_6 = Button(top3, text="6", padx=32, pady=22,font=("Arial",22), command=lambda: abutton_click(6))
    button_7 = Button(top3, text="7", padx=33, pady=22,font=("Arial",22), command=lambda: abutton_click(7))
    button_8 = Button(top3, text="8", padx=32, pady=22,font=("Arial",22), command=lambda: abutton_click(8))
    button_9 = Button(top3, text="9", padx=32, pady=22,font=("Arial",22), command=lambda: abutton_click(9))
    button_0 = Button(top3, text="0", padx=32, pady=16,font=("Arial",22), command=lambda: abutton_click(0))
    button_equal = Button(top3, text="=", padx=32, pady=16, font=("Arial",22),command=abutton_equal)
    button_quit=Button(top3, text="Exit",command=top3.destroy,font=("Arial",16),padx=26,pady=19)
    button_reset=Button(top3, text="Reset",command=abuttonreset, font=("Arial",16),padx=18, pady=9)
    button_interchange=Button(top3,text="↑↓",command=abuttoninterchange, font=("Arial",22),padx=28, pady=8)
    button_c = Button(top3, text="AC", command=abuttonc, font=("Arial", 16), padx=27, pady=9)


    button_reset.grid(row=2,column=2)
    button_interchange.grid(row=2,column=0)
    button_c.grid(row=2,column=1)

    button_7.grid(row=3, column=0)
    button_8.grid(row=3, column=1)
    button_9.grid(row=3, column=2)

    button_4.grid(row=4, column=0)
    button_5.grid(row=4, column=1)
    button_6.grid(row=4, column=2)

    button_1.grid(row=5, column=0)
    button_2.grid(row=5, column=1)
    button_3.grid(row=5, column=2)

    button_0.grid(row=6, column=1)
    button_equal.grid(row=6, column=2)
    button_quit.grid(row=6, column=0)


###Volume#####--------------------------------------------------------------------------------



def vbutton_click(number):
    global v
    current = v.get()
    v.delete(0, END)
    v.insert(0, str(current) + str(number))

def vbutton_equal():
    global vunit1
    global vunit2
    global v
    global v2
    global vunits
    initial=vunit1.get()
    final=vunit2.get()
    value1=v.get()
    if initial==vunits[0]:
        conv= int(value1)
    elif initial==vunits[1]:
        conv= int(value1)/1000000
    elif initial==vunits[2]:
        conv= int(value1)/1000000000
    elif initial==vunits[3]:
        conv= int(value1)/1000
    elif initial==vunits[4]:
        conv= int(value1)/100000
    elif initial==vunits[5]:
        conv= int(value1)/1000000
    elif initial==vunits[6]:
        conv= int(value1)/35.3146667
    elif initial==vunits[7]:
        conv= int(value1)/1.30795062
    elif initial==vunits[8]:
        conv= int(value1)/61023.7441



    if final==vunits[0]:
        ans= conv
    elif final==vunits[1]:
        ans=conv*1000000
    elif final==vunits[2]:
        ans=conv*1000000000
    elif final==vunits[3]:
        ans=conv*1000
    elif final==vunits[4]:
        ans=conv*100000
    elif final==vunits[5]:
        ans=conv*1000000
    elif final==vunits[6]:
        ans=conv*35.3146667
    elif final==vunits[7]:
        ans=conv*1.30795062
    elif final==vunits[8]:
        ans=conv*61023.7441

    v2.delete(0, END)
    v2.insert(0, ans)

def vbuttoninterchange():
    global v
    global v2
    global vunit1
    global vunit2
    global vunits
    initial=vunit1.get()
    final=vunit2.get()
    for i in vunits:
        if i==initial:
            vunit2.set(i)
            break
    for i in vunits:
        if i==final:
            vunit1.set(i)
            break




def vbuttonreset():
    global v
    global v2
    global vunit1
    global vunit2
    global vunits
    v.delete(0,END)
    v2.delete(0,END)
    vunit1.set(vunits[3])
    vunit2.set(vunits[5])

def vbuttonc():
    global v
    global v2
    v.delete(0, END)
    v2.delete(0, END)


def volume():
    global v
    global v2
    global vunit1
    global vunit2
    global vunits
    top4=Toplevel()
    top4.title('Volume Converter')
    v = Entry(top4, width=25)
    v.grid(row=0, column=1, columnspan=3,pady=5)
    vunit1=StringVar()
    vunit2=StringVar()
    vunits=[
        "Cb.Meter m³",
        "Cb.Centimeter cm³",
        "Cb.Millimeter mm³",
        "Liter l",
        "Centiliter cl",
        "Mililiter ml",
        "Cb.Foot ft³"
        "Cb.Yard yd³",
        "Cb.Inch in³",
    ]
    vunit1.set(vunits[3])
    vunit2.set(vunits[5])

    drop=OptionMenu(top4,vunit1, *vunits)
    drop.grid(row=0, column=0)

    v2 = Entry(top4, width=25)
    v2.grid(row=1, column=1, columnspan=3,pady=5)
    drop2 = OptionMenu(top4, vunit2, *vunits)
    drop2.grid(row=1, column=0)

    button_1 = Button(top4, text="1", padx=33, pady=23, font=("Arial",22),command=lambda: vbutton_click(1))
    button_2 = Button(top4, text="2", padx=32, pady=22,font=("Arial",22), command=lambda: vbutton_click(2))
    button_3 = Button(top4, text="3", padx=32, pady=22,font=("Arial",22), command=lambda: vbutton_click(3))
    button_4 = Button(top4, text="4", padx=33, pady=21,font=("Arial",22), command=lambda: vbutton_click(4))
    button_5 = Button(top4, text="5", padx=32, pady=20,font=("Arial",22), command=lambda: vbutton_click(5))
    button_6 = Button(top4, text="6", padx=32, pady=22,font=("Arial",22), command=lambda: vbutton_click(6))
    button_7 = Button(top4, text="7", padx=33, pady=22,font=("Arial",22), command=lambda: vbutton_click(7))
    button_8 = Button(top4, text="8", padx=32, pady=22,font=("Arial",22), command=lambda: vbutton_click(8))
    button_9 = Button(top4, text="9", padx=32, pady=22,font=("Arial",22), command=lambda: vbutton_click(9))
    button_0 = Button(top4, text="0", padx=32, pady=16,font=("Arial",22), command=lambda: vbutton_click(0))
    button_equal = Button(top4, text="=", padx=32, pady=16, font=("Arial",22),command=vbutton_equal)
    button_quit=Button(top4, text="Exit",command=top4.destroy,font=("Arial",16),padx=26,pady=19)
    button_reset=Button(top4, text="Reset",command=vbuttonreset, font=("Arial",16),padx=18, pady=9)
    button_interchange=Button(top4,text="↑↓",command=vbuttoninterchange, font=("Arial",22),padx=28, pady=8)
    button_c = Button(top4, text="AC", command=vbuttonc, font=("Arial", 16), padx=27, pady=9)


    button_reset.grid(row=2,column=2)
    button_interchange.grid(row=2,column=0)
    button_c.grid(row=2,column=1)

    button_7.grid(row=3, column=0)
    button_8.grid(row=3, column=1)
    button_9.grid(row=3, column=2)

    button_4.grid(row=4, column=0)
    button_5.grid(row=4, column=1)
    button_6.grid(row=4, column=2)

    button_1.grid(row=5, column=0)
    button_2.grid(row=5, column=1)
    button_3.grid(row=5, column=2)

    button_0.grid(row=6, column=1)
    button_equal.grid(row=6, column=2)
    button_quit.grid(row=6, column=0)



###Temperature#####--------------------------------------------------------------------------------

def tbutton_click(number):
    global t
    current = t.get()
    t.delete(0, END)
    t.insert(0, str(current) + str(number))

def tbutton_equal():
    global tunit1
    global tunit2
    global t
    global t2
    global tunits
    initial=tunit1.get()
    final=tunit2.get()
    value1=t.get()
    if initial==tunits[0] and final==tunits[1]:
        ans= int(value1)*1.8+32
    elif initial==tunits[1] and final==tunits[0]:
        ans= (int(value1)-32)/1.8
    elif initial==tunits[2] and final==tunits[1]:
        ans = 1.8*(int(value1)-273.15)+32
    elif initial == tunits[1] and final == tunits[2]:
        ans = ((int(value1)-32)/1.8) + 273.15
    elif initial==tunits[0] and final==tunits[2]:
        ans= int(value1)+273.15
    elif initial==tunits[2] and final==tunits[0]:
        ans= int(value1)-273.15
    elif (initial == final):
        ans = int(value1)

    t2.delete(0, END)
    t2.insert(0, ans)

def tbuttoninterchange():
    global t
    global t2
    global tunit1
    global tunit2
    global tunits
    initial=tunit1.get()
    final=tunit2.get()
    for i in tunits:
        if i==initial:
            tunit2.set(i)
            break
    for i in tunits:
        if i==final:
            tunit1.set(i)
            break




def tbuttonreset():
    global t
    global t2
    global tunit1
    global tunit2
    global tunits
    t.delete(0,END)
    t2.delete(0,END)
    tunit1.set(tunits[0])
    tunit2.set(tunits[1])

def tbuttonc():
    global t
    global t2
    t.delete(0, END)
    t2.delete(0, END)


def temperature():
    global t
    global t2
    global tunit1
    global tunit2
    global tunits
    top5=Toplevel()
    top5.title('Temperature Converter')
    t = Entry(top5, width=25)
    t.grid(row=0, column=1, columnspan=3,pady=5)
    tunit1=StringVar()
    tunit2=StringVar()
    tunits=[
        "Celcius °C",
        "Fahrenheit °F",
        "Kelvin K",
    ]
    tunit1.set(tunits[0])
    tunit2.set(tunits[1])

    drop=OptionMenu(top5,tunit1, *tunits)
    drop.grid(row=0, column=0)

    t2 = Entry(top5, width=25)
    t2.grid(row=1, column=1, columnspan=3,pady=5)
    drop2 = OptionMenu(top5, tunit2, *tunits)
    drop2.grid(row=1, column=0)

    button_1 = Button(top5, text="1", padx=33, pady=23, font=("Arial",22),command=lambda: tbutton_click(1))
    button_2 = Button(top5, text="2", padx=32, pady=22,font=("Arial",22), command=lambda: tbutton_click(2))
    button_3 = Button(top5, text="3", padx=32, pady=22,font=("Arial",22), command=lambda: tbutton_click(3))
    button_4 = Button(top5, text="4", padx=33, pady=21,font=("Arial",22), command=lambda: tbutton_click(4))
    button_5 = Button(top5, text="5", padx=32, pady=20,font=("Arial",22), command=lambda: tbutton_click(5))
    button_6 = Button(top5, text="6", padx=32, pady=22,font=("Arial",22), command=lambda: tbutton_click(6))
    button_7 = Button(top5, text="7", padx=33, pady=22,font=("Arial",22), command=lambda: tbutton_click(7))
    button_8 = Button(top5, text="8", padx=32, pady=22,font=("Arial",22), command=lambda: tbutton_click(8))
    button_9 = Button(top5, text="9", padx=32, pady=22,font=("Arial",22), command=lambda: tbutton_click(9))
    button_0 = Button(top5, text="0", padx=32, pady=16,font=("Arial",22), command=lambda: tbutton_click(0))
    button_equal = Button(top5, text="=", padx=32, pady=16, font=("Arial",22),command=tbutton_equal)
    button_quit=Button(top5, text="Exit",command=top5.destroy,font=("Arial",16),padx=26,pady=19)
    button_reset=Button(top5, text="Reset",command=tbuttonreset, font=("Arial",16),padx=18, pady=9)
    button_interchange=Button(top5,text="↑↓",command=tbuttoninterchange, font=("Arial",22),padx=28, pady=8)
    button_c = Button(top5, text="AC", command=tbuttonc, font=("Arial", 16), padx=27, pady=9)


    button_reset.grid(row=2,column=2)
    button_interchange.grid(row=2,column=0)
    button_c.grid(row=2,column=1)

    button_7.grid(row=3, column=0)
    button_8.grid(row=3, column=1)
    button_9.grid(row=3, column=2)

    button_4.grid(row=4, column=0)
    button_5.grid(row=4, column=1)
    button_6.grid(row=4, column=2)

    button_1.grid(row=5, column=0)
    button_2.grid(row=5, column=1)
    button_3.grid(row=5, column=2)

    button_0.grid(row=6, column=1)
    button_equal.grid(row=6, column=2)
    button_quit.grid(row=6, column=0)


###Speed#####--------------------------------------------------------------------------------


def sbutton_click(number):
    global s
    current = s.get()
    s.delete(0, END)
    s.insert(0, str(current) + str(number))

def sbutton_equal():
    global sunit1
    global sunit2
    global s
    global s2
    global sunits
    initial=sunit1.get()
    final=sunit2.get()
    value1=s.get()
    if initial==sunits[0] and final==sunits[1]:
        ans= int(value1)*3.6
    elif initial==sunits[0] and final==sunits[2]:
        ans= int(value1)/1000
    elif initial==sunits[0] and final==sunits[3]:
        ans= int(value1)* 2.23693629


    elif initial==sunits[1] and final==sunits[0]:
        ans= int(value1)/3.6
    elif initial==sunits[1] and final==sunits[2]:
        ans= int(value1)/3600
    elif initial==sunits[1] and final==sunits[3]:
        ans= int(value1)/1.609344


    elif initial==sunits[2] and final==sunits[0]:
        ans = int(value1)*1000
    elif initial==sunits[2] and final==sunits[1]:
        ans = int(value1)*3600
    elif initial==sunits[2] and final==sunits[3]:
        ans = int(value1)*2236.93629


    elif initial==sunits[3] and final==sunits[0]:
        ans= int(value1)/ 2.23693629
    elif initial==sunits[3] and final==sunits[1]:
        ans= int(value1)*1.609344
    elif initial==sunits[3] and final==sunits[2]:
        ans= int(value1)/2236.93629

    elif(initial==final):
        ans= int(value1)

    s2.delete(0, END)
    s2.insert(0, ans)

def sbuttoninterchange():
    global s
    global s2
    global sunit1
    global sunit2
    global sunits
    initial=sunit1.get()
    final=sunit2.get()
    for i in sunits:
        if i==initial:
            sunit2.set(i)
            break
    for i in sunits:
        if i==final:
            sunit1.set(i)
            break




def sbuttonreset():
    global s
    global s2
    global sunit1
    global sunit2
    global sunits
    s.delete(0,END)
    s2.delete(0,END)
    sunit1.set(sunits[1])
    sunit2.set(sunits[3])

def sbuttonc():
    global s
    global s2
    s.delete(0, END)
    s2.delete(0, END)


def speed():
    global s
    global s2
    global sunit1
    global sunit2
    global sunits
    top6=Toplevel()
    top6.title('Speed Converter')
    s = Entry(top6, width=25)
    s.grid(row=0, column=1, columnspan=3,pady=5)
    sunit1=StringVar()
    sunit2=StringVar()
    sunits=[
        "Meter/s m/s",
        "Kilometer/h km/h",
        "Kilometer/s km/s",
        "Miles/h m/h",
    ]
    sunit1.set(sunits[1])
    sunit2.set(sunits[3])

    drop=OptionMenu(top6,sunit1, *sunits)
    drop.grid(row=0, column=0)

    s2 = Entry(top6, width=25)
    s2.grid(row=1, column=1, columnspan=3,pady=5)
    drop2 = OptionMenu(top6, sunit2, *sunits)
    drop2.grid(row=1, column=0)

    button_1 = Button(top6, text="1", padx=33, pady=23, font=("Arial",22),command=lambda: sbutton_click(1))
    button_2 = Button(top6, text="2", padx=32, pady=22,font=("Arial",22), command=lambda: sbutton_click(2))
    button_3 = Button(top6, text="3", padx=32, pady=22,font=("Arial",22), command=lambda: sbutton_click(3))
    button_4 = Button(top6, text="4", padx=33, pady=21,font=("Arial",22), command=lambda: sbutton_click(4))
    button_5 = Button(top6, text="5", padx=32, pady=20,font=("Arial",22), command=lambda: sbutton_click(5))
    button_6 = Button(top6, text="6", padx=32, pady=22,font=("Arial",22), command=lambda: sbutton_click(6))
    button_7 = Button(top6, text="7", padx=33, pady=22,font=("Arial",22), command=lambda: sbutton_click(7))
    button_8 = Button(top6, text="8", padx=32, pady=22,font=("Arial",22), command=lambda: sbutton_click(8))
    button_9 = Button(top6, text="9", padx=32, pady=22,font=("Arial",22), command=lambda: sbutton_click(9))
    button_0 = Button(top6, text="0", padx=32, pady=16,font=("Arial",22), command=lambda: sbutton_click(0))
    button_equal = Button(top6, text="=", padx=32, pady=16, font=("Arial",22),command=sbutton_equal)
    button_quit=Button(top6, text="Exit",command=top6.destroy,font=("Arial",16),padx=26,pady=19)
    button_reset=Button(top6, text="Reset",command=sbuttonreset, font=("Arial",16),padx=18, pady=9)
    button_interchange=Button(top6,text="↑↓",command=sbuttoninterchange, font=("Arial",22),padx=28, pady=8)
    button_c = Button(top6, text="AC", command=sbuttonc, font=("Arial", 16), padx=27, pady=9)


    button_reset.grid(row=2,column=2)
    button_interchange.grid(row=2,column=0)
    button_c.grid(row=2,column=1)

    button_7.grid(row=3, column=0)
    button_8.grid(row=3, column=1)
    button_9.grid(row=3, column=2)

    button_4.grid(row=4, column=0)
    button_5.grid(row=4, column=1)
    button_6.grid(row=4, column=2)

    button_1.grid(row=5, column=0)
    button_2.grid(row=5, column=1)
    button_3.grid(row=5, column=2)

    button_0.grid(row=6, column=1)
    button_equal.grid(row=6, column=2)
    button_quit.grid(row=6, column=0)


###Mass#####--------------------------------------------------------------------------------

def mbutton_click(number):
    global m
    current = m.get()
    m.delete(0, END)
    m.insert(0, str(current) + str(number))

def mbutton_equal():
    global munit1
    global munit2
    global m
    global m2
    global munits
    initial=munit1.get()
    final=munit2.get()
    value1=m.get()
    if initial==munits[0]:
        conv= int(value1)*1000
    elif initial==munits[1]:
        conv= int(value1)
    elif initial==munits[2]:
        conv= int(value1)/1000
    elif initial==munits[3]:
        conv= int(value1)/1000000
    elif initial==munits[4]:
        conv= int(value1)*100
    elif initial==munits[5]:
        conv= int(value1)/2.20462262
    elif initial==munits[6]:
        conv= int(value1)/35.2739619



    if final==munits[0]:
        ans= conv/1000;
    elif final==munits[1]:
        ans=conv
    elif final==munits[2]:
        ans=conv*1000
    elif final==munits[3]:
        ans=conv*1000000
    elif final==munits[4]:
        ans=conv/100
    elif final==munits[5]:
        ans=conv*2.20462262
    elif final==munits[6]:
        ans=conv*35.2739619

    m2.delete(0, END)
    m2.insert(0, ans)

def mbuttoninterchange():
    global m
    global m2
    global munit1
    global munit2
    global munits
    initial=munit1.get()
    final=munit2.get()
    for i in munits:
        if i==initial:
            munit2.set(i)
            break
    for i in munits:
        if i==final:
            munit1.set(i)
            break




def mbuttonreset():
    global m
    global m2
    global munit1
    global munit2
    global munits
    m.delete(0,END)
    m2.delete(0,END)
    munit1.set(munits[1])
    munit2.set(munits[5])

def mbuttonc():
    global m
    global m2
    m.delete(0, END)
    m2.delete(0, END)


def mass():
    global m
    global m2
    global munit1
    global munit2
    global munits
    top7=Toplevel()
    top7.title('Mass Converter')
    m = Entry(top7, width=25)
    m.grid(row=0, column=1, columnspan=3,pady=5)
    munit1=StringVar()
    munit2=StringVar()
    munits=[
        "Tonne t",
        "Kilogram kg",
        "Gram g",
        "Miligram mg",
        "Quintal q",
        "Pound lb",
        "Ounce oz",
    ]
    munit1.set(munits[1])
    munit2.set(munits[5])

    drop=OptionMenu(top7,munit1, *munits)
    drop.grid(row=0, column=0)

    m2 = Entry(top7, width=25)
    m2.grid(row=1, column=1, columnspan=3,pady=5)
    drop2 = OptionMenu(top7, munit2, *munits)
    drop2.grid(row=1, column=0)

    button_1 = Button(top7, text="1", padx=33, pady=23, font=("Arial",22),command=lambda: mbutton_click(1))
    button_2 = Button(top7, text="2", padx=32, pady=22,font=("Arial",22), command=lambda: mbutton_click(2))
    button_3 = Button(top7, text="3", padx=32, pady=22,font=("Arial",22), command=lambda: mbutton_click(3))
    button_4 = Button(top7, text="4", padx=33, pady=21,font=("Arial",22), command=lambda: mbutton_click(4))
    button_5 = Button(top7, text="5", padx=32, pady=20,font=("Arial",22), command=lambda: mbutton_click(5))
    button_6 = Button(top7, text="6", padx=32, pady=22,font=("Arial",22), command=lambda: mbutton_click(6))
    button_7 = Button(top7, text="7", padx=33, pady=22,font=("Arial",22), command=lambda: mbutton_click(7))
    button_8 = Button(top7, text="8", padx=32, pady=22,font=("Arial",22), command=lambda: mbutton_click(8))
    button_9 = Button(top7, text="9", padx=32, pady=22,font=("Arial",22), command=lambda: mbutton_click(9))
    button_0 = Button(top7, text="0", padx=32, pady=16,font=("Arial",22), command=lambda: mbutton_click(0))
    button_equal = Button(top7, text="=", padx=32, pady=16, font=("Arial",22),command=mbutton_equal)
    button_quit=Button(top7, text="Exit",command=top7.destroy,font=("Arial",16),padx=26,pady=19)
    button_reset=Button(top7, text="Reset",command=mbuttonreset, font=("Arial",16),padx=18, pady=9)
    button_interchange=Button(top7,text="↑↓",command=mbuttoninterchange, font=("Arial",22),padx=28, pady=8)
    button_c = Button(top7, text="AC", command=mbuttonc, font=("Arial", 16), padx=27, pady=9)


    button_reset.grid(row=2,column=2)
    button_interchange.grid(row=2,column=0)
    button_c.grid(row=2,column=1)

    button_7.grid(row=3, column=0)
    button_8.grid(row=3, column=1)
    button_9.grid(row=3, column=2)

    button_4.grid(row=4, column=0)
    button_5.grid(row=4, column=1)
    button_6.grid(row=4, column=2)

    button_1.grid(row=5, column=0)
    button_2.grid(row=5, column=1)
    button_3.grid(row=5, column=2)

    button_0.grid(row=6, column=1)
    button_equal.grid(row=6, column=2)
    button_quit.grid(row=6, column=0)





root.mainloop()
