from tkinter import *;

def message_to_the_world():
	Button(top,text="hello world",command=message_to_the_world, pady="50px").pack()
	Tk().mainloop()
	
top = Tk()
top.geometry("500x500")

t = Checkbutton(top,text="pokemon",justify='left')

t.place(x=0,y=0)
t.place_forget()

button = Button(top,text="pokemons",command=lambda:button.pack_forget())
button.pack()

top.mainloop()
