from sys import path
path.append("spam.py")
import spam
print spam.a
spam.foo()
c = spam.bar()
print c.aa
c.grok()
print "heee"
