from django.contrib import admin

# Register your models here.
from .models import Specialites,Traiteurs

admin.site.register(Specialites)
admin.site.register(Traiteurs)
