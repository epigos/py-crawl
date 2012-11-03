import redis
import re

class ds:
	def __init__(self):
		self.db = redis.StrictRedis(host='localhost', port=6379, db=0)
	def siteexists(self, url):
		if self.db.exists(url) == 1:
			return True
		else:
			return False
	def savemetainfo(self, url,map):
		for i in map:
			self.db.hset(url,i ,map[i])
	def getmetainfo(self,url):
		print self.db.hgetall(url)
	def saveweblinks(self, url, links):
		for i in links:
			print url + " "+ i
			self.db.hset(url,i,"")
	def getweblinks(self,url):
		weblinks = []
		allkeys = self.db.hkeys(url)
		for i in allkeys:
			if i.startswith("http://"):
				weblinks.append(i)
		return weblinks
	def removeweblinks(self,url,links):
		for i in links:
			self.db.lrem(url,0,str(i))
	def markcrawled(self,url):
		self.db.hset(url,"weblinks-crawled","yes")
	def getmarkcrawled(self):
		allsites = self.db.keys("http://*")
		crawledlinks = []
		for i in allsites:
			if "weblinks-crawled" in self.db.hkeys(i):
				crawledlinks.append(i)
		return crawledlinks
	def getuncrawled(self):
		allsites = self.db.keys("http://*")
		uncrawledlinks = []
		for i in allsites:
			if ("weblinks-crawled" in self.db.hkeys(i)) == False:
				uncrawledlinks.append(i)
		return uncrawledlinks
	def getallsite(self,keypattern):
		return self.db.keys(keypattern)
	def getsitebycontent(self, searchpattern):
		allsites = self.db.keys("http://*")
		searchregex = re.compile('(.*?)'+searchpattern+'(.*?)')
		for i in allsites:
			description = self.db.hget(i, "keywords")
			list = searchregex.findall(str(str(description)))
			if len(list) != 0:
				print i + " description is "+ description
	def getdbstat(self):
		print "Total db keys : "+ str(self.db.dbsize())
		print "Total crawled : "+ str(len(self.getmarkcrawled()))
		print "Total uncrawled : "+ str(len(self.getuncrawled()))
