from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.shortcuts import render


def index(request):
    if request.user.is_authenticated():
        return render(request, "dashboard.html")
    else:
        return render(request, "index.html")


def logout(request):
    auth_logout()
    return index(request)


def login_view(request):
    pass


def register_view(request):
    pass


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
def note_view(requst):
    pass


@login_required()
def myprofile_view(request):
    pass