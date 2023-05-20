from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def home(request):
    form = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/home.html', {'form': form, 'stu': stud})

# @csrf_exempt


def save_data(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            sid = request.POST.get('stuid')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if (sid == ''):
                usr = User(name=name, email=email, password=password)
            else:
                usr = User(id=sid, name=name, email=email, password=password)

            usr.save()
            stud = User.objects.values()
            student_data = list(stud)
            return JsonResponse({'status': 'Save', 'student_data': student_data})
        else:
            return JsonResponse({'status': 0})
