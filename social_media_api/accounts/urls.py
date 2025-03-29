from django.urls import path
from .views import RegistrationView, LoginView, ProfileView, FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('follow/<int:user_id>/', FollowUserView.as_view()),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view()),
]
