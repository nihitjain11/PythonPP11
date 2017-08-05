#time after those many hours

a = int(raw_input("Enter hours between 1-12:"))
b = int(raw_input("How many hours ahead: "))
t_hr = a+b
if t_hr > 12:
	print "final time will be : ",t_hr % 12,"0' clock"
else : 
	print "final time will be : ", t_hr,"0' clock"
