from django.db import models
from bookfinds.models import Book
from RegLogInOut.models import User

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wishList = models.ForeignKey(Book, on_delete=models.CASCADE)

class MyBooks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    my_Book = models.CharField(max_length=255)
    progress = models.IntegerField()
    quote = models.TextField()