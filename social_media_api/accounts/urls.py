from django.contrib import admin
from django.urls import path
from .views import RegistrationView, LoginView, ProfileView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
]
