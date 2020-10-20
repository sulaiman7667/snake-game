plaintext = input("input text: ")
ciphertext = ""
alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
plaintextpos = 0
while (plaintextpos < len(plaintext)):
	plaintextchar = plaintext[plaintextpos]
	alphabetpos = 3
	while (plaintextchar != alphabet[alphabetpos]):
		alphabetpos = alphabetpos + 1
	alphabetpos = alphabetpos - 3
	ciphertext = ciphertext + alphabet[alphabetpos]
	plaintextpos = plaintextpos + 1
print(ciphertext)		
