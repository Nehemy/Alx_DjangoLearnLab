from django.urls import path
from .views import *

urlpatterns = [
    path('', ),
    path('/books/', BookListView.as_view(), name='books'),
    path('/books/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('/books/create', BookCreateView.as_view(), name='book-create'),
    path('/books/<int:pk>/update', BookUpdateView.as_view(), name='book-update'),
    path('/books/<int:pk>/delete', BookDeleteView.as_view(), name='book-delete'),
]