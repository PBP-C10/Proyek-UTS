from django.forms import ModelForm
from myLibrary.models import MyBooks

class ProductForm(ModelForm):
    class Meta:
        model = MyBooks
        fields = ["my_Book", "progress", "quote"]

class MyAttributeForm(ModelForm):
    class Meta:
        model = MyBooks
        fields = ["progress"]

class QuoteForm(ModelForm):
    class Meta:
        model = MyBooks
        fields = ["quote"]
