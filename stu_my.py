#-*-coding:UTF-8-*-

class student():
	"""docstring for student"""
	stuID = ""
	stuName = ""
	stuScore = ""

	def setID(self,stuID):
		self.stuID = stuID 
	def setName(self,stuName):
		self.stuName = stuName
	def setScore(self,stuScore):
		self.stuScore = stuScore
	def getID(self):
		return self.stuID
	def getName(self):
		return self.stuName
	def getScore(self):
		return self.stuScore


if __name__ == '__main__':
	test()