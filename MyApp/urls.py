from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('choose_quiz/', views.choose_quiz, name='choose_quiz'),
    path('quiz/<str:subject>/', views.quiz, name='quiz'),
    path('quiz_completion/', views.quiz_completion, name='quiz_completion'),
]
