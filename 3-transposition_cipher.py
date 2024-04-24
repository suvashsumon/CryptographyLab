def encryption(plain_text, block_size) -> str:
    cipher = ""
    text_len = len(plain_text)
    number_of_block = (text_len + block_size - 1) // block_size
    for i in range(block_size):
        for j in range(number_of_block):
            index = block_size*j + i
            if(index<text_len):
                cipher = cipher + plain_text[index]
            else:
                cipher = cipher + "*"  # * will be considered as dummy character
    return cipher

def decryption(cipher_text, block_size) -> str:
    plain_text = ""
    cipher_len = len(cipher_text)
    number_of_blocks = (cipher_len + block_size - 1) // block_size
    for i in range(number_of_blocks):
        for j in range(block_size):
            index = number_of_blocks * j + i
            if index<cipher_len and cipher_text[index]!='*':
                plain_text = plain_text + cipher_text[index]
    return plain_text

plain_text = "DEPARTMENT OF COMPUTER SCIENCE AND TECHNOLY UNIVERSITY OF RAJSHAHI BANGLADESH"
#plain_text = "helloworldbangladeshok"
print("Plain Text :", plain_text)
block_size = int(input("Enter Block Size/Width : "))
cipher_text = encryption(plain_text, block_size)
print(f"encrypted text => |{cipher_text}|")
decrypted_text = decryption(cipher_text, block_size)
print(f"decrypted text => |{decrypted_text}|")


if plain_text==decrypted_text:
    print("======= YOU SUCCESSFULY DID THIS ========")