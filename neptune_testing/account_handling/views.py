from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from . import forms

def account_registration(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            username = form.cleaned_data.get('username')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = forms.RegistrationForm()
    return render(request, 'account_handling/registration.html', {'form': form})


def client_registration(request):
    if request.method == 'POST':
        form = forms.ClientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            username = form.cleaned_data.get('username')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = forms.RegistrationForm()
    return render(request, 'account_handling/registration.html', {'form': form})


def staff_registration(request):
    if request.method == 'POST':
        form = forms.StaffRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            username = form.cleaned_data.get('username')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = forms.RegistrationForm()
    return render(request, 'account_handling/registration.html', {'form': form})


def agent_registration(request):
    if request.method == 'POST':
        form = forms.AgentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            username = form.cleaned_data.get('username')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = forms.RegistrationForm()
    return render(request, 'account_handling/registration.html', {'form': form})


def account_login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard')
            else:
                return redirect('/')
    else:
        form = forms.LoginForm()
    return render(request, 'account_handling/login.html', {'form': form})


def account_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    return render(request, 'account_handling/logout.html')
