import tkinter
import tkMessageBox

def message_to_the_world():
	tkinter.Button(top,text="hello world",command=message_to_the_world, pady="50px").pack()
	tkinter.Tk().mainloop()
	
top = tkinter.Tk()
top.geometry("500x500")

t = tkinter.Text(top)
for i in range(100):
	t.insert("insert", str(i)+" ")

t.pack()
top.mainloop()