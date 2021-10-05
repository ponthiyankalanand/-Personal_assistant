# traing module

def train():
	while(True):
		x = input("something:")
		print ("updatig !")
		fo = open("userdb.txt", "a")
		fo.write("\n")
		fo.write(x)
		print("updated")
		fo.close()
		y=input("Do u want to continue the trainig y/n")
		if (y=='n'):
			break


