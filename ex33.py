# ex33

def f(num, stepsize):
	x = 0
	numbers = []

	for i in range(0, num):
		print "At the top x is %d" % x
		numbers.append(x)
	
		x += stepsize
		
		print "Numbers now:" , numbers
		print "At the bottom x is %d" % x

	print "The numbers:"

	for num in numbers:
		print num