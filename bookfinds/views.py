from django.shortcuts import render
from bookfinds.models import Book
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def show_main(request):
    return render(request, "bookfinds.html")

def get_books(request):
    books = Book.objects.all()
    categories = request.GET.get('category')
    if categories:
        categories = categories.split(",")
        query = Q()
        for category in categories:
            query |= Q(category=category)
        books = books.filter(query)
    filter = request.GET.get('filter')
    if filter:
        books = books.filter(title__icontains=filter) | books.filter(subtitle__icontains=filter) | books.filter(author__icontains=filter)

    min_price = request.GET.get('minPrice')
    max_price = request.GET.get('maxPrice')
    if not min_price:
        min_price = 0

    if not max_price:
        max_price = 500000

    books = books.filter(price__range=[min_price, max_price])

    min_rating = request.GET.get('minRating')
    if min_rating:
        books = books.filter(average_rating__range=[min_rating,5])

    page = request.GET.get('page')
    paginator = Paginator(books, 30)
    booksInPage = paginator.get_page(page)

    if booksInPage.has_next():
        next_page = booksInPage.next_page_number()
    else:
        next_page = None

    if booksInPage.has_previous():
        prev_page = booksInPage.previous_page_number()
    else:
        prev_page = None

    data = {
        'total_page_num': paginator.num_pages,
        'current_page': int(page),
        'has_next': booksInPage.has_next(),
        'next_page': next_page,
        'has_previous': booksInPage.has_previous(),
        'prev_page': prev_page,
        'books': serializers.serialize('json', booksInPage),
    }
    return JsonResponse(data)