from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from bookclub.models import Club, Book, Bubble
from bookclub.forms import ClubForm, BubbleForm, BookRecForm
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt 

def get_club_json(request):
    clubs = Club.objects.all()
    return HttpResponse(serializers.serialize('json', clubs))

def get_bubble_json(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    bubbles = Bubble.objects.filter(club=club)
    return HttpResponse(serializers.serialize('json', bubbles))

def get_book_json(request):
    books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', books))

def get_recommended_book_json(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    recommended_books = club.recommended_books.all()
    return HttpResponse(serializers.serialize('json', recommended_books))

@login_required(login_url='/login/?next=book-club/')
def show_main(request):
    clubs = Club.objects.all()
    club_form = ClubForm()

    context = {
        'clubs': clubs,
        'club_form': club_form,
    }

    return render(request, "main.html", context)

@csrf_exempt
def create_club(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get("name")
        description = request.POST.get("description")
        recommended_books = request.POST.get("recommended_books")

        new_club = Club(owner=user, name=name, description=description)
        new_club.save()
        new_club.members.add(user)
        new_club.recommended_books.add(recommended_books)

        bubble = request.POST.get("bubble")

        new_bubble = Bubble(user=user, club=new_club, content=bubble)
        new_bubble.save()

        return HttpResponse(b"CREATED", status=201)   
    
    return HttpResponseNotFound  

@csrf_exempt
def delete_club(request, club_id):
    if request.method == 'POST':
        club = get_object_or_404(Club, id=club_id)
        club.delete()

        return HttpResponse(b"OK", status=200)

    return HttpResponseNotFound

@csrf_exempt
def join_club(request, club_id):
    if request.method == 'POST':
        club = get_object_or_404(Club, id=club_id)
        club.members.add(request.user)

        return HttpResponse(b"OK", status=200)

    return HttpResponseNotFound

@csrf_exempt
def leave_club(request, club_id):
    if request.method == 'POST':
        club = get_object_or_404(Club, id=club_id)
        club.members.remove(request.user)

        return HttpResponse(b"OK", status=200)

    return HttpResponseNotFound

@csrf_exempt
def is_owner(request, club_id):
    if request.method == 'POST':
        club = get_object_or_404(Club, id=club_id)
        
        if request.user == club.owner:
            return HttpResponse('True', content_type='text/plain')
    
    return HttpResponse('False', content_type='text/plain')

@csrf_exempt
def is_member(request, club_id):
    if request.method == 'POST':
        club = get_object_or_404(Club, id=club_id)
        
        if request.user in club.members.all():
            return HttpResponse('True', content_type='text/plain')
    
    return HttpResponse('False', content_type='text/plain')

@login_required(login_url='/login')
def show_club(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    books = club.recommended_books
    bubbles = Bubble.objects.filter(club=club)
    bubble_form = BubbleForm()
    book_recommendation_form = BookRecForm()

    context = {
        'club' : club,
        'books' : books,
        'bubbles' : bubbles,
        'bubble_form' : bubble_form,
        'book_recommendation_form' : book_recommendation_form,
    }

    return render(request, "show_club.html", context)

@csrf_exempt
def create_club(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get("name")
        description = request.POST.get("description")
        recommended_books = request.POST.get("recommended_books")

        new_club = Club(owner=user, name=name, description=description)
        new_club.save()
        new_club.members.add(user)
        new_club.recommended_books.add(recommended_books)

        bubble = request.POST.get("bubble")

        new_bubble = Bubble(user=user, username=user.username, club=new_club, content=bubble)
        new_bubble.save()

        return HttpResponse(b"CREATED", status=201)   
    
@csrf_exempt
def post_bubble(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    form = BubbleForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save(user=request.user, club=club)

        return HttpResponse("CREATED", 201)

    return HttpResponseNotFound

@csrf_exempt
def add_rec_book(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    form = BookRecForm(request.POST or None, instance=club)

    if form.is_valid() and request.method == 'POST':
        form.save(instance=club)

        return HttpResponse("CREATED", 201)

    return HttpResponseNotFound