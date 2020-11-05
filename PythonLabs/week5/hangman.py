import random
thewords = ["red", "yellow", "blue", "green", "pink"]

word = random.choice(thewords)

count = 0
win = False
guesses = ""
answer = "______"
while (count < 10 and win == False):
	count = count + 1
	guess = input("enter guess " + str(count))
	guesses = guesses + guess
	tmp = ""
	i = 0
	while (i < len(word)):
		if (word[i] == guess):
			tmp = tmp + guess
		else:
			tmp = tmp + answer[i]
		i = i + 1
	if(answer != tmp):
		print ("gd guess")
		count = count - 1
		answer = tmp
	else:
		print("not a gd guess")
	if(answer == word):
		print("well done u win")
		win = True
	print(str(10-count) + "/10 guesses left")
	print("your guesses: " + guesses)
	print("the word so far: " + answer)
