from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import StudentSignUpform,TeacherSignUpform
from account.models import Student, User
# Create your views here.

class StudentAccount(CreateView):
    model = User
    form_class = StudentSignUpform
    template_name = 'StudentSignup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('HOME')
        
    

class TeachertAccount(CreateView):
    model = User
    form_class = TeacherSignUpform
    template_name = 'TeacherSignup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('HOME')
        

def getlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Your password was updated successfully!')
            return redirect('HOME')
         
    context = {}
    return render(request, 'login.html',context)

def getlogOut(request):
    logout(request)
    return redirect('Login')