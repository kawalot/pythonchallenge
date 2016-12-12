#!/usr/bin/env python
import re

f = open('text4.txt')
string = f.read()  
stringResult = re.findall(r"[a-z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][a-z]", string)
for char in stringResult:
    print (char, end='')