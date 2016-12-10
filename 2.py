#!/usr/bin/env python

# from string import maketrans

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# alphabetCoded = 'cdefghijklmnopqrstuvwxyzab'
# challenge = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
# trantab = maketrans(alphabet, alphabetCoded)
# print (challenge.translate(trantab))
# print('map'.translate(trantab))

a="abcdefghijklmnopqrstuvwxyzab"
b="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
c=""
for i in b:
    if i in a:
        c=c+a[a.index(i)+2]
    else:
        c=c+i
print (c)

# user_input = input("Enter a string to un-ROT2.")

# i = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# e = "CDEFGHIJKLMNOPQRSTUVWXYZABcdefghijklmnopqrstuvwxyzab"

# t = str.maketrans(i, e)

# print (user_input.translate(t))

# input("\n\nPress enter to continue.")