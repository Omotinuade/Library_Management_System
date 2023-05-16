from django.urls import path

from book import views

urlpatterns = [
    path('authors/', views.find_all_author),
    path('welcome/', views.welcome),
    path('author/<int:pk>/', views.find_author, name='find_all_author'),
    path('book/<int:pk>/', views.find_book),
    path('books/', views.find_all_books)
]
