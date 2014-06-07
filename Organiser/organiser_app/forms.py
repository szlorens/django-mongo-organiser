from django import forms
from django.contrib.auth import get_user_model

__author__ = 'pawelszymanski'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name','last_name']
