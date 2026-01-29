from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Event

def login_view(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            user = authenticate(
                request,
                username=request.POST['username'],
                password=request.POST['password']
            )
            if user:
                login(request, user)
                return redirect('home')
        else:
            if not User.objects.filter(username=request.POST['reg_username']).exists():
                User.objects.create_user(
                    username=request.POST['reg_username'],
                    password=request.POST['reg_password']
                )
                return redirect('login')
    return render(request, 'events/login.html')

def home(request):
    return render(request, 'events/home.html')

def event_list(request, category):
    events = Event.objects.filter(category=category)
    return render(request, 'events/event_list.html', {
        'events': events,
        'category': category
    })

def logout_view(request):
    logout(request)
    return redirect('login')
