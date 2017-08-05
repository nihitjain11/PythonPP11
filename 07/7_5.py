# printing seconds into minutes and seconds
s = int(raw_input("Enter seconds : "))
mi = s//60
sec = s%60
print "%s seconds equals %s minutes and %s seconds."%(s, mi, sec)
