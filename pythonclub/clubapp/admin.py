from django.contrib import admin
from .models import clubProduct, clubType

# Register your models here.
# Necessary if they are to appear in the admin
admin.site.register(clubProduct)
admin.site.register(clubType)