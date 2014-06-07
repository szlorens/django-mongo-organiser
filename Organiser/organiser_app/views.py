from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import ProcessFormView, ModelFormMixin, CreateView, UpdateView, DeleteView

from organiser_app.forms import ProfileForm, NoteForm, RegisterForm

from organiser_app.models import User, Note, CalendarEvent


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
    notes = Note.objects.filter(author=user)
    events = CalendarEvent.objects.filter(author=user)
    return render(request, "organiser_app/dashboard.html", {"notes": notes, "events" : events})


@login_required
def calendar_view(request):
    pass


@login_required()
def event_view(request):
    pass


@login_required()
def contacts_view(request):
    pass


@login_required()
def contact_view(request):
    pass


@login_required()
def notes_view(request):
    pass


@login_required()
def note_view(request, note_id):
    user = request.user
    note = Note.objects.get(id=note_id)

    # if action == "delete":
    #     note.delete()
    #     return index(request)
    # else:
    return render(request, "organiser_app/note.html", {"note": note})


@login_required()
def myprofile_view(request):
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


class NoteMixin(LoginRequiredMixin):
    form_class = NoteForm
    model = Note
    template_name = 'organiser_app/note_form.html'
    pk_url_kwarg = 'note_id'


class CreateNote(NoteMixin, CreateView):
    def get_initial(self):
        initial = super(CreateNote, self).get_initial()
        initial['author'] = self.request.user._wrapped
        return initial


class EditNote(NoteMixin, UpdateView):
    pass


class DeleteNote(NoteMixin, DeleteView):
    template_name = 'note_check_delete.html'
    success_url = reverse_lazy('notes')


class CreateEvent(LoginRequiredMixin, CreateView):
    model = CalendarEvent
    pk_url_kwarg = 'event_id'





