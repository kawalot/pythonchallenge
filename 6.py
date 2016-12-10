#!/usr/bin/env python

import re

parse = b"There maybe misleading numbers in the text. One example is 82683. Look only for the next nothing and the next nothing is 63579"
ttt = re.findall(r"(\d+$)",parse)
print (ttt)