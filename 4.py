#!/usr/bin/env python

import re

def ocr(string):
    i = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    e = "CDEFGHIJKLMNOPQRSTUVWXYZABcdefghijklmnopqrstuvwxyzab"
    t = str.maketrans(i, e)
    return string.translate(t)

f = open('text4.txt')
str = f.read()  
stringResult = re.findall(r"[a-z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][a-z]", str)
for char in stringResult:
    print (char, end='')
# translateString = ''.join(stringResult)
# print ()
# print ()
# print(ocr(translateString))