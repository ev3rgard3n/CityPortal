# forms.py
from django import forms
from .models import Problems

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problems
        fields = ['name', 'description', 'address', 'image', 'category']
