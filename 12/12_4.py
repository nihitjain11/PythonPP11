while True:
	s2 = ''
	s = raw_input("enter a sentence, or 'q' to quit :")
	if s == 'q':
		break
	for i in s:
		if i.islower():
			s2 += i.upper()
		elif i.isupper():
			s2 += i.lower()
		else:
			s2 += i
	print s2
