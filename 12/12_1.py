#phone number validity check
n = raw_input("enter the phone number: ")
v = "phone number is valid"
e = "phone number is not valid"
t = True
for i in n:
	if i not in "0123456789-":
		t = False
		break
if (((n[3] and n[7]) =="-") and (len(n) ==12)) and (t == True):
        print v
else:
        print e
