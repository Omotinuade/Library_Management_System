from django_filters import FilterSet

from book.models import Author


class AuthorFilter(FilterSet):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']
