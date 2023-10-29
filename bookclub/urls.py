from django.urls import path
from bookclub.views import show_main, create_club, delete_club, join_club, leave_club, show_club
from bookclub.views import get_club_json, get_bubble_json, get_book_json, get_recommended_book_json
from bookclub.views import post_bubble, add_rec_book
from bookclub.views import is_owner, is_member

app_name = 'book-club'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-club/', create_club, name='create_club'),
    path('delete-club/<int:club_id>/', delete_club, name='delete_club'),
    path('join-club/<int:club_id>/', join_club, name='join_club'),
    path('leave-club/<int:club_id>/', leave_club, name='leave_club'),
    path('show-club/<int:club_id>/', show_club, name='show_club'),
    path('show-club/<int:club_id>/post-bubble/', post_bubble, name='post_bubble'),
    path('show-club/<int:club_id>/add-rec-book/', add_rec_book, name='add_rec_book'),
    path('get-club-json/', get_club_json, name='get_club_json'),
    path('show-club/<int:club_id>/get-bubble-json/', get_bubble_json, name='get_bubble_json'),
    path('get-book-json/', get_book_json, name='get_book_json'),
    path('show-club/<int:club_id>/get-recommended-book-json/', get_recommended_book_json, name='get_recommended_book_json'),
    path('is-owner/<int:club_id>/', is_owner, name='is_owner'),
    path('is-member/<int:club_id>/', is_member, name='is_member'),
]