#finding avg of lsit of number entered
def average():
	print "Keep entering the nos for finding the average of them \n when finished entering all the nos enter '0' to get the result."
	n = 0
	no = 1
	count = -1
	while no != 000:
		no = float(raw_input("enter a no:"))
		n += no
		count += 1
	print "the average is ", n/count

average()