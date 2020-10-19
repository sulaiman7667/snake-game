selectedchoice = int(input("enter 1 to spell check a sentence. enter 2 to spell check a file: (enter 0 to quit.) "))


if (int(selectedchoice) != int(0 or 1 or 2)):
	print("you entered an invalid input. please try again.")
	selectedchoice

elif (selectedchoice == 1):
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
	       a+=len(word)
	words_in_sentence.insert(z, sentence[a:len(sentence)])






 

else:
	file = input("enter your file name: ")
	open(file)
print(words_in_sentence)

	

