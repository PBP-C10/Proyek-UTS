from django.shortcuts import render
from bookTalk.models import Review
from django.http import HttpResponseRedirect
from bookTalk.forms import ReviewForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers
from bookfinds.models import Book
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import Book, Review
from .forms import ReviewForm
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# #Create your views here
# def buku_detail(request, book_id):
#     book = Book.objects.get(pk=book_id)
#     review = Review.objects.filter(book=book)

#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             ulasan = form.save(commit=False)
#             ulasan.user = request.user
#             ulasan.book = book
#             ulasan.save()
#             return redirect('buku_detail', book_id=book_id)
#     else:
#         form = ReviewForm()

#     context = {'book': book, 'review': review, 'form': form}
#     return render(request, 'ulasan.html', context)


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    book = Book.objects.all()
    context = {
        'book': book
    }

    return render(request, "bookTalk.html", context)

@login_required(login_url='/login')
def create_review(request):
    form = ReviewForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return HttpResponseRedirect(reverse('book-talk:show_main'))\
        
    context = {'form': form}
    return render(request, 'create_review.html', context)

def create_review_ajax (request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save(user=request.user, book=Book.objects.get(id=request.POST.get('book')))
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})

@csrf_exempt
def post_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = ReviewForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        
        form.save(reviewer_user=request.user, book=book)

        return HttpResponse("CREATED", 201)

    return HttpResponseNotFound
    
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

    page = request.GET.get('page')
    if not page:
        page = 1
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

def show_book_details(request, id):
    book = Book.objects.get(pk=id)
    price = str(book.price // 1000) + "." + str(book.price % 1000) 
    context = {
        'book': book,
        'price': price,
    }
    return render(request, 'bookList.html', context)

def get_book_json(request):
    books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', books))

def get_review_json(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = Review.objects.filter(book=book)
    return HttpResponse(serializers.serialize('json', reviews))

# def book_list(request, book_id):
#     # Ambil semua hasil review untuk buku dengan ID yang diberikan
#     reviews = Review.objects.filter(book_id=book_id)
    
#     # Cek apakah ada hasil review
#     if reviews.exists():
#         context = {
#             'reviews': reviews
#         }
#         return render(request, 'booklist.html', context)
#     else:
#         # Tampilkan pesan jika tidak ada review ditemukan
#         context = {
#             'message': 'Review not found'
#         }
#         return render(request, 'booklist.html', context)
    
def book_list(request, book_id):
    # Cari buku berdasarkan ID yang diberikan, atau tampilkan 404 jika tidak ditemukan
    book = get_object_or_404(Book, pk=book_id)
    
    # Ambil semua hasil review untuk buku dengan ID yang diberikan
    reviews = Review.objects.filter(book=book)
    
    # Cek apakah ada hasil review
    if reviews.exists():
        context = {
            'book': book,
            'reviews': reviews
        }
        return render(request, 'booklist.html', context)
    else:
        # Tampilkan pesan jika tidak ada review ditemukan
        context = {
            'book': book,
            'message': 'Review not found'
        }
        return render(request, 'booklist.html', context)
    
