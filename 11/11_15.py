# sum of sequence with factorial nos.
def fact(n):
	z = 1.0
	for i in range(1,n+1):
		z *= i
	return z

p = 1
m = int(raw_input("enter no of terms: "))
for i in range(1,m):
	p += 1/fact(i)
print p