from django.urls import path
from api import urls
from .views import BookList

urlpatterns = [
    path('', BookList.as_view(), name='book-list'),
    path('books/', BookList.as_view(), name='book-list'),
]
