from django.test import TestCase
from .models import Category,location,Image


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

class ImageTestCase(TestCase):

    def setUp(self):
        self.cat1 = Category(name = "foody")
        self.cat1.save()
        self.loc = location(location_name = "mombasa")
        self.loc.save()
        self.new_image = Image(image = "her.png",image_name = "her",description = "cool cool",image_category = self.cat1,location_taken = self.loc)
    

    def test_instance_Image(self):
         self.assertTrue(isinstance(self.new_image,Image))

    def tearDown(self):
        Category.objects.all().delete()
        location.objects.all().delete()
        Image.objects.all().delete() 
    

