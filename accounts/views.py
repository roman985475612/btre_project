from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('accounts:dashboard')

        messages.error(request, 'Test messages!')

    form = RegisterForm()

    return render(request, 'accounts/register.html', {
        'form': form,
        'title': 'Register',
    })


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Invalid credentials')

    form = LoginForm()

    return render(request, 'accounts/login.html', {
        'form': form,
        'title': 'Login',
    })


def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now logout')
    return redirect('index')

# need authorization
def dashboard(request):
    return render(request, 'accounts/dashboard.html', {
        'title': 'User Dashboard',
        'sub_title': 'Manage your BT Real Estate account',
    })
