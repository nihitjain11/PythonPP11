# dollar to rupees conversion
def dollar_rupees():
	d = float(raw_input("Enter the amount-in-dollar: "))
	rate_d = float(raw_input("Enter the rate-of-dollar ,i.e., $ 1 = Rs. "))
	r = d * rate_d
	print "$ %s = Rs. %s" % (d, r)
