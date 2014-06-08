from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import HiddenInput
from organiser_app.models import Note, CalendarEvent

__author__ = 'pawelszymanski'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name']


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username',)


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'author']
        widgets = {
            'author': HiddenInput()
        }


class CalendarEventForm(forms.ModelForm):
    #start_date = forms.DateField(widget=DateTimePicker(options={"pickTime": True}))
    #end_date = forms.DateField(widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": True}), required=False)

    class Meta:
        model = CalendarEvent
        # fields = ['title', 'description', 'start_date', 'end_date', 'location']
        #start_date = forms.DateField(widget=DateTimePicker(options={"pickTime": True}))
        widgets = {
            'start_date': DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": True}),
            'end_date': DateTimePicker(options={"format": "YYYY-MM-DD","pickTime": True})
        }
        exclude = ['author']


