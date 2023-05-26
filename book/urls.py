from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from book import views

router = SimpleRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)

# print(router.urls)
# urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
    # path('authors/', views.AuthorList.as_view()),
    path('welcome/', views.welcome),
    # path('author/<int:pk>/', views.AuthorDetail.as_view()),
    # path('book/<int:pk>/', views.BookDetail.as_view(), name='find_all_author'),
    # path('books/', views.BookList.as_view())
]
