from django.contrib import admin
from django.urls import path, include
from bookclub.views import show_main, create_club, delete_club, join_club, leave_club, show_club
from bookclub.views import register, login_user, logout_user

app_name = 'book-club'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('admin/', admin.site.urls),
    path('book-club', show_main, name='show_main'),
    path('create-club', create_club, name='create_club'),
    path('delete-club/<int:club_id>/', delete_club, name='delete_club'),
    path('join-club/<int:club_id>/', join_club, name='join_club'),
    path('leave-club/<int:club_id>/', leave_club, name='leave_club'),
    path('show-club/<int:club_id>/', show_club, name='show_club'),
]