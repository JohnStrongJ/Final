from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = 'title', 'prep_time', 'cook_time', 'servings', 'ingredients', 'instructions'

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': "Add title",
            }),
            'prep_time': forms.NumberInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': "Add prep time in minutes",
            }),
            'cook_time': forms.NumberInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': "Add cooking time in minutes",
            }),
            'servings': forms.NumberInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': "Add the amount of servings",
            }),
            'ingredients': forms.Textarea(attrs={
                'class': 'form-control mb-3',
                'placeholder': "Add each ingredient on its own line",
            }),
            'instructions': forms.Textarea(attrs={
                'class': 'form-control mb-3',
                'placeholder': "Number each instruction on its own line. For example: 1. Add water.",
            }),
        }
