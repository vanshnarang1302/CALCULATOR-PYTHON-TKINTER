# import tkinter as tk
#
# mainWindow=tk.Tk()
# mainWindow.title("Sample window")
#
# heading_label= tk.Label(mainWindow,text="Hello World")
# heading_label.pack()
#
# name_field=tk.Entry(mainWindow)
# name_field.pack()
#
# def takeValueInput():
#     name = name_field.get()
#     print(name)
#
# button=tk.Button(mainWindow,text="get value",command=lambda:takeValueInput())
# button.pack()
#
# mainWindow.mainloop()



##calculator

import tkinter as tk
import tkinter.messagebox as meassage
mainWindow=tk.Tk()
mainWindow.title("CALCULATOR")

headinglabel1=tk.Label(mainWindow,text='enter the first no.',padx=(10),pady=(10))
headinglabel1.pack()

firstnumber=tk.Entry(mainWindow)
firstnumber.pack()

headinglabel2=tk.Label(mainWindow,text='enter the 2nd no',padx=(10),pady=(10))
headinglabel2.pack()

secondnumber=tk.Entry(mainWindow)
secondnumber.pack()

operation=tk.Label(text='Operation',padx=(10),pady=(10))
operation.pack()

def addition():
    try:
        first = int(firstnumber.get())
        second = int(secondnumber.get())
        x = first + second
        # print(x)
        resaultlabel.config(text='operation result is' + str(x))

    except ValueError:

        meassage.showerror('error','please enter any interger value')

    print('ucbdc')

def sub():
    try:
        first = int(firstnumber.get())
        second = int(secondnumber.get())
        x = first - second
        # print(x)
        resaultlabel.config(text='operation result is' + str(x))
    except ValueError:

        meassage.showerror('error', 'please enter any interger value')



def mul():
    try:
        first =int(firstnumber.get())
        second =int(secondnumber.get())
        x = first * second
        # print(x)
        resaultlabel.config(text='operation result is' + str(x))

    except ValueError:

        meassage.showerror('ERROR','please enter any interger value')




def div():
    try:
        first=firstnumber.get()
        second=secondnumber.get()

        first=int(first)
        second=int(second)
        x = first / second
        resaultlabel.config(text='operation result is' + str(x))
    except ValueError:

        meassage.showerror('INVALID INPUT','Enter only interger value ')


    except ZeroDivisionError:
        meassage.showerror('error','2nd no. cannot be zero')



            # print(x)

add=tk.Button(mainWindow,text='+',command=lambda : addition())
add.pack()

subb=tk.Button(mainWindow,text='-',command=lambda  : sub())
subb.pack()

mull=tk.Button(mainWindow,text='*',command = lambda : mul())
mull.pack()

divv=tk.Button(mainWindow,text='/',command =lambda : div())
divv.pack()

resaultlabel=tk.Label(mainWindow,text='operation result is:',padx=(10),pady=(10))
resaultlabel.pack()
mainWindow.mainloop()