plaintext = input("input cyphertexttext: ")
ciphertext = ""
plaintextpos = 0
while (plaintextpos < len(plaintext)):
	plaintextchar = plaintext[plaintextpos]
	ASCIIValue = ord(plaintextchar)
	ASCIIValue = ASCIIValue + 3
	ciphertext = ciphertext + chr(ASCIIValue)
	plaintextpos = plaintextpos + 1
print(ciphertext)	