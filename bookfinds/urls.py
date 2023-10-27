from django.urls import path
from bookfinds.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('get-books/', get_books, name='get_books'),
    path('detail/<int:id>', show_book_details, name='detail'),
    path('request-book/', request_book, name='request_book'),
]