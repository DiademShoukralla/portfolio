from django.contrib.auth import login as log, authenticate
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .backend import EmailBackend as EB

def register(request):
    """View for handling auth page"""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = EB.authenticate(username=username, password=raw_password)
            if user:
                log(request, user)
                return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'authen/form_base.html', {'form': form, 'screen': 'Sign up'})


def login(request):
    """View for handling log in page"""
    if request.method == 'POST':
        form = LoginForm(request.POST, request.POST)
        if form.is_valid():
            # form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user:
                log(request, user)
                next_page = request.GET.get('next')
                return redirect(next_page) if next_page else redirect('/')

    else:
        form = LoginForm()
    return render(request, 'authen/form_base.html', {'form': form, 'screen': 'Sign in'})
