'''
Created on Aug 5, 2012

@author: Shimon
'''
import unittest
from src.mail import mail

class Test(unittest.TestCase):
    def setUp(self):
        m = mail(name='AOL Mail', server='imap.aol.com', username='llagerman@aol.com', password='travis')
    
    def testConnect(self):
        pass
    
    def testListFolders(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()