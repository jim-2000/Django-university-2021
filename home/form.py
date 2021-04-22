from django import forms
from .models import AdmissionForm, Courses
#
class Addmission_Form(forms.ModelForm):
    class Meta:
        model = AdmissionForm
        fields = '__all__'
        exclude = ['status']