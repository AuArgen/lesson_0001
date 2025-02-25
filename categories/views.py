from django.shortcuts import render

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
    context = {
        'categories': categories,
        'choose_category': choose_category
    }
    return render(request, 'detail.html', context)
