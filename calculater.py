from tkinter import *

def click(event):
	global scvalue
	text = event.widget.cget("text")
	print(text)
	if text == "=":
		if scvalue.get().isdigit():
			value = int(scvalue.get())
		else :
			value = eval(scvalue.get())
		scvalue.set(value)
		screen.update()
	elif text == "c":
		scvalue.set("")
		screen.update()
	else:
		scvalue.set(scvalue.get()+text)
		screen.update()

root = Tk()
root.geometry("644x600")
root.title("Calculator")


scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvariable= scvalue,font= "Lucida 40 bold")
screen.pack(side="top",ipadx = 10,padx = 10,pady = 10)

f1 = Frame(root,bg = "grey")

b9 = Button(f1,text = "9",font = "Lucida 35 bold",padx = 10)
b9.bind("<Button-1>",click)
b9.pack(side = "left",ipadx = 10,padx = 10,pady = 5)

b8 = Button(f1,text = "8",font = "Lucida 35 bold",padx = 10)
b8.bind("<Button-1>",click)
b8.pack(side = "left",ipadx = 10,padx = 10,pady = 5)

b7 = Button(f1,text = "7",font = "Lucida 35 bold",padx = 10)
b7.bind("<Button-1>",click)
b7.pack(side = "left",ipadx = 10,padx = 10,pady = 5)

b10 = Button(f1,text = "*",font = "Lucida 35 bold",padx = 10)
b10.bind("<Button-1>",click)
b10.pack(side = "left",ipadx = 10,padx = 10,pady = 5)
f1.pack(side = "top")

f1 = Frame(root,bg = "grey")
b6 = Button(f1,text = "6",font = "Lucida 35 bold",padx = 10)
b6.bind("<Button-1>",click)
b6.pack(side = "left",ipadx = 10,padx = 10,pady = 5)

b5 = Button(f1,text = "5",font = "Lucida 35 bold",padx = 10)
b5.bind("<Button-1>",click)
b5.pack(side = "left",ipadx = 10,padx = 10,pady = 5)

b4 = Button(f1,text = "4",font = "Lucida 35 bold",padx = 10)
b4.bind("<Button-1>",click)
b4.pack(side = "left",ipadx = 10,padx = 10,pady = 5)

b11 = Button(f1,text = "-",font = "Lucida 35 bold",padx = 10)
b11.bind("<Button-1>",click)
b11.pack(side = "left",ipadx = 10,padx = 10,pady = 5)
f1.pack(side = "top")


f1 = Frame(root,bg = "grey")
b3 = Button(f1,text = "3",font = "Lucida 35 bold",padx = 10)
b3.bind("<Button-1>",click)
b3.pack(side = "left",ipadx = 10,padx = 10,pady = 5)

b2 = Button(f1,text = "2",font = "Lucida 35 bold",padx = 10)
b2.bind("<Button-1>",click)
b2.pack(side = "left",ipadx = 10,padx = 10,pady = 5)

b1 = Button(f1,text = "1",font = "Lucida 35 bold",padx = 10)
b1.bind("<Button-1>",click)
b1.pack(side = "left",ipadx = 10,padx = 10,pady = 5)

b12 = Button(f1,text = "+",font = "Lucida 35 bold",padx = 5)
b12.bind("<Button-1>",click)
b12.pack(side = "left",ipadx = 10,padx = 10,pady = 5)
f1.pack(side = "top")

f1 = Frame(root,bg = "grey")
b13 = Button(f1,text = "0",font = "Lucida 35 bold",padx = 10)
b13.bind("<Button-1>",click)
b13.pack(side = "left",ipadx = 10,padx = 10,pady = 5)

b14 = Button(f1,text = "c",font = "Lucida 35 bold",padx = 10)
b14.bind("<Button-1>",click)
b14.pack(side = "left",ipadx = 10,padx = 10,pady = 5)

b15 = Button(f1,text = "=",font = "Lucida 35 bold",padx = 10)
b15.bind("<Button-1>",click)
b15.pack(side = "left",ipadx = 10,padx = 10,pady = 5)

b16 = Button(f1,text = "/",font = "Lucida 35 bold",padx = 10)
b16.bind("<Button-1>",click)
b16.pack(side = "left",ipadx = 10,padx = 10,pady = 5)
f1.pack(side = "top")

root.mainloop()