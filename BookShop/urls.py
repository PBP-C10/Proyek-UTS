from django.urls import path
from BookShop.views import shopping_main, add_books_to_cart, create_order,submit_order,remove_book,filter_books


app_name = 'BookShop'

urlpatterns = [
    path('shopping-main/', shopping_main, name='shopping_main'),
    path('add-books-to-cart/<int:book_id>/', add_books_to_cart, name='add_books_to_cart'),
    path('create-order/', create_order, name='create_order'),  
    path('submit-order/', submit_order, name='submit_order'),
    path('remove_book/<int:book_id>/', remove_book, name='remove_book'),
    path('get-books', filter_books, name='get_books'),
]
