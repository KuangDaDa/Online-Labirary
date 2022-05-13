from django.contrib import admin
from django.urls import path
from .views import index,book, BookDetailViewSet


urlpatterns = [
    path('',index,name='index'),
    path('book/<int:book_id>',book,name='book'),
    
]
