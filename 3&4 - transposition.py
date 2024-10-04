def encrypt(plaintext, block_size):
	ciphertext = ""
	textlen = len(plaintext)
	number_of_block = (textlen+block_size-1)//block_size
	for i in range(block_size):
		for j in range(number_of_block):
			index = block_size*j + i
			if(index<textlen):
				ciphertext += plaintext[index]
			else:
				ciphertext += "*"
	return ciphertext
	
def decrypt(ciphertext, block_size):
	plaintext = ""
	cipherlen = len(ciphertext)
	number_of_block = (cipherlen + block_size - 1)//block_size
	for i in range(number_of_block):
		for j in range(block_size):
			index = number_of_block*j + i
			if index<cipherlen and ciphertext[index]!="*":
				plaintext += ciphertext[index]
	return plaintext


#original = "DEPARTMENT OF COMPUTER SCIENCE AND TECHNOLOGY UNIVERSITY OF RAJSHAHI BANGLADESH"
original = input("Original text : ")
block_size = int(input("Enter Block Size: "))
encrypted = encrypt(original, block_size)
decrypted = decrypt(encrypted, block_size)
print("Original : ", original)
print("Encrypted : ", encrypted)
print("Decrypted : ", decrypted)

print("===============")

denc = encrypt(encrypt(original, block_size), block_size)
ddec = decrypt(decrypt(denc, block_size), block_size)
print("D. Original : ", original)
print("D. Encrypted : ", denc)
print("D. Decrypted : ", ddec)

print("===============")

tenc = encrypt(encrypt(encrypt(original, block_size), block_size), block_size)
tdec = decrypt(decrypt(decrypt(tenc, block_size), block_size), block_size)
print("T. Original : ", original)
print("T. Encrypted : ", tenc)
print("T. Decrypted : ", tdec)
