from django.urls import path
from shopping_page.views import shopping_main, get_carts
from bookfinds.views import get_books

app_name = 'shopping_page'

urlpatterns = [
    path('shopping-main/', shopping_main, name='shopping_main'),
    path('get-cart/', get_carts, name='get_cart'),
    path('get-books/', get_books, name='get_books'),
]