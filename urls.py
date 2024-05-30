from django.urls import include, path # type: ignore
from django.urls import path # type: ignore
from random_generator.views import random_number_view # type: ignore
from django.urls import path # type: ignore
from .views import authors_view, articles_view, comments_view
from django.urls import path # type: ignore
from .views import customers_view, products_view, orders_view

urlpatterns = [
    # другие маршруты
    path('__debug__/', include('debug_toolbar.urls')),
]

urlpatterns = [
    # другие маршруты
    path('random/', random_number_view, name='random_number'),
]

urlpatterns = [
    path('authors/', authors_view, name='authors'),
    path('articles/', articles_view, name='articles'),
    path('comments/', comments_view, name='comments'),
]

urlpatterns = [
    path('customers/', customers_view, name='customers'),
    path('products/', products_view, name='products'),
    path('orders/', orders_view, name='orders'),
]