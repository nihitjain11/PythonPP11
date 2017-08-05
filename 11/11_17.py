#sum of series

print "part 1 \n"
def fact(n):
	k = 1
	for i in range(1,n+1):
		k *= i
	return k

s = 0
x = float(raw_input("enter x: "))
for a in range(1,7):
	k = (x**a)/fact(a)
	if a % 2 == 0:
		s += (-k)
	else:
		s += k
print "sum of series is ", s

print "\n \n part 2 \n"

s = 0
x = float(raw_input("enter x: "))
n = int(raw_input('enter n: '))
for i in range(1,n+1):
	s += (x**i)/i
print "sum of series is ", s