from django.forms import ModelForm
from bookTalk.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["reviewer_user", "review_text", "rating"]

    def save(self, commit=True, user=None, book=None):
        instance = super(ReviewForm, self).save(commit=False)
        
        if user is not None:
            instance.reviewerUser = user

        if book is not None:
            instance.book = book

        if commit:
            instance.save()

        return instance
