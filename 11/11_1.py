# cm to inch

cm = float(raw_input("enter length in cm: "))
while cm < 0 :
	cm = float(raw_input("please enter length in cm: "))
inch = cm/2.54 
print "%s centimeters = %s inches" % ( inch , cm )