from store import webinfo
import sys
winfo = webinfo.ds()

def main(argv=sys.argv):
	print "test score"
	print sys.version
	sites = winfo.getsites()
	winfo.getdbstat()
