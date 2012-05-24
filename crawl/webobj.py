#/usr/bin/python
class webobject:
	def __init__(self, name):
		self.name = name
		self.links = []
		self.metainfo = {}
	def addlinks(self, x):
		for i in x:
			self.links.append(i)
	def getname(self):
		return self.name
	def addlink(self, x):
		self.links.append(x)
	def printme(self):
		print "#START#"	
		print "crawling url :"+self.name
		for metatag in self.metainfo:
			print metatag+ " "+ self.metainfo[metatag]
		for i in self.links:
			print i
		print "#END#"	
	def getlinks(self):
		return self.links
	def addmetainfo(self, x):
		self.metainfo = x
	def getmetainfo(self):
		return self.metainfo
