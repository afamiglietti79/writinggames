from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('course:enroll'))
    else:
        form = UserCreationForm()
    return render(request, 'home/signup.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('home:index'))
        else:
            return render(request, 'home/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'home/login.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect(reverse('home:index'))
