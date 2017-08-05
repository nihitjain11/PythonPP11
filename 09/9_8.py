def last():
	a = raw_input("Enter a: ")
	b = raw_input("Enter b: ")
	c = len(a)
	d = len(b)
	e = a[c-1]
	f = b[d-1]
	if int(e)>int(f):
		print a
	else:
		print b