import difflib
import re
import os.path
from datetime import datetime


with open("englishwords.txt", "r") as f:
	wordlist = f.read()





# Select options	
while True:
	selectedchoice = input("\nPlease select an option: \n1.Spell check a sentence. \n2.Spell check a file. \n3.Quit program. \n")
	if (selectedchoice == str(3) or selectedchoice == str(1) or selectedchoice == str(2)):
		break
	print("You entered an invalid input, please try again.")	





# quit program
if(str(selectedchoice) == str(3)):
	quit()





# spellcheck sentence
if (str(selectedchoice) == str(1)):
	sentence = input("Please type in your sentence: ")
	t0 = datetime.now()
	time = datetime.now()
	sentence = re.sub('[^A-Za-z ]+', '', sentence)
	errors = 0
	errorslist = []
	wordcounter = 0
	dicounter = 0
	sucounter = 0

	#split into list and check spelling
	for word in sentence.casefold().split():
		wordcounter = wordcounter + 1
		dictionary = wordlist.casefold().split()
		if (word not in dictionary):
			errors = errors + 1
			errorslist.append(word)

	#if errors are found select options		
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
					suggestion = (difflib.get_close_matches(errorslist[m], dictionary))
					if(suggestion == []):
						print("No suggestions found.")
					else:
						print("\nSuggestion: " + str(suggestion[0]))

						

					suggestionopt = str(input("\nSelect an option: \n" + "1. Accept suggestion.\n" + "2. Ignore suggestion.\n"))
					
					if(str(suggestionopt) == str(1)):
						sentence = sentence.replace(str(errorslist[m]),str(suggestion[0]))
						sucounter = sucounter + 1
						print("")
						print("Updated sentence: \n" + sentence)


					if(str(suggestionopt) == str(2)):
						print("")	
					break
				
				elif(str(option) == str(5)):
					quit()
				
				print("Incorrect input please try again. \n")
				option = input("")	


	t1 = datetime.now() - t0			
					




# spellcheck file
if (str(selectedchoice) == str(2)):
	while True:	
		file = str(input("enter your file name: "))
		if (os.path.exists(file)):	
			with open(file, "r") as f:
				textfile = f.read()
				break
		else:
			print("File not found or path is incorrect. \n")
			continue
	t0 = datetime.now()
	time = datetime.now()
	textfile = re.sub('[^A-Za-z ]+', '', textfile)	
	newfile = textfile
	errors = 0
	errorslist = []
	wordcounter= 0 
	dicounter = 0
	sucounter = 0

	#split into list and check spelling
	for word in textfile.casefold().split():
		wordcounter = wordcounter + 1
		dictionary = wordlist.casefold().split()
		if (word not in dictionary):
			errors = errors + 1
			errorslist.append(word)

	#if errors are found select options		
	if(errors > 0):
		for m in range(0, len(errorslist)):
			print("")
			print(str(len(errorslist)) + " Error(s) found")
			print("Error[" + str(m+1) + "]: " + errorslist[m])
			option = str(input("\nselect an option:" + "\n1. Ignore error." + "\n2. Display all errors." + "\n3. Add word to dictionary." + "\n4. Find possible suggestions. \n" + "5. Quit program. \n"))

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
					suggestion = (difflib.get_close_matches(errorslist[m], dictionary))
					if(suggestion == []):
						print("No suggestions found.")
					else:
						print("")
						print("Suggestion: " + str(suggestion[0]))
						print("")

					suggestionopt = str(input("Select an option: \n" + "1. Accept suggestion.\n" + "2. Ignore suggestion.\n"))
					
					if(str(suggestionopt) == str(1)):
						sucounter = sucounter + 1
						with open(file) as f:
							textfile = f.read()
							with open(file, "w") as f:
								textfile = textfile.replace(str(errorslist[m]),str(suggestion[0]))
								f.write(textfile)

					if(str(suggestionopt) == str(2)):
						print("")
					break

				

				elif(str(option) == str(0)):
					quit()


				print("Incorrect input please try again. \n")
				option = input("")	

	
		filename = input("Please enter a name for your textfile that contains your original text: \n ")

		
	t1 = datetime.now() - t0	






# print statistics			
print("\nNumber of words: " + str(wordcounter))
print("Number of words spelled correctly: " + str(wordcounter - errors))
print("Number of words spelled incorrectly: " + str(errors))
print("Number of words added to dictionary: " + str(dicounter))
print("Number of words replaced by suggestions: " + str(sucounter))
print("Date and time input was spellchecked: " + str(time))
print("Time elapsed: " + str(t1) + "\n")



f = open(filename,"w+")
f.write("Number of words: " + str(wordcounter) + "\n")
f.write("Number of words spelled correctly: " + str(wordcounter - errors) + "\n")
f.write("Number of words spelled incorrectly: " + str(errors) + "\n")
f.write("Number of words added to dictionary: " + str(dicounter) + "\n")
f.write("Number of words replaced by suggestions: " + str(sucounter) + "\n")
f.write("Date and time input was spellchecked: " + str(time) + "\n") 	
f.write("Time elapsed: " + str(t1) + "\n"  + "\n")
newfile1 = f.writelines(newfile)



















