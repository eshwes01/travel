from .models import Comment,Booking
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('month','no_of_people',)
