class Student(object):
	"""docstring for Student"""
	def __init__(self, name,age,score):
		super(Student, self).__init__()
		self._name = name# private
		self._age = age
		self._score = score
	def print_score(self):
		print ('%s:%s' %(self._name,self._score))
	def print_student(self):
		print ('%s:%s,%s!!!' % (self._name,self._age,self._score))
wang = Student('wang',25,100)
hu = Student('hu',25,99)
#print hu.score
hu.print_score()
wang.print_score()
hu.print_student()
wang.print_student()
		