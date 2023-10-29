from django import forms
from django.forms import ModelForm
from bookclub.models import Club, Bubble, Book
from django.shortcuts import get_object_or_404

class ClubForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Club Name'}), required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Type your club description here ...'}), required=True)
    recommended_books = forms.ModelChoiceField(queryset=Book.objects.values_list('title', flat=True).order_by('title'),)
    bubble_content = forms.CharField(label="Bubble Content", widget=forms.Textarea())

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
    
class BubbleForm(ModelForm):    
    class Meta:
        model = Bubble
        fields = ["content", "username"]

    def save(self, commit=True, user=None, club=None):
        instance = super(BubbleForm, self).save(commit=False)
        
        bubble_content = self.cleaned_data.get('content')
        instance.content = bubble_content

        if user is not None:
            instance.user = user

        if club is not None:
            instance.club = club

        if commit:
            instance.save()

        return instance
    
class BookRecForm(ModelForm):
    recommended_books = forms.ModelChoiceField(
        queryset=Book.objects.values_list('title', flat=True).order_by('title'),
        # queryset=Book.objects.all().order_by('title'),
        to_field_name='title',
        widget=forms.Select(attrs={'class': 'form-select'}), 
        required=True,
    )

    class Meta:
        model = Club
        fields = ["recommended_books"]

    def save(self, commit=True, instance=None):
        selected_book = self.cleaned_data['recommended_books']
        recommended_book = get_object_or_404(Book, title=selected_book)

        if selected_book:
            instance.recommended_books.add(recommended_book)
        
        if commit:
            instance.save()

        return instance