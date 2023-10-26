from django.urls import path
from RegLogInOut.views import show_RegLogInOut, register, login_user, logout_user

app_name = 'RegLogInOut'

urlpatterns = [
    path('', show_RegLogInOut, name='show_RegLogInOut'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]