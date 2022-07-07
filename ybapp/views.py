from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, logout
from .forms import createUserForm
from django.contrib.auth.models import Group
from .models import Student

# Create your views here.

def index(request):        
        ss = Student.objects.all()
        return render(request,'index.html', {'student': ss})

def login_user(request):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(username=username, password=password)

                if user is not None:
                        dj_login(request, user)
                        return redirect('/')
                else:
                        messages.info(request, 'error')
                        return redirect('/login')
        return render(request, 'login.html')        

def register(request):
        form = createUserForm()        
        if request.method == 'POST':
                form = createUserForm(request.POST)
                if form.is_valid():
                        user = form.save()
                        username = form.cleaned_data.get('username')

                        group = Group.objects.get(name='student')
                        user.groups.add(group)
                        user.groups.add(group)                             
                        dj_login(request, user, backend='django.contrib.auth.backends.ModelBackend')                   
                        return redirect('/user_detail')

        context = {'form': form}
        return render(request, 'register.html', context)        

def user_detail(request):
        return render(request, 'user_detail.html')


def adduserdetail(request):
        if request.method == 'POST':
                student = Student()
                i=1
                while True:
                        if(Student.objects.filter(id=i)):
                                i=i+1
                        else:
                                break           
                fname = request.POST.get('first_name')
                lname = request.POST.get('last_name')      
                email = request.POST.get('email') 
                year = request.POST.get('year')   
                username = request.POST.get('username')                                          
                student.id = i        
                student.fname = fname   
                student.lname = lname
                student.email = email
                student.year = year
                student.username=username                
                student.save()        
        return redirect('/')

def logoutuser(request):
        logout(request)
        messages.info(request, 'Logged out')
        return redirect('/')