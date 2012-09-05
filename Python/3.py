def isPrime(n):
	for x in xrange(2, int(n**0.5)+1):
		if n % x == 0:
			return False
		return True

x = 2

while x != 147:
	if 147 % x == 0:
		if isPrime( 147 / x):
			print x
			x = 147 / x
	else:
		x = x + 1

#print isPrime(10)
