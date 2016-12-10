#!/usr/bin/env python

myDict = {}
f = open('text3.txt')
for char in f.read():
    if char in myDict:
        i = myDict.get(char)
        myDict[char] = i + 1
    else:
        myDict[char] = 1
for k, v in myDict.items():
    if v < 2:
        print(k, v)
