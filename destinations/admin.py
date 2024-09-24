from django.contrib import admin
from .models import Destination,Packages,Info
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Packages)
class PackagesAdmin(SummernoteModelAdmin):

    list_display = ('package_id', 'package_title', 'price','duration')
    search_fields = ['package_title']
    # prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('itinerary',)
    
# @admin.register(Destination)
admin.site.register(Destination)

@admin.register(Info)
class InfoAdmin(SummernoteModelAdmin):

    list_display = ('get_destination','destination')
    def get_destination(self,obj):
        return obj.destination.title

    search_fields = ['things_to_do','localFood','places_to_explore']
    # prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('things_to_do', 'localFood','places_to_explore')
# admin.site.register(Packages)

