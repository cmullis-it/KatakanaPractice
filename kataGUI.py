# GUI Practice for the application

from tkinter import *
import kataPairs

# Create the master window, and name "Kat.Pract."
master = Tk()
master.title("Katakana Practice")


# Placeholders for the prompt/ correct answer that user 
# input is being compared against. 
promptKana = "マ"
promptQuestion = "Enter Romanji for this Kana"
answer = "ma"


# Answers for romanji the user is inputing
rightAns = "Correct!"
wrongAns = "Sorry, that was wrong"


# The Kana Label that will shift through the various Kana
lbl_KanaPrompt = Label(
	text=promptKana,
	height=2,
)
lbl_KanaPrompt.pack()

lbl_KanaAnswer = Label(
	text=answer,
)

# Constant prompt explaining instructions from App
lbl_QuestionPrompt = Label(
	text=promptQuestion
)
lbl_QuestionPrompt.pack()

# Entry box grabbing the input from the user. 
inputFromUser = Entry(master)
inputFromUser.pack()

################################################

'''
def checkAnswer():
	userInput = entry.get()
	if userInput == answer:
		feedBack_lbl.config(text=rightAns)
	else:
		feedBack_lbl.config(text=wrongAns)
'''

################################################

# Creates button used to check answer
button = Button(
	text='Check Answer',
)
button.pack()

# Creates label used to provide Right/Wrong Feedback
lbl_FeedBack = Label(
)
lbl_FeedBack.pack()




master.mainloop()



 