import os
import time
import json
from dahuffman import HuffmanCodec
from collections import Counter

def main():
    displayMenu()
    userInput = input("Enter a number between 1 and 4:  ")
    while inputValidation(userInput)== False:
        userInput = input("Incorrect choice. Enter a number between 1 and 4:  ")
   
    userInput = int(userInput)
    if userInput == 1:
        replaceWords()
    elif userInput == 2:
        huffmanEncode()
    elif userInput == 3:
        huffmanDecode()
    else:
        quitMessage()

def quitMessage():
    print("This file will self-destruct in 5 seconds")
    for i in range(5):
        print(i)
        time.sleep(0.5)
    print("Mission Impossible")

def displayMenu():
    print("Welcome to Mission Impossible, Ethan Hunt")
    print("Enter 1 to censor a file")
    print("Enter 2 to encrypt a file")
    print("Enter 3 to decrypt a file")
    print("Enter 4 to exit")

def inputValidation(choice):
    myset = {1, 2, 3, 4}
    if len(choice) == 0:
        return False
    if choice.strip().isdigit() == False: 
        return False
    return int(choice) in myset    

def checkFile(path):
    return os.path.isfile(path)

def replaceWords():
    path = input("please name of the text: ")
    while checkFile(path) == False:
        path = input("File not found. Please enter name of the text: ")


    wordSet = set()
    loop = True
    while loop:
        word = input("Please enter the word: ")
        if len(word) == 0:
            continue
        wordSet.add(word);
        choice = input("Do you want to add another word? Use n to quit. Any other key to continue: ")
        if choice == 'n':
            loop = False
    
    
    index = 0
    with open(path, 'r') as file:
        data = []
        for line in file:
            for word in wordSet:
                replacement = "".ljust(len(word), "*")
                line = line.replace(word, replacement)
            data.append(line)



    with open(path + "-censored", "w") as doc1:
        doc1.writelines(data)
    os.remove(path)    
    print("Processing your request...")
    time.sleep(1)
    print("Original document is removed.")
    time.sleep(1)
    print("Your file is ready.")
    
def huffmanEncode():
    path = input("Please Enter the File to be encrypted: ")
    while checkFile(path) == False:
        path = input("File not found. Please enter name of the file: ")
    
    
    with open(path, 'r') as wholefile:
        entireText = wholefile.read()
        freqDict = Counter(entireText)
            
    codec = HuffmanCodec.from_frequencies(freqDict)
    encode = codec.encode(entireText)
    

    with open(path + "-encrypted", "wb") as doc1:
        doc1.write(encode)
        
    with open("huffman.json", 'w') as jsonfile:
        json.dump(freqDict, jsonfile)

    print("Processing your request...")
    time.sleep(1.5)
    print("Your file is ready.")

def huffmanDecode():
    path = input("Please Enter the file to decrypted: ")
    while checkFile(path) == False:
        path = input("File not found. Please enter name of the file: ")

    if checkFile("huffman.json") == False or path.find("encrypted") == -1:
        print("Need a proper encrypted file first!")
        quit()
    
    with open("huffman.json", 'r') as jsonfile:
        wordDict = json.load(jsonfile)
    

    codec = HuffmanCodec.from_frequencies(wordDict) 
    with open(path, 'rb') as file:
        data = []
        for line in file:
            line = codec.decode(line)
            data.append(line)
    size = len(path)
    newPath = path[:size-10]
    with open(newPath + "-decrypted", "w") as doc:
        doc.writelines(data)

    print("Processing your request...")
    time.sleep(1.5)
    print("Decryption is completed.")

  #  if isFile:
      #  os.remove(path)

    #line in file:
     #       for word in wordSet:
      #          replacement = "".ljust(len(word), "*")
       #         line = line.replace(word, replacement)
        #    file.write(line)


   # print(wordSet)
main()
