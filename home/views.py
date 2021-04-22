from django.shortcuts import render,redirect,get_object_or_404
from .form import Addmission_Form
from .models import AdmissionForm , Courses
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='Login')
def Home(request):
    form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'index.html',context)


def Course(request):
    course = Courses.objects.all()
    context = {
        'course':course
    }
    print(course)
    return render(request, 'course-grid-2.html', context)

def CourseSingle(request,id):
    single_course = get_object_or_404(Courses,pk = id)
    context = {
        'single_course':single_course
    }
    return render(request, 'course-single.html',context)


# course-single.html




def Admission(request):   
    # form = Addmission_Form(request.POST or None, request.FILES or None)
    # if form.is_valid():
    #     instance =form.save(commit=False)
    #     instance.save()
    #     return redirect('HOME')
    # context = {
    #     'form':form
    # }     
    return render(request, 'Addmission.html', context)

###

def RegisterUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        
    context = {
        'form':form
    }
    return render(request, 'register.html',context)
