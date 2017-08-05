#designer printing

s1 = raw_input("enter string1: ")
s2 = raw_input("enter string2: ")

def swing(a):
	l = len(a)
	i = l/2
	c = 0
	if len(a)%2==1:
		i = (l/2) +1
		l -= 1
	for j in range(i):
		if (j != -(l-j-1)-1):
			print "   "*c+a[j]+"   "*l+a[len(a)-j-1]
		else :
			print "   "*c+a[j]
		l -= 2
		c += 1
if len(s1)>len(s2):
	print s1
	swing(s2)
else :
	print s2
	swing(s1)
