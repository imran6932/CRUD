from django import forms
from django.core import validators
from .models import Registration

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email','mobile', 'location']
        labels = {'name':'Full Name', 'email':'Email','location':'Location','mobile':'Mobile'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
        }
    
