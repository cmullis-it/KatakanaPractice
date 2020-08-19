# GUI Practice for the application

from tkinter import *


master = Tk()

textLine = "Hello World!"


helloWorldLabel = Label(
	text=textLine
	)
helloWorldLabel.pack()

def newLabel():
	newLabel = Label(
		text="This is a new label")
	label.pack()

button1 = Button(
	text="Press me",
	command=newLabel)
button1.pack()


master.mainloop()



 