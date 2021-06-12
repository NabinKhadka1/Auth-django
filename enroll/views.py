from django.contrib.auth import authenticate
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'User Created Successfully')       
    else:
        fm = SignUpForm()
    return render(request,'signup.html',{'form':fm})

#Login Views
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data =request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')
    

def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    else:
        return HttpResponseRedirect('/profile/')

def user_logout(request):
    logout(request)
    messages.success(request,'Successfully Logged out')
    return HttpResponseRedirect('/login/')
    
