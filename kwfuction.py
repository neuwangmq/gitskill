def persion(name,age,**kw):
	return 'name',name,'age',age,'other',kw
print persion('wang',14,city='beijing')
print persion('wang',14,city='beijing',gender = 'F')
print persion('wang',14,city='beijing',hobby = 'football')