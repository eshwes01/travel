from .models import Comment,Booking
from django import forms
from datetime import datetime


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class BookingForm(forms.ModelForm):
    booking_month = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'month'}),  # month picker
        label="Month to update",
    )

    class Meta:
        model = Booking
        fields = ('booking_month','no_of_people',)

    def clean_booking_month(self):
            booking_month = self.cleaned_data.get('booking_month')

            try:
                # Append "-01" to represent the first day of the month
                booking_month_date = datetime.strptime(booking_month + "-01", '%Y-%m-%d')
                return booking_month_date
            except ValueError:
                raise forms.ValidationError("Enter a valid month in the format YYYY-MM.")
