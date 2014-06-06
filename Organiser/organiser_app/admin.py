from django.contrib import admin
from organiser_app.models import CalendarEvent, Contact, Note, User


admin.site.register(CalendarEvent)
admin.site.register(Contact)
admin.site.register(Note)
admin.site.register(User)