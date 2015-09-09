# -*- coding: utf-8 -*-
a = range(3,1000)
temp = 2
base = 2
result = [1]
while a:
    while temp <1000:
        if temp in a:
            a.remove(temp)
        temp = temp + base #删除base的倍数
    result.append(base)
    base = a[0]
    temp = base
    del a[0]
    #result.append(base)
print result
        
        
    
