# finding the greatest no among the entries by userw
def great():
        print "enter the number to find the greatest no. When finished entering enter 0 to get the result"
        g = n = ''
        count = 1
        while n != 0:
                n = float(raw_input("Enter no: "))
                if count != 0:
                        g = n
                        count  = 0
                if n > g:
                        g = n
        print 'the greatest no entered is '+ str(g)

great()
