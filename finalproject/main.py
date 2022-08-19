#!/usr/bin/env python3
"""Rob Tai. 8.19.22. This program performs censoring, encryption and decryption"""
import os
import time
import json
from dahuffman import HuffmanCodec
from collections import Counter


def main():
    """This runs the entire program"""
    display_menu()
    user_input = input("Enter a number between 1 and 4:  ")
    while not input_validation(user_input):
        user_input = input("Incorrect choice. Enter a number between 1 and 4:  ")

    user_input = int(user_input)
    if user_input == 1:
        replace_words()
    elif user_input == 2:
        huffman_encode()
    elif user_input == 3:
        huffman_decode()
    else:
        quit_message()


def quit_message():
    """Display the message when the user decides to leave"""
    print("This file will self-destruct in 5 seconds")
    for i in range(5):
        print(i)
        time.sleep(0.5)
    print("Mission Impossible")


def display_menu():
    """Displays the menu choices"""
    print("Welcome to Mission Impossible, Ethan Hunt")
    print("Enter 1 to censor a file")
    print("Enter 2 to encrypt a file")
    print("Enter 3 to decrypt a file")
    print("Enter 4 to exit")


def input_validation(choice):
    """Performs input validation"""
    my_set = {1, 2, 3, 4}
    if len(choice) == 0:
        return False
    if not choice.strip().isdigit():
        return False
    return int(choice) in my_set


def check_file(path):
    """Check to see the file path exists"""
    return os.path.isfile(path)


def replace_words():
    """Replaces selected strings with strings made up of *"""
    path = input("please name of the text: ")
    while not check_file(path):
        path = input("File not found. Please enter name of the text: ")

    word_set = set()
    loop = True
    while loop:
        word = input("Please enter the word: ")
        if len(word) == 0:
            continue
        word_set.add(word);
        choice = input("Do you want to add another word? Use n to quit. Any other key to continue: ")
        if choice == 'n':
            loop = False

    index = 0
    with open(path, 'r') as file:
        data = []
        for line in file:
            for word in word_set:
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


def huffman_encode():
    """Performing encoding of the file"""
    path = input("Please Enter the File to be encrypted: ")
    while not check_file(path):
        path = input("File not found. Please enter name of the file: ")

    with open(path, 'r') as whole_file:
        entire_text = whole_file.read()
        freq_dict = Counter(entire_text)

    codec = HuffmanCodec.from_frequencies(freq_dict)
    encode = codec.encode(entire_text)

    with open(path + "-encrypted", "wb") as doc1:
        doc1.write(encode)

    with open("huffman.json", 'w') as jsonfile:
        json.dump(freq_dict, jsonfile)

    print("Processing your request...")
    time.sleep(1.5)
    print("Your file is ready.")


def huffman_decode():
    """Perform decoding of the file"""
    path = input("Please Enter the file to decrypted: ")
    while not check_file(path):
        path = input("File not found. Please enter name of the file: ")

    if not check_file("huffman.json") or path.find("encrypted") == -1:
        print("Need a proper encrypted file first!")
        quit()

    with open("huffman.json", 'r') as jsonfile:
        word_dict = json.load(jsonfile)

    codec = HuffmanCodec.from_frequencies(word_dict)
    with open(path, 'rb') as file:
        data = []
        for line in file:
            line = codec.decode(line)
            data.append(line)
    size = len(path)
    new_path = path[:size - 10]
    with open(new_path + "-decrypted", "w") as doc:
        doc.writelines(data)

    print("Processing your request...")
    time.sleep(1.5)
    print("Decryption is completed.")


# print(wordSet)
if __name__ == "__main__":
    main()
