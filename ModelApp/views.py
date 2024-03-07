from django.shortcuts import render
from ModelApp.form import StudentsForm


def index(request):
    stud = StudentsForm
    return render(request, 'index.html', {'form': stud})

# Create your views here.
