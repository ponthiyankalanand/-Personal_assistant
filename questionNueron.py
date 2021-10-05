 
#function for findind
def questionAns():	  
	lst =[]
	res = [] 
	reslst = []
	freslst=[] 
	treshold = 20
	file = open('questionDatabase.txt', 'r') 
	for lines in file: 
		var1 = lines
		words = var1.split()
		seen = set()
		dups = set()
		for word in words:
			if word in seen:
				if word not in dups:
					#print(word)
					dups.add(word)
					
			else:
				seen.add(word)
				lst.append(word)
	#removing repeated words
	for i in lst: 
		if i not in res: 
			res.append(i) 
	#finding repeated words
	for j in lst:
		if j in res:
			reslst.append(j)
	#comparing with treshold and find most occured words
	for k in res:
		count=0
		for l in reslst:
			if (k == l):
				count = count+1
				#print(k,l,count)

		if (count >= treshold):
			freslst.append(k)
	return(freslst)
	#print(freslst)
def findAnswer(var):
	comlist = questionAns()
	var1 = var.split()
	count = 0
	for word in var1 :
		if word in comlist:
			print(word)
			count = count+1			 
	if (count >= 2):  
		print("is question")


			 	 
		

#main 
 
