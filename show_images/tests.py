from django.test import TestCase
from .models import Category


class CategoryTestCase(TestCase):

    # setup
    def setUp(self):
        self.cat1= Category(name='goodfood')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.cat1,Category))

    
