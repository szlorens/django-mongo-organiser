from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from organiser_app.models import User, Note


def index(request):
    if request.user.is_authenticated():
        return dashboard_view(request)
    else:
        return render(request, "index.html")


def logout(request):
    auth_logout()
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
    return render(request, 'login.html', {"form": form})


def register_view(request):
    pass


@login_required()
def dashboard_view(request):
    user = request.user
    notes = Note.objects.filter(author=user)
    return render(request, "dashboard.html", {"notes": notes})


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
    return render(request, "note.html", {"note": note})


@login_required()
def myprofile_view(request):
    pass


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class MyProfile(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['email', 'password']
    template_name = 'myprofile.html'

    def get_object(self, queryset=None):
        return self.request.user




