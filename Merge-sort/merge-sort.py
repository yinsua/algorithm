#/usr/bin/python
#coding:utf-8

#归并排序
#2015-08-12

def MERGE(A,p,q,r):
	n1 = q-p+1
	n2 = r-q
	L = [x for x in range(n1)]
	R = [x for x in range(n2)]
	for x in range(len(L)):
		L[x] = A[p + x -1]
	for x in range(len(R)):
		R[x] = A[q + x]
	L.append('\n')
	R.append('\n')
	i=0
	j=0
	for k in range(p-1,r):
		if L[i] <= R[j]:
			A[k] = L[i]
			i = i+1
		else:
			A[k] = R[j]
			j = j+1
			
a=[22,12,8,10,19,44,65,3,56,66,87,99]
print "raw :\t" + `a`
MERGE(a,3,7,12)
print "after :\t" + `a`
				
	