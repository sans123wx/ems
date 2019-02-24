from django.contrib import auth
from django.urls import reverse
from django.contrib.auth import logout
from django.shortcuts import render , redirect
from .forms import *

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            auth.login(request , user)
            return redirect(reverse('wbz_all'))
    else:
        form = LoginForm()
    context = {}
    context['form'] = form
    print(form)
    return render(request , 'login/login.html' , context)

def logout_view(request):
    logout(request)
    return redirect(reverse('wbz_all'))