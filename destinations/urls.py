from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_dest, name='my_dest'),
]