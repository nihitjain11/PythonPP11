# to compute simple interest and compound interest
p = float(raw_input("Enter the principal amount"))
r = float(raw_input("Enter the rate of interest"))
t = float(raw_input("Enter the time period as per the rate of int."))
si = p*r*t/100
ci = p(((100+r)/100)**t) - p
print "Simple Interest is ",si
print "Compound Interest is ",ci