from django.urls import path
from BookShop.views import shopping_main, get_carts,create_order,confirm_order
from bookfinds.views import get_books

app_name = 'BookShop'

urlpatterns = [
    path('shopping-main/', shopping_main, name='shopping_main'),
    path('get-cart/', get_carts, name='get_cart'),
    path('get-books/', get_books, name='get_books'),
    path('create-order/', create_order, name='create_order'),
    path('confirm_order/<int:order_id>/', confirm_order, name='confirm_order')
]