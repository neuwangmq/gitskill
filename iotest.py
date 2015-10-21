# -*- coding: utf-8 -*-
import codecs
with open('e:/py/spam.py', 'r',encoding='GBK') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
s = "print 'hello_w '"
print(s)
with open('e:/py/hello_w.py', 'w') as f:
    f.write(s)
with open('e:/py/hello_w.py', 'r',encoding='GBK') as f:
    print(f.read())

