from django.urls import path
from bookTalk.views import create_review, show_main, create_review_ajax, get_books, get_book_json, get_review_json
from bookTalk.views import book_list

app_name = 'book-talk'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-review', create_review, name='create_review'),
    path('create-review-ajax', create_review_ajax, name='create_review_ajax'),
    path('get-books', get_books, name='get_books'),
    path('get-book-json', get_book_json, name='get_book_json'),
    path('get-review-json', get_review_json, name='get_review_json'),
    path('book/<int:book_id>/', book_list, name='book_list'),
]