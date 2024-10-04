def encrypt(plaintext, onetimepad):
	plaintextlen = len(plaintext)
	ciphertext = ""
	for i in range(plaintextlen):
		ch = plaintext[i]
		key = onetimepad[i]
		if ch.isupper():
			ciphertext += chr(((ord(ch)-65) + (ord(key)-65))%26 + 65)
		elif ch.islower():
			ciphertext += chr(((ord(ch)-97) + (ord(key)-65))%26 + 97)
	return ciphertext
	
def decrypt(ciphertext, onetimepad):
	ciphertextlen = len(ciphertext)
	plaintext = ""
	for i in range(ciphertextlen):
		ch = ciphertext[i]
		key = onetimepad[i]
		if ch.isupper():
			plaintext += chr(((ord(ch)-65) - (ord(key)-65))%26 + 65)
		elif ch.islower():
			plaintext += chr(((ord(ch)-97) - (ord(key)-65))%26 + 97)
	return plaintext

original = input("Original : ")
onetimepad = "JFUEOFVBOUGJHBFDVKDFVKBADMVCBAKLJFGBOAURBFLKAVBLKAJVBBHFVSEHFIUADAKVJCHAERFGAJDFNVAMKNVADUORFHAKJDFNOUADHGVKADHBVKAKASDFAJFVBAKLGALJFKADFLABLDJKFGABDUVASGHVFKAKAJDEFGDSFDSDFBJHBEBSJBFJSDUYYFBJSBDFKVBSDYFGCSDGKSBCVKSSSSSSKJHJHAEWQQWEUHWIRUDSSDBBZZXCZXMVXNSJFOIHFSKJDBCSIUEJKJSHDFSDGFSDFJKSDKJBSAKBCVIEURBFVKSJDLSKSDFJHSDJHFJSDRGJHDSFJVSDJFVSUYEGKIERJBSDVBDVFVBJSCGZXJCVKXZJVFYXZCTVEWUYWIOUUWEOVBSKDJFHSWUFSIEYWIE"
encrypted = encrypt(original, onetimepad)
decrypted = decrypt(encrypted, onetimepad)
print("Encrypted : ", encrypted)
print("Decrypted : ", decrypted)
