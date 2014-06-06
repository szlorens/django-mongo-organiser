# coding=utf-8
from django.contrib.auth.models import AbstractUser
from django.db import models
from djangotoolbox.fields import EmbeddedModelField


class User(AbstractUser):
    pass


class Note(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Data utworzenia")
    edit_date = models.DateTimeField(verbose_name="Data edycji")
    content = models.TextField(verbose_name="Treść")
    author = EmbeddedModelField('User', verbose_name="Autor")


class Contact(models.Model):
    first_name = models.TextField(verbose_name="Imię")
    last_name = models.TextField(verbose_name="Nazwisko")
    birthdate = models.DateField(verbose_name="Data urodzenia")
    phone_number = models.TextField(max_length=12, verbose_name="Numer telefonu")
    location = models.TextField(max_length=300, verbose_name="Miejsce zamieszkania")
    additional_info = models.TextField(max_length=500, verbose_name="Dodatkowe informacje")


class CalendarEvent(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.TextField(max_length=300, verbose_name="Miejsce wydarzenia")