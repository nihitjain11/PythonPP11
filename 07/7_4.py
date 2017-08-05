# computing [mod(a-b) / a+b]
import math
a = int(raw_input("Enter a: "))
b = int(raw_input("Enter b: "))
ans = (math.fabs(a-b))/(a+b)
print "answer is",ans