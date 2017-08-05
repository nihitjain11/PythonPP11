#age group sorter
n = ''
group1 = 0
group2 = 0
group3 = 0
while n != 'tell':
	n = raw_input("enter the age of employee: ")
	if n == 'tell':
		pass
	elif int(n) >= 26 and int(n) <= 35:
		group1 += 1
	elif int(n) >= 36 and int(n) <= 45:
		group2 += 1
	elif int(n) >= 46 and int(n) <= 55:
		group3 += 1
	else :
		print 'out of range (26 - 55)'
print 'no of people in age groups are: \n 26 - 35 = %s \n 36 - 45 = %s \n 46 - 55 = %s' % (group1, group2, group3 )
