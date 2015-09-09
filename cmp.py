def my_cmp(x,y):
	if not (isinstance(x,(int ,float)) and isinstance(y,(int ,float))):
		print "wrong"
		raise TypeError("bad operand TypeError")
	if x>y:
		return 1
	elif x<y:
		return -1
	else:
		return 0
a = my_cmp(3,'a')
print a
