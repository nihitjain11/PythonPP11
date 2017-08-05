#string, digits and sum
s = raw_input("enter a string: ")
digits = ""
d_sum = 0
for i in s:
	if i in "0123456789":
		digits += i
		d_sum += int(i)
if digits == "":
	print s+"has no digits"
else :
	print s+" has the digits "+digits+" which sum to ",d_sum
