from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import render


def option_selection(request):
    return render(request, 'tasks/option_selection.html')

def math_page(request):
    return render(request, 'tasks/Math.html')

def enterprise_computing_page(request):
    return render(request, 'tasks/Enterprise_Computing.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')  # Redirect to the page after login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')

def user_login(request):
    return render(request, 'tasks/login.html')
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('option_selection')  # Redirect here after login
        else:
            return render(request, 'tasks/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'tasks/login.html')

