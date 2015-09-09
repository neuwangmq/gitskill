#-*-coding:UTF-8-*-
import stu_my
import os
import sys
import re
import string
global FILEPATH
FILEPATH = "E:/py/test.txt"

def init():
	if os.path.exists(FILEPATH):
		print "load data success!!!"
	else:
		try:
			f = open(FILEPATH,"a")
		except Exception, e:
			print "can not open file "
			sys.exit()
			#raise e
		finally:
			f.close

def queryALL():
	f = open(FILEPATH,"r")
	i = 0
	for eachline in f :
		i = i + 1
		#if cmp(eachline.strip("\n"),"d\n")==0:
		#	print "match"
		#else:
		#	print "not match"
		#print eachline.strip("\n")
	f.close()
	if i == 0:
		print "no data"
	print "hahahhaha"
	print "dadfaf"

	f = open(FILEPATH,"rb")
	u = f.read().decode('utf-8')
	print u

def addStudent():
	stu = stu_my.student()
	while(True):
		stuID = raw_input("please input student id (001-999):")
		p = re.match("^[0-9]{3}$",stuID)
		if p:
			stu.setID(stuID)
			break
		else:
			print "wrong id， please re-input"

	while(True):
		stuName = raw_input("please input student name  :")
		p = re.match("^[a-zA-Z]{1,15}$",stuName)
		if p:
			stu.setName(stuName)
			break
		else:
			print "wrong name， please re-input"

	while(True):
		stuScore = raw_input("please input student score  :")
		p = re.match("^[0-9]{2}$",stuScore)
		if p:
			stu.setScore(stuScore)
			break
		else:
			print "wrong score， please re-input"
	#print stu.getID()+"\t"+"256ds56f"+stu.getName()+"\t"+stu.getScore()+"\n"
	#save to file
	f = open(FILEPATH,"a")
	f.write(stu.getID()+"\t"+stu.getName()+"\t"+stu.getScore()+"\n")
	f.close()
	print "add student success"
if __name__ == '__main__':
	init()
	queryALL()
#	addStudent()
	#queryALL()
	#main()