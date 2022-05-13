from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Book, Category
from .forms import SearchBookForm
from rest_framework import viewsets
from .serializers import BookDetailSerializer


def index(request):
    total_books = Book.objects.count()
    if request.method == 'POST':
        form = SearchBookForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            books  = Book.objects.filter(name__icontains=name)
            return render(request, 'list.html', {'books': books})
    else:
        form = SearchBookForm()
    context = {'form': form,'total_books': total_books}
    return render(request, 'index.html',context)


def book(request,book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book.html',{'book':book})


class BookDetailViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer




