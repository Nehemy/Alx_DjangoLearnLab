'''
Prepare a Python script query_samples.py in the relationship_app directory. This script should contain the query for each of the following of relationship:
Query all books by a specific author.
List all books in a library.
Retrieve the librarian for a library.
'''

from .models import Book, Library, Librarian

books = Book.objects.get(author="Name")
print(books.author)

books = Library.objects.get(name=library_name)
print(books.all())

librarian = Librarian.objects.all()
print(librarian.library)