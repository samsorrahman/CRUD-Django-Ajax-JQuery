from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
# Createyour views here.


def home(request):
    form = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/home.html', {'form': form, 'stu': stud})
