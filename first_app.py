from tkinter import *;

def message_to_the_world():
	Button(top,text="hello world",command=message_to_the_world, pady="50px").pack()
	Tk().mainloop()
	
top = Tk()
top.geometry("500x500")
top.mainloop()