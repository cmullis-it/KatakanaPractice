# Katakana Practice

import random		# random is imported for shuffle to mix up the order
import kataPairs 	# Katkana dictionary used to pair up katakana and romanji

# This grabs the dictionary and creates a name for it here. 
kataDict = kataPairs.katakanaPairs

# Grabs the keys from the Dictionary and create a list, and shuffles order
kataList = list(kataDict.keys())
random.shuffle(kataList)


# Prints the kana, then asks the user for input, checks against value in 
# dictionary to see if correct
for kata in kataList:
	print(kata)
	answer = input('How do you pronounce this kana?\n')
	stripped_answer = answer.strip()
	if stripped_answer.lower() == "exit":
		break
	elif stripped_answer.lower() == kataDict[kata]:
		print("Right!\n")

	else:
		print("Incorrect :(\n")
	

##### Features that need to be added

'''

[x] Seperate the data from the code that runs the actual practice app
[x] Clean up the current 'UI' 
[x] Added 'exit' command for quick debugging right now

[ ] Add full list of katakana and romanji to match. 

[ ] Add a counter so you know how many you got wrong, and how many you got right.

[ ] Need to be able to decide which Kana you want to be able to practice

[ ] Make it so that it goes through the ones that you have missed, again.

[ ] Add a UI


'''

