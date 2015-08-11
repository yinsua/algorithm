#/usr/bin/python
#coding:utf-8

#插入排序
#2015-08-11

import os
import sys
import time

def insertionSort(List):
	for loop in range(len(List)):		
		after = List[loop]
		front = loop-1
		while front >= 0 and List[front] > after:
			List[front+1] = List[front]
			front = front-1
		List[front+1] = after
		#print x

x = [32,465,46,41,30,8,98,564]
print "raw :\t" + `x`
insertionSort(x)
print "after :\t" + `x`	