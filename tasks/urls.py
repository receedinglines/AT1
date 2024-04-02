from django.urls import path
from . import views
from .views import math_quiz


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('options/', views.option_selection, name='option_selection'),
    path('math/', views.math_page, name='math_page'),
    path('enterprise-computing/', views.enterprise_computing_page, name='enterprise_computing_page'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('math/quiz/<int:question_id>/', math_quiz, name='math_quiz'),
    path('math/quiz/start/', views.start_math_quiz, name='start_math_quiz'),
    path('math/quiz/<int:question_id>/', views.math_quiz, name='math_quiz'),
    path('results/', views.results_page, name='results_page'),


]
