#!/bin/bash

addUser(){
echo "tell me the name"
read USER
echo "password"
read PASS

echo "Tell me the group"
read GROUP


useradd -p $PASS $USER

usermod -aG $GROUP $USER

tail -n 1 /etc/passwd
tail -n 1 /etc/shadow


}

    addUser
    






