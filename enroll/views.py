from django.contrib.auth import authenticate, update_session_auth_hash
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import EditAdminProfileForm, EditUserProfile, SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'User Created Successfully')  
            return HttpResponseRedirect('/login/')     
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
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user,data = request.POST)
                users = User.objects.all()
            else:
                fm = EditUserProfile(instance=request.user,data = request.POST)
                users = None
            if fm.is_valid():
                fm.save()
                messages.success(request,'User Profile Updated')
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfile(instance=request.user)
                users = None
        return render(request,'profile.html',{'name':request.user, 'form':fm, 'users':users })
    else:
        return HttpResponseRedirect('/profile/')

def user_logout(request):
    logout(request)
    messages.success(request,'Successfully Logged out')
    return HttpResponseRedirect('/login/')
    
# change password with old password
def user_passchange(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user = request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password Changed Successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user = request.user)
        return render(request,'change_password.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

# change password without old password
def user_passchange1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user = request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password Changed Successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user = request.user)
        return render(request,'change_password.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def user_detail(request,id):
    pi = User.objects.get(pk = id)
    fm = EditAdminProfileForm(instance = pi)
    return render(request,'userdetail.html',{'form': fm })