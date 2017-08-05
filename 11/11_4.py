# r u a leap year?

y = int(raw_input("enter a year: "))\
if y%4 == 0:
	print "leap year"
else :
	print "no it isn't. ", y%4 , " years to next leap year"
	