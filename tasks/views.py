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
    

from django.shortcuts import get_object_or_404, render, redirect, reverse
from .models import Question
from django.contrib import messages

def math_page(request):
    # Find the first question by ID
    first_question = Question.objects.order_by('id').first()
    if first_question is not None:
        # Redirect to the first question of the math quiz
        return redirect('math_quiz', question_id=first_question.id)
    else:
        # Handle the case where no questions exist
        messages.error(request, "No questions are available.")
        return redirect('option_selection')  # Redirect to a safe page

# This view displays each question of the quiz and handles answer submission.
def math_quiz(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    next_question_id = None
    prev_question_id = None
    
    # Determine if there are next or previous questions
    if Question.objects.filter(pk=question_id+1).exists():
        next_question_id = question_id + 1
    if question_id > 1 and Question.objects.filter(pk=question_id-1).exists():
        prev_question_id = question_id - 1

    # Process the answer submission
    if request.method == 'POST':
        selected_answer = request.POST.get('answer')
        correct_answer = question.answers.filter(is_correct=True).first()
        if correct_answer and selected_answer == correct_answer.text:
            messages.success(request, "Correct!")
            if next_question_id:
                return redirect(reverse('math_quiz', kwargs={'question_id': next_question_id}))
            else:
                # Redirect to the results page when there are no more questions
                return redirect('results_page')
        else:
            messages.error(request, "Incorrect.")

    # Render the quiz question template
    return render(request, 'tasks/math_quiz.html', {
        'question': question,
        'next_question_id': next_question_id,
        'prev_question_id': prev_question_id,
    })
def results_page(request):
    # Logic to calculate results or display end of quiz message
    return render(request, 'tasks/results_page.html')

def results_page(request):
    # Assuming you store the user's answers in the session or a database, calculate the score
    score = ...  # Code to calculate the score based on user's answers
    total_questions = Question.objects.count()  # Total number of questions

    return render(request, 'tasks/results_page.html', {
        'score': score,
        'total_questions': total_questions,
    })
def start_math_quiz(request):
    # Assuming you want to start with the first Question
    first_question = Question.objects.order_by('id').first()
    if first_question:
        return redirect('math_quiz', question_id=first_question.id)
    else:
        # Handle the case where there are no questions
        # You might want to show a message or redirect to a different page
        messages.info(request, "There are currently no questions available.")
        return redirect('option_selection')

