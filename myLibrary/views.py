from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from myLibrary.forms import ProductForm, MyAttributeForm, QuoteForm
from myLibrary.models import MyBooks
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_myLibrary(request):
    products = MyBooks.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'products': products
    }
    return render(request, "myLibrary.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('myLibrary:show_myLibrary'))
    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = MyBooks.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyBooks.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyBooks.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MyBooks.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def edit_product(request, id):
    product = MyBooks.objects.get(pk = id)
    form = MyAttributeForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('myLibrary:show_myLibrary'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def reset_product(request, id):
    product = MyBooks.objects.get(pk = id)
    MyBooks.objects.filter(pk = id).update(progress=0)
    return HttpResponseRedirect(reverse('myLibrary:show_myLibrary'))

def edit_quote(request, id):
    product = MyBooks.objects.get(pk = id)
    form = QuoteForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('myLibrary:show_myLibrary'))

    context = {'form': form}
    return render(request, "edit_quote.html", context)

def get_product_json(request):
    product_item = MyBooks.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        my_Book = request.POST.get("my_Book")
        progress = request.POST.get("progress")
        quote = request.POST.get("quote")
        user = request.user

        new_product = MyBooks(my_Book=my_Book, progress=progress, quote=quote, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

def edit_product_ajax(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ProductForm(instance=product)
        html = render_to_string('edit_product.html', {'form': form})
        return JsonResponse({'success': True, 'html': html})
