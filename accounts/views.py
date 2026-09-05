from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Profile

# class based view for register and login
class RegisterCreateView(CreateView):
  form_class = RegisterForm
  template_name = 'register.html'
  success_url = reverse_lazy('login')

class LoginCreateView(LoginView):
  template_name = 'login.html'
  success_url = reverse_lazy('login')


def exit(request):
  logout(request)
  return redirect('login')

class ProfileListView(ListView):
  model = Profile
  template_name = 'profile.html'
  context_object_name = 'profiles'

  def get_queryset(self):
    return Profile.objects.filter(user=self. request.user)

class ProfileUpdateView(UpdateView):
  model = Profile
  template_name = 'update.html'
  form_class = ProfileForm
  success_url = reverse_lazy('login')

