#!/usr/bin/env python
# -*- coding: utf-8 -*-
_author_ = 'wangmingqiang'
import sys
def test():
	args = sys.argv
	print args
	if len(args) == 1:
		print 'hello world'
	else:
		print 'hello %s' %args[1]
#test()
if _name_ == '_main_':
	test()