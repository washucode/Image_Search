from django.test import TestCase
from .models import Category,location


class CategoryTestCase(TestCase):

    # setup
    def setUp(self):
        self.cat1= Category(name='goodfood')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.cat1,Category))


class LocationTestCase(TestCase):

    def setUp(self):
        self.loc1= location(location_name='Nairobi')

    def test_instance_Location(self):
        self.assertTrue(isinstance(self.loc1,location))
    

