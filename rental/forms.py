from django import forms
from .models import Console

class ConsoleForms(forms.ModelForm):
    class Meta:
        model = Console
        fields = ['name','status']
        widgets = {
            'status':forms.RadioSelect(choices=Console.STATUS_CHOICES)
        }

