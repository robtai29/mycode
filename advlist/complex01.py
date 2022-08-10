#!/usr/bin/env python3

def main():

    list1 = ["bear", "cats", "foxes"]
    
    print(list1)
    
    print(list1[1])
    
    list2 = ["juniper"]
    
    list1.extend(list2)
    
    print(list1)
    
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]
    
    list1.append(list3)
    
    print(list1)
    
    print(list1[4])
    
    print(list1[4][0])


    list3 = ["parrot", "mouse", "cat", "panda", "dog"]
    print(list3)


main()

