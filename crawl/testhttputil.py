import httputil
import unittest

class testhttputil(unittest.TestCase):
	
	def setUp(self):
		self.httputil = httputil.util()	
	def test_getmeta(self):
		print self.httputil.getmeta("http://techcrunch.com")
	def test_getlinks(self):
		print self.httputil.getlinks("http://techcrunch.com")

if __name__ == '__main__':
	unittest.main()
