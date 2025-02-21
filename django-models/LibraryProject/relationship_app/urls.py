from django.urls import path
from .views import list_books, LibraryDetailView, admin_view, librarian_view, member_view, BookListView, add_book, edit_book, delete_book
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/add/', add_book, name="add_book"),
    path('books/edit/<int:book_id>/', edit_book, name="edit_book"),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
]
