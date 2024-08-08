from django.db import models

# Create your models here.
class Blogs(models.Model):
    images= models.ImageField(upload_to="blog_images")
    title= models.CharField(max_length=100,unique=True)
    mini_description= models.TextField()
    readingTime= models.IntegerField()
    content=models.TextField()

    
    
