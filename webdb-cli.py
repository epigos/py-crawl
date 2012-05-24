import sys
sys.path.append(".")
from store import webinfo
webinfo = webinfo.ds()
def main(argv=sys.argv):
	global webinfo
	if argv[1] == "list":
		print list
		print webinfo.getallsite("http://*")
	elif argv[1] == "stat":
		print webinfo.getdbstat()
	else:
		print "available options : cli list/show-link/stat"



if __name__ == "__main__":
	main()
