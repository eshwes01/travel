from .models import Comment, Booking
from django import forms
from datetime import datetime


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class BookingForm(forms.ModelForm):
    """
        Booking Form
    """
    booking_month = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'date'}),  # month picker
        label="Select Month to Book ",
    )

    class Meta:
        model = Booking
        fields = ('booking_month', 'no_of_people',)

    def clean_booking_month(self):
        booking_month = self.cleaned_data.get('booking_month')

        try:
            return booking_month
        except ValueError:
            raise forms.ValidationError
            ("Enter a valid month in the format YYYY-MM.")
