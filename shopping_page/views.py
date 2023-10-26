from django.shortcuts import render, redirect
from .forms import OrderForm  # Pastikan Anda mengimpor OrderForm
from shopping_page.models import Cart
from django.http import HttpResponseRedirect
from django.urls import reverse
from bookfinds.models import Book
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def shopping_main(request):
    if not request.user.is_anonymous:
        cart, created = Cart.objects.get_or_create(user=request.user, defaults={'total_price': 0})
    else:
        cart = None

    book_data = []

    if cart:
        books = cart.book.all()
        for book in books:
            book_info = {
                'title': book.title,
                'price': book.price,
                'thumbnail': book.thumbnail
            }
            book_data.append(book_info)

    return render(request, "shopping_cart.html", {'book_data': book_data, 'cart': cart})



def get_carts(request):
    cart = Cart.objects.get(user=request.user)
    books = cart.books.all()

    book_data = []

    for book in books :
        book_info = {
            'title' : book.title,
            'price' : book.price,
            'thumbnail' : book.thumbnail
         }
        book_data.append(book_info)
    return JsonResponse(book_data, safe=False)


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_success')  # Ganti 'order_success' dengan nama view untuk halaman sukses
    else:
        form = OrderForm()

    return render(request, 'create_order.html', {'form': form})



