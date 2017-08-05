# int between 1 and n divisible by m ,also r they odd or env??
n = int(raw_input("enter the final limit, n : "))
m = int(raw_input("a num to divide it, m : "))
for i in range(1,n):
	if i % m == 0:
		if i % 2 == 0:
			print i, 'is even'
		else :
			print i, 'is odd'
