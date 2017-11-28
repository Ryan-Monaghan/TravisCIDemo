import unittest

class TravisCIDemo(unittest.TestCase):
	def setUp(self):
		print 'Travis CI Demo'
	
	def test_search_in_python_org(self):
		print 'Travis CI Demo'
		
	def tearDown(self):
		print 'Travis CI Test'
		
unittest.main()