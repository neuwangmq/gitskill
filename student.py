class Student:
	stuID = ""
	name = ""
	sex = "M"
	classID = "NULL"
	
	#set ID 
	def setStuID(self,stuID):
		self.stuID = stuID
	
	def setName(self,name):
		self.name = name
	
	def setSex(self,sex):
		self.sex = sex
		
	def setClassID(self,classID):
		self.classID = classID
	
	def getStuId(self):
		return self.stuID
	
	def getName(self):
		return self.name
	
	def getSex(self):
		return self.sex
	
	def getClassID(self):
		return self.classID