from django.forms import ModelForm
from bookTalk.models import Review
from django import forms
from bookfinds.models import Book


# class ReviewForm(ModelForm):
#     # books = forms.ModelChoiceField(
#     #     queryset=Book.objects.values_list('title', flat=True).order_by('title'),
#     #     # queryset=Book.objects.all().order_by('title'),
#     #     to_field_name='title',
#     #     widget=forms.Select(attrs={'class': 'form-select'}), 
#     #     required=True,
#     # )
#     class Meta:
#         model = Review
#         fields = ["book", "username", "reviewer_user", "review_text", "rating"]

#     def save(self, commit=True, user=None, book=None):
                
#         print(user)
#         print(book.title)
#         instance = super(ReviewForm, self).save(commit=False)
#         review_text = self.cleaned_data.get('review_text')
#         instance.review_text = review_text
#         selected_rating = self.cleaned_data.get('rating')
#         instance.rating = selected_rating

#         if user is not None:
#             instance.reviewer_user = user

#         if book is not None:
#             instance.book = book

#         # if username is not None:
#         #     instance.username = username

#         if commit:
#             instance.save()

#         return instance

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["review_text", "rating", "book",]
