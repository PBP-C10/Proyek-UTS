import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from bookclub.models import Club, Bubble
from bookclub.forms import ClubForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.urls import reverse

def show_main(request):
    clubs = Club.objects.all()

    context = {
        'clubs': clubs
    }

    return render(request, "main.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('book-club:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("book-club:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('book-club:login')

@login_required(login_url='/login')
def create_club(request):
    form = ClubForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save(user=request.user)

        return HttpResponseRedirect(reverse('book-club:show_main'))

    context = {'form': form}
    return render(request, "create_club.html", context)

@login_required(login_url='/login')
def delete_club(request, club_id):
    club = get_object_or_404(Club, id=club_id)

    if request.user == club.owner:
        club.delete()

    return redirect('book-club:show_main')

@login_required(login_url='/login')
def join_club(request, club_id):
    club = get_object_or_404(Club, id=club_id)

    if request.user not in club.members.all():
        club.members.add(request.user)

    return redirect('book-club:show_main')

@login_required(login_url='/login')
def leave_club(request, club_id):
    club = get_object_or_404(Club, id=club_id)

    if request.user in club.members.all():
        club.members.remove(request.user)

    return redirect('book-club:show_main')

def show_club(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    books = club.recommended_books
    bubbles = Bubble.objects.filter(club=club)

    context = {
        'club' : club,
        'books' : books,
        'bubbles' : bubbles,
    }

    return render(request, "show_club.html", context)