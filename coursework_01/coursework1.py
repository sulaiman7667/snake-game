import difflib
import re
import os.path
from datetime import datetime
#import time

with open("englishwords.txt", "r") as f:
	wordlist = f.read()


	

#####################################################
while True:
	selectedchoice = input("\nPlease select an option: \n1.Spell check a sentence. \n2.Spell check a file. \n3.Quit program. \n")
	if (selectedchoice == str(3) or selectedchoice == str(1) or selectedchoice == str(2)):
		break
	print("You entered an invalid input, please try again.")	


if(str(selectedchoice) == str(3)):
	quit()
if (str(selectedchoice) == str(1)):
	sentence = input("Please type in your sentence: ")
	t0 = datetime.now()
	time = datetime.now()
	sentence = re.sub('[^A-Za-z ]+', '', sentence)
	errors = 0
	errorslist = []
	wordcounter = 0
	dicounter = 0
	for word in sentence.casefold().split():
		wordcounter = wordcounter + 1
		if (word not in wordlist):
			errors = errors + 1
			errorslist.append(word)
	if(errors > 0):
		for m in range(0, len(errorslist)):
			print("")
			print(str(len(errorslist)) + " Error(s) found")
			print("Error[" + str(m+1) + "]: " + errorslist[m])
			option = str(input("\nSelect an option:" + "\n1.Ignore error." + "\n2.Display all errors." + "\n3.Add word to dictionary." + "\n4.Find possible suggestions.\n" + "5.Quit program\n"))

			while True:

				if (str(option) == str(1)):
						print()
						break

				elif (str(option) == str(2)):
					for i in range (0, len(errorslist)):
						print("?" + errorslist[i] + "?")
					break		
					

				elif(str(option) == str(3)):
					f = open("englishwords.txt", "a")
					f.write("\n" + errorslist[m])
					dicounter = dicounter + 1
					break

				elif (str(option) == str(4)):
					with open("englishwords.txt", "r") as f:
						wordlist = f.read()
					print (difflib.get_close_matches(errorslist[m], wordlist))
					break
				elif(str(option) == str(5)):
					quit()
				
				print("Incorrect input please try again. \n")
				option = input("")	


	t1 = datetime.now() - t0			
					



if (str(selectedchoice) == str(2)):
	while True:	
		file = input("enter your file name: ")
		if (os.path.exists(file)):	
			with open(file, "r") as f:
				textfile = f.read()
				break
		else:
			print("Incorrect input please try again. \n")
			continue
	t0 = datetime.now()
	time = datetime.now()
	textfile = re.sub('[^A-Za-z ]+', '', textfile)	
	errors = 0
	errorslist = []
	wordcounter= 0 
	dicounter = 0
	for word in textfile.casefold().split():
		wordcounter = wordcounter + 1
		if (word not in wordlist):
			errors = errors + 1
			errorslist.append(word)
	if(errors > 0):
		for m in range(0, len(errorslist)):
			print("")
			print(str(len(errorslist)) + " Error(s) found")
			print("Error[" + str(m+1) + "]: " + errorslist[m])
			option = str(input("\nselect an option:" + "\n1. Ignore error." + "\n2. Display all errors." + "\n3. Add word to dictionary." + "\n4. Find possible suggestions. \n"))

			while True:
				if (str(option) == str(1)):
					print()
					break	

				elif (str(option) == str(2)):
					for i in range (0, len(errorslist)):
						print("?" + errorslist[i] + "?")
					break	
					




				elif(str(option) == str(3)):
					f = open("englishwords.txt", "a")
					f.write("\n" + errorslist[m])
					dicounter = dicounter + 1
					break

				elif (str(option) == str(4)):
					for g in range (0, len(errorslist)):
						print(difflib.get_close_matches(errorslist[g], wordlist))
					break
				print("Incorrect input please try again. \n")
				option = input("")			
	t1 = datetime.now() - t0			
print("\nNumber of words: " + str(wordcounter))
print("Number of words spelled correctly: " + str(wordcounter - errors))
print("Number of words spelled incorrectly: " + str(errors))
print("Number of words added to dictionary: " + str(dicounter))
print("Date and time input was spellchecked: " + str(time))
print("Time elapsed: " + str(t1) + "\n")

















