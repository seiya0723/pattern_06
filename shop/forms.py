from django import forms 
from .models import Pattern,PatternRecipe

class PatternForm(forms.ModelForm):

    class Meta:
        model   = Pattern
        fields  = [ "title","img","size" ]

class PatternRecipeForm(forms.ModelForm):

    class Meta:
        model   = PatternRecipe
        fields  = [ "target","color","number" ]




