from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Destination(models.Model):
    slug = models.SlugField(max_length=200,unique =True)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Destination Title  {self.title}"

    class Meta:
        ordering = ["created_on"]

class Packages(models.Model):
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name = "packages"
    )

    body= models.TextField()
    price = models.FloatField(default="0.0")
    duration = models.CharField(max_length=200)

    
    
