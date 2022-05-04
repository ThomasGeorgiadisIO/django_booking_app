from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        widgets = {
            'password': forms.PasswordInput(),
        }


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    class Meta:
        model = EndUser
        fields = ('username', 'first_name', 'last_name', 'email')


class GuideRegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    class Meta:
        model = TourGuide
        fields = ('username', 'first_name', 'last_name', 'guideDescription', 'email')


class ExperienceRegistrationForm(forms.ModelForm):
    class meta:
        model = TourExperience
        fields = ('tourTitle','tourLocation', 'tourDuration', 'tourPrice', 'tourAvailableDate', 'tourMaxNumberOfPeople', 'tourDescription', 'tourImage')


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    first_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    

    last_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


