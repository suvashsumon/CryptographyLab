def encrypt(in_text, shift=3):
	out_text = ""
	for ch in in_text:
		if ch.isalpha() and ch.isupper():
			out_text += chr((ord(ch)-65+shift)%26+65)
		elif ch.isalpha() and ch.islower():
			out_text += chr((ord(ch)-97+shift)%26+97)
		else:
			out_text += ch
	return out_text

def decrypt(in_text, shift=3):
	out_text = ""
	for ch in in_text:
		if ch.isalpha() and ch.isupper():
			out_text += chr((ord(ch)-65-shift)%26+65)
		elif ch.isalpha() and ch.islower():
			out_text += chr((ord(ch)-97-shift)%26+97)
		else:
			out_text += ch
	return out_text		
	
original = "Amar Sonar Bangla Ami 1234&721)8923"	
encrypted = encrypt(original)
decrypted = decrypt(encrypted)
print("Original Text: ", original)
print("Encrypted: ", encrypted)
print("Decrypted: ", decrypted)
if original==decrypted:
	print("SUCCESS")
