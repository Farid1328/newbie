from . models import Gold, Comment

from django.forms import ModelForm
from django import forms
from captcha.fields import CaptchaField



class Goldform(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Gold
        fields = '__all__'

class Commentform(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Comment
        fields = ['text', 'captcha']

