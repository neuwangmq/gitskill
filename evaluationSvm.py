__author__ = 'IAP-wmq'
import codecs

count = 0
with open("E:/testlibsvm.txt", 'r') as f:
    with open("E:/result.txt", 'r') as result:
        for l in f.readlines():
            r=result.readline()
            print(float(l.split(" ")[0]), float(r))
            if abs(float(l.split(" ")[0])-float(r)) < 0.00001:
                print("dadad")
                count=count+1
print(count/3822)
