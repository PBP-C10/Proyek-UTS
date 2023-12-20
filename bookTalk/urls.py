from django.urls import path
from bookTalk.views import show_main, create_review_ajax, get_books, get_book_json, get_review_json, create_review
from bookTalk.views import book_list, post_review, create_review_flutter, get_review_flutter

app_name = 'book-talk'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-review/', create_review, name='create_review'),
    path('create-review-ajax/', create_review_ajax, name='create_review_ajax'),
    path('get-books/', get_books, name='get_books'),
    path('get-book-json/', get_book_json, name='get_book_json'),
    path('book/<int:book_id>/get-review-json/', get_review_json, name='get_review_json'),
    path('book/<int:book_id>/', book_list, name='book_list'),
    path('book/<int:book_id>/post-review/', post_review, name='post_review'),
    path('book/<int:book_id>/create-review-flutter/', create_review_flutter, name='create_review_flutter'),
    path('get-review-flutter/', get_review_flutter, name='get_review_flutter'),
]