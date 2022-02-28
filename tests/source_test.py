import unittest
from app.models import source
Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.new_source = Source('business-insider', 'Business Insider', 'Business Insider is a fast-growing business site with deep financial, media, tech, and other industry verticals. Launched in 2007, the site is now the largest business news site on the web.', 'http://www.businessinsider.com', 'business', 'en', 'us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))