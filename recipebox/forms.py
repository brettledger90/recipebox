from django import forms
from django.forms import ModelForm
from recipebox.models import Author
from recipebox.models import Recipe

class RecipeAdd(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'author','description', 'instructions', 'timerequired']

class AuthorAdd(forms.Form):
    name = forms.CharField(max_length = 50)
    biosection = forms.Textarea()
