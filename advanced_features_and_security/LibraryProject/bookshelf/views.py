from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import ListView
from django.db.models import Q
from .models import Book
from .forms import BookForm, ExampleForm


@login_required
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    query = request.GET.get("q", "")
    books = Book.objects.all()
    
    if query:
        # ✅ Securely filter books instead of using raw SQL
        books = books.filter(Q(title__icontains=query) | Q(author__name__icontains=query))

    return render(request, "bookshelf/book_list.html", {"books": books})

@login_required
@permission_required("bookshelf.can_create", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():  # 🚀 Secure input validation
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    
    return render(request, "bookshelf/add_book.html", {"form": form})

@login_required
@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)

    return render(request, "bookshelf/edit_book.html", {"form": form})

@login_required
@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == "POST":
        book.delete()
        return redirect("book_list")

    return render(request, "bookshelf/delete_book.html", {"book": book})
