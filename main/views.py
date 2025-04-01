
from django.shortcuts import render
from .models import Category, Items


def index(request):
    categories = Category.objects.filter(is_visible=True)

    pass



    context = {
        'categories': categories

    }

    return render(request, 'base.html')