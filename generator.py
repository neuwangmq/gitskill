L = [x*x for x in range(10)]
print L
#generator save the algorithm to calculate the next element
g = (x*x for x in range(10))
for n in g:
	print n