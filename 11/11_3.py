# close enough?? or not
a = float(raw_input("Enter a no.: "))
b = float(raw_input("Enter a no.: "))
if a-0.001 == b:
	print "Close "
elif b-0.001 == a:
	print "Close"
else :
	print "Not close "