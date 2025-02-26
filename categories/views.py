from django.shortcuts import render

from books.models import Book
from categories.models import Category


def index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context)

def detail(request, aba):
    categories = Category.objects.all()
    choose_category = Category.objects.get(id=aba)
    books = Book.objects.filter(category_id=aba, published=True)
    context = {
        'categories': categories,
        'choose_category': choose_category,
        'books': books,
    }
    return render(request, 'detail.html', context)
