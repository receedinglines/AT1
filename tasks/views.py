from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Question
from django.urls import reverse


def option_selection(request):
    return render(request, 'tasks/option_selection.html')

def math_page(request):
    return render(request, 'tasks/Math.html')

def enterprise_computing_page(request):
    return render(request, 'tasks/Enterprise Computing.html')

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

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username, password=password)  # Create user first
            login(request, user)  # Then log the user in
            return redirect('option_selection')
        except Exception as e:
            return render(request, 'tasks/register.html', {'error': str(e)})
    else:
        return render(request, 'tasks/register.html')
    

from django.shortcuts import render
from .models import Question  # Ensure you have a Question model in models.py

def math_quiz(request):
    question = Question.objects.first()  # Get the first question from your database
    if question is not None:
        return render(request, 'math_quiz.html', {'question': question})
    else:
        # If no question exists, you can redirect or show a message
        return render(request, 'math_quiz.html', {'error': 'No questions available.'})
