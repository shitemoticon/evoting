from django.urls import path
from account import views

urlpatterns = [
    path('sign-up/', views.Signup.as_view()),
    path('log-in/', views.Login.as_view()),
    path('log-out/', views.Logout.as_view()),
]
