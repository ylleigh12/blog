from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import signup_form

class user_register_view(generic.CreateView):
    form_class = signup_form
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')