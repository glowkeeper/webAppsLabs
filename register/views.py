from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from register.forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

import logging

logging.basicConfig(level=logging.INFO)

@csrf_exempt
def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # logging.info("register form:")
            user = form.save()
            # login(request, user)
            return redirect("login")
            # messages.success(request, "Registration successful.")
            # return HttpResponse("Homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterForm()
    return render(request, "register/register.html", {"register_user": form})

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
                # return render(request, "commentstore/home.html")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "register/login.html", {"login_user": form})

@csrf_exempt
def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")