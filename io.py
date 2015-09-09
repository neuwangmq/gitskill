# -*- coding: utf-8 -*-
import codecs
with open('e:/py/spam.py','r') as f:
	print f.readline()
	print f.readline()
	print f.readline()
	print f.readline()
s="print 'hello_w 昨天和阿姿看了个电影'"
print s
with open('e:/py/hello_w.py','w') as f:
	f.write(s)
with open('e:/py/hello_w.py','r') as f:
	print f.read()

