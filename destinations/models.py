from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Destination(models.Model):
    slug = models.SlugField(max_length=200, unique =True)
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
    package_title = models.CharField(max_length=250, unique=True, default="")
    package_id = models.AutoField(primary_key=True,auto_created=True)
    body= models.TextField(default = "Package Body")
    price = models.FloatField(default="0.0")
    duration = models.CharField(max_length=200)
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f"{self.package_title} : {self.destination.title}"

class Itinerary(models.Model):
    package = models.ForeignKey(
        Packages,
        on_delete=models.CASCADE,
        related_name = 'itinerary'
    )
    day_schedule = models.TextField(default = "This is your Itinerary")
    
    def __str__(self):
        return f"Itinerary for {self.package.package_title}"


class Info(models.Model):
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name = "info"
    )
    content = models.TextField(default = "This is the info page")
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Info for {self.destination.title}"
    
