from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Book(models.Model):
    isbn = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    thumbnail = models.URLField()
    description = models.TextField()
    published_year = models.IntegerField()
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)
    num_pages = models.IntegerField()
    ratings_count = models.IntegerField()
    price = models.IntegerField()

class BookRequest(models.Model):

    class Status(models.TextChoices):
        REQUESTED = "REQ", _("Requested")
        ACCEPTED = "ACC", _("Accepted")
        DENIED = "DEN", _("Denied")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    status = models.CharField(
        max_length = 3,
        choices= Status.choices,
        default=Status.REQUESTED,
    )
    
