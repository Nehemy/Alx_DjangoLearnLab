from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user for authentication-required endpoints.
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()

        # Create an Author instance.
        self.author = Author.objects.create(name="Author One")
        
        # Create a Book instance to use for testing retrieval and updates.
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )
        
        # Define endpoint URLs using reverse with names from urls.py.
        self.book_list_url = reverse("books")
        self.book_detail_url = reverse("book-detail", kwargs={"pk": self.book.id})
        self.book_create_url = reverse("book-create")
        self.book_update_url = reverse("book-update", kwargs={"pk": self.book.id})
        self.book_delete_url = reverse("book-delete", kwargs={"pk": self.book.id})
    
    def test_get_book_list(self):
        """Ensure we can retrieve the list of books."""
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test Book", str(response.data))
    
    def test_get_book_detail(self):
        """Ensure we can retrieve a single book's details."""
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")
    
    def test_create_book_unauthenticated(self):
        """Ensure that creating a book without authentication is not allowed."""
        new_book_data = {
            "title": "New Book",
            "publication_year": 2019,
            "author": self.author.id
        }
        response = self.client.post(self.book_create_url, new_book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_create_book_authenticated(self):
        """Ensure that an authenticated user can create a new book."""
        self.client.login(username="testuser", password="testpass")
        new_book_data = {
            "title": "New Book",
            "publication_year": 2019,
            "author": self.author.id
        }
        response = self.client.post(self.book_create_url, new_book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")
    
    def test_update_book_authenticated(self):
        """Ensure that an authenticated user can update an existing book."""
        self.client.login(username="testuser", password="testpass")
        updated_data = {
            "title": "Updated Book Title",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.put(self.book_update_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Book Title")
        self.assertEqual(response.data["publication_year"], 2021)
    
    def test_delete_book_authenticated(self):
        """Ensure that an authenticated user can delete a book."""
        self.client.login(username="testuser", password="testpass")
        response = self.client.delete(self.book_delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Confirm deletion by attempting to retrieve the deleted book.
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_filtering_books(self):
        """Test filtering the book list by publication_year."""
        response = self.client.get(self.book_list_url, {"publication_year": 2020})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_search_books(self):
        """Test search functionality for books by title or author."""
        response = self.client.get(self.book_list_url, {"search": "Test"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test Book", str(response.data))
    
    def test_ordering_books(self):
        """Test ordering books by title in descending order."""
        response = self.client.get(self.book_list_url, {"ordering": "-title"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
