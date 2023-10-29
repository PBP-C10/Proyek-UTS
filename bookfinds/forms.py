from django.forms import ModelForm
from bookfinds.models import BookRequest

class BookRequestForm(ModelForm):
    class Meta:
        model = BookRequest
        fields = ["title", "author", "category", "status"]