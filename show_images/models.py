from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class location(models.Model):
     location_name = models.CharField(max_length=60)

     def __str__(self):
         return self.location_name

class Image(models.Model):
     image = models.ImageField(upload_to='images/')
     image_name = models.CharField(max_length=30)
     description = models.TextField()
     location_taken= models.ForeignKey(location)
     image_category = models.ForeignKey(Category)

     def save_image(self):
        return self.save()
     def delete_image(self):
        return self.delete()

     @classmethod
     def allphotos(cls):
         images = cls.objects.all()
         return images
     @classmethod
     def search_by_category(cls,search_term):
        category_id = Category.objects.filter(name__icontains=search_term)
        id_length = len(category_id)
        image_s = []
        for ids in range(id_length):
            found_images = cls.objects.filter(image_category_in=[category_id[ids].ids])
            image_s.append(found_images)
        return image_s

        
     @classmethod
     def find_by_location(cls,locationterm):
        location_id = location.objects.filter(location_name__icontains=locationterm)
        id_length = len(location_id)
        image_s = []
        for ids in range(id_length):
            found_images = cls.objects.filter(location_taken_in=[location_id[ids].ids])
            image_s.append(found_images)
        return image_s


    



# Create your models here.
