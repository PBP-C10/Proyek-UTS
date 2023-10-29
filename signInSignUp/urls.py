from django.urls import path

from signInSignUp.views import register, login_user, logout_user

app_name = 'signInSignUp'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]