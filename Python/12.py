d = 0
i = 3
s = 0

for n in xrange(1,1000):
	s+=n

	tmp = s
	i = 3
	print s

	while tmp > 1:
		if tmp%i == 0:
			tmp/=i
		else:
			i+=2
		print "hola"
