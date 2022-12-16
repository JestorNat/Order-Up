from tkinter import *

mainPage= Tk()
mainPage.geometry('350x350')
mainPage.title('Order Up')

name_label = Label(mainPage,text='Name for the order:')
name_label.grid(row=0, column=0)

name_entry = Entry(mainPage, width=20)
name_entry.grid(row=0, column=1)

address_label = Label(mainPage,text='Address for delivery:')
address_label.grid(row=1, column=0)

address_entry = Entry(mainPage, width=20)
address_entry.grid(row=1, column=1)

#Sizes of Pizza
size_label = Label(mainPage,text='Pick a size of Pizza \nSmall = 5$ Medium = 7.50$ Large = 9$')
size_label.grid(row=2, column=1)

sizesOfpizza = ('Small','Medium','Large')


secondPage= Tk()
secondPage.geometry('250x350')
secondPage.title('Your Total')









 
mainPage.mainloop()
