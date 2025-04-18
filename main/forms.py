from django import forms
from .models import Reservations

class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservations
        fields = ('name', 'email', 'phone',
                  'date', 'time', 'message','number_guests')






