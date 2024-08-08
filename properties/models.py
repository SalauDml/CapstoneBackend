from django.db import models

# Create your models here.
class Properties(models.Model):
    # index = models.AutoField(unique = True,null=True)
    image= models.ImageField(upload_to="propertyImage")
    title= models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    mini_description = models.TextField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    location= models.CharField(max_length=20)
    property_type=models.CharField(max_length=20)
    pricing_range=models.CharField(max_length=20)
    property_size = models.CharField(max_length=20,blank=True,null=True)

class PropertyImages(models.Model):
    owner_property = models.ForeignKey(Properties,on_delete=models.CASCADE)
    image1= models.ImageField(upload_to="specificPropertyImages")
    image2= models.ImageField(upload_to="specificPropertyImages")
    image3= models.ImageField(upload_to="specificPropertyImages")
    image4= models.ImageField(upload_to="specificPropertyImages")
    image5= models.ImageField(upload_to="specificPropertyImages")
    image6= models.ImageField(upload_to="specificPropertyImages")
    image7= models.ImageField(upload_to="specificPropertyImages")
    image8= models.ImageField(upload_to="specificPropertyImages")
    image9= models.ImageField(upload_to="specificPropertyImages")
    image10= models.ImageField(upload_to="specificPropertyImages")

