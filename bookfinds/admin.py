from django.contrib import admin
from bookfinds.models import Book, BookRequest
# Register your models here.
admin.site.register(BookRequest)
admin.site.register(Book)