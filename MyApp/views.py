from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('choose_quiz')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# Define your quizzes here as a sample
QUIZZES = {
    'Math': [
        {'id': 1, 'question': 'What is 2 + 2?', 'options': ['2', '3', '4', '5'], 'answer': '4'},
        # ... add more questions
    ],
    'Enterprise Computing': [
        {'id': 1, 'question': 'Enterprise software is used to satisfy the needs of an organization rather than individual users. True or False?', 'options': ['True', 'False'], 'answer': 'True'},
        # ... add more questions
    ]
}

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('choose_quiz')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def choose_quiz(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'choose_quiz.html')

def quiz(request, subject):
    if not request.user.is_authenticated:
        return redirect('login')
    # Implement your logic to handle quiz progression and answer checking
    # ...
    return render(request, 'quiz.html', {'subject': subject, 'questions': QUIZZES[subject]})

def quiz_completion(request):
    if not request.user.is_authenticated:
        return redirect('login')
    # Implement your logic to display quiz results
    # ...
    return render(request, 'quiz_completion.html')
