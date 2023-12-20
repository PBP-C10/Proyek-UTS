from django.urls import path
from BookShop.views import *


app_name = 'BookShop'

urlpatterns = [
    path('shopping-main/', shopping_main, name='shopping_main'),
    path('add-books-to-cart/<int:book_id>/', add_books_to_cart, name='add_books_to_cart'),
    path('create-order/', create_order, name='create_order'),  
    path('submit-order/', submit_order, name='submit_order'),
    path('remove_book/<int:book_id>/', remove_book, name='remove_book'),
    path('shopping-main/filter-books', filter_books, name='filter_books'),
    path('json/', show_json, name='show_json'),
    path('add-book-to-cart/', add_book_to_cart, name='add_book_to_cart'),
    path('get-carts-flutter/', get_carts_flutter, name='get_carts_flutter'),
]
