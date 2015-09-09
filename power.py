def power(a,n=2):
	multi = 1
	if n==2:
		return a*a
	else:
		while n>0:
			multi = multi *a
			n = n-1
			print multi
		return multi
t = power(3,3)
print t