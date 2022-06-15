from . models import Gold, Comment
from django import forms
from django.forms import  ModelForm


class Goldform(forms.ModelForm):
    class Meta:
        model = Gold
        fields = '__all__'

class Commentform(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

