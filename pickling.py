#_*_codeing = utf-8_*_
try:
	import cPickle as pickle
except ImportError, e:
	import error
	#raise e

d = dict(name = 'bob',age = 30,score = 99)
print d.items()
pickle.dumps(d)
f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()
d['name'] = 'tom'
print d.items()
for (k,v) in d.items():
	print 'd[%s]=' % k,v
f = open('dump.txt','rb')
t = pickle.load(f)
print t