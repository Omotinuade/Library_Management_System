from django.shortcuts import render, get_object_or_404
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from book.models import Author, Book
from book.serializers import AuthorSerializer, BookSerializer


@api_view()
def find_all_author(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def welcome(request):
    return Response('ok')


@api_view()
def find_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    serializer = AuthorSerializer(author)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def find_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def find_all_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)
