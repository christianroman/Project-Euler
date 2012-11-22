top = 100
a = b = 0

for x in range (1,top+1):
	a += x*x
	b += x

print b*b - a
