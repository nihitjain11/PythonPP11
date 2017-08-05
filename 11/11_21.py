# ascending order

a = int(raw_input("A: "))
b = int(raw_input("B: "))
c = int(raw_input("C: "))

mx=md=mn=0

if a<=b and a<=c:
	if b<=c:
		mn,md,mx=a,b,c
	else :
		mn,md,mx=a,c,b

if b<=a and b<=c:
	if a<=c:
		mn,md,mx=b,a,c
	else :
		mn,md,mx=b,c,a
		
if c<=b and c<=c:
	if a<=b:
		mn,md,mx=c,a,b
	else :
		mn,md,mx=c,b,a
		
print "Smallest number = %s \nNext higher number = %s \nHighest number = %s"%(mn,md,mx)
