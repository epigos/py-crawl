import httputil
from store import webinfo
import sys
webinfo = webinfo.ds()
httputil = httputil.util()

def main(argv=sys.argv):
	sites = webinfo.getuncrawled()
	for i in sites:
		links = webinfo.getweblinks(i)
		for j in links:
			crawl(j)
        	webinfo.markcrawled(i)
def crawl(url):
        global webinfo,startcount,httputil
	if webinfo.siteexists(url) == False:
        	metainfo = httputil.getmeta(url)
        	links = httputil.getlinks(url)
        	print "meta data size :"+str(len(metainfo))+" links size : "+str(len(links))
        	webinfo.savemetainfo(url, metainfo)
        	webinfo.saveweblinks(url, links)
if __name__ == "__main__":
	sys.exit(main())

