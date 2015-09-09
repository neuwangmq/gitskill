#-*-coding : UTF-8-*-
import getopt
import sys
def usage():
	print sys.argv[0]+' -i inputname'+'-o outname'
	print sys.argv[0]+' -h #get help info'
if __name__ == '__main__':
	
	try:
		opts,args = getopt.getopt(sys.argv[1:],'hi:o:',["help","input=","output="])
	except Exception, e:
		usage()
		raise e
	for name,value in opts:
		if name in ("-h","help"):
			usage()
		if name in ("-i","--input"):
			print "inputname is :",value
		if name in ("-o","--output"):
			print "outputname is :",value
