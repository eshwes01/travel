from django.urls import path
from . import views

urlpatterns = [
        path('<slug:slug>/package_detail/',views.package_detail, name='package_detail'),
        path('<slug:slug>/info_detail/',views.info_detail, name='info_detail'),
        path('<int:itinerary_id>',views.itinerary_detail, name= 'itinerary_detail'),
        path('',views.DestinationsList.as_view(), name='home'),      
]