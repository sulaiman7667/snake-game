import difflib

with open("englishwords.txt", "r") as f:
	wordlist = f.read()


	

#####################################################
while True:
	selectedchoice = input("enter 1 to spell check a sentence. enter 2 to spell check a file: (enter 0 to quit.) ")
	if (int(selectedchoice) < 3):
		break
	print("you entered an invalid input. please try again.")	



if (int(selectedchoice) == 1):
	sentence = input("type in your sentence: ")
	errors = 0
	errorslist = []
	for word in sentence.casefold().split():
		if (word not in wordlist):
			errors = errors + 1
			errorslist.append(word)
	if(errors > 0):
		option = input("select an option:" + "\n1. Ignore error." + "\n2. Find error." + "\n3. Add word to dictionary." + "\n4. Find possible suggestions.")
		
		if (int(option) == 1):
				quit()

		elif (int(option) == 2):
			for i in range (0, len(errorslist)):
				print("?" + errorslist[i] + "?")
			




		elif(int(option) == 3):
				f = open("englishwords.txt", "a")
				for g in range (0, len(errorslist)):
			 		f.write("\n" + errorslist[g])

		elif (int(option) == 4):
			for g in range (0, len(errorslist)):
				suggestion = difflib.get_close_matches(errorslist[g], wordlist)
				print(f' did you mean {", ".join(str(x) for x in suggestion)} instead of lol')

				 		


		
				



if (int(selectedchoice) == 2):
	file = input("enter your file name: ")
	with open(file, "r") as f:
		textfile = f.read()
	errors = 0
	errorslist = []
	for word in textfile.casefold().split():
		if (word not in wordlist):
			errors = errors + 1
			errorslist.append(word)
	if(errors > 0):
		option = input("select an option:" + "\n1. Ignore error." + "\n2. Find error." + "\n3. Add word to dictionary." + "\n4. Find possible suggestions.")
		
		if (int(option) == 1):
				quit()

		elif (int(option) == 2):
			for i in range (0, len(errorslist)):
				print("?" + errorslist[i] + "?")
			




		elif(int(option) == 3):
				f = open("englishwords.txt", "a")
				for g in range (0, len(errorslist)):
			 		f.write("\n" + errorslist[g])

		elif (int(option) == 4):
			for g in range (0, len(errorslist)):
				suggestion = difflib.get_close_matches(errorslist[g], wordlist)
				print(f' did you mean {", ".join(str(x) for x in suggestion)} instead of lol')	

















