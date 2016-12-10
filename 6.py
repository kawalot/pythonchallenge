#!/usr/bin/env python

import pickle

with open('banner.p','rb') as f:
	data_new = pickle.load(f)
#print(data_new)
for data in data_new:
	print("".join([entry[0]*entry[1] for entry in data]))