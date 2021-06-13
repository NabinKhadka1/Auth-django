from django.contrib.auth import forms
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields, widgets

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label = 'Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email': 'Email'}

class EditUserProfile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined']
        labels = {'email': 'Email'}