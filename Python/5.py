top,n = 20,0
ends = False

while not ends:
	n+=top
	for x in xrange(11,top+1):
		if n % x:
			break
		ends = True if x == top else False
print n
