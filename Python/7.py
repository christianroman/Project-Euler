def isPrime(n):
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			return False
	return True

n,i = 1,0
while i < 10001:
	n+=1
	if isPrime(n):
		i+=1
print n
