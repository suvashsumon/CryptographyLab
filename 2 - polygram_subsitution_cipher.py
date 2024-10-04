def encryption(in_text, dictionary, block=3):
	out_text = ""
	count = 0
	blk = ""
	for ch in in_text:
		blk += ch
		count += 1
		if count==block:
			out_text += dictionary[blk]
			blk = ""
			count = 0
	if blk!="":
		out_text += dictionary[blk]
	return out_text
	
def decryption(in_text, dictionary, block=3):
	out_text = ""
	count = 0
	blk = ""
	for ch in in_text:
		blk += ch
		count += 1
		if count==block:
			out_text += dictionary[blk]
			blk = ""
			count = 0
	if blk!="":
		out_text += dictionary[blk]
	return out_text

# reading input
original = "AMARSONARBANGLAAS"
file = open("keymap.txt", "r")
lines = file.readlines()
fdict = {}
bdict = {}
for line in lines:
	key1, key2 = line.split()
	fdict[key1] = key2
	bdict[key2] = key1

# computing output
encrypted = encryption(original, fdict)
decrypted = decryption(encrypted, bdict)
print("Original: ", original)
print("Encrypted: ", encrypted)
print("Decrypted: ", decrypted)
if original == decrypted:
	print("SUCCESS")

