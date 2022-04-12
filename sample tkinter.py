from tkinter import *

calculator = Tk()

def hisobla():
    pass
   
    
     

kiritiladiganjoy1 = Entry(calculator, width=26,bg = "PowderBlue",fg = "DarkRed", borderwidth = 10).place(x = 25,y = 25)
#kiritiladiganjoy.insert(0,"Sonni kiriting:\t")
kiritiladiganjoy2 = Entry(calculator, width=26,bg = "PowderBlue",fg = "DarkRed", borderwidth = 10).place(x = 25,y = 65)
bosilsin = Button(calculator, text = "Hisobla",bg = "LightSalmon",borderwidth = 7, width=8, command = hisobla).place(x = 204,y = 65)
tozala = Button(calculator, text = "Tozala",bg = "LightSalmon",borderwidth = 7, width=8, command = hisobla).place(x = 204,y = 25)

one = Button(calculator, text = "1",bg = "LightSalmon",borderwidth = 7,width = 5).place(x=24,y=104)
two = Button(calculator, text = "2",bg = "LightSalmon",borderwidth = 7,width = 5).place(x=84,y=104)
three = Button(calculator, text = "3",bg = "LightSalmon",borderwidth = 7,width = 5).place(x=144,y=104)
plus = Button(calculator, text = "+",bg = "LawnGreen",borderwidth = 7,width = 5).place(x=204,y=104)
four = Button(calculator, text = "4",bg = "LightSalmon",borderwidth = 7,width = 5).place(x=24,y=144)
five = Button(calculator, text = "5",bg = "LightSalmon",borderwidth = 7,width = 5).place(x=84,y=144)
six = Button(calculator, text = "6",bg = "LightSalmon",borderwidth = 7,width = 5).place(x=144,y=144)
minus = Button(calculator, text = "-",bg = "LawnGreen",borderwidth = 7,width = 5).place(x=204,y=144)
seven = Button(calculator, text = "7",bg = "LightSalmon",borderwidth = 7,width = 5).place(x=24,y=184)
eight = Button(calculator, text = "8",bg = "LightSalmon",borderwidth = 7,width = 5).place(x=84,y=184)
nine = Button(calculator, text = "9",bg = "LightSalmon",borderwidth = 7,width = 5).place(x=144,y=184)
kop = Button(calculator, text = "*",bg = "LawnGreen",borderwidth = 7,width = 5).place(x=204,y=184)

calculator.mainloop()