import urllib2
import re
import sys
import webobj
import redis
from sets import Set
hrefregex = re.compile('<a\shref=[\'"](.*?)[\'"]')
metaregex = re.compile('<meta\s(.*?)=[\'"](.*?)[\'"]\s(.*?)=[\'"](.*?)[\'"]')
contentregex = re.compile('content=[\'"](.*?)[\'"]')
httpdomainregex = re.compile('[(http).*?(www).*?]://(.*?).com')

class util:
	def __init__(self):
		self.hrefregex = re.compile('<a\shref=[\'"](.*?)[\'"]')
		self.metaregex = re.compile('<meta\s(.*?)=[\'"](.*?)[\'"]\s(.*?)=[\'"](.*?)[\'"]')
		self.contentregex = re.compile('content=[\'"](.*?)[\'"]')
		self.httpdomainregex = re.compile('[(http).*?(www).*?]://(.*?).com')

	def getmeta(self, url):	
		keyvalue = {}
		try:
			response = urllib2.urlopen(url)
			for line in response:
                		list = self.metaregex.findall(line.rstrip())
                		if len(list)!= 0:
                        		for i in list:
                                		keyvalue[i[1]]=i[3]
		except Exception as e:
			print e
		return keyvalue
	def getlinks(self,url):
		links = []
		try:
			response = urllib2.urlopen(url)
			for line in response:
                		list = self.hrefregex.findall(line.rstrip())
                		if len(list) != 0:
                        		for i in list:
                                		links.append(i)
		except Exception as e :
			print e
		return self.pruneduplicatelinks(links) 
	def pruneduplicatelinks(self, links):
		uniquedomains = Set()
		for i in links:
			domainlist = self.httpdomainregex.findall(i)
			if len(domainlist) != 0:
				for j in domainlist:
					uniquedomains.add("http://"+j+".com") #temp-fix: prepend and append http and com for now
		return uniquedomains
		
