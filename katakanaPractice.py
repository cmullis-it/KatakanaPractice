# Katakana Practice

import random

kataDict = {
	'ア': 'a',
	'イ': 'i',
	'ウ': 'u',
	'エ': 'e',
	'オ': 'o',
	}

kataList = list(kataDict.keys())
random.shuffle(kataList)


for kata in kataList:
	print(kata)
	answer = input('How do you pronounce this kana?\n')
	stripped_answer = answer.strip()
	if stripped_answer.lower() == kataDict[kata]:
		print("Right!\n")

	else:
		print("Wrong.\n")
	

# Debug Code: print(kataDict)





##### Features that need to be added

'''
Need to be able to decide which Kana you want to be able to practice

Make it so that it goes through the ones that you have missed, again.

Add a UI

Clean up the current 'UI' 

'''

