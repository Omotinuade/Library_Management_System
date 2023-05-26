from decimal import Decimal

from rest_framework import serializers

from book.models import Author, Book

from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['title', 'description', 'genre', 'language', 'price', 'author', 'book_number', 'discount_price']

    # author = serializers.HyperlinkedRelatedField(
    #     queryset=Author.objects.all(), view_name='find_all_authors')
    book_number = serializers.CharField(max_length=15, source="isbn")
    discount_price = serializers.SerializerMethodField(method_name='calculate')

    def calculate(self, book: Book):
        return book.price - book.price * Decimal(0.1)


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
