from django.conf.global_settings import LOGIN_URL
from django.conf.urls import patterns, include, url
from django.contrib import admin
from organiser_app import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.RegisterView.as_view(),  name='register'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^calendar$', views.calendar_view, name='calendar'),
    url(r'^event/(?P<event_id>[^/]+)$', views.event_view, name='event'),
    url(r'^events/$', views.event_view, name='events'),
    url(r'^events/new$', views.CreateEvent.as_view(), name='event-new'),
    url(r'^contacts$', views.contacts_view, name='contacts'),
    url(r'^contact/(?P<contact_id>[^/]+)$', views.contact_view, name='contact'),
    url(r'^notes$', views.notes_view, name='notes'),
    url(r'^note/(?P<note_id>[^/]+)$', views.note_view, name='note'),
    url(r'^note/(?P<note_id>[^/]+)/edit$', views.EditNote.as_view(), name='note-edit'),
    url(r'^note/(?P<note_id>[^/]+)/delete', views.DeleteNote.as_view(), name='note-delete'),
    #url(r'^note/(?P<note_id>[^/]+)/(?P<action>[^/]+)$', views.note_view, name='note'),
    url(r'^notes/new$', views.CreateNote.as_view(), name='note-new'),
    url(r'^profile', views.myprofile_view, name='my-profile'),


    url(r'^logout$',  'django.contrib.auth.views.logout', {'next_page': LOGIN_URL}, name='logout'),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^bootstrap-calendar/', include('django_bootstrap_calendar.urls')),

)
