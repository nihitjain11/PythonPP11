# is it palindrome ? 
def palindrome():
	n = raw_input("enter the no to check if its palindrome: ")
	k = len(n)
	count = 0
	rev_count = k-1
	while count != (len(n)/2):
		if n[count] == n[rev_count] :
			print "yo"
			count += 1
			rev_count -= 1
		else:
			print "no"
			break

palindrome()

