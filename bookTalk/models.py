from django.db import models
from bookfinds.models import Book
from django.contrib.auth.models import User

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer_user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()

