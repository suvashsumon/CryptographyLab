def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isalpha() and char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif (char.isalpha() and char.islower()):
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char

    return result

def decrypt(text, s):
    return encrypt(text, 26-s)
 


text = input("Enter a text to check : ")
s = 3
cipher = encrypt(text, s)
print ("Text  : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + cipher)
print ("Decrypted Text: " + decrypt(cipher,s))

if(text==decrypt(cipher,s)):
    print(" ............... this works .........")