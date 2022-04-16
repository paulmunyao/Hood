from django.shortcuts import render,redirect,HttpResponse
from .forms import SignUpForm

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    form = SignUpForm(request.POST)
    return render(request,'signup.html',{'form':form})      