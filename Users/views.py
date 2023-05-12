
from.forms import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect('product:index')
            else:
                messages.error(request,'Authentication failed')
                return render(request, 'layout/login.html', {'form': form})
        else:
            return render(request, 'layout/login.html', {'form': form})
        print("=="*5, name, password, "=="*5)
    else:
        form = LoginForm()
    return render(request, 'layout/login.html', {'form': form})

def logoutView(request):
    logout(request)
    return redirect('product:index')

def logupView(request):
    if request.method == 'POST':
        form = LogupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            pwd1 = form.cleaned_data['pwd1']
            pwd2 = form.cleaned_data['pwd2']

            
            user = User.objects.filter(Q(username=name)|Q(email=email))
            if user:
                messages.error(request, 'L\'utilisateur exist déjà')
            else:
                if len(pwd1) <5:
                    messages.error(request, 'password trop court')
                elif pwd2 != pwd1:
                    messages.error(request, 'password de confirmation est différent')
                else:
                    user = User(
                        username=name,
                        email=email,
                    )
                    user.set_password(pwd1)
                    user.save()
                    return redirect('users:login')
                
            print("=="*5, name, email, pwd1, "=="*5)
    form = LogupForm()
    return render(request, 'layout/logup.html', {'form': form})

