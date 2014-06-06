from django.conf.urls import patterns, include, url
from django.contrib import admin
from organiser_app import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),

    url(r'^admin/', include(admin.site.urls)),
)
