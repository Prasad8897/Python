import tkinter
import tkMessageBox

def message_to_the_world():
	tkinter.Button(top,text="hello world",command=message_to_the_world, pady="50px").pack()
	tkinter.Tk().mainloop()
	
top = tkinter.Tk()
top.geometry("500x500")

t = tkinter.Checkbutton(top,text="pokemon",justify='left')

t.place(x=0,y=0)
top.mainloop()