from django.core import validators
from django import forms
from .models import User

class ProductRegistration(forms.ModelForm):
    class Meta:
        model = User
        #fields = ['pid', 'name', 'quantity', 'price']
        fields = ['name', 'quantity', 'price']
        widgets = {
            #'pid': forms.NumberInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
