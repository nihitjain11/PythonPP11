#sum of sequences
print "part (a)"

a = 2.0
b = 9.0
c = a/b
d = -((a+3)/(b+4))
n = int(raw_input("enter final limit: "))
m = 0
for i in range(n):
	z = c + d
	m += z
	a += 3
	b += 4
print m,'\n \n \n'


print "part (b)"

a = 1
z = 0
n = int(raw_input("enter last term: "))
while a != n+2 :
	z += a**2
	a += 2
print z
