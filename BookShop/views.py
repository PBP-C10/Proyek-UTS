import json
from django.shortcuts import render, redirect
from BookShop.forms import OrderForm
from BookShop.models import Cart, Order
from bookfinds.models import Book
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, Http404
from django.db.models import Q
from django.core import serializers
from django.core.paginator import Paginator


def filter_books(request):
    books = Book.objects.all()

    min_price = request.GET.get('minPrice')
    max_price = request.GET.get('maxPrice')

    if not min_price:
        min_price = 0

    if not max_price or max_price == "":
        max_price = 500000

    books = books.filter(price__range=[min_price, max_price])

    min_rating = request.GET.get('minRating')
    if min_rating:
        books = books.filter(average_rating__range=[min_rating,5])

    return HttpResponse(serializers.serialize('json', books))
    


def shopping_main(request):
    if not request.user.is_anonymous:
        cart, created = Cart.objects.get_or_create(user=request.user, defaults={'total_price': 0})
    else:
        cart = None

    book_data = []

    if cart:
        books = cart.books.all()

        for book in books:
            book_info = {
                'title': book.title,
                'price': book.price,
                'thumbnail': book.thumbnail,
                'id': book.id,
            }
            book_data.append(book_info)

        current_order = Order.objects.filter(user=request.user, cart=cart, status=0).first()
    else:
        current_order = None

    return render(request, "shopping_cart.html", {
        'book_data': book_data,
        'cart': cart,
        'current_order': current_order,
        'total_price': cart.total_price if cart else 0
    })


def get_carts_flutter(request):
    if not request.user.is_anonymous:
        cart, created = Cart.objects.get_or_create(user=request.user, defaults={'total_price': 0})
    else:
        cart = None

    book_data = []

    if cart:
        books = cart.books.all()

        for book in books:
            book_info = {
                'title': book.title,
                'price': book.price,
                'thumbnail': book.thumbnail,
                'id': book.id,
            }
            book_data.append(book_info)

        current_order = Order.objects.filter(user=request.user, cart=cart, status=0).first()

        response_data = {
            "books": book_data,
            "current_order": {
                "id": current_order.id if current_order else None,
                "status": current_order.status if current_order else None,
            }
        }

        return HttpResponse(serializers.serialize("json", books))

    # This line should not be reached if the user is anonymous
    return JsonResponse({"status": "error"}, status=401)

    



def add_books_to_cart(request, book_id):
    if request.method == 'GET':
        book = Book.objects.get(pk=book_id)

        cart, created = Cart.objects.get_or_create(user=request.user, defaults={'total_price': 0})

        if book not in cart.books.all():
            cart.books.add(book)
            cart.total_price += book.price
            cart.save()

    return HttpResponse(b'OK', 200)


def add_book_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        cart = Cart.objects.get(user=request.user)
        book = Book.objects.get(id=data["book_id"])
        if cart:
            if book not in cart.books.all():
                cart.books.add(book)
                cart.total_price += book.price
                cart.save()
                return JsonResponse({"status": "success"}, status=200)
            else:
                return JsonResponse({"status": "fail", "message": "Buku sudah ada di cart"}, status=400)
        else:
            cart = Cart.objects.create(
                user = request.user,
                total_price = book.price,
            )
            cart.books.add(book)
            cart.save()
            return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=400)
    
def book_in_cart(request):
    if request.method == 'GET':
        data = json.loads(request.body)
        cart = Cart.objects.get(user=request.user)
        book = Book.objects.get(id=data["book_id"])

        if cart:
            if book in cart.books.all():
                return JsonResponse({"status": "true"}, status=200)
            else:
                return JsonResponse({"status": "false"}, status=200)
        else:
            return JsonResponse({"status": "false"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=400)

def create_order(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            email = order_form.cleaned_data['email']
            payment_method = order_form.cleaned_data['payment_method']

            cart, created = Cart.objects.get_or_create(user=request.user, defaults={'total_price': 0})

            total_price = cart.total_price

            order = Order(user=request.user, cart=cart, email=email, payment_method=payment_method)
            order.save()

            cart.status = 1
            cart.save()

            messages.success(request, 'Pesanan Anda telah berhasil diajukan. Keranjang belanja kosong.')

            return render(request, "create_order.html", {
                'order_form': order_form,
                'total_price': total_price,
            })
    else:
        order_form = OrderForm()
        total_price = 0

        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user, defaults={'total_price': 0})
            total_price = cart.total_price

        return render(request, "create_order.html", {'order_form': order_form, 'total_price': total_price})
    

def create_order_flutter(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            email = order_form.cleaned_data['email']
            payment_method = order_form.cleaned_data['payment_method']

            cart, created = Cart.objects.get_or_create(user=request.user, defaults={'total_price': 0})

            total_price = cart.total_price

            order = Order(user=request.user, cart=cart, email=email, payment_method=payment_method)
            order.save()

            cart.status = 1
            cart.save()

            

            return JsonResponse({"status": "success"}, status=200)
    else:
            order_form = OrderForm()
            total_price = 0

            if request.user.is_authenticated:
                cart, created = Cart.objects.get_or_create(user=request.user, defaults={'total_price': 0})
                total_price = cart.total_price
                return JsonResponse({"status": "error"}, status=401)
    


def submit_order(request):

    cart, created = Cart.objects.get_or_create(user=request.user, defaults={'total_price': 0})

    cart.books.clear()
    cart.total_price = 0
    cart.save()

    messages.success(request, 'Pesanan Anda telah berhasil diajukan. Keranjang belanja kosong.')

    return redirect('BookShop:shopping_main')

@csrf_exempt
def submit_order_flutter(request,):
     if request.method == 'POST':
        cart, created = Cart.objects.get_or_create(user=request.user, defaults={'total_price': 0})

        cart.books.clear()
        cart.total_price = 0
        cart.save()
        
        return JsonResponse({"status": "success"}, status=200)
    


def remove_book(request, book_id):
    if request.method == 'GET':
        book = Book.objects.get(pk=book_id)

        cart, created = Cart.objects.get_or_create(user=request.user, defaults={'total_price': 0})

        if book in cart.books.all():
            cart.books.remove(book)
            cart.total_price -= book.price
            cart.save()

    return redirect('BookShop:shopping_main')

def remove_book_flutter(request, book_id):
    if request.method == 'GET':
        book = Book.objects.get(pk=book_id)

        cart, created = Cart.objects.get_or_create(user=request.user, defaults={'total_price': 0})

        if book in cart.books.all():
            cart.books.remove(book)
            cart.total_price -= book.price
            cart.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)



def show_json(request):
    data = Cart.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


