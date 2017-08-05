import math
print "Q1"
x = int(raw_input("enter x: "))
if x > 0:
    if 10**math.log(x) == x :
        print "True"
    else:
        print "e"
        print 10**math.log(x)
else:
    print "error"

print
print
print "Q2"

a = math.sqrt(3**2+4**2)
b = 5
if a == b :
    print True
