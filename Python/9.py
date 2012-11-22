r = 1000

for a in xrange(1,r):
	for b in xrange(a+1,r):
			c = r - a -b
			if a+b+c == r and a*a+b*b == c*c:
				print a*b*c
				exit()
