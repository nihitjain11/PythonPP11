#usr ,word count ch count % aplha-num
i = raw_input("enter some sentence(s) followed by \"enter\": ")
print i
w = len(i.split())
an = 0
for j in i:
	if j in "abcdefghijklmnopqrstuvwxyz1234567890":
		an += 1
print "total no of words:",w
print "total no of characters:",len(i)-5
print "percentage of aplha-numeric characters:",(an*100.0)/len(i),"%"
