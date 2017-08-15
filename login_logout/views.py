from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import UserInfo
from .forms import UserRegistrationForm,UserForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from notes.models import Notes,Event
from datetime import datetime
from django.shortcuts import render_to_response,redirect
# Create your views here.

def register(request):
    form = UserForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        retypepassword = form.cleaned_data['retype_password']
        if len(password) < 8:
            context = {
                "form" : form,
                "error_message" : "Password length should be grater than or equal to 8",
            }
            return render(request, 'register.html' , context)
        if password != retypepassword:
            context = {
                "form" : form,
                "error_message" : "Password and retype password are not equal",
            }
            return render(request, 'register.html' , context)
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                regform = UserRegistrationForm()
                context = {
                	"form" : regform,
                	"username" : username,
                	"email" : email
                }
                return render(request, 'fillUserData.html', context)
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)



def logout_user(request):
    logout(request)
    #form = UserForm(request.POST or None)
    #context = {
    #    "form": form,
    #}
    return render(request, 'homepage.html',)



def login_user(request):
        if request.user.is_authenticated():
            return redirect('login_logout:index')
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username , password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    email = request.user.email
                    user = User.objects.get(username=username)
                    ob = Notes.objects.filter(UserName = user)
                    today = datetime.now().date()
                    year = today.year
                    month = today.month
                    day = today.day

                    events = Event.objects.filter(UserName=request.user,start_date__day__gte=day,).exclude(
                        end_date__year__lte=year,
                        end_date__month__lte=month,
                        ).order_by('start_date')
                    return render(request, 'index.html', { "username" : username , "Notes" : ob, "Event" : events})
                    #return render(request, 'index.html' , { "username": username, "email" : email})
                else:
                    return render(request, 'login.html' , { "error_message" : "Username or Password is Incorrect!!!"})
            else:
                return render(request, 'login.html' , { "error_message" : "Username or Password is Incorrect!!!"})
        return render(request, 'login.html',)

def register_form(request):
    form = UserForm()
    return render(request, 'register.html', {"form" : form})


def filluserdata(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = UserRegistrationForm(request.POST, request.FILES)
            if form.is_valid():
                
                Username = request.user.username
                FullName = form.cleaned_data['FullName']
                BirthDate = form.cleaned_data['BirthDate']
                Gender = form.cleaned_data['Gender']
                Email = request.user.email
                ProfilePic = form.cleaned_data['ProfilePic']
                newUser = UserInfo(UserName = User.objects.get(username=Username), FullName = FullName, BirthDate = BirthDate, Email = Email, Gender = Gender, ProfilePic= ProfilePic)
                newUser.save()
                return render(request, 'index.html',)
            else:
                regform = UserRegistrationForm()
                context = {
                    "form" : regform,
                    "username" : request.user.username,
                    "email" : request.user.email,
                    "error_message" : "Form id invalid"
                }
                return render(request, 'fillUserData.html', context)
        return render(request, 'index.html',)
    else:
        return redirect('login_logout:register')

def index(request):
    if request.user.is_authenticated():
        username = request.user.username
        user = User.objects.get(username=username)
        ob = Notes.objects.filter(UserName = user)
        today = datetime.now().date()
        year = today.year
        month = today.month
        day = today.day
        
        events = Event.objects.order_by('start_date','my_date').filter(UserName=request.user).exclude(
            end_date__year__lte=year,
            end_date__month__lte=month,
            end_date__day__lt=day,
            )
        return render(request, 'index.html', { "username" : username , "Notes" : ob, 
            "Event" : events
            })
    else:
        return redirect('login_logout:login_user')

def homepage(request):
    return render(request,'homepage.html',)

def aboutme(request):
    if request.user.is_authenticated():
        me = UserInfo.objects.filter(UserName=request.user)
        return render(request,'aboutme.html',{"me" : me})
    else:
        return redirect('login_logout:login_user')
