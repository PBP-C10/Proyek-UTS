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
import json

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


# # Create your views here.
# @login_required(login_url='/login')
# def show_main(request):
#     book = Book.objects.all()
#     context = {
#         'book': book
#     }

#     return render(request, "bookTalk.html", context)

# @login_required(login_url='/login')
# def create_review(request):
#     form = ReviewForm(request.POST or None)

#     if form.is_valid() and request.method == 'POST':
#         form.save()
#         return HttpResponse(b"Created", status=201)
        
#     # context = {'form': form}
#     # return HttpResponseNotFound()
#     context = {'form': form}
#     return render(request, "create_review.html", context)

# # def create_review_ajax (request):
# #     if request.method == 'POST':
# #         form = ReviewForm(request.POST)
# #         if form.is_valid():
# #             form.save(user=request.user, book=Book.objects.get(id=request.POST.get('book')))
# #             return JsonResponse({'success': True})
# #         else:
# #             return JsonResponse({'success': False})
# def create_review_ajax2 (request):
#     print("masuk")
#     if request.method == 'POST':
#         review_text = request.POST.get('review_text')
#         rating = request.POST.get('rating')
#         book = request.POST.get('book')

#         review = Review(review_text=review_text, rating=rating, book=book)
#         review.save()
#         return HttpResponse(b"CREATED", 201)
#     return HttpResponseNotFound()
    

# @csrf_exempt
# # def post_review(request, book_id):
# #     book = get_object_or_404(Book, id=book_id)
# #     form = ReviewForm(request.POST or None)
# #     if form.is_valid() and request.method == "POST":
        
# #         form.save(reviewer_user=request.user, book=book)

# #         return HttpResponse("CREATED", 201)

# #     return HttpResponseNotFound()

# def post_review(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.reviewer_user = request.user
#             review.book = book
#             review.save()
#             return redirect('book_list', book_id=book_id)
#     else:
#         form = ReviewForm()
#     return render(request, 'review_form.html', {'form': form})
    
# def get_books(request):
#     books = Book.objects.all()

#     categories = request.GET.get('category')
#     if categories:
#         categories = categories.split(",")
#         query = Q()
#         for category in categories:
#             query |= Q(category=category)
#         books = books.filter(query)

#     filter = request.GET.get('filter')
#     if filter:
#         books = books.filter(title__icontains=filter) | books.filter(subtitle__icontains=filter) | books.filter(author__icontains=filter)

#     page = request.GET.get('page')
#     if not page:
#         page = 1
#     paginator = Paginator(books, 30)
#     booksInPage = paginator.get_page(page)

#     if booksInPage.has_next():
#         next_page = booksInPage.next_page_number()
#     else:
#         next_page = None

#     if booksInPage.has_previous():
#         prev_page = booksInPage.previous_page_number()
#     else:
#         prev_page = None

#     data = {
#         'total_page_num': paginator.num_pages,
#         'current_page': int(page),
#         'has_next': booksInPage.has_next(),
#         'next_page': next_page,
#         'has_previous': booksInPage.has_previous(),
#         'prev_page': prev_page,
#         'books': serializers.serialize('json', booksInPage),
#     }
#     return JsonResponse(data)

# def show_book_details(request, id):
#     book = Book.objects.get(pk=id)
#     price = str(book.price // 1000) + "." + str(book.price % 1000) 
#     context = {
#         'book': book,
#         'price': price,
#     }
#     return render(request, 'bookList.html', context)

# def get_book_json(request):
#     books = Book.objects.all()
#     return HttpResponse(serializers.serialize('json', books))

# def get_review_json(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     reviews = Review.objects.filter(book=book)
#     return HttpResponse(serializers.serialize('json', reviews))

# # def book_list(request, book_id):
# #     # Ambil semua hasil review untuk buku dengan ID yang diberikan
# #     reviews = Review.objects.filter(book_id=book_id)
    
# #     # Cek apakah ada hasil review
# #     if reviews.exists():
# #         context = {
# #             'reviews': reviews
# #         }
# #         return render(request, 'booklist.html', context)
# #     else:
# #         # Tampilkan pesan jika tidak ada review ditemukan
# #         context = {
# #             'message': 'Review not found'
# #         }
# #         return render(request, 'booklist.html', context)
    
# def book_list(request, book_id):
#     # Cari buku berdasarkan ID yang diberikan, atau tampilkan 404 jika tidak ditemukan
#     book = get_object_or_404(Book, pk=book_id)
    
#     # Ambil semua hasil review untuk buku dengan ID yang diberikan
#     reviews = Review.objects.filter(book=book)
    
#     # Cek apakah ada hasil review
#     if reviews.exists():
#         context = {
#             'book': book,
#             'reviews': reviews
#         }
#         return render(request, 'bookList.html', context)
#     else:
#         # Tampilkan pesan jika tidak ada review ditemukan
#         context = {
#             'book': book,
#             'message': 'Review not found'
#         }
#         return render(request, 'bookList.html', context)
    
# # @csrf_exempt
# # def post_review(request, book_id):
# #     form = ReviewForm(request.POST or None)
# #     book = Book.objects.get(pk=book_id)
# #     # form.book = book

# #     if form.is_valid() and request.method == 'POST':
# #         review = form.save(commit=False)
# #         review.reviewer_user = request.user
# #         review.book = book
# #         review.save()
# #         return HttpResponse(b"Created", status=201)
    
# #     # context = {'form': form}
# #     return HttpResponseNotFound()

#-----------------------------------------------------------
def buku_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    review = Review.objects.filter(book=book)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            ulasan = form.save(commit=False)
            ulasan.user = request.user
            ulasan.book = book
            ulasan.save()
            return redirect('buku_detail', book_id=book_id)
    else:
        form = ReviewForm()

    context = {'book': book, 'review': review, 'form': form}
    return render(request, 'ulasan.html', context)

# Display list of books
@login_required(login_url='/login')
def show_main(request):
    book = Book.objects.all()
    context = {'book': book}
    return render(request, "bookTalk.html", context)

# Create a review for a book
@login_required(login_url='/login')
def create_review(request):
    form = ReviewForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return HttpResponse(b"Created", status=201)
        
    context = {'form': form}
    return render(request, "create_review.html", context)

# Create a review for a book using AJAX
@csrf_exempt
def create_review_ajax(request):
    if request.method == 'POST':
        review_text = request.POST.get('review_text')
        rating = request.POST.get('rating')
        book_id = request.POST.get('book')

        book = get_object_or_404(Book, pk=book_id)

        review = Review(review_text=review_text, rating=rating, book=book)
        review.save()
        return HttpResponse(b"CREATED", 201)
    return HttpResponseNotFound()

# Post a review for a book
@csrf_exempt
def post_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer_user = request.user
            review.book = book
            review.save()
            return redirect('book_list', book_id=book_id)
    else:
        form = ReviewForm()
    return render(request, 'review_form.html', {'form': form})

# Get a paginated list of books based on filters
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

    page = request.GET.get('page', 1)
    paginator = Paginator(books, 30)
    booksInPage = paginator.get_page(page)

    data = {
        'total_page_num': paginator.num_pages,
        'current_page': int(page),
        'has_next': booksInPage.has_next(),
        'next_page': booksInPage.next_page_number() if booksInPage.has_next() else None,
        'has_previous': booksInPage.has_previous(),
        'prev_page': booksInPage.previous_page_number() if booksInPage.has_previous() else None,
        'books': serializers.serialize('json', booksInPage),
    }
    return JsonResponse(data)

# Display details of a specific book
def show_book_details(request, id):
    book = get_object_or_404(Book, pk=id)
    price = f"{book.price // 1000}.{book.price % 1000:03}"
    context = {'book': book, 'price': price}
    return render(request, 'bookList.html', context)

# Get all books in JSON format
def get_book_json(request):
    books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', books))

# Get all reviews for a specific book in JSON format
def get_review_json(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book)
    return HttpResponse(serializers.serialize('json', reviews))

# Display the list of reviews for a specific book
def book_list(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book)
    
    if reviews.exists():
        context = {'book': book, 'reviews': reviews}
        return render(request, 'bookList.html', context)
    else:
        context = {'book': book, 'message': 'Review not found'}
        return render(request, 'bookList.html', context)

@csrf_exempt
def create_review_flutter(request):
    if request.method == 'POST':
        user = request.user
        review_text = request.POST.get('review_text')
        rating = request.POST.get('rating')
        book_id = request.POST.get('book')
        book = (get_object_or_404(Book, pk=book_id))

        new_review = Review(reviewer_user=user, review_text=review_text, rating=rating, book=book)
        new_review.save()

        return JsonResponse({"status" : "success"})
    
    return JsonResponse({"status" : "failed"}) 

def get_review_flutter(request, book_id):
    reviews = Review.objects.all()
    review_data = []

    for review in reviews:
        review_serialized = serializers.serialize('json', [review, ])
        review_dict = json.loads(review_serialized)[0]

        review_data.append(review_dict)

        # Return a JSON response with the list of modified club data
    return JsonResponse({'clubs': review_data})