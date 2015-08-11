#/usr/bin/python
#coding:utf-8

import os
import sys
import time

def insertionSort(x):
	for y in range(len(x)):
		key = x[y]
		a = y-1
		while a >= 0 and x[a] > key:
			x[a+1] = x[a]
			a = a-1
		x[a+1] = key
		#print x

x = [32,465,46,41,30,8,98,564]
print "raw :\t" + `x`
insertionSort(x)
print "after :\t" + `x`	
