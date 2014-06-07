# coding=utf-8
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, UserManager
from django.core.urlresolvers import reverse_lazy
from django.db import models
from djangotoolbox.fields import EmbeddedModelField, RawField


class User(AbstractUser):
    # objects = UserManager()
    def __str__(self):
        return self.get_full_name() + " [" + self.email + "]"


class Note(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Data utworzenia")
    edit_date = models.DateTimeField(verbose_name="Data edycji", null=True, blank=True, auto_now=True)
    title = models.CharField(verbose_name="Tytuł", max_length=100)
    content = models.TextField(verbose_name="Treść", default=None)
    author = models.ForeignKey(User)

    def get_absolute_url(self):
        return reverse_lazy('note', args=(self.id,))

    def __str__(self):
        return self.author.get_full_name() + " - " + self.title


class Contact(models.Model):
    first_name = models.TextField(verbose_name="Imię")
    last_name = models.TextField(verbose_name="Nazwisko")
    birthdate = models.DateField(verbose_name="Data urodzenia", null=True, blank=True)
    phone_number = models.TextField(max_length=12, verbose_name="Numer telefonu")
    location = models.TextField(max_length=300, verbose_name="Miejsce zamieszkania")
    additional_info = models.TextField(max_length=500, verbose_name="Dodatkowe informacje")
    author = models.ForeignKey(User)


class CalendarEvent(models.Model):
    title = models.TextField(max_length=100, verbose_name="Tytuł")
    description = models.TextField(default=None, null=True, blank=True, verbose_name="Opis")
    start_date = models.DateTimeField(verbose_name="Data rozpoczęcia")
    end_date = models.DateTimeField(default=None, null=True, blank=True, verbose_name="Data zakończenia")
    location = models.TextField(max_length=300, verbose_name="Miejsce wydarzenia", default=None, null=True, blank=True)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.author.get_full_name() + " - " + self.title + " [" + str(self.start_date)+ "]"