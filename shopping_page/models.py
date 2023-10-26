from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    total_price = models.IntegerField()

class Book(models.Model):
    title =  models.CharField(max_length=255)
    price = models.IntegerField()
    persons = models.ManyToManyField(Person)

