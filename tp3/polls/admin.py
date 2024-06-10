from django.contrib import admin

# Register your models here.

from .models import PatientData

admin.site.register(PatientData)
