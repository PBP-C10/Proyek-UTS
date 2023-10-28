from django.forms import ModelForm
from MyLib.models import MyBooks

class BookTrackForm(ModelForm):
    class Meta:
        model = MyBooks
        fields = ["my_Book", "progress", "quote"]