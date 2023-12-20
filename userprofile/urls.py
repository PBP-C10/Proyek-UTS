
from django.urls import path
from userprofile.views import *


app_name = 'user-profile'

urlpatterns = [
    path('has-profile', has_profile, name='has_profile'),
    path('create-profile', create_profile, name='create_profile'), 
    path('edit-profile', edit_profile, name='edit_profile'),
    path('delete-profile', delete_profile, name='delete-profile'),
]