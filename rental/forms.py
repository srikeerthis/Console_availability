from django import forms
from .models import Console

class ConsoleForms(forms.ModelForm):
    class Meta:
        model = Console
        fields = ['name','is_rented']

