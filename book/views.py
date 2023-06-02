from django.shortcuts import render, get_object_or_404
# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from book.filters import AuthorFilter, BookFilter
from book.models import Author, Book
from book.pagination import DefaultPagination
from book.serializers import AuthorSerializer, BookSerializer


# @api_view(['GET', 'POST'])
# def find_all_author(request):
#     if request.method == 'GET':
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         deserialize = AuthorSerializer(data=request.data)
#         deserialize.is_valid(raise_exception=True)
#         deserialize.validated_data
#         deserialize.save()
#         return Response("Success", status=status.HTTP_201_CREATED)
# class AuthorList(ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#
# class AuthorDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


# class AuthorList(ListCreateAPIView):
#     def get_queryset(self):
#         return Author.objects.all()
#
#     def get_serializer_class(self):
#         return AuthorSerializer


@api_view()
def welcome(request):
    return Response('ok')


# @api_view(['GET', 'PUT', 'DELETE'])
# def find_author(request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     if request.method == 'GET':
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = AuthorSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("Successfully updated", status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         if author.book_set.count() > 0:
#             return Response({"error": "Author is associated with book and cannot be deleted"})
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class BookDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookList(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# @api_view(['GET', 'PUT', 'DELETE'])
# def find_book(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = BookSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("Edited Successfully", status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def find_all_books(request):
#     books = Book.objects.all()
#     if request.method == 'GET':
#         serializer = BookSerializer(books, many=True)  # , context={'request': request}
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("Success", status=status.HTTP_201_CREATED)

# class AuthorView(APIView):
#     def get(self, request):
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         deserialize = AuthorSerializer(data=request.data)
#         deserialize.is_valid(raise_exception=True)
#         # deserialize.validated_data
#         deserialize.save()
#         return Response("Success", status=status.HTTP_201_CREATED)
#

# class AuthorDetailView(APIView):
#     def get(self, request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self,request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         serializer = AuthorSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("Successfully updated", status=status.HTTP_200_OK)
#
#     def delete(self, request,pk):
#         author = get_object_or_404(Author, pk=pk)
#         if author.book_set.count() > 0:
#             return Response({"error": "Author is associated with book and cannot be deleted"})
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AuthorFilter
    search_fields = ['first_name']
    permission_classes = [IsAuthenticated]


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BookFilter
    search_fields = ['title']
    permission_classes = [IsAdminUser]

# class BookViewSet(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# def get_serializer_context(self):
#     return {"request": self.request}
