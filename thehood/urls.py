from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('display', views.display, name='display'),
    path('profile', views.profile, name='profile'),
]