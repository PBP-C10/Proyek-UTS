from django.urls import path
from bookclub.views import show_main, create_club, delete_club, join_club, leave_club, show_club
from bookclub.views import get_club_json, get_bubble_json, get_book_json, get_recommended_book_json
from bookclub.views import get_club_flutter, create_club_flutter, delete_club_flutter, join_club_flutter, leave_club_flutter
from bookclub.views import post_bubble_flutter, add_rec_book_flutter
from bookclub.views import post_bubble, add_rec_book
from bookclub.views import is_owner, is_member

app_name = 'book-club'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-club/', create_club, name='create_club'),
    path('create-club-flutter/', create_club_flutter, name='create_club_flutter'),
    path('delete-club/<int:club_id>/', delete_club, name='delete_club'),
    path('delete-club-flutter/<int:club_id>/', delete_club_flutter, name='delete_club_flutter'),
    path('join-club/<int:club_id>/', join_club, name='join_club'),
    path('join-club-flutter/<int:club_id>/', join_club_flutter, name='join_club_flutter'),
    path('leave-club/<int:club_id>/', leave_club, name='leave_club'),
    path('leave-club-flutter/<int:club_id>/', leave_club_flutter, name='leave_club_flutter'),
    path('show-club/<int:club_id>/', show_club, name='show_club'),
    path('show-club/<int:club_id>/post-bubble/', post_bubble, name='post_bubble'),
    path('<int:club_id>/post-bubble-flutter/', post_bubble_flutter, name='post_bubble_flutter'),
    path('show-club/<int:club_id>/add-rec-book/', add_rec_book, name='add_rec_book'),
    path('<int:club_id>/add-rec-book-flutter/', add_rec_book_flutter, name='add_rec_book_flutter'),
    path('get-club-json/', get_club_json, name='get_club_json'),
    path('get-club-flutter/', get_club_flutter, name='get_club_flutter'),
    path('show-club/<int:club_id>/get-bubble-json/', get_bubble_json, name='get_bubble_json'),
    path('<int:club_id>/get-bubble-flutter/', get_bubble_json, name='get_bubble_flutter'),
    path('get-book-json/', get_book_json, name='get_book_json'),
    path('show-club/<int:club_id>/get-recommended-book-json/', get_recommended_book_json, name='get_recommended_book_json'),
    path('is-owner/<int:club_id>/', is_owner, name='is_owner'),
    path('is-member/<int:club_id>/', is_member, name='is_member'),
]