from django.urls import path
from BookShop.views import shopping_main, add_books_to_cart, create_order,submit_order,remove_book,filter_books,show_json
from BookShop.views import get_carts_flutter,remove_book_flutter,submit_order_flutter,create_order_flutter


app_name = 'BookShop'

urlpatterns = [
    path('shopping-main/', shopping_main, name='shopping_main'),
    path('add-books-to-cart/<int:book_id>/', add_books_to_cart, name='add_books_to_cart'),
    path('create-order/', create_order, name='create_order'),  
    path('submit-order/', submit_order, name='submit_order'),
    path('remove_book/<int:book_id>/', remove_book, name='remove_book'),
    path('shopping-main/filter-books', filter_books, name='filter_books'),
    path('json/', show_json, name='show_json'), 
    path('get-carts-flutter/', get_carts_flutter,name='get_carts_flutter'),
    path('submit-order-flutter/',submit_order_flutter, name='submit_order_flutter'),
    path('create-order-flutter/', create_order_flutter, name='create_order_flutter'),
    path('remove-book-flutter/<int:book_id>/', remove_book_flutter, name='remove_book_flutter'),
   
]
