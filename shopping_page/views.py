from django.shortcuts import render

# Create your views here.

def show_cart(request):
    context = {
        'name': 'Pak Bepe',
    }
    return render(request, "shopping_cart.html", context)