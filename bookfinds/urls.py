from django.urls import path
from bookfinds.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('get-books/', get_books, name='get_books'),
]