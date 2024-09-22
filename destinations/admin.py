from django.contrib import admin
from .models import Destination,Packages
# from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

# @admin.register(Destination)
admin.site.register(Destination)
admin.site.register(Packages)

