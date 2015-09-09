# map 
#dict
from collections import OrderedDict
a = {"a":1,"b":2,"c":3,"d":4}
print a["c"]
print "a" in a
print "f" in a
print a.get("a")
print a.get("a",1)
a.pop("a")
print a

d = dict([('a',1),('b',2),('c',3)])
print d
#OrderedDict
d = OrderedDict([('a',1),('b',2),('c',3)])
print d