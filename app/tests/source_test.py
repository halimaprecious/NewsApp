import unittest
from app.models import Source

class sourcetest(unittest.TestCase):

    def setUp(self):
        '''runs before each test case'''
        self.new_source = Source("abc-news","ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.", "en","us","https://abcnews.go.com")
    
    def test_instance(self):
        '''checks if object is an instance of class Source'''
        self.assertTrue(isinstance(self.new_source,Source))

    def test_init(self):
        '''test if object is initialized properly'''
        self.assertEqual(self.new_source.id,"abc-news")
        self.assertEqual(self.new_source.name,"ABC News")
        self.assertEqual(self.new_source.description,"Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.")
        self.assertEqual(self.new_source.language,"en")
        self.assertEqual(self.new_source.country,"us")
        self.assertEqual(self.new_source.url,"https://abcnews.go.com")


