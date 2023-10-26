from django import forms
from django.forms import ModelForm
from bookclub.models import Club, Bubble, Book

class ClubForm(ModelForm):
    recommended_books = forms.ModelChoiceField(
        queryset=Book.objects.all(),
    )

    bubble_content = forms.CharField(
        label="Bubble Content",
        widget=forms.Textarea(),   
    )

    class Meta:
        model = Club
        fields = ["name", "description", "recommended_books"]

    def save(self, commit=True, user=None):
        instance = super(ClubForm, self).save(commit=False)
        
        if user is not None:
            instance.owner = user
            instance.save()
            instance.members.add(user)

        selected_book = self.cleaned_data.get('recommended_books')
        if selected_book:
            instance.recommended_books.add(selected_book)
        
        bubble_content = self.cleaned_data.get('bubble_content')
        if bubble_content:
            bubble = Bubble(user=user, club=instance, content=bubble_content)
            bubble.save()
        if commit:
            instance.save()

        return instance