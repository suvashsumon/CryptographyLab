def bigmod(base, power, mod):
	if power==1:
		return base
	sq = (base*base)%mod
	if power%2==0:
		return bigmod(sq, power//2, mod)
	else:
		return (bigmod(sq, power//2, mod)*base)%mod

def encryptblock(block, key, mod):
	block = int(block)
	#encrypted_block = (block**key)%mod
	encrypted_block = bigmod(block, key, mod)
	block_cipher = str(encrypted_block)
	return block_cipher

def encrypt(plaintext, key, mod, inputsize):
	ciphertext = ""
	plaintextlen = len(plaintext)
	for i in range(0, plaintextlen, inputsize):
		block = plaintext[i:i+inputsize]
		block_cipher = encryptblock(block, key, mod)
		ciphertext += block_cipher
	return ciphertext


original = "6882326879666683"
ans = "15702756209122762423158"
e = 79
d = 1019
n = 3337
encrypted = encrypt(original, e, n, 3)
decrypted = encrypt(encrypted, d, n, 4)
print("Original : ", original)
print("Encrypted : ", encrypted)
print("Decrypted : ", decrypted)
