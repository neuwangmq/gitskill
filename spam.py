#coding:utf-8
# file : spam.py
a = 37                    # 一个变量
def foo():                # 一个函数
    print "I'm foo"
class bar:                # 一个类
    aa = 123
    def grok(self):
        print "I'm bar.grok"

if __name__ == '__main__':
	main()
	print 'hello hahaha'
	b = bar()                 # 创建一个实例
	print b.aa
	b.grok()