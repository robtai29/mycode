import os
import time

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
    
    
    with open(path, 'r') as file:
        data = []
        for line in file:
            for word in wordSet:
                replacement = "".ljust(len(word), "*")
                line = line.replace(word, replacement)
            data.append(line)



    with open("censored.txt", "w") as doc1:
        doc1.writelines(data)
    
    if isFile:
        os.remove(path)

    #line in file:
     #       for word in wordSet:
      #          replacement = "".ljust(len(word), "*")
       #         line = line.replace(word, replacement)
        #    file.write(line)


   # print(wordSet)
    


replaceWords()
quitMessage()


