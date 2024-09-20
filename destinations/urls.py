from django.urls import path
from . import views

urlpatterns = [
        path('<slug:slug>/',views.package_detail, name='package_detail'),
        path('',views.DestinationsList.as_view(), name='home'),      
]