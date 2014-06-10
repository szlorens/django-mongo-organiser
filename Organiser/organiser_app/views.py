from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.datetime_safe import datetime
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from itertools import groupby
from operator import itemgetter
from organiser_app.forms import ProfileForm, NoteForm, RegisterForm, CalendarEventForm, ContactForm
from organiser_app.models import Note, CalendarEvent, Contact


def index(request):
    if request.user.is_authenticated():
        return dashboard_view(request)
    else:
        return render(request, "organiser_app/index.html")


def logout(request):
    auth_logout(request)
    return index(request)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            form = AuthenticationForm(request.POST)
    else:
        form = AuthenticationForm()
    return render(request, 'organiser_app/login.html', {"form": form})


@login_required()
def dashboard_view(request):
    user = request.user
    notes = Note.objects.filter(author=user)[:5].reverse()
    events = CalendarEvent.objects.filter(
        Q(start_date__gte=datetime.today()) | Q(start_date__lte=datetime.today() + timedelta(days=7)),
        author=user).order_by('start_date')[:5]
    return render(request, "organiser_app/dashboard.html", {"notes": notes, "events": events})


@login_required
def calendar_view(request):
    return render(request, 'organiser_app/calendar.html')


@login_required()
def event_view(request):
    pass


@login_required()
def contacts_view(request):
    user = request.user
    contacts = Contact.objects.filter(author=user).order_by('last_name')
    # nc = {}
    # for letter, last_names in groupby(sorted(contacts), key=itemgetter(0)):
    #     nc[letter] = last_names
    return render(request, 'organiser_app/contacts.html',{"contacts" : contacts})


@login_required()
def contact_view(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, "organiser_app/contact.html", {"contact": contact})


@login_required()
def notes_view(request):
    user = request.user
    notes = Note.objects.filter(author=user).reverse()
    notes1 = notes[::3]
    notes2 = notes[1::3]
    notes3 = notes[2::3]
    notes = [notes1, notes2, notes3]
    return render(request, 'organiser_app/notes.html', {"notes": notes, "message" : {"type": "info", "content": "Hello!"}})


@login_required()
def note_view(request, note_id):
    user = request.user
    note = Note.objects.get(id=note_id)

    # if action == "delete":
    # note.delete()
    # return index(request)
    # else:
    return render(request, "organiser_app/note.html", {"note": note})


@login_required()
def MyProfileView(request):
    form = ProfileForm(instance=request.user)
    return render(request, 'organiser_app/myprofile.html', {"form": form})


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = '/login'
    template_name = 'organiser_app/register.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        return super(RegisterView, self).get(request, *args, **kwargs)


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


# Notes classes
class NoteMixin(LoginRequiredMixin):
    form_class = NoteForm
    model = Note
    template_name = 'organiser_app/note_form.html'
    pk_url_kwarg = 'note_id'


class CreateNote(NoteMixin, CreateView):
    def get_initial(self):
        initial = super(CreateNote, self).get_initial()
        initial['author'] = self.request.user
        return initial


class EditNote(NoteMixin, UpdateView):
    pass


class DeleteNote(NoteMixin, DeleteView):
    template_name = 'organiser_app/note_check_delete.html'
    success_url = reverse_lazy('notes')


# Events classes
class EventMixin(LoginRequiredMixin):
    # form_class = CalendarEventForm
    model = CalendarEvent
    pk_url_kwarg = 'event_id'
    template_name = 'organiser_app/event_form.html'


class ShowEvent(EventMixin, DetailView):
    template_name = 'organiser_app/event.html'

    def get_context_data(self, **kwargs):
        context = super(ShowEvent, self).get_context_data(**kwargs)
        return context


class EditEvent(EventMixin, UpdateView):
    form_class = CalendarEventForm
    success_url = reverse_lazy('events')


class DeleteEvent(EventMixin, DeleteView):
    template_name = 'organiser_app/event_check_delete.html'
    success_url = reverse_lazy('events')


class CreateEvent(EventMixin, CreateView):
    model = CalendarEvent
    form_class = CalendarEventForm
    pk_url_kwarg = 'event_id'

    def get_initial(self):
        initial = super(CreateEvent, self).get_initial()
        initial['author'] = self.request.user
        return initial


# Contacts classes
class ContactMixin(LoginRequiredMixin):
    model = Contact
    pk_url_kwarg = 'contact_id'
    template_name = 'organiser_app/contact_form.html'
    form_class = ContactForm


class CreateContact(ContactMixin, CreateView):
    def get_initial(self):
        initial = super(CreateContact, self).get_initial()
        initial['author'] = self.request.user
        return initial


class EditContact(ContactMixin, UpdateView):
    form_class = ContactForm
    success_url = reverse_lazy('contacts')


class DeleteContact(ContactMixin, DeleteView):
    template_name = 'organiser_app/contact_check_delete.html'
    success_url = reverse_lazy('contacts')


class NoteList(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)


class CalendarView(LoginRequiredMixin, ListView):
    model = CalendarEvent
    context_object_name = 'events'
    template_name = 'organiser_app/calendar.html'

    def get_queryset(self):
        return CalendarEvent.objects.filter(author=self.request.user)

    def get_initial(self):
        initial = super(CalendarView, self).get_initial()
        initial['author'] = self.request.user
        return initial


