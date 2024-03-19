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
 


text = input("Enter a text to check : ")
s = 3
cipher = encrypt(text, s)
print ("Text  : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + cipher)
print ("Decrypted Text: " + encrypt(cipher,s=26-s))

if(text==encrypt(cipher,s=26-s)):
    print(" ............... this works .........")