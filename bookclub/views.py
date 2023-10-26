from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from bookclub.models import Club, Bubble
from bookclub.forms import ClubForm, BubbleForm, BookRecForm
from django.urls import reverse

def show_main(request):
    clubs = Club.objects.all()

    context = {
        'clubs': clubs
    }

    return render(request, "main.html", context)

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

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def post_bubble(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    form = BubbleForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save(user=request.user, club=club)

        return HttpResponseRedirect(reverse('book-club:show_main'))

    context = {'form': form}
    return render(request, "post_bubble.html", context)

@login_required(login_url='/login')
def add_rec_book(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    form = BookRecForm(request.POST or None, instance=club)

    if form.is_valid() and request.method == 'POST':
        form.save(instance=club)

        return HttpResponseRedirect(reverse('book-club:show_club', args=[club_id]))

    context = {'form': form}
    return render(request, "add_rec_book.html", context)