s = 0
f = n = 1

while f < 4000000:
	f,n = n,f+n
	s += f if (f%2==0) else 0

print s
