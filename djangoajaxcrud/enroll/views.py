from django.shortcuts import render
from .forms import StudentRegistration
# Createyour views here.


def home(request):
    form = StudentRegistration()
    context = {
        'form': form
    }
    return render(request, 'enroll/home.html', context)
