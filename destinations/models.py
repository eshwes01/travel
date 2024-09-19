from django.db import models
from cloudinary.models import CloudinaryField

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

    
