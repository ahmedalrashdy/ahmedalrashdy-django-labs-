
from django import forms
from .models import Patients
class PatientsForm(forms.ModelForm):
    class Meta:
        model = Patients

        # fields = ['first_name','last_name','age','report']
        fields = '__all__'