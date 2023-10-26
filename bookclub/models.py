from django.db import models
from django.contrib.auth.models import User
from bookfinds.models import Book

class Club(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=30)
    description = models.TextField()
    members = models.ManyToManyField(User, related_name='clubs_joined')
    recommended_books = models.ManyToManyField(Book, related_name='recommended_in_clubs')

class Bubble(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)