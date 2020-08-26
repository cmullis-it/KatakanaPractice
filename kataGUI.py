# GUI Practice for the application

import tkinter as tk
import kataPairs

# Create the master window, and name "Kat.Pract."
master = tk.Tk()
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
lbl_KanaPrompt = tk.Label(
	text=promptKana,
	height=2,
)
lbl_KanaPrompt.pack()


# Constant prompt explaining instructions from App
lbl_QuestionPrompt = tk.Label(
	text=promptQuestion
)
lbl_QuestionPrompt.pack()

# Entry box grabbing the input from the user. 
inputFromUser = tk.Entry(master)
inputFromUser.pack()

################################################


def checkAnswer():
	userInput = inputFromUser.get()
	if userInput == answer:
		lbl_FeedBack.config(text=rightAns)
	else:
		lbl_FeedBack.config(text=wrongAns)


################################################

# Creates button used to check answer
button = tk.Button(
	text='Check Answer',
)
button.pack()

# Creates label used to provide Right/Wrong Feedback
lbl_FeedBack = tk.Label(
)
lbl_FeedBack.pack()


master.mainloop()



 