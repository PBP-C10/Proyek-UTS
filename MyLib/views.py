from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from MyLib.forms import BookTrackForm #, BookQuoteForm
from MyLib.models import MyBooks
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers

def show_myLib(request):
    products = MyBooks.objects.all()
    context = {
        'name': request.user.username,
        'my_Book': my_Book,
        'progress': progress,
        'quote': quote
    }
    return render(request, "MyLib.html", context)

def BookTracker(request):
    form = BookTrackForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('MyLib:show_myLib'))
        context = {'form': form}
    return render(request, "BookTracker.html", context)

def EditTracker(request, id):
    # Get product berdasarkan ID
    product = MyBooks.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = BookTrackForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_myLib'))

    context = {'form': form}
    return render(request, "EditTracker.html", context)

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