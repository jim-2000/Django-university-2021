from django.contrib import admin
from .models import AdmissionForm, Courses
# Register your models here.
admin.site.register(Courses)
admin.site.register(AdmissionForm)