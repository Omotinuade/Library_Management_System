from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    pass


class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=False, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} "


class Book(models.Model):
    LANGUAGE_CHOICES = [
        ('Y', 'YORUBA'),
        ('H', 'HAUSA'),
        ('I', 'IGBO'),
        ('E', 'ENGLISH'),
    ]
    GENRE_CHOICES = [
        ('FIC', 'FICTION'),
        ('POL', 'POLITIC'),
        ('FIN', 'FINANCE'),
        ('ROM', 'ROMANCE'),
    ]
    title = models.CharField(max_length=255, blank=False, null=False)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    description = models.CharField(max_length=255, blank=False, null=False)
    isbn = models.CharField(max_length=255, blank=False, null=False)
    date_added = models.DateTimeField(blank=True, null=True)
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES)
    language = models.CharField(max_length=1, choices=LANGUAGE_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Title: {self.title}"


class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('A', 'AVAILABLE'),
        ('B', 'BORROWED'),
    ]
    unique_id = models.UUIDField(primary_key=True, default=uuid4)
    due_back = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.book} status is {self.status}, \
        borrowed by {self.borrower},{self.due_back}"
