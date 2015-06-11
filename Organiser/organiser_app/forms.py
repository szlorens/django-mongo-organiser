from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import HiddenInput
from organiser_app.models import Note, CalendarEvent, Contact

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


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'author': HiddenInput(),
            'birthdate': DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}),
        }


class CalendarEventForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        widgets = {
            'author': HiddenInput(),
            'start_date': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm", "pickTime": True, }),
            'end_date': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm", "pickTime": True})
        }


