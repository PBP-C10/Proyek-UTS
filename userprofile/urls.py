
from django.urls import path
from userprofile.views import show_main


app_name = 'user-profile'

urlpatterns = [
    path('', show_main, name='show_main'),
]