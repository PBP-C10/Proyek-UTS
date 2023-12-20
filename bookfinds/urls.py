from django.urls import path
from bookfinds.views import *

app_name = 'bookfinds'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('get-books/', get_books, name='get_books'),
    path('detail/<int:id>', show_book_details, name='detail'),
    path('request-book/', request_book, name='request_book'),
    path('get-book-requests/', get_book_request, name='get_book_requests'),
    path('delete-book-request/<int:id>/', delete_book_request, name='delete_book_request'),
    path('get-books-flutter/', get_books_flutter, name='get_books_flutter'),
    path('request-book-flutter/', request_book_flutter, name='request_book_fluter'),
]