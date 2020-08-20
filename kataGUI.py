# GUI Practice for the application

from tkinter import *

master = Tk()
master.title("Katakana Practice")

prompt = "マ"

answer = "ma"

rightAns = "Correct!"
wrongAns = "Sorry, that was wrong"

def checkAnswer():
		feedBack_lbl.config(text=rightAns)


label = Label(
	text=prompt
	)
label.pack()

button = Button(
	text='Check Answer',
	command=checkAnswer,
)
button.pack()

entry = Entry()
entry.pack()

userInput = entry.get()

feedBack_lbl = Label(
	text=''
)
feedBack_lbl.pack()




master.mainloop()



 