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
     image_category = models.ManyToManyField(Category)
     



# Create your models here.
