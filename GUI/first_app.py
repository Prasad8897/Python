from tkinter import *;
from methods import *;
top = Tk()
top.geometry("500x500")

butt = Button(top,text='add a cb',command=createcb((top,)))
cb=Checkbutton(top,text='this is a lable frame')
cb.pack()
butt.pack()

top.mainloop()
