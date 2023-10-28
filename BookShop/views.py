from django.shortcuts import render, redirect
from BookShop.forms import OrderForm  # Pastikan Anda mengimpor OrderForm
from BookShop.models import Cart,Order
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
    total_price = 0

    if cart:
        # Ganti cart.books.all() menjadi cart.cart_books.all() jika diperlukan
        books = cart.cart_books.all()
        for book in books:
            book_info = {
                'title': book.title,
                'price': book.price,
                'thumbnail': book.thumbnail
            }
            book_data.append(book_info)
            total_price += book.price

        return render(request, "shopping_cart.html", {'book_data': book_data, 'cart': cart, 'total_price': total_price})
    else:
        return render(request, "shopping_cart.html", {'book_data': book_data, 'cart': cart, 'total_price': 0})

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
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            # Redirect to the confirm_order page with the order_id as a parameter
            return redirect('confirm_order', order_id=order.id)
    else:
        form = OrderForm()

    return render(request, 'create_order.html', {'form': form})

def confirm_order(request):
    if request.method == 'POST':
        selected_books = request.POST.getlist('selected_books')

        # Pastikan keranjang belanja pengguna sudah ada
        cart, created = Cart.objects.get_or_create(user=request.user, defaults={'total_price': 0})

        # Buat objek pesanan dan hubungkan dengan keranjang belanja pengguna
        order = Order.objects.create(cart=cart, email=request.user.email, payment_method=1)

        # Tambahkan buku yang dipilih ke dalam pesanan
        for book_id in selected_books:
            book = Book.objects.get(pk=book_id)
            order_item = Order(order=order, book=book)
            order_item.save()

        

        # Redirect ke halaman konfirmasi pesanan atau halaman lain jika diperlukan
        return redirect('confirm_order', order_id=order.id)

    # Handle metode GET atau lainnya jika diperlukan
    return render(request, 'create_order.html', {'form': form})






