from .models import Book, Library, Librarian, Author

author = Author.objects.get(name='author_name')
books_by_author = Book.objects.filter(author=author)

books = Library.objects.get(name='library_name')
print(books.all())

library = Library.objects.get(name='library_name')
librarian = library.librarian