#!/usr/bin/env python

import urllib.request
import re

nothing = "12345"
while nothing:
	url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing
	f = urllib.request.urlopen(url)
	string = f.read()
	print(string.decode("utf-8"))
	if "Divide" in string.decode("utf-8"):
		nothing = str(int(nothing) / 2)
	else:
		nothing = "".join(re.findall(r"(\d+$)",string.decode("utf-8")))