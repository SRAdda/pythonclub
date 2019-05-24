from django.contrib import admin
from .models import Meeting, Resource, Event

# Register your models here.
# Necessary if they are to appear in the admin

admin.site.register(Meeting)
admin.site.register(Resource)
admin.site.register(Event)