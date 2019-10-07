from django.test import TestCase
from .models import Category,location,Image


class CategoryTestCase(TestCase):

   
    def setUp(self):
        '''
        set up instance

        '''
        self.cat1= Category(name='goodfood')
    
    def test_instance(self):
        '''
        Test object instance of the model
        
        '''
        self.assertTrue(isinstance(self.cat1,Category))

    def test_save_category(self):
        '''
        Test save category behaivour
        
        '''
        self.cat1.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def tearDown(self):
        '''
        Test delete category behaivour
        
        '''
        Category.objects.all().delete()
        
    def test_update_category(self):
        '''
        Test if  Category object can be updated.
        '''
        self.cat1.save_category()
        self.category = Category.objects.filter(name = 'goodfood').update(name = "good good")
        self.category_u = Category.objects.get(name = 'good good')
        self.assertEqual(self.category_u.name,"good good")


 


class LocationTestCase(TestCase):

    def setUp(self):
        self.loc1= location(location_name='Nairobi')

    def test_instance_Location(self):
        self.assertTrue(isinstance(self.loc1,location))

    def test_save_location(self):
        self.loc1.save_location()
        locations = location.objects.all()
        self.assertTrue(len(locations) > 0)

    def tearDown(self):
       location.objects.all().delete()
    
    def test_update_category(self):
        '''
        Test if  location object can be updated.
        '''
        self.loc1.save_location()
        self.location = location.objects.filter(location_name = 'Nairobi').update(location_name = "Kisumu")
        self.location_u = location.objects.get(location_name = 'Kisumu')
        self.assertEqual(self.location_u.location_name,"Kisumu")

    

 

class ImageTestCase(TestCase):

    def setUp(self):
        self.cat1 = Category(name = "foody")
        self.cat1.save()
        self.loc = location(location_name = "mombasa")
        self.loc.save()
        self.new_image = Image(image = "her.png",image_name = "her",description = "cool cool",image_category = self.cat1,location_taken = self.loc)
    

    def test_instance_Image(self):
         self.assertTrue(isinstance(self.new_image,Image))

    

    def test_save_image(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
 
    def tearDown(self):
        Category.objects.all().delete()
        location.objects.all().delete()
        Image.objects.all().delete() 

    def test_delete_image(self):
        self.new_image.save_image()
        self.image2 = Image(image = "herme.png",image_name = "herme",description = "morecool",image_category = self.cat1,location_taken = self.loc)
        self.image2.save_image()
        self.new_image.delete_image()
        all_images = Image.objects.all()
        self.assertEqual(len(all_images),1)

    # def  test_update_image(self):
    #      self.new_image.save_image()

    #      saved_image = Image.objects.filter(image_name='herme')
        
    #      self.new_image.update_image(image_name ='esther')
      
    #      self.assertTrue(new.image.image_name =='esther')
         
