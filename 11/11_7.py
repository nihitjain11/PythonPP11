#print n odd nums in decending orders
n = int(raw_input("enter final limit: "))
for i in range(n,0,-1):
    if (i%2)==1:
        print i
