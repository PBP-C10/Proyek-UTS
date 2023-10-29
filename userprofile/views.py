from django.shortcuts import render
from RegLogInOut.models import User

# Create your views here.
def show_main(request):
    user = User.objects.filter
    context = {
        'name' : request.user.username,

    }