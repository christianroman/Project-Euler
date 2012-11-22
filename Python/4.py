def isP(n):
	return str(n) == str(n)[::-1]

n = 999
p = 0

for i in xrange(n,100,-1):
	for j in xrange(n,100,-1):
		if j > i:
			continue
		if isP(i*j) and i*j > p:
			p = i*j

print p
