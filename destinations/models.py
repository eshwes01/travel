from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Destination model 
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

# Info model
class Info(models.Model):
    destination = models.OneToOneField(
        Destination,
        on_delete= models.CASCADE,
        primary_key=True
    )
    things_to_do = models.TextField(default = "Things to do")
    localFood = models.TextField(default = "Local Food ")
    places_to_explore = models.TextField(default = "Place to explore")
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Info for {self.destination.title}"

# Package model 
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
    itinerary = models.TextField(default = "Itinerary Detail")

    def __str__(self):
        return f"{self.package_title} : {self.destination.title}"

# Comment model
class Comment(models.Model):
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name = "comments"
    )

    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "commenter"
    )

    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
class Booking(models.Model):
    user = models.ForeignKey(
        User,
        on_delete= models.CASCADE,
        related_name = "user"
    )
    package = models.ForeignKey(
        Packages,
        on_delete=models.CASCADE,
        related_name= "bookings"
    )
    month = models.IntegerField()
    no_of_people = models.IntegerField(default = 1)

# def profile_page(request):
#     user = get_object_or_404(User, user=request.user)
#     # Retrieve all comments for the user object
#     comments = user.commenter.all()
