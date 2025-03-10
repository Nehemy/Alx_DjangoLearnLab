from django.urls import path
from .views import *

urlpatterns = [
    path('', ),
    path('/books/', BookListView.as_view(), name='books'),
    path('/books/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('/books/create', BookCreateView.as_view(), name='book-create'),
    path('/books/update/<int:pk>', BookUpdateView.as_view(), name='book-update'),
    path('/books/delete/<int:pk>', BookDeleteView.as_view(), name='book-delete'),
]