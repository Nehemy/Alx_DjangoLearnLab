# Retrieved and displayed all attributes of the book
book = Book.objects.get(title="1984")
print("Title:", book.title)
print("Author:", book.author)
print("Publication Year:", book.publication_year)