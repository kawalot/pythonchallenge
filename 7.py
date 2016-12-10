#!/usr/bin/env python

import zipfile
import re

start = "90052.txt"
collect = []
z = zipfile.ZipFile("channel.zip", "a")
print(z.read(start))
while True:
    try:
        start = re.search(b"(\d+)", z.read(start)).group(0).decode("utf-8") + ".txt"
        collect.append((z.getinfo(start).comment).decode("utf-8"))
    except:
        print(z.read(start))
        break
print("".join(collect))