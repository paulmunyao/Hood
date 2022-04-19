from logging import PlaceHolder
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Neighbourhood, Business
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, EmailInput, PasswordInput


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Inform a valid email address.',
        widget=EmailInput(attrs={'placeholder': 'email', 'class': 'mail'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        widgets = {
            'username': TextInput(attrs={'placeholder': 'username', 'class': 'control'}),
            'password1': PasswordInput(attrs={'class': 'pass1', 'type': 'password', 'placeholder': 'password'}),
            'password2': PasswordInput(attrs={'class': 'pass2', 'type': 'password', 'placeholder': 'confirm password'}),
        }


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=EmailInput(attrs={'class': 'form-control'}),
    )

    username = forms.CharField(
        max_length=255,
        required=True,
        widget=TextInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email', )
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
        }


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'location', 'description']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'biograpghy'}),
            'location': forms.TextInput(attrs={'class': 'loca'}),
            'description': forms.Textarea(attrs={'class': 'descrip'}),
        }


class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['name','image', 'location', 'occupants', 'admin']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'nam'}),
            'location': forms.TextInput(attrs={'class': 'locat'}),
            'occupants': forms.NumberInput(attrs={'class': 'occup'}),
            'admin': forms.Select(attrs={'class': 'adm'}),
        }


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name','image', 'neighbourhood', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'names'}),
            'neighbourhood': forms.Select(attrs={'class': 'neigh'}),
            'email': forms.EmailInput(attrs={'class': 'mai'}),
        }
