import random
import unittest
import webinfo

class testwebinfo(unittest.TestCase):

    def setUp(self):
	self.ds = webinfo.ds()
    def test_getallweblinks(self):
	print self.ds.getweblinks("url1")
    def test_removeweblinks(self):
	links = ["url10","url20"]
	self.ds.removeweblinks("url1",links)
    def test_keyexists(self):
	print self.ds.siteexists("url1")
    def test_getdbstat(self):
	self.ds.getdbstat()
if __name__ == '__main__':
    unittest.main()
