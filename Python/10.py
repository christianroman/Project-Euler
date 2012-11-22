def isPrime(n):
	for x in xrange(2, int(n**0.5)+1):
		if n % x == 0:
			return False
	return True

s = 0

for x in xrange(2, 2000001):
	if isPrime(x):
		s+= x

print s
