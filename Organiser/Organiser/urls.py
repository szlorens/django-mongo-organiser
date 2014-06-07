from django.conf.urls import patterns, include, url
from django.contrib import admin
from organiser_app import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register_view, name='register'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^calendar$', views.calendar_view, name='calendar'),
    url(r'^event/(?P<event_id>\*)$', views.event_view, name='event'),
    url(r'^contacts$', views.contacts_view, name='contacts'),
    url(r'^contact/(?P<contact_id>\*)$', views.contact_view, name='contact'),
    url(r'^notess$', views.notes_view, name='notes'),
    url(r'^contact/(?P<note_id>\*)$', views.note_view, name='note'),
    url(r'^myprofile$', views.myprofile_view, name='myprofile'),
    url(r'^logout$', views.login_view, name='logout'),

    url(r'^admin/', include(admin.site.urls)),
)
