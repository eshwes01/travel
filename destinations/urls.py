from django.urls import path
from . import views

urlpatterns = [
        path('<slug:slug>/package_detail/',views.package_detail, name='package_detail'),
        path('<slug:slug>/info_detail/',views.info_detail, name='info_detail'),
        path('<int:package_id>',views.itinerary_detail, name= 'itinerary_detail'),
        path('<slug:slug>/info_detail/edit_comment/<int:comment_id>',views.comment_edit, name='comment_edit'),
        path('mybooking/', views.my_booking, name='my_booking'), 
        path('',views.DestinationsList.as_view(), name='home'),   
]