# Book item created
create_book = Book(title="1984", author="George Orwell", publication_year=1949)
create_book.save()

# Retrieved and displayed all attributes of the book
book = Book.objects.get(title="1984")
print("Title:", book.title)
print("Author:", book.author)
print("Publication Year:", book.publication_year)

# Updated the title
book.title = "1985"
book.save()

book.delete()
# Delete the book