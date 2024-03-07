from django import forms
from ModelApp.models import Students


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
