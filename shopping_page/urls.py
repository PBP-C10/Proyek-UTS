from django.urls import path
from shopping_page.views import show_cart

app_name = 'shopping_page'

urlpatterns = [
    path('', show_cart, name='show_cart'),
]