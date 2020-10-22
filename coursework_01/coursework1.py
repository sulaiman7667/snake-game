

selectedchoice = input("enter 1 to spell check a sentence. enter 2 to spell check a file: (enter 0 to quit.) ")


if (int(selectedchoice) > 2):
	print("you entered an invalid input. please try again.")

elif (int(selectedchoice) == 1):
		sentence = input("type in your sentence: ")
		words_in_sentence = []
		y = 0
		z = 0
		a = 0
		for x in range (0, len(sentence)):
	      
		   if(sentence[x] == " "):
		   
		      words_in_sentence.insert(z, sentence[a:x])
		      y = len(words_in_sentence[z])
		      z = z+1
		      a = 0
		      for word in words_in_sentence:
		       a+=len(word) + 1
		words_in_sentence.insert(z, sentence[a:len(sentence)])

		
		import sys

		with open("englishwords.txt", "r") as f:
			wordlist = f.read()
			for f in range(0, len(words_in_sentence)):
				if (words_in_sentence[f] not in wordlist):

					print("false")
		print(words_in_sentence)
		
		
				



elif (int(selectedchoice) == 2):
	file = input("enter your file name: ")



	






	

