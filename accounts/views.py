from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from problems.models import Problems
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Вход после регистрации
            return redirect('/')  # Перенаправление на главную страницу
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})




@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def logout_account(request):
    logout(request)
    return redirect('main:index')