# how many items kharide??

n = raw_input("Enter the no. of items bought : ")
if len(n) == 1:
	price = int(n) * 120
elif len(n) == 2:
	price = int(n) * 100
elif len(n) == 3:
	price = int(n) * 70
print "total price = ",price