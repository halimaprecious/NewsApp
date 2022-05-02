import unittest 
from app.models import Article


class articles_test(unittest.TestCase):

    def setUp(self):
        self.new_article = Article('Covid-19 Case arise','More people diagonised with covid-19', 'https://www.cbc.ca/news/canada/newfoundland-labrador/apocalypse-then-wave-prediction-1.6435963','https://i.cbc.ca/1.5471199.1582299129!/fileImage/httpImage/image.jpg_gen/derivatives/16x9_620/crashing-waves-at-st-shott-s.jpg','This column is an instalment in our series Apocalypse Then\r\n, in which cultural historian Ainsley Hawthorn examines the issues of COVID-19 through the lens of the past. \r\nSince the beginning of the C… [+5646 chars]','2022-05-01T14:25:59Z')

    def test_instance(self):
        '''checks if object is an instance of class Article'''
        self.assertTrue(isinstance(self.new_article,Article))
        
    def test_init(self):
        '''test if object is initialized properly'''
        self.assertEqual(self.new_article.title,"Covid-19 Case arise")
        self.assertEqual(self.new_article.description,"More people diagonised with covid-19")
        self.assertEqual(self.new_article.url,"https://www.cbc.ca/news/canada/newfoundland-labrador/apocalypse-then-wave-prediction-1.6435963")
        self.assertEqual(self.new_article.urlToImage,"https://i.cbc.ca/1.5471199.1582299129!/fileImage/httpImage/image.jpg_gen/derivatives/16x9_620/crashing-waves-at-st-shott-s.jpg'")
        self.assertEqual(self.new_article.content,"This column is an instalment in our series Apocalypse Then\r\n, in which cultural historian Ainsley Hawthorn examines the issues of COVID-19 through the lens of the past. \r\nSince the beginning of the C… [+5646 chars]")
        self.assertEqual(self.new_article.publishedAt,"2022-05-01T14:25:59Z")

