from itertools import groupby
import numpy as np
def speechExtraction(alphabet):
	data = alphabet.split() #split string into a list
	a=[]
	i=0
	a.append(0)
	#finding matching line
	def finder():
	    for temp in data:
	        
	        with open('userdb.txt','r') as myFile:
	            for num, line in enumerate(myFile, 0):
	                if temp in line:
	                   a.append(num)
	    print (a)
#finding perfect line
	def findline():
	   counts = np.bincount(a)
	   value = np.argmax(counts)
	   f=open('userdb.txt')
	   lines=f.readlines()
	   ans = lines[value]
	   return(ans)
	finder()
	fans = findline()
	return(fans)

 
 
