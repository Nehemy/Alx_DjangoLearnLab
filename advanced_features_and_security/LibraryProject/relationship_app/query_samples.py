from .models import Book, Library, Librarian, Author

author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

books = Library.objects.get(name=library_name)
print(books.all())

librarian = Librarian.objects.get(library=library_name)
librarr = librarian.library