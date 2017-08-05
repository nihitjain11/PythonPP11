l=map(int,raw_input("Enter a list:(no. b/w 1-12)\n"))
for i in xrange(len(l)):
	if l[i]>10:
		l[i]=10
print l