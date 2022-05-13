from rest_framework import serializers

from .models import Book


class BookDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['id','name','author','book_cover','published_date','description']
