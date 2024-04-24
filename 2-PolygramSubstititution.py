def encryption(text, blocksize, forwardDict):
    result = ""
    cnt = 1
    block = ""
    for char in text:
        block += char
        cnt+=1
        if cnt>blocksize :
            cnt = 1
            result += forwardDict[block]
            block = ""
    if block!="":
        result+=forwardDict[block]
    return result

def decryption(text, blocksize, backwordDict):
    result = ""
    cnt = 1
    block = ""
    for char in text:
        block += char
        cnt+=1
        if cnt>blocksize :
            cnt = 1
            result += backwordDict[block]
            block = ""
    if block!="":
        result+=backwordDict[block]
    return result


# reading file
forwardDict = {}
backwordDict = {}
file = open("keyMap.txt", "r")
lines = file.readlines()
for line in lines:
    t, c = line.split()
    forwardDict[t] = c
    backwordDict[c] = t

text = "ABCSDKTYR123XZ"
cipher = encryption(text, 3, forwardDict)
decryptedText = decryption(cipher, 3, backwordDict)
print("Original Text : ", text)
print("Cipher : ",cipher)
print("Decrypted text : ", decryptedText)
