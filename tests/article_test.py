import unittest
from app.models import article
Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.new_article = Article('bloomberg', 'Mark Gurman', 'Apple Has a Chance to Launch an iPhone Costing Just $199', 'Apple is planning to unveil a 5G iPhone SE in March—but the big news could be a price drop for the current model. Also: Amazon’s Astro robot remains elusive, and it was a wild week for Apple Stores.', 'https://www.bloomberg.com/news/newsletters/2022-02-27/when-is-apple-aapl-launching-5g-iphone-se-will-apple-drop-iphone-se-price-l05dwajk', 'https://assets.bwbx.io/images/users/iqjWHBFdfxIU/i56tvB.mjm3E/v1/1200x774.jpg', '2022-02-27T14:45:17Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))