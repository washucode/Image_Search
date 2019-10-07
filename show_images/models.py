from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        '''
         method to display category
        '''
        return self.name


    def save_category(self):

        '''
         method to save category
        '''
        return self.save()


    def delete_category(self):

        '''
         method to delete category
        '''

        return self.delete()
    
    def update_category(self, cat1):
        '''
         method to update  category
        '''
        self.update(location_name = cat1)


class location(models.Model):
        location_name = models.CharField(max_length=60)

        def __str__(self):

            '''
            method to update location
            '''
            return self.location_name


        def save_location(self):
            '''
            method to save location
            '''
            return self.save()


        def delete_location(self):
            '''
            method to delete location
            '''
            return self.delete()


        def update_location(self, loc1):
            '''
                method to update location
            '''
            self.update(location_name = loc1)


class Image(models.Model):

    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=30)
    description = models.TextField()
    location_taken= models.ForeignKey(location)
    image_category = models.ForeignKey(Category)



    def __str__(self):

        '''
        method to display image
        '''
        return self.image_name

    def save_image(self):
        '''
        method to save image
        '''
        return self.save()

    def delete_image(self):

        '''
        method to delete image
        '''
        return self.delete()


    def update_image(self, img):
        '''
            Method to update image
        '''
        self.update(name = img)

    @classmethod
    def allphotos(cls):

        '''
        method to get all images 
        '''
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls,id):
        '''
            Method to get image using the id
        '''
        image = cls.objects.get(id = id)
        return image  

    @classmethod
    def search_by_category(cls,search_term):
        '''
        method to search images by category 
        '''
        category_id = Category.objects.filter(name__icontains=search_term)
        id_length = len(category_id)
        image_s = []
        for ids in range(id_length):
            found_images = cls.objects.filter(image_category__in=[category_id[ids].id])
            image_s.append(found_images)
        return image_s


    @classmethod
    def find_by_location(cls,locationterm):

        '''
        method to find image by location
        '''

        location_id = location.objects.filter(location_name__icontains=locationterm)
        id_length = len(location_id)
        image_s = []
        for ids in range(id_length):
            found_images = cls.objects.filter(location_taken__in=[location_id[ids].id])
            image_s.append(found_images)
        return image_s







