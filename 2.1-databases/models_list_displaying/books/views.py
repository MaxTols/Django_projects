from django.shortcuts import render, redirect, get_object_or_404
from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, template, context)

def book(request, pub_date):
    template = 'books/book.html'
    book = get_object_or_404(Book, pub_date=pub_date)
    next_page = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    previous_page = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
    context = {
        'book': book,
        'next_page': next_page,
        'previous_page': previous_page,
    }
    return render(request, template, context)
