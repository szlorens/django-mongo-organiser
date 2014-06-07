from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import HiddenInput
from organiser_app.models import Note

__author__ = 'pawelszymanski'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name','last_name']


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