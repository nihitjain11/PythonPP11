# finding if sqrt of a num is prime!

from math import *

def sqrt_prime(n):
	i = sqrt(n)
	for j in range(2,int(i)):
		if i%j != 0:
			print "square root is ",int(i),"which is prime"
			break
		else:
			print "not prime"

n = int(raw_input("enter no to find if its square root is prime : "))
sqrt_prime(n)