#pattern printing

#part 1

print "part(a) \n"

max_star=int(raw_input("max: "))
a = max_star-1
i = 1
while (a!=0) and (i!=max_star+1):
	print " "*a,"* "*i
	a-=1
	i+=1
while (a!=max_star) and (i!=0):
	print " "*a,"* "*i
	a+=1
	i-=1



#part 2

print "part(b)\n"

max_star = int(raw_input("max: "))
c = 1
while c != max_star+1:
	print "* "*c
	c += 1
c-=2
while c != 0:
        print "* "*c
        c -= 1




#part 3

print "part(c)\n"

max_star = int(raw_input("max: "))
a = max_star-1
i = 1
print " "*max_star+"*"
while (a>=0) and (i<=(max_star*2)-2):
	print " "*a+"*"+" "*(i)+"*"
	a-=1
	i+=2
a+=2
i-=4
while (a<max_star) and (i>0):
	print " "*a+"*"+" "*(i)+"*"
	a+=1
	i-=2
print " "*max_star+"*"


#part 4

print "part(d)\n"
max_star = int(raw_input("max: "))
a = max_star-1
i = 1
print "*"
while (i<=(max_star*2)-2):
	print "*"+" "*(i)+"*"
	i+=2
i-=4
while (a<max_star) and (i>0):
	print "*"+" "*(i)+"*"
	i-=2
print "*"
