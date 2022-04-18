from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, Profile, UpdateUserForm, UpdateProfileForm, NeighbourhoodForm, BusinessForm
from .models import Profile, Neighbourhood, Business

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


@login_required(login_url='login')
def display(request):
    return render(request, 'display.html')


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        profile_form = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(
                request, ('Your profile was successfully updated!'))
            return redirect('profile')
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'profile_form': profile_form})


def neighbourhood(request):
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('neighbourhood')
    else:
        form = NeighbourhoodForm()
    return render(request, 'neighbourhood.html', {'form': form})


def business(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES, instance=request.user.business)
        if form.is_valid():
            form.save()
            return redirect('business')
    else:
        form = BusinessForm()
    return render(request, 'business.html', {'form': form})


def search(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_by_business(search_term)
        message = f"{search_term}"

        return render(request, 'display.html', {"message": message, "business": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'display.html', {"message": message})