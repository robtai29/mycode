import os
import time
import json
from dahuffman import HuffmanCodec

def quitMessage():
    print("This message will self-destruct in 10 seconds")
    for i in range(10):
        print(i)
        time.sleep(1)
    print("Mission Impossible")

def displayMenu():
    print("Welcome to Mission Impossible, Ethan Hunt")
    print("Enter 1 to censor a file")
    print("Enter 2 to encrypt a file")
    print("Enter 3 to decrpt a file")
    print("Enter 4 to exit")



def replaceWords():
    path = input("please name of the text")
    isFile = os.path.isfile(path)
    print(isFile)



    wordSet = set()
    loop = True
    while loop:
        word = input("Please enter the word: ")
        wordSet.add(word);
        choice = input("Do you want to add another word? y/n")
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



    with open("censored.txt", "w") as doc1:
        doc1.writelines(data)
    

    print(replaceMap)
    with open('json.txt', 'w') as json_file:
        json.dump(replaceMap, json_file)

def huffmanEncode():
    path = input("Please Enter the File to be encrypted: ")
    isFile = os.path.isfile(path)
    print(isFile)
    
    with open(path, 'r') as file:
        data = []
        for line in file:
            codec = HuffmanCodec.from_data(line)
            line = codec.encode(line)
            data.append(line)

    with open(path + "-encrypted", "wb") as doc1:
        doc1.writelines(data)

    
def huffmanDecode():
    path = input("Please Enter the file to decrypted: ")
    isFile = os.path.isfile(path)
    print(isfile)

    with open(path, 'r') as file:
        data = []
        

  #  if isFile:
      #  os.remove(path)

    #line in file:
     #       for word in wordSet:
      #          replacement = "".ljust(len(word), "*")
       #         line = line.replace(word, replacement)
        #    file.write(line)


   # print(wordSet)
    

huffmanEncode()
#replaceWords()
#quitMessage()

