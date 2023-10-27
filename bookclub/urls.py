from django.urls import path
from bookclub.views import show_main, create_club, delete_club, join_club, leave_club, show_club
from bookclub.views import get_club_json, get_bubble_json, get_book_json
from bookclub.views import create_club_ajax
from bookclub.views import post_bubble, add_rec_book
from bookclub.views import is_owner, is_member
from RegLogInOut.views import register, login_user, logout_user

app_name = 'book-club'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('book-club', show_main, name='show_main'),
    path('create-club', create_club, name='create_club'),
    path('delete-club/<int:club_id>/', delete_club, name='delete_club'),
    path('join-club/<int:club_id>/', join_club, name='join_club'),
    path('leave-club/<int:club_id>/', leave_club, name='leave_club'),
    path('show-club/<int:club_id>/', show_club, name='show_club'),
    path('post-bubble/<int:club_id>/', post_bubble, name='post_bubble'),
    path('add-rec-book/<int:club_id>/', add_rec_book, name='add_rec_book'),
    path('get-club-json', get_club_json, name='get_club_json'),
    path('get-bubble-json/<int:club_id>/', get_bubble_json, name='get_bubble_json'),
    path('get-book-json', get_book_json, name='get_book_json'),
    path('create-club-ajax', create_club_ajax, name='create_club_ajax'),
    path('is-owner/<int:club_id>/', is_owner, name='is_owner'),
    path('is-member/<int:club_id>/', is_member, name='is_member'),
]