from django.shortcuts import render, redirect, HttpResponse
from .forms import SignUpForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def display(request):
    return render(request, 'display.html')