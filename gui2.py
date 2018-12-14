from tkinter import *




window = Tk()
#initialize the value that you enter
e1_value = StringVar()
def delete():
    t1.delete(0, 'end')
    t2.delete(0, 'end')
    t3.delete(0, 'end')

def conversion():
    delete()
    grams = int(e1_value.get())*1000
    t1.insert(END,grams)
    pounds= int(e1_value.get())*2.20462
    t2.insert(END,pounds)
    ounces= int(e1_value.get())*35.274
    t3.insert(END,ounces)

#make a label so you can have the kg be static without you being able to change it
l1 = Label(window, text="KG")
#put it in the first row first column
l1.grid(row=0, column =0)

#make the text field that you enter the number you wish to Convert
e1 = Entry(window, textvariable = e1_value)
e1.grid(row =0, column = 1)
#this is the button that will collect the variable
b1 = Button(window, text = "Convert", command = conversion)
b1.grid(row = 0, column = 2)

t1 = Entry(window)
t1.grid(row=1, column = 0)

t2 = Entry(window)
t2.grid(row=1, column = 1)

t3 = Entry(window)
t3.grid(row=1, column = 2)

window.mainloop()
