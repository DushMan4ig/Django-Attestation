from django.shortcuts import render # type: ignore
import random
from django.shortcuts import render # type: ignore
from .models import Author, Article, Comment
from django.shortcuts import render # type: ignore
from .models import Customer, Product, Order

def random_number_view(request):
    number = random.randint(1, 100)
    return render(request, 'random_generator/number.html', {'number': number})



def authors_view(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})

def articles_view(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

def comments_view(request):
    comments = Comment.objects.all()
    return render(request, 'comments.html', {'comments': comments})


def customers_view(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})

def products_view(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def orders_view(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})