from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# Serializes all fields of the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
    
    # Validate that the publication year is not in the future.
    def validate(self, data):
        current_year = datetime.now().year
        if data['publication_year'] > current_year:
            raise serializers.ValidationError('Year cannot be in the future.')
        return data
    
    
class AuthorSerializer(serializers.ModelSerializer):
    # The serialized book model is passed into the books variable, and then passed in for nesting into the Author serializer
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']