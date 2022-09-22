from django import forms
from django.forms import ModelForm
from .models import MeetingBookModel

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type='time'

class MeetingBookForm(ModelForm):
    class Meta:
        model = MeetingBookModel
        fields = ['user_name','date','time','location','booked']
        widgets = {
            'date': DateInput(),
            'time':TimeInput(),
        }
