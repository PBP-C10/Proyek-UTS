from django.forms import ModelForm
from shopping_page.models import Book

class PersonForm(ModelForm):
    class Meta:
        model = Book
        fields = ["name","email","total_price",]