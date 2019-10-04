from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class location(models.Model):
     location = models.CharField(max_length=60)

     def __str__(self):
         return self.location



# Create your models here.
