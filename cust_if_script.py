#!/usr/bin/env python3

message = 'welcome to rob\'s noob project'
print(message)

user_input = input("what did you get on the last project?")

print("you said you got " + user_input)

grade = int(user_input)


if grade >= 90:
    message =  'you got an A, bro'
elif grade >= 80:
    message = 'you got a B'
elif grade >= 70:
    message = 'you got a c'
elif grade >= 60:
    message = 'you got a D'
else:
    message = 'you failed'

print(message)

