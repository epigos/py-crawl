import urllib2
import sys
import httputil
from store import webinfo
crawledlinks = []
startcount = 0
start_with_url = 'start_with_url.txt' 
httputil = httputil.util()
webinfo = webinfo.ds()
def main(argv=sys.argv):
	if (len(argv) == 1):
		f = open(start_with_url, 'r')
		newurl = f.read()
		f.close()
	else:
		newurl = argv[1]
	crawl(str(newurl))

def crawlfromdb():
        global webinfo,httputil
        if webinfo.getuncrawled() == False:
                metainfo = httputil.getmeta(url)
                links = httputil.getlinks(url)
                print "meta data size :"+str(len(metainfo))+" links size : "+str(len(links))
                webinfo.savemetainfo(url, metainfo)
                webinfo.saveweblinks(url, links)
		webinfo.markcrawled(url)
def crawl(url):
	global webinfo,startcount,httputil,crawledlinks,start_with_url
	f = open(start_with_url, 'w')
	f.write(url)
	f.close()
	if (startcount == 10):
		crawlfromdb() # instead of exit, go and crawl the rest from db.
	metainfo = httputil.getmeta(url)
	links = httputil.getlinks(url)
	print "meta data size :"+str(len(metainfo))+" links size : "+str(len(links))
	webinfo.savemetainfo(url, metainfo)
	webinfo.saveweblinks(url, links)
	print url+ " " + str(len(crawledlinks))
	for i in links:
		if webinfo.siteexists(i):
			print url+" already crawled!!!!!!.. so skipping....."	
		else:
			startcount +=1
			crawl(str(i))
if __name__ == "__main__":
	sys.exit(main())
