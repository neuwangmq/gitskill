a = [1,2,56,23,45,18,16,22]
print sorted(a)
def f(x,y):
	if x>y:
		return -1
	elif x<y:
		return 1
	else:
		return 0
print sorted(a,f)
def converse_sort(c,f):
	return sorted(c,f)
print converse_sort(a,f)

