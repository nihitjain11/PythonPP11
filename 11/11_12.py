# complete prog_
def hello():
	x = int(raw_input("Enter X: ")) #part 1
	n = len(str(x))    #part 2
	y = (n*10)+int(str(x)[0])   #part 3
	print y    #part 4

hello()