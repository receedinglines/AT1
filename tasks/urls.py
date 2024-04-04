from django.urls import path
from . import views
from .views import math_quiz


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('options/', views.option_selection, name='option_selection'),
    path('math/', views.math_page, name='math_page'),
    path('enterprise-computing/', views.enterprise_computing_page, name='enterprise_computing_page'),
    path('register/', views.register, name='register'),
    path('math/quiz/<int:question_id>/', views.math_quiz, name='math_quiz'),
]